(function(){

    var mtable = { props: ['url', 'filter', 'order', 'editable', 'create', 'deletable', 'render'], data: null, methods: {}};
    
    mtable.data = function() {        
        var data = {url: this.url,
                    busy: false,
                    filter: this.filter || '',
                    order: this.order ||  '',
                    errors: {},
                    item: null,
                    message: '',
                    reference_options: {},
                    table: { model: [], items: [], count: 0}};
        mtable.methods.load.call(data);
        return data;
    };
    
    mtable.methods.toggle = function(obj, key) {
        obj[key] = !obj[key];
    };
    mtable.methods.load = function() {
        let self = this;
        let length = this.table.items.length;
        let url = this.url + '?@limit=20';
        if (length) url+='&@offset='+length; else url+='&@model=true';
        let filters = self.filter.split(' and ').filter((f)=>{return f.trim() != ''});
        filters = filters.filter((f)=>{return f.trim();}).map((f)=>{                
                let parts = (f
                             .replace(/ equals? /,'==')
                             .replace('==','.eq=')
                             .replace('!=','.ne=')
                             .replace('<','.lt=')
                             .replace('>','.gt=')
                             .replace('<=','.le=')
                             .replace('>=','.ge=')
                             .replace(' in ','.in=')
                             .replace(' startswith ','~')
                             .replace('~','startswith=')
                             .split(/[=]/));
                let negate = false; 
                if (parts[0].substr(0,4) == 'not ') {
                    negate=true; 
                    parts[0]=parts[0].substr(4);
                }
                return ((negate?'not.':'') + 
                        parts[0].replace(/ /ig,'') +
                        '=' + parts[parts.length-1].replace(/^ /,''));
            });
        if (filters.length) url += '&'+filters.join('&');
        if (self.order) url += '&@order='+self.order;
        self.busy = true;
        axios.get(url).then(function (res) {
                self.busy = false;
                if(!length) self.table = res.data; 
                else self.table.items = self.table.items.concat(res.data.items);
            });
    };
    
    mtable.methods.reorder = function (field) {
        if (this.order == '~' + field.name) this.order = null;
        else if (this.order == field.name) this.order = '~'+field.name;
        else this.order = field.name;
        this.table.items = [];
        this.load();
    };

    mtable.methods.clear = function() {
        this.errors = {};
        this.item = null;
        this.message = '';
    }

    mtable.methods.open_create = function () {
        this.populate_reference_options();
        this.item = {};
        for(var field in this.model) this.item[field.name] = field.default||'';
    };
    
    mtable.methods.open_edit = function (item) {
        this.populate_reference_options();
        this.item = {};
        this.item = item;
    };

    mtable.methods.populate_reference_options = function(){
        let self = this;
        for(var field of this.table.model){
            console.log(field.name);
            if(field.type == "reference"){
                if (!(field.references in this.reference_options)){
                    Vue.set(this.reference_options, field.references, []);
                    let reference_table_url = self.url.split('/');                    
                    reference_table_url.pop()
                    reference_table_url.push(field.references)
                    reference_table_url = reference_table_url.join('/') + '?@options_list=true';
                    axios.get(reference_table_url).then(function (res) {
                        let url_components = res.config.url.split('?')[0].split('/');
                        self.reference_options[url_components[url_components.length - 1 ]] = res.data.items;
                     });
                    
                }
            }
        }
    }

    mtable.methods.parse_and_validate_json = function(event){
        try {
            event.target.style.borderColor = "";
            return JSON.parse(event.target.value);
        }
        catch (error) {
            event.target.style.borderColor = "#ff0000";
        }
    }

    mtable.methods.trash = function (item) {
        if (window.confirm("Really delete record?")) {
            let url = this.url + '/' + item.id;            
            this.table.items = this.table.items.filter((i)=>{return i.id != item.id;});
            axios.delete(url);
            if (item==this.item) this.item = null;
        }
    };
    
    mtable.methods.save = function (item) {
        let url = this.url;
        self.busy = true;
        if (item.id) {
            url += '/' + item.id;
            axios.put(url, item).then(mtable.handle_response('put', this),
                                      mtable.handle_response('put', this));
        } else {
            axios.post(url, item).then(mtable.handle_response('post', this),
                                       mtable.handle_response('post', this));
        }
    };

    mtable.handle_response = function(method, data) {
        self.busy = false;
        return function(res) {
            if (res.response) res = res.response; // deal with error weirdness
            if (method == 'post') {
                data.table.items = [];
                console.log(data);
                mtable.methods.load.call(data);
            }
            console.log('a');
            console.log(res);
            if (res.data.status == 'success') {
                data.clear();
            } else {
                console.log('b')
                data.errors = res.data.errors;
                data.message = res.data.message;
            }
            console.log('c');
        };
    };

    mtable.methods.close = function () {
        this.clear();
    };
    
    mtable.methods.search = function () { 
        this.clear();
        this.table.items = [];
        this.table.count = 0;
        this.load();
    };

    mtable.methods.go_ref_by = function(tablefield, item_id) {
        tablefield = (tablefield+'.id').split('.');
        var tablename = tablefield[0], fieldname = tablefield[1];
        var source = window.location.search.substring(1);
        var vars={}, items=source.split('&');
        items.map(function(item){
                var pair = item.split('=');
                vars[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
            });
        vars['tablename'] = tablename
        vars['filter'] = fieldname+'=='+item_id;
        source = Object.keys(vars).map(function(key){
                return key+'='+encodeURIComponent(vars[key]);
            }).join('&');
        window.location = window.location.href.split('?')[0]+'?'+source;
    };



    var scripts = document.getElementsByTagName('script');
    var src = scripts[scripts.length-1].src;
    var path = src.substr(0, src.length-3) + '.html';
    Q.register_vue_component('mtable', path, function(template) {        
            mtable.template = template.data;
            return mtable;
        });
})();
