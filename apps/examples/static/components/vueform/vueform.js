(function(){

    var form = {
        props: ['url', 'check_url'],
        data: null,
        readonly: false,
        methods: {}
    };

    form.data = function() {
        var data = {
            server_url: this.url,
            validation_url: this.check_url,
            fields: [],
            readonly: false,
            time_offset: luxon.DateTime.local().offsetNameShort,
            time_zone: luxon.DateTime.local().zoneName,
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
        if (res.data.redirect_url) {
            window.location = res.data.redirect_url;
        } else {
            self.fields = preprocess_fields(self, res.data.fields);
            self.readonly = res.data.readonly;
            form.decorate(self.fields);
        }
    }

    function preprocess_fields(self, fields) {
        // Preprocesses the fields.
        for (let f of fields) {
            f.readonly = !f.writable;
            if (f.type === 'datetime') {
                console.log("converting time", f.value)
                let m = luxon.DateTime.fromISO(f.value, {zone: "UTC"});
                let local_m = m.setZone(self.time_zone);
                f.date = local_m.toFormat("y-MM-dd");
                f.time = local_m.toFormat("HH:mm");
                f.date_readonly = local_m.toLocaleString(luxon.DateTime.DATE_HUGE);
                f.datetime_readonly = local_m.toLocaleString({
                    year: "numeric", month: "long",
                    day: "numeric", weekday: "long",
                    hour: "numeric", minute: "numeric",
                    timeZoneName: "short",
                });
            }
        }
        return fields;
    }

    function set_date_field_value(field) {
        // Reconstructs the field value, in UTC.
        local_t = luxon.DateTime.fromISO(field.date + "T" + field.time);
        utc_t = local_t.setZone("utc");
        field.value = utc_t.toString();
    }

    form.methods.submit = function () {
        let self = this;
        let d = {};
        for (field of self.fields) {
            if (field.type === "datetime") {
                set_date_field_value(field);
            }
            d[field.name] = field.value;
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

    form.methods.set_readable_date = function(field_idx) {
        let self = this;
        let field = self.fields[field_idx];
        if (field.type === 'datetime') {
            local_m = luxon.DateTime.fromISO(field.date);
            field.date_readonly = local_m.toLocaleString(luxon.DateTime.DATE_HUGE);
        }
    };

    form.methods.validate_field = function (field_idx) {
        let self = this;
        let field = self.fields[field_idx];
        if (field._modified) {
            if (field.type === 'datetime') {
                set_date_field_value(field);
            }
            field._modified = false;
            axios.post(self.validation_url, {
                name: field.name,
                value: field.value
            }).then(function (res) {
                field.error = res.data.error;
            });
        }
    };

    Q.register_vue_component('vueform', 'components/vueform/vueform.html',
        function(template) {
            form.template = template.data;
            return form;
        });
})();
