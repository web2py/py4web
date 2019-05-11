(function(){

    var mtable = { props: ['url', 'filter', 'order'], data: null, methods: {}};
    
    mtable.data = function() {        
        var data = {url: this.url,
                    filter: this.filter || '',
                    order: this.order ||  '',
                    item: null,
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
        axios.get(url).then(function (res) {
                if(!length) self.table = res.data; 
                else self.table.items = self.table.items.concat(res.data.items);
                if(self.table.items.length==1) { self.item=self.table.items[0]; }
            });
    };
    
    mtable.methods.reorder = function (field) {
        if (this.order == '~' + field.name) this.order = null;
        else if (this.order == field.name) this.order = '~'+field.name;
        else this.order = field.name;
        this.table.items = [];
        this.load();
    };
    
    mtable.methods.open_create = function () {
        this.item = {};
        for(var field in this.model) this.item[field.name] = field.default||'';
    };
    
    mtable.methods.open_edit = function (item) {
        this.item = item;
    };
    
    mtable.methods.trash = function (item) {
        if (window.confirm("Really delete record?")) {
            console.log(this.table.items);
            let url = this.url + '/' + item.id;            
            this.table.items = this.table.items.filter((i)=>{return i.id != item.id;});
            axios.delete(url);
            if (item==this.item) this.item = null;
        }
    };
    
    mtable.methods.save = function (item) {
        let url = this.url;
        if (item.id) {
            url += '/' + item.id;
            axios.put(url, item);
        } else {
            axios.post(url);
        }
        this.item = null;
    };
    
    mtable.methods.close = function () {
        this.item = null;
    };
    
    mtable.methods.search = function () { 
        this.item = null;
        this.table.items = [];
        this.table.count = 0;
        this.load();
    };
    
    utils.register_vue_component('mtable', 'components/mtable.html', function(template) {        
            mtable.template = template.data;
            return mtable;
        });
})();
