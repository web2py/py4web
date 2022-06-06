(function(){

    var form = {
        props: ['url', 'check_url', 'cancel_url'],
        data: null,
        readonly: false,
        methods: {},
        computed: {some_error: has_some_error}
    };

    form.data = function() {
        var data = {
            server_url: this.url,
            validation_url: this.check_url,
            cancel_url_: this.cancel_url,
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

    form.methods.cancel = function () {
        let self = this;
        if (self.cancel_url_) {
            window.location = self.cancel_url_;
        }
    }

    function set_results(self, res) {
        // This either sets new values (including errors) for the form,
        // or it implements the redirection that one may wish after the post.
        if (res.data.redirect_url) {
            window.location = res.data.redirect_url;
        } else {
            self.fields = preprocess_fields(self, res.data.fields);
            console.log("Set fields:", self.fields);
            self.readonly = res.data.readonly;
            form.decorate(self.fields);
        }
    }

    function preprocess_fields(self, fields) {
        // Preprocesses the fields.
        for (let f of fields) {
            f.readonly = !f.writable;
            if (f.type === 'datetime') {
                if (f.value === null) {
                    f.time = null;
                    f.date = null;
                    f.date_readonly = null;
                    f.datetime_readonly = null;
                } else {
                    // console.log("converting time", f.value)
                    let m = luxon.DateTime.fromISO(f.value, {zone: "UTC"});
                    // console.log("parsed:", m);
                    let local_m = m.setZone(self.time_zone);
                    f.date = local_m.toFormat("y-MM-dd");
                    f.time = local_m.toLocaleString(luxon.DateTime.TIME_SIMPLE);
                    f.date_readonly = local_m.toLocaleString(luxon.DateTime.DATETIME_HUGE);
                    f.datetime_readonly = local_m.toLocaleString({
                        year: "numeric", month: "long",
                        day: "numeric", weekday: "long",
                        hour: "numeric", minute: "numeric",
                        timeZoneName: "short",
                    });
                }
            }
            if (f.type === 'date') {
                if (f.value == null) {
                    f.date = null;
                    f.date_readonly = null;
                } else {
                    let m = luxon.DateTime.fromISO(f.value, {zone: "UTC"});
                    f.date = m.toFormat("y-MM-dd");
                    f.date_readonly = m.toLocaleString(luxon.DateTime.DATE_HUGE);
                }
            }
            if (f.type === 'dropdown' && f.readonly) {
                f.text = '';
                for (let labtext of f.values) {
                    if (labtext.label === f.value) {
                        f.text = labtext.text;
                    }
                }
            }
        }
        return fields;
    }

    function has_some_error() {
        let self = this;
        for (let field of self.fields) {
            if (field.error) {
                return true;
            }
        }
        return false;
    }

    function get_datetime_luxon(field) {
        let field_date = "";
        let field_time = "";
        if (field.date !== null) {
            field_date = field.date;
        }
        if (field.time !== null) {
            field_time = field.time;
        }
        console.log("Getting date of:", field_date + " " + field_time);
        let d = Sugar.Date(field_date + " " + field_time);
        return luxon.DateTime.fromISO(d.raw.toISOString());
    }

    function get_datetime_field_value(field) {
        let local_t = get_datetime_luxon(field);
        let utc_t = local_t.setZone("utc");
        return utc_t.toISO();
    }

    function get_date_field_value(field) {
        // Parses the date, and puts it into the field value.
        let d = Sugar.Date(field.value);
        return Sugar.Date.format(d, "%Y-%m-%d");
    }

    function get_field_value(field) {
        if (field.type === "datetime") {
            return get_datetime_field_value(field);
        } else if (field.type === "date") {
            return get_date_field_value(field);
        } else {
            return field.value;
        }
    }

    form.methods.submit = function () {
        let self = this;
        let d = {};
        let ok = true;
        for (let field of self.fields) {
            try {
                d[field.name] = get_field_value(field);
            } catch (e) {
                field.error = "Invalid format";
                ok = false;
            }
        }
        if (ok) {
            console.log("Posting:", d);
            axios.post(self.server_url, d).then(function (res) {
                set_results(self, res);
            });
        }
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
            try {
                local_m = get_datetime_luxon(field);
                field.date_readonly = local_m.toLocaleString(luxon.DateTime.DATETIME_HUGE);
            } catch (e) {
                field.date_readonly = "";
            }
        }
    };

    form.methods.validate_field = function (field_idx) {
        let self = this;
        let field = self.fields[field_idx];
        if (field._modified) {
            // Gets a parsed value, so we fix the presentation of dates.
            let obtained = false;
            let parsed_value = null;
            try {
                parsed_value = get_field_value(field);
                obtained = true;
            } catch (e) {
                field.error = "Invalid format";
            }
            if (obtained) {
                field._modified = false;
                axios.post(self.validation_url, {
                    name: field.name,
                    value: parsed_value,
                }).then(function (res) {
                    field.error = res.data.error;
                });
            }
        }
    };

    Q.register_vue_component('vueform', 'components-bulma/vueform/vueform.html',
        function(template) {
            form.template = template.data;
            return form;
        });
})();
