(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d21ed34"], {
        d6e1: function(a, l, e) {
            "use strict";
            e.r(l);
            var t = function() {
                    var a = this,
                        l = a.$createElement,
                        e = a._self._c || l;
                    return e("div", {
                        staticClass: "file-upload"
                    }, [e("div", {
                        staticClass: "row"
                    }, [e("div", {
                        staticClass: "flex xs12"
                    }, [e("va-card", {
                        attrs: {
                            title: a.$t("fileUpload.advancedMediaGallery")
                        }
                    }, [e("va-file-upload", {
                        attrs: {
                            type: "gallery",
                            "file-types": ".png, .jpg, .jpeg, .gif",
                            dropzone: ""
                        },
                        model: {
                            value: a.advancedGallery,
                            callback: function(l) {
                                a.advancedGallery = l
                            },
                            expression: "advancedGallery"
                        }
                    })], 1)], 1), e("div", {
                        staticClass: "flex xs12"
                    }, [e("va-card", {
                        attrs: {
                            title: a.$t("fileUpload.advancedUploadList")
                        }
                    }, [e("va-file-upload", {
                        attrs: {
                            dropzone: ""
                        },
                        model: {
                            value: a.advancedList,
                            callback: function(l) {
                                a.advancedList = l
                            },
                            expression: "advancedList"
                        }
                    })], 1)], 1), e("div", {
                        staticClass: "flex xs12"
                    }, [e("va-card", {
                        attrs: {
                            title: a.$t("fileUpload.single")
                        }
                    }, [e("va-file-upload", {
                        attrs: {
                            type: "single"
                        },
                        model: {
                            value: a.single,
                            callback: function(l) {
                                a.single = l
                            },
                            expression: "single"
                        }
                    })], 1)], 1), e("div", {
                        staticClass: "flex xs12"
                    }, [e("va-card", {
                        attrs: {
                            title: a.$t("fileUpload.mediaGallery")
                        }
                    }, [e("va-file-upload", {
                        attrs: {
                            type: "gallery",
                            "file-types": ".png, .jpg, .jpeg, .gif"
                        },
                        model: {
                            value: a.gallery,
                            callback: function(l) {
                                a.gallery = l
                            },
                            expression: "gallery"
                        }
                    })], 1)], 1), e("div", {
                        staticClass: "flex xs12"
                    }, [e("va-card", {
                        attrs: {
                            title: a.$t("fileUpload.uploadList")
                        }
                    }, [e("va-file-upload", {
                        model: {
                            value: a.list,
                            callback: function(l) {
                                a.list = l
                            },
                            expression: "list"
                        }
                    })], 1)], 1)])])
                },
                s = [],
                i = {
                    name: "file-upload",
                    data: function() {
                        return {
                            advancedGallery: [],
                            advancedList: [],
                            single: [],
                            gallery: [],
                            list: []
                        }
                    }
                },
                d = i,
                n = e("2877"),
                c = Object(n["a"])(d, t, s, !1, null, null, null);
            l["default"] = c.exports
        }
    }
]);
