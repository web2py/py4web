(function(){

    var auth = { data: {}, methods: {}};
    
    auth.data = function() {        
        var parts = window.location.href.split('?')[0].split('/');
        var data = {
            plugins: [],
            allowed_actions: [],
            fields: [],
            page: parts[parts.length-1],
            next: utils.getQuery()['next'] || '../index',
            form: {},
            errors: {},
            user: null
        };
        return data;
    };
    
    auth.methods.go = function(page, no_history) {
        var self=this;
        console.log(this);
        if (['login','logout','403','404'].indexOf(page)<0 && 
            self.allowed_actions.indexOf('all')<0 && 
            self.allowed_actions.indexOf(page)<0) {
            page = '404';
        }
        var url_noqs = window.location.href.split('?')[0] ;
        var url = url_noqs.substring(0, url_noqs.lastIndexOf('/')) + '/' + page;
        if (page == 'login') url += '?next=' + self.next ;
        if (!no_history) history.pushState({'page': page}, null, url);
        if (page == '403' || page == '404') 
            self.form = {}
        else if (page == 'register') {
            self.form = {username: '', email:'', password:'', password2:'', first_name:'', last_name: ''};
            self.fields.map(function(f){ if(!(f.name in self.form)) {f._added=true; self.form[f.name]=''; } else f._added=false; });
        }
        else if (page == 'login') 
            self.form = {email:'', password:''};
        else if (page == 'request_reset_password') 
            self.form = {email:''};
        else if (page == 'reset_password') 
            self.form = {new_password:'', new_password2:''};
        else if (page == 'change_password') 
            self.form = {old_password:'', new_password:'', new_password2:''};
        else if (page == 'change_email') 
            self.form = {password: '', new_email:'', new_email2:''};
        else if (page == 'edit_profile') 
            self.form = {first_name:'', last_name: ''};
        else 
            self.form = {};
        self.errors = {}        
        for(var key in self.form) self.errors[key] = null;
        self.page = page;
    };

    auth.methods.submit_login = function() {
        var self = this;
        axios.post('../auth/api/login', self.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else window.location = self.next;
            });
    };
    auth.methods.submit_register = function() {
        var self = this;
        var form = utils.clone(this.form)
        delete form['password2']
        axios.post('../auth/api/register', form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else self.go('registered');
            });
    };
    auth.methods.submit_request_reset_password = function() {
        var self = this;
        axios.post('../auth/api/request_reset_password', this.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else self.go('request_sent');
            });
    };
    auth.methods.submit_reset_password = function() {
        var self = this;
        this.form.token = utils.getQuery()['token'];
        axios.post('../auth/api/reset_password', this.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else self.go('login');
            });        
    };
    auth.methods.submit_change_password = function() {
        var self = this;
        axios.post('../auth/api/change_password', this.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else window.location = self.next;
            });        
    };
    auth.methods.submit_change_email = function() {
        var self = this;
        axios.post('../auth/api/change_email', this.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else window.location = self.next;
            });        
    };
    auth.methods.submit_edit_profile = function() {
        var self = this;
        axios.post('../auth/api/profile', this.form).then(function(res){
                if(res.data.errors) self.errors = res.data.errors;
                else if (res.data.status=='error') alert(res.data.message);
                else window.location = self.next;
            });        
    };
    auth.created = function() {
        var self = this;
        window.addEventListener('popstate', function (event) {
                self.go(event.state.page, true);
            }, false);
        axios.get('../auth/api/config').then(function(res){
                self.plugins=res.data.plugins;
                self.allowed_actions=res.data.allowed_actions;
                self.fields=res.data.fields;
                self.go(self.page, true);
            });
    };
    utils.register_vue_component('auth', 'components/auth.html', function(template) {
            auth.template = template.data;
            return auth;
        });
    
})();
