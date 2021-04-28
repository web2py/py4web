(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-c016350e"], {
        "10c4": function(e, t, a) {},
        "17d6": function(e, t, a) {
            "use strict";
            a.r(t);
            var r = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("div", {
                        staticClass: "tree-view sets-list row"
                    }, [a("div", {
                        staticClass: "flex md12 xs12"
                    }, [a("div", {
                        staticClass: "row"
                    }, [a("div", {
                        staticClass: "small-set flex lg6 xs12"
                    }, [a("va-card", {
                        attrs: {
                            title: e.$t("treeView.basic")
                        }
                    }, [a("tree-view-basic-preview")], 1)], 1), a("div", {
                        staticClass: "small-set flex lg6 xs12"
                    }, [a("va-card", {
                        attrs: {
                            title: e.$t("treeView.icons")
                        }
                    }, [a("tree-view-icons-preview")], 1)], 1)]), a("div", {
                        staticClass: "row"
                    }, [a("div", {
                        staticClass: "small-set flex lg6 xs12"
                    }, [a("va-card", {
                        attrs: {
                            title: e.$t("treeView.advanced")
                        }
                    }, [a("tree-view-advanced-preview")], 1)], 1), a("div", {
                        staticClass: "small-set flex lg6 xs12"
                    }, [a("va-card", {
                        attrs: {
                            title: e.$t("treeView.editable")
                        }
                    }, [a("tree-view-editable-preview")], 1)], 1)]), a("div", {
                        staticClass: "row"
                    }, [a("div", {
                        staticClass: "small-set flex lg6 xs12"
                    }, [a("va-card", {
                        attrs: {
                            title: e.$t("treeView.selectable")
                        }
                    }, [a("tree-view-selectable-preview")], 1)], 1)])])])
                },
                n = [],
                s = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("va-tree-root", [a("va-tree-category", {
                        attrs: {
                            label: "Electronics"
                        }
                    }, [a("va-tree-node", [e._v("Cellphones")]), a("va-tree-node", [e._v("Camera Body Kits")]), a("va-tree-node", [e._v("External HDDs")])], 1), a("va-tree-category", {
                        attrs: {
                            isOpen: "",
                            label: "Products"
                        }
                    }, [a("va-tree-category", {
                        attrs: {
                            label: "Cables"
                        }
                    }, [a("va-tree-node", [e._v("Audio")]), a("va-tree-node", [e._v("Video")]), a("va-tree-node", [e._v("Optical")])], 1), a("va-tree-node", [e._v("Monitors")]), a("va-tree-node", [e._v("Keyboards")])], 1), a("va-tree-category", {
                        attrs: {
                            label: "Apparel"
                        }
                    }, [a("va-tree-node", [e._v("Jackets")]), a("va-tree-node", [e._v("Pants")]), a("va-tree-node", [e._v("Skirts")])], 1)], 1)
                },
                i = [],
                o = {
                    name: "tree-view-basic-preview"
                },
                l = o,
                c = a("2877"),
                v = Object(c["a"])(l, s, i, !1, null, null, null),
                d = v.exports,
                u = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("va-tree-root", [a("va-tree-category", {
                        attrs: {
                            label: "Images",
                            icon: "ion ion-md-images"
                        }
                    }, [a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-image"
                        }
                    }, [e._v(" sick_catz_cuddling.jpg ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-image"
                        }
                    }, [e._v(" pins-and-needles.jpg ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-image"
                        }
                    }, [e._v(" avatar_50x50.jpg ")])], 1), a("va-tree-category", {
                        attrs: {
                            label: "Music",
                            isOpen: "",
                            icon: "ion ion-md-star-outline"
                        }
                    }, [a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-musical-notes"
                        }
                    }, [e._v(" Taylor_swift_hello.mp3 ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-musical-notes"
                        }
                    }, [e._v(" straight_to_the_bank.wav ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-musical-notes"
                        }
                    }, [e._v(" imagine_dragons_promo.mp3 ")])], 1), a("va-tree-category", {
                        attrs: {
                            label: "Miscellaneous",
                            icon: "ion ion-md-list"
                        }
                    }, [a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-grid"
                        }
                    }, [e._v(" dump.sql ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-help"
                        }
                    }, [e._v(" unknown-file ")]), a("va-tree-node", {
                        attrs: {
                            icon: "ion ion-md-key"
                        }
                    }, [e._v(" secure.key ")])], 1)], 1)
                },
                m = [],
                p = {
                    name: "tree-view-icons-preview"
                },
                _ = p,
                w = Object(c["a"])(_, u, m, !1, null, null, null),
                b = w.exports,
                f = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("va-tree-root", [a("va-tree-category", {
                        attrs: {
                            label: "Products"
                        }
                    }, e._l(e.products, (function(t) {
                        return a("va-tree-node", {
                            key: t.id
                        }, [a("va-checkbox", {
                            attrs: {
                                slot: "checkbox"
                            },
                            slot: "checkbox",
                            model: {
                                value: t.selected,
                                callback: function(a) {
                                    e.$set(t, "selected", a)
                                },
                                expression: "product.selected"
                            }
                        }), e._v(" " + e._s(t.name) + " ")], 1)
                    })), 1), a("va-tree-category", {
                        attrs: {
                            isOpen: "",
                            label: "Electronics"
                        }
                    }, e._l(e.electronics, (function(t) {
                        return a("va-tree-node", {
                            key: t.id
                        }, [a("va-checkbox", {
                            attrs: {
                                slot: "checkbox"
                            },
                            slot: "checkbox",
                            model: {
                                value: t.selected,
                                callback: function(a) {
                                    e.$set(t, "selected", a)
                                },
                                expression: "electronic.selected"
                            }
                        }), e._v(" " + e._s(t.name) + " ")], 1)
                    })), 1)], 1)
                },
                x = [],
                g = {
                    name: "tree-view-selectable-preview",
                    data: function() {
                        return {
                            electronics: [{
                                id: 1,
                                name: "Cellphones",
                                selected: !1
                            }, {
                                id: 2,
                                name: "Camera Body Kits",
                                selected: !1
                            }, {
                                id: 3,
                                name: "External HDDs",
                                selected: !1
                            }],
                            products: [{
                                id: 4,
                                name: "Cables",
                                selected: !1
                            }, {
                                id: 5,
                                name: "Monitors",
                                selected: !1
                            }, {
                                id: 6,
                                name: "Keyboards",
                                selected: !1
                            }]
                        }
                    }
                },
                k = g,
                y = Object(c["a"])(k, f, x, !1, null, null, null),
                h = y.exports,
                C = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("div", {
                        staticClass: "tree-view-advanced-preview"
                    }, [a("div", {
                        staticClass: "tree-view-advanced-preview__buttons"
                    }, [a("va-button", {
                        on: {
                            click: function(t) {
                                return e.$refs.treeView.expand()
                            }
                        }
                    }, [e._v(" EXPAND ALL ")]), a("va-button", {
                        on: {
                            click: function(t) {
                                return e.$refs.treeView.collapse()
                            }
                        }
                    }, [e._v(" COLLAPSE ALL ")])], 1), a("va-tree-root", {
                        ref: "treeView"
                    }, [a("va-tree-category", {
                        attrs: {
                            label: "Electronics"
                        }
                    }, [a("va-tree-node", [e._v("Cellphones")]), a("va-tree-node", [e._v("Camera Body Kits")]), a("va-tree-node", [e._v("External HDDs")])], 1), a("va-tree-category", {
                        attrs: {
                            isOpen: "",
                            label: "Products"
                        }
                    }, [a("va-tree-category", {
                        attrs: {
                            label: "Cables"
                        }
                    }, [a("va-tree-node", [e._v("Audio")]), a("va-tree-node", [e._v("Video")]), a("va-tree-node", [e._v("Optical")])], 1), a("va-tree-node", [e._v("Monitors")]), a("va-tree-node", [e._v("Keyboards")])], 1), a("va-tree-category", {
                        attrs: {
                            label: "Apparel"
                        }
                    }, [a("va-tree-node", [e._v("Jackets")]), a("va-tree-node", [e._v("Pants")]), a("va-tree-node", [e._v("Skirts")])], 1)], 1)], 1)
                },
                E = [],
                P = {
                    name: "tree-view-advanced-preview"
                },
                $ = P,
                V = (a("f031"), Object(c["a"])($, C, E, !1, null, null, null)),
                O = V.exports,
                A = function() {
                    var e = this,
                        t = e.$createElement,
                        a = e._self._c || t;
                    return a("va-tree-root", [a("va-tree-category", {
                        attrs: {
                            label: "Electronics"
                        }
                    }, e._l(e.electronics, (function(t) {
                        return a("va-tree-node", {
                            key: t.id
                        }, [a("va-input", {
                            staticClass: "mb-0",
                            model: {
                                value: t.name,
                                callback: function(a) {
                                    e.$set(t, "name", a)
                                },
                                expression: "electronic.name"
                            }
                        })], 1)
                    })), 1), a("va-tree-category", {
                        attrs: {
                            isOpen: "",
                            label: "Products"
                        }
                    }, [e._l(e.products, (function(t) {
                        return a("va-tree-node", {
                            key: t.id
                        }, [a("div", {
                            staticClass: "flex row align--center"
                        }, [a("va-input", {
                            staticClass: "mb-0",
                            model: {
                                value: t.name,
                                callback: function(a) {
                                    e.$set(t, "name", a)
                                },
                                expression: "product.name"
                            }
                        }), a("va-icon", {
                            staticClass: "ml-2 pa-1 shrink",
                            staticStyle: {
                                cursor: "pointer"
                            },
                            attrs: {
                                name: "ion ion-md-close",
                                color: "info"
                            },
                            nativeOn: {
                                click: function(a) {
                                    return e.removeProduct(t)
                                }
                            }
                        })], 1)])
                    })), a("va-tree-node", [a("va-button", {
                        staticClass: "mb-2",
                        on: {
                            click: function(t) {
                                return e.addProduct()
                            }
                        }
                    }, [e._v(" Add new product ")])], 1)], 2)], 1)
                },
                D = [],
                j = {
                    name: "tree-view-editable-preview",
                    data: function() {
                        return {
                            electronics: [{
                                id: 1,
                                name: "Cellphones"
                            }, {
                                id: 2,
                                name: "Camera Body Kits"
                            }, {
                                id: 3,
                                name: "External HDDs"
                            }],
                            products: [{
                                id: 4,
                                name: "Cables"
                            }, {
                                id: 5,
                                name: "Monitors"
                            }, {
                                id: 6,
                                name: "Keyboards"
                            }]
                        }
                    },
                    methods: {
                        addProduct: function() {
                            this.products.push({
                                id: Math.floor(1e5 * Math.random()),
                                name: "New product"
                            })
                        },
                        removeProduct: function(e) {
                            this.products = this.products.filter((function(t) {
                                return t !== e
                            }))
                        }
                    }
                },
                K = j,
                M = Object(c["a"])(K, A, D, !1, null, null, null),
                L = M.exports,
                T = {
                    name: "tree-view",
                    components: {
                        TreeViewEditablePreview: L,
                        TreeViewAdvancedPreview: O,
                        TreeViewSelectablePreview: h,
                        TreeViewIconsPreview: b,
                        TreeViewBasicPreview: d
                    },
                    data: function() {
                        return {
                            treeViewData: {}
                        }
                    }
                },
                B = T,
                S = Object(c["a"])(B, r, n, !1, null, null, null);
            t["default"] = S.exports
        },
        f031: function(e, t, a) {
            "use strict";
            var r = a("10c4"),
                n = a.n(r);
            n.a
        }
    }
]);
