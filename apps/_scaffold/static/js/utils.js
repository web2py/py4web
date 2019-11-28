
// ASSUMES Vue and Axios

if (!String.prototype.format) {
    // allow "bla {a} bla {b}".format({'a': 'hello', 'b': 'world'})
    String.prototype.format = function (args) {
        return this.replace(/\{([^}]+)\}/g, function(match, k) { return args[k]; });
    };
}

utils = {};

utils.getQuery = function(source) {
    source = source || window.location.search.substring(1);
    var vars={}, items=source.split('&');
    items.map(function(item){
            var pair = item.split('=');
            vars[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
        });
    return vars;
};

utils.getCookie = function(name) {
    var cookie=RegExp(""+name+"[^;]+").exec(document.cookie);
    if (!cookie) return null;
    return decodeURIComponent(!!cookie ? cookie.toString().replace(/^[^=]+./,"") : "");
};

utils.getSessionToken = function() {
    var app_name = utils.getCookie('app_name');
    return utils.getCookie(app_name + '_session');
};

// clone any object
utils.clone = function(data) { return JSON.parse(JSON.stringify(data)); };

// load data from localstorage
utils.retrieve = function(key) {
    try {
        return JSON.parse(window.localStorage.getItem(key));
    } catch(e) {
        return null;
    }
};

// save data to localstorage
utils.store = function(key, value) {
    window.localStorage.setItem(key, JSON.stringify(value));
};

// load components lazily: https://vuejs.org/v2/guide/components.html#Async-Components
utils.register_vue_component = function (name, src, onload) {
    Vue.component(name, function (resolve, reject) {
            axios.get(src).then(function(data) { resolve(onload(data)); });
        });
};

// passes binary data to callback on drop of file in element_id
utils.upload_helper = function(element_id, callback) {
    // function from http://jsfiddle.net/eliseosoto/JHQnk/
    var element = document.getElementById(element_id);
    if(element) {
        var files = element.files;
        var reader = new FileReader();
        if (files && files[0]) {
            reader.onload = function(event) {
                var b64 = btoa(event.target.result);
                callback(files[0].name, b64);
            };
            reader.readAsBinaryString(files[0]);
        } else {
            callback();
        }
    }
};

// Internationalization helper
// Usage:
// T.translations = {'dog': {0: 'no cane', 1: 'un case', 2: '{n} cani', 10: 'tanti cani'}};
// T('dog').format({n: 5}) -> "5 cani"
var T = function(text) {
    var obj = {
        toString: function() { return T.format(text); },
        format: function(args) { return T.format(text, args); }
    };
    return obj;
};
T.format = function(text, args) {
    args = args || {};
    translations = (T.translations||{})[text];
    var n = ('n' in args)?args.n:1;
    if (translations) {
        var k = 0;
        for (var key in translations) {                    
            var i = parseInt(key);
            if (i<=n) k = i; else break;
        }
        text = translations[k];
    }
    return text;
};

// a Vue app prototype
utils.app = function() {
    self = {};
    self.element_id = 'vue';
    self.data = { loading: 0, page: null, state: null };
    self.methods = {};
    self.filters = {};
    self.watch = {};
    self.pages = {};
    // translations
    self.methods.T = T;
    // toggles a variable
    self.methods.toggle = function(obj, key) { obj[key] = !obj[key] };
    // sets a variable
    self.methods.set = function(obj, key, value) { obj[key] = value; };
    // goto a given page and state (state should be 1 level deep dict
    self.methods.go = function(page, state, push) { 
        self.v.loading++; 
        var pagecall = self.pages[page];
        if (pagecall) pagecall(state, function(){
                if(push) {
                    var path = self.base + '/' + page;
                    if(state) for(var key in state) path += '/' + key + '/' + state[key];
                    window.history.pushState(self.v, page, path); 
                }
                self.v.loading--;
                self.v.page = page; 
                self.v.state = state;
            }); 
    };
    // Restores state when navigating history
    self.onpopstate = function(event) {
        for(var key in event.state) self.v[key] = event.state[key];
    };
    self.start = function(base) {
        self.base = base = base || window.location.href;;
        self.v = new Vue({el: '#' + self.element_id, 
                          data: self.data, 
                          methods: self.methods, 
                          watch: self.watch,
                          filters: self.filters});
        var parts = window.location.href.substr(base.length);
        var page = parts[0];
        var state = {};
        for(var i=1; i<parts.length; i+=2) state[parts[i]] = parts[i+1];
        self.v.go(page, state, false);
        window.onpopstate = self.onpopstate;
    };
    return self;
};
