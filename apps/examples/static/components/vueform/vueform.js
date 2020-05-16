(function(){

    var form = {
        props: ['url', 'check_url', 'redirect_url'],
        data: null,
        methods: {}
    };

    form.data = function() {
        var data = {
            server_url: this.url,
            validation_url: this.check_url,
            redir_url: this.redirect_url,
            fields: [],
            readonly: false,
        };
        form.methods.load.call(data);
        return data;
    };

    form.decorate = function (a) {
        let k=0;
        a.map(function(e) {
            e._idx = k++;
            e._modified = false;
        });
    };

    form.methods.load = function () {
        // This method loads the structure and values for the form.
        let self = this;
        axios.get(self.server_url, {params: {page: self.page}})
            .then(function(res) {
                set_results(self, res);
            })
    };

    function set_results(self, res) {
        // This either sets new values (including errors) for the form,
        // or it implements the redirection that one may wish after the post.
        if (res.data.ok) {
            window.location = self.redir_url;
        } else {
            self.fields = res.data.fields;
            self.readonly = res.data.readonly;
            form.decorate(self.fields);
        }
    }

    form.methods.submit = function () {
        let self = this;
        let d = {};
        for (var i = 0; i < self.fields.length; i++) {
            d[self.fields[i].name] = self.fields[i].value;
        }
        axios.post(self.server_url, d).then(function (res) {
            set_results(self, res);
        })
    };

    form.methods.mark_field = function (field_idx) {
        let self = this;
        let field = self.fields[field_idx];
        field._modified = true;
    };

    form.methods.validate_field = function (field_idx) {
        let self = this;
        let field = self.fields[field_idx];
        if (field._modified) {
            field._modified = false;
            axios.post(self.validation_url, {
                name: field.name,
                value: field.value
            }).then(function (res) {
                field.error = res.data.error;
            });
        }
    };

    utils.register_vue_component('vueform', 'components/vueform/vueform.html',
        function(template) {
            form.template = template.data;
            return form;
        });
})();
