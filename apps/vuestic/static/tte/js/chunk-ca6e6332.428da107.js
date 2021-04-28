(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-ca6e6332"], {
        "228e": function(t, s, e) {},
        "48a8": function(t, s, e) {
            "use strict";
            e.r(s);
            var i = function() {
                    var t = this,
                        s = t.$createElement,
                        e = t._self._c || s;
                    return e("va-card", {
                        staticClass: "sets-list",
                        attrs: {
                            title: t.$t("icons.title")
                        }
                    }, [e("div", {
                        staticClass: "row"
                    }, t._l(t.sets, (function(s, i) {
                        return e("div", {
                            key: i,
                            staticClass: "flex lg6 xs12 mb-4 sets-list__set fill-height"
                        }, [e("router-link", {
                            staticStyle: {
                                color: "inherit"
                            },
                            attrs: {
                                to: {
                                    path: s.href
                                }
                            }
                        }, [e("div", {
                            staticClass: "sets-list__set__content"
                        }, [e("div", {
                            staticClass: "sets-list__set__content__overlay flex-center pa-3 fill-height"
                        }, [e("va-button", {
                            attrs: {
                                to: {
                                    path: s.href
                                },
                                append: ""
                            }
                        }, [t._v(" " + t._s(s.name.toUpperCase()) + " ")])], 1), t._l(s.filteredLists, (function(i, a) {
                            return [2 !== i.length ? e("div", {
                                key: a,
                                staticClass: "row pa-3"
                            }, t._l(i, (function(i, a) {
                                return e("div", {
                                    key: a,
                                    staticClass: "flex xs2 flex-center"
                                }, [e("div", {
                                    staticClass: "sets-list__icon pa-3 flex-center vuestic-icon"
                                }, [e("va-icon", {
                                    attrs: {
                                        name: t.iconClass(s, i)
                                    }
                                }, [t._v(t._s(t.iconData(s, i)))])], 1)])
                            })), 0) : t._e(), 2 === i.length ? e("div", {
                                key: a,
                                staticClass: "row pa-3",
                                class: 1 === a ? "sets-list__set__content--middle" : ""
                            }, [e("div", {
                                staticClass: "flex xs2 flex-center"
                            }, [e("div", {
                                staticClass: "sets-list__icon pa-3 flex-center vuestic-icon"
                            }, [e("va-icon", {
                                attrs: {
                                    name: t.iconClass(s, i[0])
                                }
                            }, [t._v(t._s(t.iconData(s, i[0])))])], 1)]), e("div", {
                                staticClass: "flex xs8"
                            }), e("div", {
                                staticClass: "flex xs2 flex-center"
                            }, [e("div", {
                                staticClass: "sets-list__icon pa-3 flex-center vuestic-icon"
                            }, [e("va-icon", {
                                attrs: {
                                    name: t.iconClass(s, i[1])
                                }
                            }, [t._v(t._s(t.iconData(s, i[1])))])], 1)])]) : t._e()]
                        }))], 2)])], 1)
                    })), 0)])
                },
                a = [],
                n = {
                    name: "iconsList",
                    props: ["sets"],
                    methods: {
                        iconClass: function(t, s) {
                            return "material-icons" === t.prefix ? t.prefix : t.prefix + " " + t.prefix + "-" + s
                        },
                        iconData: function(t, s) {
                            return "material-icons" === t.prefix ? s : ""
                        }
                    }
                },
                c = n,
                l = (e("80fb"), e("2877")),
                r = Object(l["a"])(c, i, a, !1, null, null, null);
            s["default"] = r.exports
        },
        "80fb": function(t, s, e) {
            "use strict";
            var i = e("228e"),
                a = e.n(i);
            a.a
        }
    }
]);
