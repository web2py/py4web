(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d210669"], {
        b874: function(a, t, l) {
            "use strict";
            l.r(t);
            var e = function() {
                    var a = this,
                        t = a.$createElement,
                        l = a._self._c || t;
                    return l("div", {
                        staticClass: "rating"
                    }, [l("div", {
                        staticClass: "row"
                    }, [l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.singleIcon")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            color: "danger",
                            icon: "fa fa-bug"
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.twoIcons")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            icon: "fa fa-bell-slash",
                            emptyIcon: "fa fa-bell"
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.small")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            size: "small",
                            color: "warning"
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.large")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            size: "large",
                            color: "info"
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.numbers")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            numbers: ""
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1), l("div", {
                        staticClass: "flex md6 xs12"
                    }, [l("va-card", {
                        attrs: {
                            title: a.$t("rating.halves")
                        }
                    }, [l("va-rating", {
                        attrs: {
                            color: "warning",
                            emptyIcon: "fa fa-star-o",
                            halves: ""
                        },
                        model: {
                            value: a.value,
                            callback: function(t) {
                                a.value = t
                            },
                            expression: "value"
                        }
                    })], 1)], 1)])])
                },
                s = [],
                n = {
                    name: "rating",
                    data: function() {
                        return {
                            value: 2
                        }
                    }
                },
                i = n,
                r = l("2877"),
                c = Object(r["a"])(i, e, s, !1, null, null, null);
            t["default"] = c.exports
        }
    }
]);
