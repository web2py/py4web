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
      modelist: null,
      last_error: "",
      show_system_info: false
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
    to_json(r) {
      let json = {};
      try {
        json = r.json();
      } catch (e) {
        app.vue.last_error = "Invalid JSON:\n" + r.data;
        return {};
      }      
      if (json.status === "error") { 
        app.vue.last_error = json.traceback || json.message || "Unknown error"; 
        return json;  // Return json to preserve message field
      }
      return json;
    },
    activate_editor(path, payload) {
      this.files[path] = payload;
      if (!this.editor) {
        this.editor = ace.edit("editor");
        var dashboardTheme = document.documentElement.getAttribute("data-theme") || "";
        var aceTheme = dashboardTheme === "AlienLight"
          ? "ace/theme/chrome"
          : "ace/theme/pastel_on_dark";
        this.editor.setTheme(aceTheme);
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
      let vue = this;     
      if(this.selected_filename)
        this.files[this.selected_filename] = this.editor.getValue();

      let lpath = path.toLowerCase();
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
              let url = '../load/'+path;
              if(this.selected_type != 'text') url = '../load_bytes/'+path;
              Q.get(url).then(r=>{
                  let payload = vue.to_json(r).payload;
                  if (payload) this.activate_editor(path, payload);
              });
          }
      }
      this.selected_filename = path;
    },

    modal_dismiss() {
      this.modal = null;
    },

    change_password() {
      if (!this.modal || !this.modal.form) return;
      const old_pwd = this.modal.form.old_password;
      const pwd = this.modal.form.password;
      const pwd_confirm = this.modal.form.password_confirm;
      
      if (!old_pwd) {
        alert('Current password is required');
        return;
      }
      if (!pwd) {
        alert('New password cannot be empty');
        return;
      }
      if (pwd !== pwd_confirm) {
        alert('Passwords do not match');
        return;
      }
      
      Q.post('../change_password', { old_password: old_pwd, password: pwd })
        .then(r => {
          const response = this.to_json(r);
          if (response.status === 'success') {
            alert('Password changed successfully');
            this.modal_dismiss();
          } else {
            alert('Failed to change password: ' + (response.message || 'Unknown error'));
          }
        })
        .catch((e) => {
          alert('Error changing password: ' + e);
        });
    },

    open_change_password_modal() {
      this.modal = {
        title: 'Change Dashboard Password',
        color: 'orange',
        message: 'Enter your current password and new password',
        form_name: 'change-password',
        form: {old_password: '', password: '', password_confirm: ''},
        buttons: [
          {text: 'Change', onclick: () => {this.change_password();}},
          {text: 'Cancel', onclick: () => {this.modal_dismiss();}}
        ]
      };
    },

    copy_system_info() {
      if (!this.info || this.info.length === 0) return;
      
      // Format system info as text
      let text = 'System Information\n';
      text += '==================\n\n';
      for (let i = 0; i < this.info.length; i++) {
        text += this.info[i].name + ': ' + this.info[i].version + '\n';
      }
      
      // Copy to clipboard
      navigator.clipboard.writeText(text).then(() => {
        alert('System information copied to clipboard');
      }).catch(() => {
        alert('Failed to copy to clipboard');
      });
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
      let path = this.selected_filename;
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
      let path = this.selected_filename;
      this.files[path] = this.editor.getValue();
      Q.post('../save/'+path, this.files[path]).then(()=>this.file_saved());
    },

    download_selected_app() {
      let url = '../packed/py4web.app.' + this.selected_app.name + '.zip?' + (new Date()).getTime();
      window.open(url, 'Download');
    },

    deploy_selected_app() {
      this.confirm('Deploy App','green','Ready to deploy',()=>{});
    },

    confirm(title, color, message, callback) {
      let buttons = [{text: 'Yes', onclick:callback}, {text:'No', onclick: this.modal_dismiss}];
      this.modal = {title: title, color:color, message:message, buttons:buttons};
    },

    close_dialog_error() {
      this.last_error = "";
    },

    process_new_app() {
      let form = this.modal.form;
      if(!form.name) alert('An app name must be provided');
      else if(!form.name.match(/^[\w_]+$/)) alert('Invalid file name');
      else if(form.mode=='new' && this.apps.map((a)=>{return a.name;}).indexOf(form.name)>=0) {
        alert('Cannot create an app with this name. It already exists');
      } else {
        Q.post('../new_app', form).then(()=>this.reload());
      }
    },

    process_new_file() {
      let app_name = this.selected_app.name;
      let form = this.modal.form;
      if(!form.filename) { alert('A file name must be provided'); return; }
      /*reload entire page needed to see the new file listed*/
      Q.post('../new_file/'+app_name+'/'+form.filename).then(()=>{
        this.walk = [];
        let payload = this.to_json(r).payload;
        if (!payload) return;
        Q.get('../walk/'+app_name).then(r=>{this.walk=payload;});
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
      let app_name = this.selected_app.name;
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
      let name = this.selected_filename;
      this.confirm("Delete File","blue","Do you really want to delete "+name+"?",()=>{
        this.modal_dismiss();
        Q.post('../delete/'+name).then((r)=>{this.to_json(r); this.init();});
      });
    },

    delete_selected_app() {
      let name = this.selected_app.name;
      this.confirm("Delete App","blue","Do you really want to delete "+name+"?",()=>{
        this.modal_dismiss();
        Q.post('../delete_app/'+name).then((r)=>{this.to_json(r); this.init();});
      });
    },

    reload_info() {
      Q.get('../info').then(r=>{
        this.info=this.to_json(r).payload || [];
      });
    },

    reload_apps() {
      Q.get('../apps').then(r=>{
        this.apps=this.to_json(r).payload || [];
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
        this.routes=this.to_json(r).payload || [];
      });
    },

    reload_tickets() {
      this.tickets = [];
      Q.get('../tickets').then(r=>{
        this.tickets = this.to_json(r).payload || [];
      });
    },

    reload_files() {
      if (!this.selected_app) {
        return;
      }
      this.walk = { files: [], dirs: [] }; // Always reset to an object
      let name = this.selected_app.name;
      Q.get('../walk/' + name).then(r => {
        const payload = this.to_json(r).payload;
        if (payload && Array.isArray(payload.files) && Array.isArray(payload.dirs)) {
          this.walk = payload;
        } else {
          this.walk = { files: [], dirs: [] };
        }
      });
      Q.get('../rest/' + name).then(r => { this.databases = this.to_json(r).databases || []; });
      this.selected_filename = null;
    },

    clear_tickets() {
      this.tickets = [];
      Q.get('../clear').then(()=>this.reload_tickets());
    },
    
    login() {
      Q.post('../login', { password: this.password })
        .then (r => {
          if (this.to_json(r).user) {
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
    },

    handleEdit(appName) {
      const selected = this.apps.filter((appItem) => appItem.name === appName)[0] || null;
      if (!selected) {
        return;
      }
      this.select(selected);
    }
  },
  
  filters: {
    mil: (value) => { return (''+value).substring(0,6); }
  }
});

// **Register globally for recursion to work**
app.component('TreeFiles', TreeFiles);

app.vue = app.mount('#target');