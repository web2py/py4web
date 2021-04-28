(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0e521d"], {
        "92d2": function(l, e, s) {
            "use strict";
            s.r(e);
            var a = function() {
                    var l = this,
                        e = l.$createElement,
                        s = l._self._c || e;
                    return s("div", {
                        staticClass: "sliders"
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex md12"
                    }, [s("va-card", {
                        attrs: {
                            title: l.$t("sliders.slider")
                        }
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.simple")))]), s("va-slider", {
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--danger mb-3",
                        style: {
                            color: this.$themes.danger
                        }
                    }, [l._v(l._s(l.$t("sliders.value")))]), s("va-slider", {
                        attrs: {
                            color: "danger",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex d-flex align--end xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            label: l.$t("sliders.label"),
                            color: "info",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex d-flex align--end xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            label: l.$t("sliders.label"),
                            "invert-label": !0,
                            color: "warning",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.labelPlusIcon")))]), s("va-slider", {
                        attrs: {
                            icon: "fa fa-music"
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--danger mb-3",
                        style: {
                            color: this.$themes.danger
                        }
                    }, [l._v(l._s(l.$t("sliders.labelPlusIcon")))]), s("va-slider", {
                        attrs: {
                            color: "danger",
                            "icon-right": "fa fa-check-circle",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.pins")))]), s("va-slider", {
                        attrs: {
                            pins: "",
                            step: 20
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--warning mb-3",
                        style: {
                            color: this.$themes.warning
                        }
                    }, [l._v(l._s(l.$t("sliders.pinsAndValue")))]), s("va-slider", {
                        attrs: {
                            pins: "",
                            step: 10,
                            color: "warning",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            "value-visible": "",
                            "with-input": ""
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            color: "info",
                            icon: "fa fa-volume-off",
                            "icon-right": "fa fa-volume-up"
                        },
                        model: {
                            value: l.value,
                            callback: function(e) {
                                l.value = e
                            },
                            expression: "value"
                        }
                    })], 1)])])], 1), s("div", {
                        staticClass: "flex md12"
                    }, [s("va-card", {
                        attrs: {
                            title: l.$t("sliders.range")
                        }
                    }, [s("div", {
                        staticClass: "row"
                    }, [s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.simple")))]), s("va-slider", {
                        attrs: {
                            range: ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--danger mb-3",
                        style: {
                            color: this.$themes.danger
                        }
                    }, [l._v(l._s(l.$t("sliders.value")))]), s("va-slider", {
                        attrs: {
                            range: "",
                            color: "danger",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex d-flex align--end xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            range: "",
                            label: l.$t("sliders.label"),
                            color: "info",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex d-flex align--end xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            range: "",
                            label: l.$t("sliders.label"),
                            "invert-label": !0,
                            color: "warning",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.labelPlusIcon")))]), s("va-slider", {
                        attrs: {
                            range: "",
                            icon: "fa fa-music"
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--danger mb-3",
                        style: {
                            color: this.$themes.danger
                        }
                    }, [l._v(l._s(l.$t("sliders.labelPlusIcon")))]), s("va-slider", {
                        attrs: {
                            range: "",
                            color: "danger",
                            "icon-right": "fa fa-check-circle",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title mb-3",
                        style: {
                            color: this.$themes.primary
                        }
                    }, [l._v(l._s(l.$t("sliders.pins")))]), s("va-slider", {
                        attrs: {
                            range: "",
                            pins: "",
                            step: 20
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("div", {
                        staticClass: "title title--warning mb-3",
                        style: {
                            color: this.$themes.warning
                        }
                    }, [l._v(l._s(l.$t("sliders.pinsAndValue")))]), s("va-slider", {
                        attrs: {
                            range: "",
                            pins: "",
                            step: 10,
                            color: "warning",
                            "value-visible": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            range: "",
                            "with-input": ""
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1), s("div", {
                        staticClass: "flex xs12 lg6 xl4 mb-2"
                    }, [s("va-slider", {
                        attrs: {
                            range: "",
                            color: "info",
                            icon: "fa fa-volume-off",
                            "icon-right": "fa fa-volume-up"
                        },
                        model: {
                            value: l.value2,
                            callback: function(e) {
                                l.value2 = e
                            },
                            expression: "value2"
                        }
                    })], 1)])])], 1)])])
                },
                i = [],
                t = {
                    name: "sliders",
                    data: function() {
                        return {
                            value: 90,
                            value2: [20, 60]
                        }
                    }
                },
                v = t,
                r = s("2877"),
                c = Object(r["a"])(v, a, i, !1, null, null, null);
            e["default"] = c.exports
        }
    }
]);
