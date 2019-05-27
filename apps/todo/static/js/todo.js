// initialize the app
var myapp = utils.app();
// data exposed to the view
myapp.api = '/' + window.location.href.split('/')[3] + '/api';
myapp.data.items = [];
myapp.data.input = '';
// methods exposed to the view
myapp.methods.edit = function(item_id) { };
myapp.methods.remove = function(item_id) { 
    axios.delete(myapp.api + '/' + item_id).then(function(){
            myapp.v.items=myapp.v.items.filter(function(item){
                    return item.id!=item_id;
                }); 
        });
};
myapp.methods.save = function(item_id) { 
    var data = {};
    data.info = myapp.v.input;
    axios.post(myapp.api, data).then(function(res){            
            if (myapp.v.input) myapp.v.items.unshift({id:res.data.id, info: myapp.v.input});
            myapp.v.input='';
        });
};

// start the app
myapp.start();
axios.get(myapp.api).then(function(res){
        myapp.v.items = res.data.items;
    });
