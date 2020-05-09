(function(){

    var grid = {
        props: ['url'],
        data: null,
        methods: {}
    };

    grid.data = function() {
        var data = {
            server_url: this.url,
            has_previous: false,
            has_more: false,
            page: 1,
            rows: [],
        };
        grid.methods.load.call(data);
        return data;
    };

    grid.enumerate = function (a) {
        // Adds an _idx attribute to each element of array a.
        let k=0;
        a.map(function(e) {e._idx = k++;});
    };

    grid.methods.load = function () {
        // In use, self will correspond to the data of the table,
        // as this is called via grid.methods.load
        let self = this;
        axios.get(self.server_url, {params: {page: self.page}})
            .then(function(res) {
                self.page = res.data.page;
                self.has_more = res.data.has_more;
                self.has_previous = self.page > 1;
                self.rows = res.data.rows;
                grid.enumerate(self.rows);
            })
    };

    grid.methods.incpage = function (inc) {
        i = parseInt(inc);
        if ((i > 0 && this.has_more) || (i < 0 && this.has_previous)) {
            this.page += parseInt(inc);
            this.load();
        }
    };

    utils.register_vue_component('grid', 'components/grid/grid.html', function(template) {
            grid.template = template.data;
            return grid;
        });
})();
