"user strict";

// Allows "bla {a} bla {b}".format({'a': 'hello', 'b': 'world'})
if (!String.prototype.format) {
    String.prototype.format = function (args) {
        return this.replace(/\{([^}]+)\}/g, function (match, k) { return args[k]; });
    };
}

// Similar to jQuery $ but lighter
window.Q = function(sel, el) { return (el||document).querySelectorAll(sel); };

// Clone any object
Q.clone = function (data) { return JSON.parse(JSON.stringify(data)); };

Q.eval = function(text) { return eval('('+text+')'); };

// Given a url retuns an object with parsed query string
Q.get_query = function (source) {
    source = source || window.location.search.substring(1);
    var vars = {}, items = source.split('&');
    items.map(function (item) {
        var pair = item.split('=');
        vars[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1]);
    });
    return vars;
};

// a wrapper for fetch return a promise
Q.ajax = function(method, url, data, headers) {
    var options = {
        method: method,
        referrerPolicy: 'no-referrer',
    }
    if (data){
        if ( !(data instanceof FormData)){
            options.headers = {'Content-type': 'application/json'};
            data = JSON.stringify(data);
        }
        options.body = data;
    }
    if (headers) for(var name in headers) options.headers[name] = headers[name];
    return new Promise(function(resolve, reject) {
            fetch(url, options).then(function(res){
                    res.text().then(function(body){
                            res.data = body;                            
                            res.json = function(){return JSON.parse(body);};
                            resolve(res);
                        }, reject);}).catch(reject);
    });
}

Q.get = (url, headers) => Q.ajax("GET", url, null, headers);
Q.post = (url, data, headers) => Q.ajax("POST", url, data, headers);
Q.put = (url, data, headers) => Q.ajax("PUT", url, data, headers);
Q.delete = (url, headers) => Q.ajax("DELETE", url, null, headers);

// Gets a cookie value
Q.get_cookie = function (name) {
    var cookie = RegExp("" + name + "[^;]+").exec(document.cookie);
    if (!cookie) return null;
    return decodeURIComponent(!!cookie ? cookie.toString().replace(/^[^=]+./, "") : "");
};

// Load components lazily: https://vuejs.org/v2/guide/components.html#Async-Components
Q.register_vue_component = function (name, src, onload) {
    Vue.component(name, function (resolve, reject) {
            Q.ajax('GET', src).then(function(res){resolve(onload(res));});
        });
};

// Passes binary data to callback on drop of file in elem_id
Q.upload_helper = function (elem_id, callback) {
    // function from http://jsfiddle.net/eliseosoto/JHQnk/
    var elem = document.getElementById(elem_id);
    if (elem) {
        var files = elem.files;
        var reader = new FileReader();
        if (files && files[0]) {
            reader.onload = function (event) {
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
var T = function (text) {
    var obj = {
        toString: function () { return T.format(text); },
        format: function (args) { return T.format(text, args); }
    };
    return obj;
};

// Adds a convenience format method to the client-side translator object
T.format = function (text, args) {
    args = args || {};
    translations = (T.translations || {})[text];
    var n = ('n' in args) ? args.n : 1;
    if (translations) {
        var k = 0;
        for (var key in translations) {
            var i = parseInt(key);
            if (i <= n) k = i; else break;
        }
        text = translations[k];
    }
    return text;
};

// Originally inspired by  David Walsh (https://davidwalsh.name/javascript-debounce-function)
Q.debounce = (func, wait) => {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
};

// https://levelup.gitconnected.com/throttle-in-javascript-improve-your-applications-performance-984a4e020a3f
Q.throttle = (callback, delay) => {
    let throttleTimeout = null;
    let storedEvent = null;
    const throttledEventHandler = event => {
        storedEvent = event;
        const shouldHandleEvent = !throttleTimeout;
        if (shouldHandleEvent) {
            callback(storedEvent);
            storedEvent = null;
            throttleTimeout = setTimeout(() => {
                throttleTimeout = null;
                if (storedEvent) {
                    throttledEventHandler(storedEvent);
                }
            }, delay);
        }
    };
    return throttledEventHandler;
};

// Renders a JSON field with tags_input
Q.tags_input = function(elem, options) {
    if (typeof elem === typeof '') elem = Q(elem)[0];
    if (!options)
        options = Q.eval(elem.dataset.options||'{}');
    // preferred set of tags
    if (options.tags === undefined) options.tags = [];
    // set to false to only allow selecting one of the specified tags
    if (options.freetext === undefined) options.freetext = true;
    // how to transform typed tags to convert to actual tags
    if (options.transform === undefined) options.transform = function(x) {return x.toLowerCase();}
    // how to display tags
    if (options.labels === undefined) options.labels = {};
    // placeholder for the freetext field
    if (options.placeholder === undefined) options.placeholder = "";
    // autocomplete list attribute https://www.w3schools.com/tags/tag_datalist.asp
    if (options.autocomplete_list === undefined) options.autocomplete_list = null;
    var tags = options.tags;
    if(!elem) { console.log('Q.tags_input: elem '+selector+' not found'); return; }
    elem.type = "hidden";
    var repl = document.createElement('ul');
    repl.classList.add('tags-list')
    elem.parentNode.insertBefore(repl, elem);
    var keys = Q.eval(elem.value||'[]');
    keys.map(function(x) { if(tags.indexOf(x)<0) tags.push(x); });
    var fill = function(elem, repl) {
      repl.innerHTML = '';
      tags.forEach(function(x){
        var item = document.createElement('li');
        item.innerHTML = options.labels[x] || x;
        item.dataset.value = x;
        item.dataset.selected = keys.indexOf(x)>=0;
        repl.appendChild(item);
        item.onclick = function(evt){
          if(item.dataset.selected=='false') keys.push(x); else keys = keys.filter(function(y){ return x!=y; });
          item.dataset.selected = keys.indexOf(x)>=0;          
          elem.value = JSON.stringify(keys);
          elem.dispatchEvent(new Event('input', { bubbles: true }));
        };
      });
    };
    if (options.freetext) {
      var inp = document.createElement('input');
      elem.parentNode.insertBefore(inp, elem);
      inp.type = "text";
      inp.classList = elem.classList;
      inp.placeholder = options.placeholder;
      inp.setAttribute('list',  options.autocomplete_list);
      inp.onchange = function(evt) {
        inp.value.split(',').map(function(x){
	  x = options.transform(x.trim());
	  if (options.regex && !x.match(options.regex)) return;
          if (x && tags.indexOf(x)<0) tags.push(x); 
          if (x && keys.indexOf(x)<0) keys.push(x); 
        });
        inp.value = '';
        elem.value = JSON.stringify(keys);
        elem.dispatchEvent(new Event('input', { bubbles: true }));
        fill(elem, repl);
      };
    }
    fill(elem, repl);
};

// Password strenght calculator
Q.score_password = function(text) {
    var score = -10, counters = {};
    text.split('').map(function(c){counters[c]=(counters[c]||0)+1; score += 5/counters[c];});
    [/\d/, /[a-z]/, /[A-Z]/, /\W/].map(function(re){ score += re.test(text)?10:0; });
    return Math.round(Math.max(0, score));
};

// Apply the strength calculator to some input field
Q.score_input = function(elem, reference) {
    if (typeof elem === typeof '') elem = Q(elem)[0];
    reference = reference || 100;
    elem.style.backgroundPosition = 'center right';
    elem.style.backgroundRepeat = 'no-repeat';
    elem.onkeyup = elem.onchange = function(evt) {
      var score = Q.score_password(elem.value.trim());
      var r = Math.round(255*Math.max(0,Math.min(2-2*score/reference,1)));
      var g = Math.round(255*Math.max(0,Math.min(2*score/reference,1)));
      elem.style.backgroundImage = (score==0)?"":("url('"+'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="30"><circle cx="5" cy="5" r="3" stroke-width="0" fill="rgb('+r+','+g+',0)"/></svg>'+"')");
    };
};

// Traps a form submission
Q.trap_form = function (action, elem_id) {
    Q('#' + elem_id + ' form:not(.no-form-trap)').forEach(function (form) {
        var target = form.dataset['component_target'] || elem_id;
        form.dataset['component_target'] = target;
        var url = form.action;
        if (url === '' || url === '#' || url === void 0) url = action;
        var clickable = 'input[type=submit], input[type=image], button[type=submit], button:not([type])';        
        form.querySelectorAll(clickable).forEach(function (elem) {
            elem.onclick = function(event) {
                event.preventDefault();
                form.querySelectorAll(clickable).forEach(function(elem) {
                    elem.disabled = true;
                });
                var form_data = new FormData(form); // Allows file uploads.
                Q.load_and_trap('POST', url, form_data, target);            };
        });
    });
};

// loads a component via ajax and traps its forms
Q.load_and_trap = function (method, url, form_data, target) {
    method = (method || 'GET').toLowerCase();
    /* if target is not there, fill it with something that there isn't in the page*/
    if (target === void 0 || target === '') target = 'none';
    var onsuccess = function(res) {
        if (res.redirected) window.location = res.url;
        Q('#'+target)[0].innerHTML = res.data;
        Q.trap_form(url, target);
        var flash = res.headers.get('component-flash');
        if (flash) Q.flash(JSON.parse(flash));
    };
    var onerror = function(res) {
        alert('ajax error');
    };
    Q.ajax(method, url, form_data).then(onsuccess).catch(onerror);
};

// Loads all ajax components
Q.handle_components = function() {
    Q('ajax-component').forEach(function(elem) {
        Q.load_and_trap('GET', elem.attributes.url.value, null, elem.attributes.id.value);
    });    
};

// Displays flash messages
Q.handle_flash = function() {
    var elem = Q('flash-alerts')[0];
    var make_delete_handler = function(node) {
        return function(event) {
            node.parentNode.removeChild(node);
        };
    };
    var make_handler = function(elem) {
        return function (event) { 
            var node = document.createElement("div");
            node.innerHTML = '<div role="alert"><span class="close"></span>{0}</div>'.format([event.detail.message]);
            node = Q('[role="alert"]', node)[0];
            node.classList.add(event.detail.class||'info');
            elem.appendChild(node);
            Q('[role="alert"] .close',node)[0].onclick = make_delete_handler(node);
        };
    };
    if (elem) {
        elem.addEventListener('flash', make_handler(elem), false);
        Q.flash = function(detail) {elem.dispatchEvent(new CustomEvent('flash', {detail: detail}));};
        if (elem.dataset.alert) Q.flash(Q.eval(elem.dataset.alert));
    }    
};

Q.handle_components();
Q.handle_flash();
Q('input[type=text].type-list-string').forEach(function(elem){Q.tags_input(elem);});
Q('input[type=text].type-list-integer').forEach(function(elem){Q.tags_input(elem, {regex:/[-+]?[\d]+/});});
Q('input[name=password],input[name=new_password]').forEach(Q.score_input);
