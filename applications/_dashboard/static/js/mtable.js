let app = {}; 
let init = (app) => {
    app.data = {
        loading: true,
        modal: null,
        item: null,
        message: 'test',
        app: '',
        dbname: '',
        tablename: '',
        base_url: '',
        order: null,
        table: {
            model:[],
            items:[]
        },
        filters: [{value: ''}]
    };
    app.modal_dismiss = () => {
        app.vue.modal = null;
    };
    app.confirm = (title, color, message, callback) => {
        var buttons = [{text: 'Yes', onclick:callback}, {text:'No', onclick: app.modal_dismiss}];
        app.vue.modal = {title: title, color:color, message:message, buttons:buttons};
    };
    app.methods = {};
    app.methods.toggle = function(obj, key) {
        obj[key] = !obj[key];
    };
    app.methods.load_more = () => {
        let hash = window.location.hash.substr(1);
        let length = app.vue.table.items.length;
        let url = app.vue.base_url + '?limit=20';
        if (length) url+='&offset='+length; else url+='&model=true';
        let filters = app.vue.filters.filter((f)=>{return f.value.trim() != ''});
        filters = filters.filter((f)=>{return f.value.trim();}).map((f)=>{                
                let parts = (f.value
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
        if (filters.length) url=url+'&'+filters.join('&');
        if (app.vue.order) url=url+'&order='+app.vue.order;
        axios.get(url).then((res)=>{
                if(!length) app.vue.table=res.data; 
                else app.vue.table.items=app.vue.table.items.concat(res.data.items);
                if(app.vue.table.items.length==1) { app.vue.item=app.vue.table.items[0]; }
            });
    };
    app.methods.reorder = (field) => {
        if (app.vue.order == '~' + field.name) app.vue.order = null;
        else if (app.vue.order == field.name) app.vue.order = '~'+field.name;
        else app.vue.order = field.name;
        app.vue.table.items = [];
        app.vue.load_more();
    };
    app.methods.open_create = () => {};
    app.methods.open_edit = (item) => {};
    app.methods.trash = (item) => {
        if (window.confirm("Really delete record?")) {
            let url = app.vue.base_url + '/' + item.id;            
            app.vue.table.items = app.vue.table.items.filter((i)=>{return i.id != item.id;});
            axios.delete(url);
            if (item==app.vue.item) app.vue.item = null;
        }
    };
    app.methods.save = () => {
        let item = app.vue.item;
        let url = app.vue.base_url;
        if (item.id) {
            url += '/' + item.id;
            axios.put(url, item);
        } else {
            axios.post(url);
        }
    };
    app.methods.add_filter = () => { app.vue.filters.push({value:''}); };
    app.methods.del_filter = (f) => { 
        if (app.vue.filters.length>1) app.vue.filters=app.vue.filters.filter((x)=>{return x!=f;}); 
        else app.vue.filters[0].value='';
        app.methods.search();
    };
    app.methods.search = () => { 
        app.vue.table.items = [];
        app.vue.table.count = 0;
        app.methods.load_more();
    };
    app.filters = {};
    app.vue = new Vue({el: '#target', data: app.data, methods: app.methods, filters:app.filters});
    app.init = () => {  
        app.vue.loading = false;
        var hash = window.location.hash.substr(1);
        var base = hash.split('?')[0];
        app.vue.base_url = '/_dashboard/dbapi/' + base;
        app.vue.app = base.split('/')[0];
        app.vue.dbname = base.split('/')[0];
        app.vue.tablename = base.split('/')[0];
        app.vue.load_more();
    };
    app.init();
};    

init(app);