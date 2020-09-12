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
            search_placeholder: '',
            search_text: '',
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

    grid.methods.do_search = function () {
        let self = this;
        self.page = 1; // Restart from page 1 for every search.
        self.load();
    };

    grid.methods.clear_search = function () {
        let self = this;
        self.search_text = "";
        self.page = 1;
        self.load();
    };

    grid.methods.search_enter = function (e) {
        let self = this;
        if (e.keyCode === 13) {
            self.do_search();
            e.target.blur();
        }
    }

    grid.methods.do_sort = function (cell_idx) {
        let self = this;
        let header = self.rows[0];
        for (let cell of header.cells) {
            if (cell._idx === cell_idx) {
                // Toggles sort of selected cell.
                if (cell.sortable) {
                    cell.sort = cell.sort + 1;
                    if (cell.sort === 2) {
                        cell.sort = -1;
                    }
                }
            } else {
                // Other cells are not sorted.
                cell.sort = 0;
            }
        }
        self.page = 1;
        self.load();
    }

    grid.methods.load = function () {
        // In use, self will correspond to the data of the table,
        // as this is called via grid.methods.load
        let self = this;
        let sort_order = null;
        if (self.rows.length > 0) {
            sort_order = JSON.stringify(self.rows[0].cells.map(c => c.sort));
        }
        axios.get(self.server_url,
            {params: {
                    page: self.page,
                    q: self.search_text,
                    sort_order: sort_order,
                }}).then(function(res) {
            self.page = res.data.page;
            self.has_more = res.data.has_more;
            self.has_previous = self.page > 1;
            self.search_placeholder = res.data.search_placeholder;
            let rows = res.data.rows;
            grid.enumerate(rows);
            for (let r of rows) {
                grid.enumerate(r.cells);
                for (let c of r.cells) {
                    if (!c.sort) {
                        // Note that on purpose, we can have sorted fields
                        // that are not sortable via a UI click.
                        c.sort = 0;
                    }
                }
            }
            self.rows = rows;
        })
    };

    grid.methods.incpage = function (inc) {
        let self = this;
        i = parseInt(inc);
        if ((i > 0 && self.has_more) || (i < 0 && self.has_previous)) {
            self.page += parseInt(inc);
            self.load();
        }
    };

    Q.register_vue_component('grid', 'components/grid/grid.html', function(template) {
            grid.template = template.data;
            return grid;
        });
})();
