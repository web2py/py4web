let app = {}; 
let init = (app) => {
    app.data = {
        loading: true,
        modal: null,
        message: 'test',
        tablename: '',
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
    app.methods.load_more = () => {
        let hash = window.location.hash.substr(1);
        let length = app.vue.table.items.length;
        let url = '/_dashboard/dbapi/'+hash+'?limit=20';
        if (length) url+='&offset='+length; else url+='&model=true';
        let filters = app.vue.filters.filter((f)=>{return f.value.trim() != ''});
        filters = filters.filter((f)=>{return f.value.trim();}).map((f)=>{
                let parts = f.value.replace('==','.eq=').replace('!=','.ne=').replace('<','.lt=').replace('>','.gt=').replace('<=','.le=').replace('>=','.ge=').replace(' in ','.in=').split(/[=]/);
                return parts[0].replace(/ /ig,'')+'='+parts[parts.length-1].replace(/^ /,'');
            });
        if (filters.length) url=url+'&'+filters.join('&');
        axios.get(url).then((res)=>{
                if(!length) app.vue.table=res.data; else app.vue.table.items=app.vue.table.items.concat(res.data.items);
            });
    };
    app.methods.add_filter = () => { app.vue.filters.push({value:''}); };
    app.methods.del_filter = (f) => { 
        if (app.vue.filters.length>1) app.vue.filters=app.vue.filters.filter((x)=>{return x!=f;}); 
        else app.vue.filters[0].value='';
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
        app.vue.tablename = hash.split('?')[0];
        app.vue.load_more();
    };
    app.init();
};    

init(app);