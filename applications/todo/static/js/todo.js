//
// do not edit this function, it is just here to expose a standard API
//
var initialize = function() {
    var self  = {}; 
    self.data = {};
    self.methods = {};
    self.filters = {};
    self.start = function() {
        self.vue = new Vue({el: '#vue', data: self.data, methods: self.methods, filters: self.filters});
        self.on_load();
    };
    return self;
};    

// initialize the app
var myapp = initialize();
// data exposed to the view
myapp.api = '/' + window.location.href.split('/')[3] + '/api';
myapp.data.items = [];
myapp.data.input = '';
// methods exposed to the view
myapp.methods.edit = function(item_id) { };
myapp.methods.remove = function(item_id) { 
    axios.delete(myapp.api + '/' + item_id).then(function(){
            myapp.vue.items=myapp.vue.items.filter(function(item){
                    return item.id!=item_id;
                }); 
        });
};
myapp.methods.save = function(item_id) { 
    axios.post(myapp.api, {info: myapp.vue.input}).then(function(res){            
            if (myapp.vue.input) myapp.vue.items.unshift({id:res.data.id, info: myapp.vue.input});
            myapp.vue.input='';
        });
};
// special methods
myapp.on_load = function() {  
    axios.get(myapp.api).then(function(res){ 
            myapp.vue.items = res.data.items; 
        });
};
// start the app
myapp.start();
