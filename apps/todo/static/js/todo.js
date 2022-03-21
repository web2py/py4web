// initialize the app
var app = {data:{}, methods:{}};
// data exposed to the view
app.api = '/' + window.location.href.split('/')[3] + '/api';
app.data.items = [];
app.data.input = '';
// methods exposed to the view
app.methods.edit = function(item_id) { };
app.methods.remove = function(item_id) { 
    axios.delete(app.api + '/' + item_id).then(function(){
            app.vue.items=app.vue.items.filter(function(item){
                    return item.id!=item_id;
                }); 
        });
};
app.methods.save = function(item_id) { 
    var data = {};
    data.info = app.vue.input;
    axios.post(app.api, data).then(function(res){            
            if (app.vue.input) app.vue.items.unshift({id:res.data.id, info: app.vue.input});
            app.vue.input='';
        });
};

// start the app
app.vue = new Vue({el:"#vue", data: app.data, methods: app.methods});
axios.get(app.api).then(function(res){
        app.vue.items = res.data.items;
    });
