/**
 * File Tree Component
 */
const TreeFiles = {
  name: 'TreeFiles',
  props: ['f','p'],
  template: `<div>
    <ul class="files">
      <li v-for="name in f.files" v-on:click="select_file(p,name)">
        <a><tt>{{name}}</tt></a>
      </li>
    </ul>
    <ul class="dirs">
      <li v-for="dir in f.dirs">
        <div class="accordion">
          <input type="checkbox" v-bind:id="combineb64(p,dir.name)">
          <label v-bind:for="combineb64(p,dir.name)" v-on:click="select_folder(p,dir.name)">
            <a><tt>{{dir.name}}</tt></a>
          </label>
          <div class="subfolder">
            <tree-files :f="dir.content" :p="combine(p,dir.name)"></tree-files>
          </div>
        </div>
      </li>
    </ul>
  </div>`,
  methods: {
    select_file(path, name) { this.$root.select_filename(path + '/' + name); },
    select_folder(path, name) { return true; },
    combine(path, name) { return path + '/' + name; },
    combineb64(path, name) { return btoa(path + '/' + name); },
  }
};

/**
 * Main Application
 */
const app = Vue.createApp({
  data() {
    return {
      password: '',
      user: USER_ID,
      loading: true,
      message: 'test',
      info: [],
      apps: [],
      newapp: {name:''},
      routes: [],
      walk: { files: [], dirs: [] },
      databases: {},
      toggled_folders: {},
      selected_app: null,
      selected_filename: null,
      selected_type: 'text',
      selected_file_link: null,
      files: {},
      tickets:[],
      modal: null,
      editor: null,
      modelist: null
    };
  },
  
  mounted() {
    if (this.user) this.init();
  },
  
  methods: {
    select(appobj) {
      this.selected_app = appobj;
      this.reload_files();
    },
    
    activate_editor(path, payload) {
      this.files[path] = payload;
      if (!this.editor) {
        this.editor = ace.edit("editor");
        this.editor.setTheme("ace/theme/pastel_on_dark");
        this.editor.$blockScrolling = Infinity;
      }
      this.editor.session.setValue(payload);
      
      if (!this.modelist) {
        this.modelist = ace.require("ace/ext/modelist");
      }
      const mode = this.modelist.getModeForPath(path).mode;
      this.editor.session.setMode(mode);
    },
    
    select_filename(path, force) {                
      if(this.selected_filename)
        this.files[this.selected_filename] = this.editor.getValue();

      var lpath = path.toLowerCase();
      if(lpath.endsWith('.mp4','.mov','.mpg','.mpeg')) this.selected_type = 'video';
      else if(lpath.endsWith('.wav') || lpath.endsWith('.mp3') || lpath.endsWith('.ogg')) 
          this.selected_type = 'audio';
      else if(lpath.endsWith('.png') || lpath.endsWith('.gif') || lpath.endsWith('.jpg')) 
          this.selected_type = 'image';
      else 
          this.selected_type = 'text';        
      this.selected_file_link = '../load_bytes/'+path;
      if(this.selected_type) {
          if(!force && path in this.files) {
              this.activate_editor(path, this.files[path]);
          } else {            
              var url = '../load/'+path;
              if(this.selected_type != 'text') url = '../load_bytes/'+path;
              Q.get(url).then(r=>{
                  this.activate_editor(path, r.json().payload);
              });
          }
      }
      this.selected_filename = path;
    },

    modal_dismiss() {
      this.modal = null;
    },

    reload(name) {
      this.modal_dismiss();
      this.loading = true;        
      Q.get(name?'../reload/'+name:'../reload').then(()=>this.init());
    },

    gitlog(name) {
      window.open('../gitlog/'+name);
    },

    load_file() {
      var path = this.selected_filename;
      this.select_filename(path, true);
    },

    file_saved() {
      // pass
    },

    save_file() {
      if(this.selected_type != 'text') {
        alert("Unable to save this file, it is not of type text");
        return;
      }
      var path = this.selected_filename;
      this.files[path] = this.editor.getValue();
      Q.post('../save/'+path, this.files[path]).then(()=>this.file_saved());
    },

    download_selected_app() {
      var url = '../packed/py4web.app.' + this.selected_app.name + '.zip?' + (new Date()).getTime();
      window.open(url, 'Download');
    },

    deploy_selected_app() {
      this.confirm('Deploy App','green','Ready to deploy',()=>{});
    },

    confirm(title, color, message, callback) {
      var buttons = [{text: 'Yes', onclick:callback}, {text:'No', onclick: this.modal_dismiss}];
      this.modal = {title: title, color:color, message:message, buttons:buttons};
    },

    process_new_app() {
      var form = this.modal.form;
      console.log(form);
      if(!form.name) alert('An app name must be provided');
      else if(!form.name.match(/^[\w_]+$/)) alert('Invalid file name');
      else if(form.mode=='new' && this.apps.map((a)=>{return a.name;}).indexOf(form.name)>=0) {
        alert('Cannot create an app with this name. It already exists');
      } else {
        Q.post('../new_app', form).then(()=>this.reload());
      }
    },

    process_new_file() {
      var app_name = this.selected_app.name;
      var form = this.modal.form;
      if(!form.filename) { alert('A file name must be provided'); return; }
      /*reload entire page needed to see the new file listed*/
      Q.post('../new_file/'+app_name+'/'+form.filename).then(()=>{
        this.walk = [];
        Q.get('../walk/'+app_name).then(r=>{this.walk=r.json().payload;});
        this.modal_dismiss();
      });
    }, 

    handle_upload_file() {
      Q.upload_helper('upload-file', (name, data)=>{this.modal.form.file=data; this.modal.form.type = "upload";});
    },

    upload_new_app() { 
      this.modal = {
        title:'Create or Upload App', 
        color:'blue', 
        message:'',
        form_name: 'create-app',
        form: {type: 'scaffold', name: '', source: '', mode: 'new', file: ''},
        buttons: [{text: 'Create', onclick: () => {this.process_new_app();}}, 
                  {text:'Close', onclick: this.modal_dismiss}]
      }; 
    },

    create_new_file() { 
      var app_name = this.selected_app.name;
      this.modal = {
        title:'Create a new file under ' + app_name, 
        color:'green', 
        message:'Ex: somedir/some_file.py',
        form_name: 'create-file',
        form: {'filename': ''},
        buttons: [{text: 'Create', onclick: () => {this.process_new_file();}}, 
                  {text:'Close', onclick: this.modal_dismiss}]
      }; 
    },

    upload_new_file() { 
      this.modal ={title:'Upload New File', color:'blue',message:'[WORK IN PROGRESS]'};
    },

    delete_selected_file() {
      var name = this.selected_filename;
      this.confirm("Delete File","blue","Do you really want to delete "+name+"?",()=>{
        this.modal_dismiss();
        Q.post('../delete/'+name).then(()=>this.init());
      });
    },

    delete_selected_app() {
      var name = this.selected_app.name;
      this.confirm("Delete App","blue","Do you really want to delete "+name+"?",()=>{
        this.modal_dismiss();
        Q.post('../delete_app/'+name).then(()=>this.init());
      });
    },

    reload_info() {
      Q.get('../info').then(r=>{
        this.info=r.json().payload || [];
      });
    },

    reload_apps() {
      Q.get('../apps').then(r=>{
        this.apps=r.json().payload || [];
        // Update selected_app if it exists
        if(this.selected_app) {
          this.selected_app = this.apps.filter((a) => {
            return a.name == this.selected_app.name;
          })[0] || null;
        }
      });
    },

    reload_routes() {
      Q.get('../routes').then(r=>{
        this.routes=r.json().payload || [];
      });
    },

    reload_tickets() {
      this.tickets = [];
      Q.get('../tickets').then(r=>{
        this.tickets = r.json().payload || [];
      });
    },

    reload_files() {
      if (!this.selected_app) {
        return;
      }
      this.walk = { files: [], dirs: [] }; // Always reset to an object
      var name = this.selected_app.name;
      Q.get('../walk/' + name).then(r => {
        const payload = r.json().payload;
        if (payload && Array.isArray(payload.files) && Array.isArray(payload.dirs)) {
          this.walk = payload;
        } else {
          this.walk = { files: [], dirs: [] };
        }
      });
      Q.get('../rest/' + name).then(r => { this.databases = r.json().databases; });
      this.selected_filename = null;
    },

    clear_tickets() {
      this.tickets = [];
      Q.get('../clear').then(()=>this.reload_tickets());
    },
    
    login() {
      Q.post('../login', { password: this.password })
        .then (r => {
          if (r.json().user) {
            this.user = true;
            this.password = '';
            this.init();
            location.reload();
          } else {
            alert("Login failed! Please try again.");
          }
        });
    },

    logout() {
      Q.post('../logout').then(()=>window.location.reload());
    },
    
    init() {
      this.reload_info();
      this.reload_apps();
      this.reload_routes();
      this.reload_tickets();
      this.reload_files();
      setTimeout(()=>{this.loading=false;}, 1000);
    }
  },
  
  filters: {
    mil: (value) => { return (''+value).substring(0,6); }
  }
});

// **Register globally for recursion to work**
app.component('TreeFiles', TreeFiles);

app.mount('#target');