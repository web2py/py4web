(function(){

    var auth = { props: ['action'], data: null, methods: {}};
    
    auth.data = function() {        
        var data = {
            action: null,
            form: {},
            errors: {},
            user: null
        };
        return data;
    };
    
    auth.methods.go = function(action) {
        if (action == 'register') 
            this.form = {email:'', password:'', password2:'', first_name:'', last_name: ''};
        else if (action == 'login') 
            this.form = {email:'', password:''};
        else if (action == 'request_reset_password') 
            this.form = {email:''};
        else if (action == 'reset_password') 
            this.form = {new_password:'', new_password2:''};
        else if (action == 'change_password') 
            this.form = {old_password:'', new_password:'', new_password2:''};
        else if (action == 'change_email') 
            this.form = {password: '', new_email:'', new_email2:''};
        else if (action == 'edit_profile') 
            this.form = {first_name:'', last_name: ''};
        else return;
        this.errors = {}
        for(var key in this.form) this.errors[key] = null;
        this.action = action;
    };

    auth.methods.submit_login = function() {
        axios.post('/_scaffold/auth/login', this.form);
    };
    auth.methods.submit_register = function() {
        var form = utils.clone(this.form)
        delete form['password2']
        axios.post('/_scaffold/auth/register', form);
    };
    auth.methods.submit_request_reset_password = function() {
        alert('not implemented');
    };
    auth.methods.submit_reset_password = function() {
        alert('not implemented');
    };
    auth.methods.submit_change_password = function() {
        alert('not implemented');
    };
    auth.methods.submit_change_email = function() {
        alert('not implemented');
    };
    auth.methods.submit_edit_profile = function() {
        alert('not implemented');
    };
    
    utils.register_vue_component('auth', 'components/auth.html', function(template) {
            auth.template = template.data;
            return auth;
        });
    
})();
