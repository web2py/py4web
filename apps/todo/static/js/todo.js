// initialize the app
const app = {data:{}, methods:{}};
// data exposed to the view
app.api = '/' + window.location.href.split('/')[3] + '/api';
app.data.items = [];
app.data.input = '';
// methods exposed to the view
app.methods.edit = function(item_id) { };
app.methods.remove = function(item_id) { 
    Q.delete(app.api + '/' + item_id).then(function(){
            app.vue.items=app.vue.items.filter(function(item){
                    return item.id!=item_id;
                }); 
        });
};
app.methods.save = function(item_id) { 
    const data = {};
    data.info = app.vue.input;
    Q.post(app.api, data).then(function(res){            
        if (app.vue.input) app.vue.items.unshift({id:res.json().id, info: app.vue.input});
        app.vue.input='';
    });
};

// start the app (Vue 3 version)
app.vue = Vue.createApp({
    data() {            // data is now a function
        return app.data;
    },
    methods: app.methods
}).mount("#vue");

Q.get(app.api).then(function(res){
    app.vue.items = res.json().items;
});
