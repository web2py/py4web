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
    select_folder(path, name) { this.$root.select_folder(path + '/' + name); return true; },
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
      reloadingApps: false,
      toggled_folders: {},
      selected_folder: null,
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
      show_system_info: false,
      show_classic_tickets: false,
      classic_tickets_loading: false,
      classic_tickets_error: "",
      classic_tickets_sort_key: 'timestamp',
      classic_tickets_sort_dir: 'desc',
      routes_sort_key: 'rule',
      routes_sort_dir: 'asc'
    };
  },
  
  mounted() {
    if (this.user) this.init();
  },
  
  methods: {
    go_to_main_dashboard() {
      window.location.href = '../index?_=' + Date.now();
    },

    is_classic_theme() {
      const htmlTheme = document.documentElement.getAttribute('data-theme');
      return (htmlTheme || SELECTED_THEME || '') === 'Classic';
    },

    select(appobj) {
      this.selected_app = appobj;
      this.selected_folder = null;
      this.reload_files();
    },

    select_folder(path) {
      this.selected_folder = path || null;
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

    format_route_metric(value) {
      const numeric = Number(value);
      return Number.isFinite(numeric) ? numeric.toFixed(2) : '0.00';
    },

    set_routes_sort(key) {
      if (this.routes_sort_key === key) {
        this.routes_sort_dir = this.routes_sort_dir === 'asc' ? 'desc' : 'asc';
        return;
      }
      this.routes_sort_key = key;
      this.routes_sort_dir = (key === 'time' || key === 'calls' || key === 'errors') ? 'desc' : 'asc';
    },

    get_sorted_routes_for_selected_app() {
      const selectedName = this.selected_app && this.selected_app.name;
      const routeList = (selectedName && this.routes[selectedName]) ? this.routes[selectedName] : [];
      const sortKey = this.routes_sort_key;
      const sortDir = this.routes_sort_dir === 'asc' ? 1 : -1;
      const metricKeys = new Set(['time', 'calls', 'errors']);
      return [...routeList].sort((left, right) => {
        let leftValue = left?.[sortKey];
        let rightValue = right?.[sortKey];
        if (metricKeys.has(sortKey)) {
          leftValue = Number(leftValue || 0);
          rightValue = Number(rightValue || 0);
        } else {
          leftValue = String(leftValue || '').toLowerCase();
          rightValue = String(rightValue || '').toLowerCase();
        }
        if (leftValue < rightValue) return -1 * sortDir;
        if (leftValue > rightValue) return 1 * sortDir;
        return 0;
      });
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

      const lastSlash = path.lastIndexOf('/');
      this.selected_folder = lastSlash > 0 ? path.substring(0, lastSlash) : null;

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

    open_forgotten_password_modal() {
      this.modal = {
        title: 'Forgotten Administrator Password',
        color: 'orange',
        message: 'Run "py4web set_password" from your py4web project folder and follow the prompt to create a new administrator password. Then return to this page and sign in with the new password.',
        buttons: [
          {text: 'Close', onclick: () => {this.modal_dismiss();}}
        ]
      };
    },

    show_message(title, message, color='blue') {
      this.modal = {
        title: title,
        color: color,
        message: message,
        buttons: [{text: 'Close', onclick: () => {this.modal_dismiss();}}]
      };
    },

    build_system_info_text() {
      if (!this.info || this.info.length === 0) return '';
      let text = 'System Information\n';
      text += '==================\n\n';
      for (let i = 0; i < this.info.length; i++) {
        text += this.info[i].name + ': ' + this.info[i].version + '\n';
      }
      return text;
    },

    copy_system_info() {
      const text = this.build_system_info_text();
      if (!text) return;
      
      // Copy to clipboard
      navigator.clipboard.writeText(text).then(() => {
        alert('System information copied to clipboard');
      }).catch(() => {
        alert('Failed to copy to clipboard');
      });
    },

    async save_system_info() {
      const text = this.build_system_info_text();
      if (!text) {
        this.show_message('Save details', 'No system information available to save', 'orange');
        return;
      }

      const now = new Date();
      const pad = (value) => String(value).padStart(2, '0');
      const filename = 'py4web-system-details-' +
        now.getFullYear() +
        pad(now.getMonth() + 1) +
        pad(now.getDate()) + '-' +
        pad(now.getHours()) +
        pad(now.getMinutes()) +
        pad(now.getSeconds()) +
        '.txt';

      if (window.showSaveFilePicker && window.isSecureContext) {
        try {
          const handle = await window.showSaveFilePicker({
            suggestedName: filename,
            types: [
              {
                description: 'Text Files',
                accept: {'text/plain': ['.txt']}
              }
            ]
          });
          const writable = await handle.createWritable();
          await writable.write(text);
          await writable.close();
          this.show_message(
            'Save details',
            'System information saved locally as ' + (handle.name || filename),
            'green'
          );
        } catch (e) {
          if (e && e.name === 'AbortError') return;
          this.show_message('Save details', 'Failed to save system information locally', 'red');
        }
        return;
      }

      try {
        const blob = new Blob([text], {type: 'text/plain;charset=utf-8'});
        const blobUrl = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = blobUrl;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(blobUrl);
        this.show_message(
          'Save details',
          'Download started. If your browser does not ask for a location, check your default Downloads folder for ' + filename,
          'blue'
        );
      } catch (e) {
        this.show_message('Save details', 'Failed to save system information locally', 'red');
      }
    },

    reload(name) {
      this.modal_dismiss();
      this.loading = true;
      this.reloadingApps = true;
      const endpoint = name ? '../reload/' + name : '../reload';
      Q.get(endpoint)
        .then((r) => {
          const payload = this.to_json(r);
          if (payload && payload.status === 'error') {
            this.show_message('Reload', payload.message || 'Reload failed', 'orange');
          }
        })
        .catch(() => {
          this.show_message(
            'Reload',
            'Reload endpoint is unavailable in this mode. Refreshed dashboard data only.',
            'orange'
          );
        })
        .finally(() => {
          this.reloadingApps = false;
          this.init();
        });
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

    handle_upload_file(inputId = 'upload-file') {
      Q.upload_helper(inputId, (name, data)=>{
        if (!this.modal || !this.modal.form) return;
        this.modal.form.file = data || '';
        if (name) {
          const filename = this.modal.form.filename || '';
          if (!filename) {
            this.modal.form.filename = name;
          } else if (filename.endsWith('/')) {
            this.modal.form.filename = filename + name;
          }
        }
        if (this.modal.form_name === 'create-app') {
          this.modal.form.type = "upload";
        }
      });
    },

    process_upload_new_file() {
      const app_name = this.selected_app && this.selected_app.name;
      const form = this.modal && this.modal.form ? this.modal.form : {};
      if (!app_name) {
        alert('No application selected');
        return;
      }
      if (!form.filename) {
        alert('A target file path is required');
        return;
      }
      if (!form.file) {
        alert('Please choose a local file to upload');
        return;
      }

      Q.post('../new_file/' + app_name + '/' + form.filename, { file: form.file }).then((r) => {
        const response = this.to_json(r);
        if (response.status === 'error') {
          alert(response.message || 'Upload failed');
          return;
        }
        this.modal_dismiss();
        this.reload_files();
        const classicRefresh = window.classicRefreshCurrentFiles;
        if (this.is_classic_theme() && typeof classicRefresh === 'function') {
          classicRefresh();
        }
      });
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
      const app_name = this.selected_app && this.selected_app.name;
      if (!app_name) {
        alert('Please select an app first');
        return;
      }

      const appPrefix = app_name + '/';
      let defaultPath = '';
      if (this.selected_folder) {
        defaultPath = this.selected_folder.startsWith(appPrefix)
          ? this.selected_folder.substring(appPrefix.length)
          : this.selected_folder;
      }
      const defaultFilename = defaultPath
        ? (defaultPath.endsWith('/') ? defaultPath : defaultPath + '/')
        : '';

      this.modal = {
        title: 'Upload New File',
        color: 'blue',
        message: 'Choose a local file and destination path under ' + app_name,
        form_name: 'upload-file',
        form: { filename: defaultFilename, file: '' },
        buttons: [
          { text: 'Upload', onclick: () => { this.process_upload_new_file(); } },
          { text: 'Close', onclick: this.modal_dismiss }
        ]
      };
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
      this.selected_folder = null;
      let name = this.selected_app.name;
      const walkUrl = '../walk/' + name + '?_=' + Date.now();
      Q.get(walkUrl).then(r => {
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

    load_classic_tickets() {
      this.classic_tickets_loading = true;
      this.classic_tickets_error = "";
      this.tickets = [];
      Q.get('../tickets')
        .then((r) => {
          const response = this.to_json(r);
          if (response.status === 'error') {
            this.classic_tickets_error = response.message || 'Unable to load tickets';
            return;
          }
          this.tickets = response.payload || [];
        })
        .catch(() => {
          this.classic_tickets_error = 'Unable to load tickets';
        })
        .finally(() => {
          this.classic_tickets_loading = false;
        });
    },

    set_classic_tickets_sort(key) {
      if (this.classic_tickets_sort_key === key) {
        this.classic_tickets_sort_dir = this.classic_tickets_sort_dir === 'asc' ? 'desc' : 'asc';
        return;
      }
      this.classic_tickets_sort_key = key;
      this.classic_tickets_sort_dir = key === 'timestamp' ? 'desc' : 'asc';
    },

    get_sorted_classic_tickets() {
      const sortKey = this.classic_tickets_sort_key;
      const sortDir = this.classic_tickets_sort_dir === 'asc' ? 1 : -1;
      return [...this.tickets].sort((left, right) => {
        let leftValue = left?.[sortKey];
        let rightValue = right?.[sortKey];

        if (sortKey === 'count') {
          leftValue = Number(leftValue || 0);
          rightValue = Number(rightValue || 0);
        } else {
          leftValue = String(leftValue || '').toLowerCase();
          rightValue = String(rightValue || '').toLowerCase();
        }

        if (leftValue < rightValue) return -1 * sortDir;
        if (leftValue > rightValue) return 1 * sortDir;
        return 0;
      });
    },

    open_classic_tickets_view() {
      this.show_system_info = false;
      this.show_classic_tickets = true;
      this.load_classic_tickets();
    },

    back_classic_tickets_view() {
      this.show_classic_tickets = false;
      this.classic_tickets_loading = false;
      this.classic_tickets_error = "";
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
      this.show_classic_tickets = false;
      if (typeof window.classicEditHandler === 'function') {
        window.classicEditHandler(appName, 'files');
        return;
      }
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
window.py4webDashboardApp = app.vue;