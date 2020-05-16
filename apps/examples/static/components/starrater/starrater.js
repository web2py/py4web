(function(){

    var starrater = {
        props: ['url', 'callback_url'],
        data: null,
        methods: {}
    };

    starrater.data = function() {
        var data = {
            num_stars_display: 0,
            num_stars_assigned: 0,
            star_indices: [1, 2, 3, 4, 5],
            get_url: this.url,
            set_url: this.callback_url,
        };
        starrater.methods.load.call(data);
        return data;
    };

    starrater.methods.stars_over = function (star_idx) {
        // When hovering over a star, we display that many stars.
        console.log("Over:", star_idx);
        let self = this;
        self.num_stars_display = star_idx;
    };

    starrater.methods.stars_out = function () {
        // Sets the number of stars back to the number of true stars.
        let self = this;
        self.num_stars_display = self.num_stars_assigned;
    };

    starrater.methods.set_stars = function (star_idx) {
        // Sets and sends to the server the number of stars.
        let self = this;
        self.num_stars_assigned = star_idx;
        axios.get(self.set_url,
            {params: {num_stars: self.num_stars_assigned}});
    };

    starrater.methods.load = function () {
        // In use, self will correspond to the data of the table,
        // as this is called via grid.methods.load
        let self = this;
        axios.get(self.get_url)
            .then(function(res) {
                self.num_stars_assigned = res.data.num_stars;
                self.num_stars_display = res.data.num_stars;
            })
    };

    utils.register_vue_component('starrater', 'components/starrater/starrater.html',
        function(template) {
            starrater.template = template.data;
            return starrater;
        });
})();
