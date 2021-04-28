(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-4b68bb8a"], {
        1631: function(t, s, a) {
            "use strict";
            var e = a("e347"),
                i = a.n(e);
            i.a
        },
        e347: function(t, s, a) {},
        f036: function(t, s, a) {
            "use strict";
            a.r(s);
            var e = function() {
                    var t = this,
                        s = t.$createElement,
                        a = t._self._c || s;
                    return a("div", {
                        staticClass: "cards"
                    }, [a("div", {
                        staticClass: "cards-container row d-flex wrap align--start"
                    }, [t._l(t.listLoops, (function(s) {
                        return [a("div", {
                            key: s + "-1",
                            staticClass: "flex xs12 sm6"
                        }, [a("va-card", {
                            attrs: {
                                title: t.$t("cards.title.default")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-2",
                            staticClass: "flex xs12 sm6"
                        }, [a("va-card", {
                            attrs: {
                                title: t.$t("cards.title.withControls")
                            }
                        }, [a("template", {
                            slot: "actions"
                        }, [a("va-button", {
                            attrs: {
                                icon: "fa fa-refresh"
                            }
                        }), a("va-button", {
                            attrs: {
                                icon: "fa fa-gear"
                            }
                        })], 1), t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")], 2)], 1), a("div", {
                            key: s + "-3",
                            staticClass: "flex xs12 sm6"
                        }, [a("va-card", [a("template", {
                            slot: "header"
                        }, [a("va-icon", {
                            attrs: {
                                name: "fa fa-cogs mr-3",
                                color: "success"
                            }
                        }), a("h5", {
                            staticClass: "mt-0 mb-0"
                        }, [t._v(t._s(t.$t("cards.title.customHeader")))])], 1), t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")], 2)], 1), a("div", {
                            key: s + "-4",
                            staticClass: "flex xs12 sm6"
                        }, [a("va-card", [a("p", [t._v(t._s(t.$t("cards.title.withoutHeader")))]), t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-5",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                image: "https://picsum.photos/300/200/?image=1043",
                                title: t.$t("cards.title.withImage")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentText")) + " ")])], 1), a("div", {
                            key: s + "-6",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                overlay: "",
                                titleOnImage: "",
                                image: "https://picsum.photos/300/200/?image=898",
                                title: t.$t("cards.title.withTitleOnImage")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentText")) + " ")])], 1), a("div", {
                            key: s + "-7",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                overlay: "",
                                titleOnImage: "",
                                image: "https://picsum.photos/300/200/?image=898",
                                title: t.$t("cards.title.withCustomTitleOnImage")
                            }
                        }, [a("va-button", {
                            staticClass: "ma-0",
                            attrs: {
                                slot: "header"
                            },
                            slot: "header"
                        }, [t._v(" Read More ")])], 1)], 1), a("div", {
                            key: s + "-8",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                stripe: "danger",
                                title: t.$t("cards.title.withStripe")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-9",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                color: "success"
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-10",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                color: "danger"
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-11",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                stripe: "info",
                                title: t.$t("cards.title.withStripe")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentTextLong")) + " ")])], 1), a("div", {
                            key: s + "-12",
                            staticClass: "flex xs12 sm6 lg4 xl3"
                        }, [a("va-card", {
                            attrs: {
                                overlay: "",
                                titleOnImage: "",
                                image: "https://picsum.photos/300/200/?image=1067",
                                title: t.$t("cards.title.withTitleOnImage")
                            }
                        }, [t._v(" " + t._s(t.$t("cards.contentText")) + " ")])], 1)]
                    }))], 2), a("va-inner-loading", {
                        staticClass: "flex-center py-3",
                        attrs: {
                            loading: t.isLoading
                        }
                    }, [a("va-button", {
                        on: {
                            click: function(s) {
                                return t.addCards()
                            }
                        }
                    }, [t._v(" Show More ")])], 1)], 1)
                },
                i = [],
                c = {
                    name: "cards",
                    data: function() {
                        return {
                            listLoops: 1,
                            counter: 1,
                            isLoading: !1
                        }
                    },
                    methods: {
                        addCards: function() {
                            var t = this;
                            this.isLoading = !0, setTimeout((function() {
                                t.isLoading = !1, ++t.listLoops
                            }), 1e3)
                        }
                    }
                },
                l = c,
                r = (a("1631"), a("2877")),
                n = Object(r["a"])(l, e, i, !1, null, null, null);
            s["default"] = n.exports
        }
    }
]);
