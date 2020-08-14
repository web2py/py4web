(function(){

    var uploader = {
        props: ['url'],
        data: null,
        methods: {}
    };

    uploader.data = function() {
        var data = {
            server_url: this.url,
        };
        return data;
    };

    uploader.enumerate = function (a) {
        // Adds an _idx attribute to each element of array a.
        let k=0;
        a.map(function(e) {e._idx = k++;});
    };

    uploader.methods.upload_file = function (event) {
        let self = this;
        // Reads the file.
        let input = event.target;
        let file = input.files[0];
        if (file) {
            let formData = new FormData();
            formData.append('file', file);
            axios.post(self.server_url, formData,
                {headers: {'Content-Type': 'multipart/form-data'}})
                .then(function () {
                    console.log("Uploaded");
                })
                .catch(function () {
                    console.log("Failed to upload");
                });
        }
    };

    utils.register_vue_component('fileupload', 'components/fileupload/fileupload.html', function(template) {
            uploader.template = template.data;
            return uploader;
        });
})();
