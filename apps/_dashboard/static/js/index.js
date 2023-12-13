Vue.component('treefiles', {
        props: ['f','p'],
        template: '<div><ul class="files"><li v-for="name in f.files" v-on:click="select_file(p,name)"><a><tt>{{name}}</tt></a></li></ul><ul class="dirs"><li v-for="dir in f.dirs"><div class="accordion"><input type="checkbox" v-bind:id="combineb64(p,dir.name)"><label v-bind:for="combineb64(p,dir.name)" v-on:click="select_folder(p,dir.name)"><a><tt>{{dir.name}}</tt></a></label><div class="subfolder"><treefiles :f="dir.content" :p="combine(p,dir.name)"></treefiles></div></div></div>',
        methods: {
            select_file: (path, name) => { app.select_filename(path+'/'+name); },
            select_folder: (path, name) => { return true; },
            combine: (path, name) => { return path+'/'+name; },
            combineb64: (path, name) => { return btoa(path+'/'+name); },
        }
    });

let app = {}; 
let init = (app) => {
    app.data = {
        password: '',
        user: USER_ID,
        loading: true,
        message: 'test',
        info: [],
        apps: [],
        newapp: {name:''},
        routes: [],
        walk: [],
        databases: {},
        toggled_folders: {},
        selected_app: null,
        selected_filename: null,
        selected_type: 'text',
        selected_file_link: null,
        files: {},
        tickets:[],
        modal: null
    };
    app.select_app = (appobj) => {
        app.vue.selected_app = appobj;
        app.reload_files();
    };
    app.activate_editor = (path, payload) => {
        app.vue.files[path] = payload;
        app.editor.session.setValue(payload);
        var mode = app.modelist.getModeForPath(path).mode
        app.editor.session.setMode(mode);
    }
    app.select_filename = (path, force) => {                
        if(app.vue.selected_filename)
            app.vue.files[app.vue.selected_filename] = app.editor.getValue();

        var lpath = path.toLowerCase();
        if(lpath.endsWith('.mp4','.mov','.mpg','.mpeg')) app.vue.selected_type = 'video';
        else if(lpath.endsWith('.wav') ||
                lpath.endsWith('.mp3') ||
                lpath.endsWith('.ogg')) 
            app.vue.selected_type = 'audio';
        else if(lpath.endsWith('.png') ||
                lpath.endsWith('.gif') ||
                lpath.endsWith('.jpg')) 
            app.vue.selected_type = 'image';
        else 
            app.vue.selected_type = 'text';        
        app.vue.selected_file_link = '../load_bytes/'+path;
        if(app.vue.selected_type) {
            app.modelist = ace.require("ace/ext/modelist");
            app.editor = ace.edit("editor");
            app.editor.setTheme("ace/theme/pastel_on_dark");
            app.editor.$blockScrolling = Infinity;
            if(!force && path in app.vue.files) {
                app.activate_editor(path, app.vue.files[path]);
            } else {            
                var url = '../load/'+path;
                if(app.vue.selected_type != 'text') url = '../load_bytes/'+path;
                Q.get(url).then(r=>{
                        app.activate_editor(path, r.json().payload);
                    });
            }
        }
        app.vue.selected_filename = path;
    };
    app.modal_dismiss = () => {
        app.vue.modal = null;
    };
    app.reload = (name) => {
        app.modal_dismiss();
        app.vue.loading = true;        
        Q.get(name?'../reload/'+name:'../reload').then(r=>app.init());
    };
    app.gitlog = (name) => {
        window.open('../gitlog/'+name);
    };
    app.load_file = () => {
        var path = app.vue.selected_filename;
        app.select_filename(path, true);
    };
    app.file_saved = () => {
        // pass
    };
    app.save_file = () => {
	if(app.vue.selected_type != 'text') {
	    alert("Unable to save this file, it is not of type text");
	    return;
	}
        var path = app.vue.selected_filename;
        app.vue.files[path] = app.editor.getValue();
        Q.post('../save/'+path, app.vue.files[path]).then(r=>app.file_saved());
    };
    app.download_selected_app = () => {
        var url = '../packed/py4web.app.' + app.vue.selected_app.name + '.zip?' + (new Date()).getTime()
        window.open(url, 'Download');
    };
    app.deploy_selected_app = () => {
        app.confirm('Deploy App','green','Ready to deploy',()=>{});
    };
    app.confirm = (title, color, message, callback) => {
        var buttons = [{text: 'Yes', onclick:callback}, {text:'No', onclick: app.modal_dismiss}];
        app.vue.modal = {title: title, color:color, message:message, buttons:buttons};
    };
    app.process_new_app = () => {
        var form = app.vue.modal.form;
        console.log(form);
        if(!form.name) alert('An app namemust be provided');
        else if(!form.name.match(/^[\w_]+$/)) alert('Invalid file name');
        else if(form.mode=='new' && app.vue.apps.map((a)=>{return a.name;}).indexOf(form.name)>=0) {
            alert('Cannot create an app with this name. It already exists');
        } else {
            Q.post('../new_app', form).then(r=>app.reload());
        }
    };
    app.process_new_file = () => {
        var app_name = app.vue.selected_app.name;
        var form = app.vue.modal.form;
        if(!form.filename) { alert('An file name must be provided'); return; }
        /*reload entire page needed to see the new file listed*/
        Q.post('../new_file/'+app_name+'/'+form.filename).then(r=>{
                app.vue.walk = [];
                Q.get('../walk/'+app_name).then(r=>{app.vue.walk=r.json().payload;});
                app.modal_dismiss();
            });
    }; 
    app.handle_upload_file = () => {
        Q.upload_helper('upload-file', (name, data)=>{app.vue.modal.form.file=data; app.vue.modal.form.type = "upload";});
    };
    app.upload_new_app = ()=> {
        app.vue.modal = {
            title:'Create or Upload App', 
            color:'blue', 
            message:'',
            form_name: 'create-app',
            form: {type: 'scaffold', name: '', source: '', mode: 'new', file: ''},
            buttons: [{text: 'Create', onclick: function() {app.process_new_app();}}, 
                      {text:'Close', onclick: app.modal_dismiss}]
        }; 
    };
    app.create_new_file = ()=> {
        var app_name = app.vue.selected_app.name;
        app.vue.modal = {
            title:'Create a new file under ', 
            color:'green', 
            message:'Ex: somedir/some_file.py',
            form_name: 'create-file',
            form: {'filename': ''},
            buttons: [{text: 'Create', onclick: function() {app.process_new_file();}}, 
                      {text:'Close', onclick: app.modal_dismiss}]
        }; 
    };
    app.upload_new_file = ()=> {
        app.vue.modal ={title:'Upload New File', color:'blue',message:'[WORK IN PROGRESS]'};
    };
    app.delete_selected_file = () => {
        var name = app.vue.selected_filename;
        app.confirm("Delete File","blue","Do you really want to delete "+name+"?",()=>{
            app.modal_dismiss();
            Q.post('../delete/'+name).then(r=>app.init());
        });
    };
    app.delete_selected_app = () => {
        var name = app.vue.selected_app.name;
        app.confirm("Delete App","blue","Do you really want to delete "+name+"?",()=>{
            app.modal_dismiss();
            Q.post('../delete_app/'+name).then(r=>app.init());
        });
    };
    app.reload_info = () => {
        Q.get('../info').then(r=>{
            app.vue.info=r.json().payload || [];
        });
    };
    app.reload_apps = () => {
        Q.get('../apps').then(r=>{
            app.vue.apps=r.json().payload || []; app.update_selected();
        });
    };
    app.reload_routes = () => {
        Q.get('../routes').then(r=>{
                app.vue.routes=r.json().payload || [];
            });
    };
    app.reload_tickets = () => {
        app.vue.tickets = [];
        Q.get('../tickets').then(r=>{
                app.vue.tickets = r.json().payload || [];
            });
    };
    app.reload_files = () => {
        if (!app.vue.selected_app) return;
        app.vue.walk = [];
        var name = app.vue.selected_app.name;
        Q.get('../walk/'+name).then(r=>{app.vue.walk=r.json().payload;});
        Q.get('../rest/'+name).then(r=>{app.vue.databases=r.json().databases;});
        app.vue.selected_filename = null;
    }
    app.clear_tickets = () => {
        app.vue.tickets = [];
        Q.get('../clear').then(r=>app.reload_tickets());
    };
    app.login = () => {
        Q.post('../login', {'password': app.vue.password})
	    
	    .then(r=>{
                app.vue.password = '';
                if( r.user) {
                    app.vue.user = true;
                    app.init();
                }
		location.reload();    
            });
    };
    app.logout = () => {
        Q.post('../logout').then(r=>window.location.reload());
    };
    app.methods = {
        select: app.select_app,
        select_filename: app.select_filename,
        save_file: app.save_file,
        load_file: app.load_file,
        reload: app.reload,
        gitlog: app.gitlog,
        delete_selected_app: app.delete_selected_app,
        download_selected_app: app.download_selected_app,
        deploy_selected_app: app.deploy_selected_app,
        delete_selected_file: app.delete_selected_file,
        create_new_app: app.create_new_app,
        upload_new_app: app.upload_new_app,
        create_new_file: app.create_new_file,
        upload_new_file: app.upload_new_file,
        reload_tickets: app.reload_tickets,
        clear_tickets: app.clear_tickets,
        modal_dismiss: app.modal_dismiss,
        handle_upload_file: app.handle_upload_file,
        login: app.login,
        logout: app.logout
    };
    app.filters = {
        mil: (value) => { return (''+value).substring(0,6); }
    };
    app.vue = new Vue({el: '#target', data: app.data, methods: app.methods, 
                       filters:app.filters});    
    app.update_selected = () => {
        if(app.vue.selected_app) 
            app.vue.selected_app = app.vue.apps.filter((a) => {
                    return a.name==app.vue.selected_app.name;
                })[0];
    };
    app.init = () => {
        app.reload_info();
        app.reload_apps();
        app.reload_routes();
        app.reload_tickets();
        app.reload_files();
        setTimeout(()=>{app.vue.loading=false;}, 1000);
    };    
    if (USER_ID) app.init();
};    

init(app);
