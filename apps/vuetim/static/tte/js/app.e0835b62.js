(function(t) {
    function e(e) {
        for (var s, o, r = e[0], l = e[1], c = e[2], m = 0, u = []; m < r.length; m++) o = r[m], Object.prototype.hasOwnProperty.call(i, o) && i[o] && u.push(i[o][0]), i[o] = 0;
        for (s in l) Object.prototype.hasOwnProperty.call(l, s) && (t[s] = l[s]);
        d && d(e);
        while (u.length) u.shift()();
        return n.push.apply(n, c || []), a()
    }

    function a() {
        for (var t, e = 0; e < n.length; e++) {
            for (var a = n[e], s = !0, r = 1; r < a.length; r++) {
                var l = a[r];
                0 !== i[l] && (s = !1)
            }
            s && (n.splice(e--, 1), t = o(o.s = a[0]))
        }
        return t
    }
    var s = {},
        i = {
            app: 0
        },
        n = [];

    function o(e) {
        if (s[e]) return s[e].exports;
        var a = s[e] = {
            i: e,
            l: !1,
            exports: {}
        };
        return t[e].call(a.exports, a, a.exports, o), a.l = !0, a.exports
    }
    o.m = t, o.c = s, o.d = function(t, e, a) {
        o.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: a
        })
    }, o.r = function(t) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }, o.t = function(t, e) {
        if (1 & e && (t = o(t)), 8 & e) return t;
        if (4 & e && "object" === typeof t && t && t.__esModule) return t;
        var a = Object.create(null);
        if (o.r(a), Object.defineProperty(a, "default", {
                enumerable: !0,
                value: t
            }), 2 & e && "string" != typeof t)
            for (var s in t) o.d(a, s, function(e) {
                return t[e]
            }.bind(null, s));
        return a
    }, o.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t["default"]
        } : function() {
            return t
        };
        return o.d(e, "a", e), e
    }, o.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }, o.p = "/";
    var r = window["webpackJsonp"] = window["webpackJsonp"] || [],
        l = r.push.bind(r);
    r.push = e, r = r.slice();
    for (var c = 0; c < r.length; c++) e(r[c]);
    var d = l;
    n.push([0, "chunk-vendors"]), a()
})({
    0: function(t, e, a) {
        t.exports = a("56d7")
    },
    "0efd": function(t, e, a) {
        "use strict";
        var s = a("cd1f"),
            i = a.n(s);
        i.a
    },
    "4b83": function(t, e, a) {
        "use strict";
        var s = a("6de7"),
            i = a.n(s);
        i.a
    },
    "4ba2": function(t, e, a) {},
    5436: function(t, e, a) {
        "use strict";
        var s = a("738c"),
            i = a.n(s);
        i.a
    },
    "56d7": function(t, e, a) {
        "use strict";
        a.r(e);
        a("e623"), a("e379"), a("5dc8"), a("37e1");
        var s = a("2b0e"),
            i = a("8c4f"),
            n = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("router-view")
            },
            o = [],
            r = {},
            l = r,
            c = a("2877"),
            d = Object(c["a"])(l, n, o, !1, null, null, null),
            m = d.exports,
            u = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "wrapper",
                    class: {
                        "nav-open": t.$sidebar.showSidebar
                    }
                }, [a("notifications"), a("side-bar", {
                    attrs: {
                        "sidebar-item-color": t.sidebarBackground,
                        "sidebar-background-image": t.sidebarBackgroundImage
                    }
                }, [a("mobile-menu", {
                    attrs: {
                        slot: "content"
                    },
                    slot: "content"
                }), a("sidebar-link", {
                    attrs: {
                        to: "/dashboard"
                    }
                }, [a("md-icon", [t._v("dashboard")]), a("p", [t._v("Dashboard")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/user"
                    }
                }, [a("md-icon", [t._v("person")]), a("p", [t._v("User Profile")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/table"
                    }
                }, [a("md-icon", [t._v("content_paste")]), a("p", [t._v("Table list")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/typography"
                    }
                }, [a("md-icon", [t._v("library_books")]), a("p", [t._v("Typography")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/icons"
                    }
                }, [a("md-icon", [t._v("bubble_chart")]), a("p", [t._v("Icons")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/maps"
                    }
                }, [a("md-icon", [t._v("location_on")]), a("p", [t._v("Maps")])], 1), a("sidebar-link", {
                    attrs: {
                        to: "/notifications"
                    }
                }, [a("md-icon", [t._v("notifications")]), a("p", [t._v("Notifications")])], 1), a("sidebar-link", {
                    staticClass: "active-pro",
                    attrs: {
                        to: "/upgrade"
                    }
                }, [a("md-icon", [t._v("unarchive")]), a("p", [t._v("Upgrade to PRO")])], 1)], 1), a("div", {
                    staticClass: "main-panel"
                }, [a("top-navbar"), a("fixed-plugin", {
                    attrs: {
                        color: t.sidebarBackground,
                        image: t.sidebarBackgroundImage
                    },
                    on: {
                        "update:color": function(e) {
                            t.sidebarBackground = e
                        },
                        "update:image": function(e) {
                            t.sidebarBackgroundImage = e
                        }
                    }
                }), a("dashboard-content"), t.$route.meta.hideFooter ? t._e() : a("content-footer")], 1)], 1)
            },
            p = [],
            f = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("md-toolbar", {
                    staticClass: "md-transparent",
                    attrs: {
                        "md-elevation": "0"
                    }
                }, [a("div", {
                    staticClass: "md-toolbar-row"
                }, [a("div", {
                    staticClass: "md-toolbar-section-start"
                }, [a("h3", {
                    staticClass: "md-title"
                }, [t._v(t._s(t.$route.name))])]), a("div", {
                    staticClass: "md-toolbar-section-end"
                }, [a("md-button", {
                    staticClass: "md-just-icon md-simple md-toolbar-toggle",
                    class: {
                        toggled: t.$sidebar.showSidebar
                    },
                    on: {
                        click: t.toggleSidebar
                    }
                }, [a("span", {
                    staticClass: "icon-bar"
                }), a("span", {
                    staticClass: "icon-bar"
                }), a("span", {
                    staticClass: "icon-bar"
                })]), a("div", {
                    staticClass: "md-collapse"
                }, [a("div", {
                    staticClass: "md-autocomplete"
                }, [a("md-autocomplete", {
                    staticClass: "search",
                    attrs: {
                        "md-options": t.employees
                    },
                    model: {
                        value: t.selectedEmployee,
                        callback: function(e) {
                            t.selectedEmployee = e
                        },
                        expression: "selectedEmployee"
                    }
                }, [a("label", [t._v("Search...")])])], 1), a("md-list", [a("md-list-item", {
                    attrs: {
                        href: "#/"
                    }
                }, [a("i", {
                    staticClass: "material-icons"
                }, [t._v("dashboard")]), a("p", {
                    staticClass: "hidden-lg hidden-md"
                }, [t._v("Dashboard")])]), a("li", {
                    staticClass: "md-list-item"
                }, [a("a", {
                    staticClass: "md-list-item-router md-list-item-container md-button-clean dropdown",
                    attrs: {
                        href: "#/notifications"
                    }
                }, [a("div", {
                    staticClass: "md-list-item-content"
                }, [a("drop-down", [a("md-button", {
                    staticClass: "md-button md-just-icon md-simple",
                    attrs: {
                        slot: "title",
                        "data-toggle": "dropdown"
                    },
                    slot: "title"
                }, [a("md-icon", [t._v("notifications")]), a("span", {
                    staticClass: "notification"
                }, [t._v("5")]), a("p", {
                    staticClass: "hidden-lg hidden-md"
                }, [t._v("Notifications")])], 1), a("ul", {
                    staticClass: "dropdown-menu dropdown-menu-right"
                }, [a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Mike John responded to your email")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("You have 5 new tasks")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("You're now friend with Andrew")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Another Notification")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Another One")])])])], 1)], 1)])]), a("md-list-item", {
                    attrs: {
                        href: "#/user"
                    }
                }, [a("i", {
                    staticClass: "material-icons"
                }, [t._v("person")]), a("p", {
                    staticClass: "hidden-lg hidden-md"
                }, [t._v("Profile")])])], 1)], 1)], 1)])])
            },
            h = [],
            v = {
                data: function() {
                    return {
                        selectedEmployee: null,
                        employees: ["Jim Halpert", "Dwight Schrute", "Michael Scott", "Pam Beesly", "Angela Martin", "Kelly Kapoor", "Ryan Howard", "Kevin Malone"]
                    }
                },
                methods: {
                    toggleSidebar: function() {
                        this.$sidebar.displaySidebar(!this.$sidebar.showSidebar)
                    }
                }
            },
            b = v,
            g = Object(c["a"])(b, f, h, !1, null, null, null),
            y = g.exports,
            C = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("footer", {
                    staticClass: "footer"
                }, [a("div", {
                    staticClass: "container"
                }, [t._m(0), a("div", {
                    staticClass: "copyright text-center"
                }, [t._v(" © " + t._s((new Date).getFullYear()) + " "), a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/?ref=mdf-vuejs",
                        target: "_blank"
                    }
                }, [t._v("Creative Tim")]), t._v(", made with "), a("i", {
                    staticClass: "fa fa-heart heart"
                }), t._v(" for a better web ")])])])
            },
            _ = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("nav", [a("ul", [a("li", [a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com"
                    }
                }, [t._v("Creative Tim")])]), a("li", [a("a", {
                    attrs: {
                        href: "https://creative-tim.com/presentation"
                    }
                }, [t._v(" About Us ")])]), a("li", [a("a", {
                    attrs: {
                        href: "http://blog.creative-tim.com"
                    }
                }, [t._v(" Blog ")])]), a("li", [a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/license"
                    }
                }, [t._v(" Licenses ")])])])])
            }],
            w = {},
            k = w,
            x = Object(c["a"])(k, C, _, !1, null, null, null),
            S = x.exports,
            T = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("transition", {
                    attrs: {
                        name: "fade",
                        mode: "out-in"
                    }
                }, [a("router-view")], 1)
            },
            O = [],
            z = {},
            $ = z,
            I = (a("5436"), Object(c["a"])($, T, O, !1, null, null, null)),
            j = I.exports,
            D = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("ul", {
                    staticClass: "nav nav-mobile-menu"
                }, [a("li", [a("md-field", [a("label", [t._v("Search")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.search,
                        callback: function(e) {
                            t.search = e
                        },
                        expression: "search"
                    }
                })], 1)], 1), t._m(0), a("li", [a("drop-down", [a("a", {
                    staticClass: "dropdown-toggle",
                    attrs: {
                        slot: "title",
                        "data-toggle": "dropdown"
                    },
                    slot: "title"
                }, [a("i", {
                    staticClass: "material-icons"
                }, [t._v("notifications")]), a("span", {
                    staticClass: "notification"
                }, [t._v("5")]), a("p", [t._v("Notifications")])]), a("ul", {
                    staticClass: "dropdown-menu dropdown-menu-right"
                }, [a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Mike John responded to your email")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("You have 5 new tasks")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("You're now friend with Andrew")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Another Notification")])]), a("li", [a("a", {
                    attrs: {
                        href: "#"
                    }
                }, [t._v("Another One")])])])])], 1), t._m(1)])
            },
            M = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", [a("a", {
                    staticClass: "dropdown-toggle",
                    attrs: {
                        href: "#",
                        "data-toggle": "dropdown"
                    }
                }, [a("i", {
                    staticClass: "material-icons"
                }, [t._v("dashboard")]), a("p", [t._v("Dashboard")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", [a("a", {
                    staticClass: "dropdown-toggle",
                    attrs: {
                        href: "#",
                        "data-toggle": "dropdown"
                    }
                }, [a("i", {
                    staticClass: "material-icons"
                }, [t._v("person")]), a("p", [t._v("Profile")])])])
            }],
            P = {
                data: function() {
                    return {
                        search: null,
                        selectedEmployee: null,
                        employees: ["Jim Halpert", "Dwight Schrute", "Michael Scott", "Pam Beesly", "Angela Martin", "Kelly Kapoor", "Ryan Howard", "Kevin Malone"]
                    }
                }
            },
            E = P,
            A = Object(c["a"])(E, D, M, !1, null, null, null),
            N = A.exports,
            B = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    directives: [{
                        name: "click-outside",
                        rawName: "v-click-outside",
                        value: t.closeDropDown,
                        expression: "closeDropDown"
                    }],
                    staticClass: "fixed-plugin"
                }, [a("div", {
                    staticClass: "dropdown show-dropdown",
                    class: {
                        show: t.isOpen
                    }
                }, [a("a", {
                    attrs: {
                        "data-toggle": "dropdown"
                    }
                }, [a("i", {
                    staticClass: "fa fa-cog fa-2x",
                    on: {
                        click: t.toggleDropDown
                    }
                })]), a("ul", {
                    staticClass: "dropdown-menu",
                    class: {
                        show: t.isOpen
                    }
                }, [a("li", {
                    staticClass: "header-title"
                }, [t._v("Sidebar Filters")]), a("li", {
                    staticClass: "adjustments-line text-center"
                }, t._l(t.sidebarColors, (function(e) {
                    return a("span", {
                        key: e.color,
                        staticClass: "badge filter",
                        class: ["badge-" + e.color, {
                            active: e.active
                        }],
                        attrs: {
                            "data-color": e.color
                        },
                        on: {
                            click: function(a) {
                                return t.changeSidebarBackground(e)
                            }
                        }
                    })
                })), 0), a("li", {
                    staticClass: "header-title"
                }, [t._v("Images")]), t._l(t.sidebarImages, (function(e) {
                    return a("li", {
                        key: e.image,
                        class: {
                            active: e.active
                        },
                        on: {
                            click: function(a) {
                                return t.changeSidebarImage(e)
                            }
                        }
                    }, [a("a", {
                        staticClass: "vuetim/static/tte/img-holder switch-trigger"
                    }, [a("vuetim/static/tte/img", {
                        attrs: {
                            src: e.image,
                            alt: ""
                        }
                    })])])
                })), a("li", {
                    staticClass: "button-container"
                }, [a("div", {}, [a("md-button", {
                    staticClass: "md-success md-block",
                    attrs: {
                        href: t.freeUrl,
                        target: "_blank"
                    }
                }, [t._v("Free Download")])], 1)]), a("li", {
                    staticClass: "button-container"
                }, [a("div", {}, [a("md-button", {
                    staticClass: "md-block md-primary",
                    attrs: {
                        href: t.documentationLink,
                        target: "_blank"
                    }
                }, [t._v("Documentation")])], 1)]), a("li", {
                    staticClass: "header-title d-flex justify-content-center"
                }, [t._v(" Thank you for sharing! ")]), a("li", {
                    staticClass: "button-container"
                }, [a("social-sharing", {
                    attrs: {
                        url: t.shareUrl,
                        title: "Vue Material Dashboard - Admin Template for Vue.js",
                        hashtags: "vuejs, dashboard, vuematerial",
                        "twitter-user": "creativetim"
                    },
                    inlineTemplate: {
                        render: function() {
                            var t = this,
                                e = t.$createElement,
                                a = t._self._c || e;
                            return a("div", {
                                staticClass: "centered-buttons"
                            }, [a("network", {
                                staticClass: "md-button md-round md-just-icon md-facebook",
                                attrs: {
                                    network: "facebook"
                                }
                            }, [a("i", {
                                staticClass: "fab fa-facebook-f"
                            })]), a("network", {
                                staticClass: "md-button md-round md-just-icon md-twitter",
                                attrs: {
                                    network: "twitter"
                                }
                            }, [a("i", {
                                staticClass: "fab fa-twitter"
                            })])], 1)
                        },
                        staticRenderFns: []
                    }
                })], 1), a("li", {
                    staticClass: "github-buttons"
                }, [a("gh-btns-star", {
                    attrs: {
                        slug: "creativetimofficial/vue-material-dashboard",
                        "show-count": ""
                    }
                })], 1)], 2)])])
            },
            L = [],
            H = (a("4160"), a("159b"), a("5299")),
            F = a.n(H),
            R = a("f676");
        a("3a06");
        s["default"].use(F.a), s["default"].use(R["a"], {
            useCache: !0
        });
        var U = {
                data: function() {
                    return {
                        documentationLink: "https://creativetimofficial.github.io/vue-material-dashboard/documentation",
                        shareUrl: "https://www.creative-tim.com/product/vue-material-dashboard",
                        buyUrl: "",
                        freeUrl: "https://www.creative-tim.com/product/vue-material-dashboard",
                        isOpen: !1,
                        sidebarColors: [{
                            color: "purple",
                            active: !1
                        }, {
                            color: "blue",
                            active: !1
                        }, {
                            color: "green",
                            active: !0
                        }, {
                            color: "orange",
                            active: !1
                        }, {
                            color: "red",
                            active: !1
                        }],
                        sidebarImages: [{
                            image: a("7d6d"),
                            active: !1
                        }, {
                            image: a("9524"),
                            active: !0
                        }, {
                            image: a("aeef"),
                            active: !1
                        }, {
                            image: a("eb9e"),
                            active: !1
                        }]
                    }
                },
                methods: {
                    toggleDropDown: function() {
                        this.isOpen = !this.isOpen
                    },
                    closeDropDown: function() {
                        this.isOpen = !1
                    },
                    toggleList: function(t, e) {
                        t.forEach((function(t) {
                            t.active = !1
                        })), e.active = !0
                    },
                    updateValue: function(t, e) {
                        console.log(t), this.$emit("update:".concat(t), e)
                    },
                    changeSidebarBackground: function(t) {
                        this.$emit("update:color", t.color), this.toggleList(this.sidebarColors, t)
                    },
                    changeSidebarImage: function(t) {
                        this.$emit("update:image", t.image), this.toggleList(this.sidebarImages, t)
                    }
                }
            },
            V = U,
            K = (a("dac3"), Object(c["a"])(V, B, L, !1, null, null, null)),
            G = K.exports,
            J = {
                components: {
                    TopNavbar: y,
                    DashboardContent: j,
                    ContentFooter: S,
                    MobileMenu: N,
                    FixedPlugin: G
                },
                data: function() {
                    return {
                        sidebarBackground: "green",
                        sidebarBackgroundImage: a("9524")
                    }
                }
            },
            W = J,
            Y = Object(c["a"])(W, u, p, !1, null, null, null),
            Q = Y.exports,
            X = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-33"
                }, [a("chart-card", {
                    attrs: {
                        "chart-data": t.dailySalesChart.data,
                        "chart-options": t.dailySalesChart.options,
                        "chart-type": "Line",
                        "data-background-color": "blue"
                    }
                }, [a("template", {
                    slot: "content"
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Daily Sales")]), a("p", {
                    staticClass: "category"
                }, [a("span", {
                    staticClass: "text-success"
                }, [a("i", {
                    staticClass: "fas fa-long-arrow-alt-up"
                }), t._v(" 55% ")]), t._v(" increase in today sales. ")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("access_time")]), t._v(" updated 4 minutes ago ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-33"
                }, [a("chart-card", {
                    attrs: {
                        "chart-data": t.emailsSubscriptionChart.data,
                        "chart-options": t.emailsSubscriptionChart.options,
                        "chart-responsive-options": t.emailsSubscriptionChart.responsiveOptions,
                        "chart-type": "Bar",
                        "data-background-color": "red"
                    }
                }, [a("template", {
                    slot: "content"
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Email Subscription")]), a("p", {
                    staticClass: "category"
                }, [t._v(" Last Campaign Performance ")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("access_time")]), t._v(" updated 10 days ago ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-33"
                }, [a("chart-card", {
                    attrs: {
                        "chart-data": t.dataCompletedTasksChart.data,
                        "chart-options": t.dataCompletedTasksChart.options,
                        "chart-type": "Line",
                        "data-background-color": "green"
                    }
                }, [a("template", {
                    slot: "content"
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Completed Tasks")]), a("p", {
                    staticClass: "category"
                }, [t._v(" Last Campaign Performance ")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("access_time")]), t._v(" campaign sent 26 minutes ago ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-25"
                }, [a("stats-card", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("template", {
                    slot: "header"
                }, [a("md-icon", [t._v("store")])], 1), a("template", {
                    slot: "content"
                }, [a("p", {
                    staticClass: "category"
                }, [t._v("Revenue")]), a("h3", {
                    staticClass: "title"
                }, [t._v("$34,245")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("date_range")]), t._v(" Last 24 Hours ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-25"
                }, [a("stats-card", {
                    attrs: {
                        "data-background-color": "orange"
                    }
                }, [a("template", {
                    slot: "header"
                }, [a("md-icon", [t._v("content_copy")])], 1), a("template", {
                    slot: "content"
                }, [a("p", {
                    staticClass: "category"
                }, [t._v("Used Space")]), a("h3", {
                    staticClass: "title"
                }, [t._v(" 49/50 "), a("small", [t._v("GB")])])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", {
                    staticClass: "text-danger"
                }, [t._v("warning")]), a("a", {
                    attrs: {
                        href: "#pablo"
                    }
                }, [t._v("Get More Space...")])], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-25"
                }, [a("stats-card", {
                    attrs: {
                        "data-background-color": "red"
                    }
                }, [a("template", {
                    slot: "header"
                }, [a("md-icon", [t._v("info_outline")])], 1), a("template", {
                    slot: "content"
                }, [a("p", {
                    staticClass: "category"
                }, [t._v("Fixed Issues")]), a("h3", {
                    staticClass: "title"
                }, [t._v("75")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("local_offer")]), t._v(" Tracked from Github ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-50 md-xsmall-size-100 md-size-25"
                }, [a("stats-card", {
                    attrs: {
                        "data-background-color": "blue"
                    }
                }, [a("template", {
                    slot: "header"
                }, [a("i", {
                    staticClass: "fab fa-twitter"
                })]), a("template", {
                    slot: "content"
                }, [a("p", {
                    staticClass: "category"
                }, [t._v("Folowers")]), a("h3", {
                    staticClass: "title"
                }, [t._v("+245")])]), a("template", {
                    slot: "footer"
                }, [a("div", {
                    staticClass: "stats"
                }, [a("md-icon", [t._v("update")]), t._v(" Just Updated ")], 1)])], 2)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50"
                }, [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": "orange"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Employees Stats")]), a("p", {
                    staticClass: "category"
                }, [t._v("New employees on 15th September, 2016")])]), a("md-card-content", [a("ordered-table", {
                    attrs: {
                        "table-header-color": "orange"
                    }
                })], 1)], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-50"
                }, [a("nav-tabs-card", [a("template", {
                    slot: "content"
                }, [a("span", {
                    staticClass: "md-nav-tabs-title"
                }, [t._v("Tasks:")]), a("md-tabs", {
                    staticClass: "md-success",
                    attrs: {
                        "md-alignment": "left"
                    }
                }, [a("md-tab", {
                    attrs: {
                        id: "tab-home",
                        "md-label": "Bugs",
                        "md-icon": "bug_report"
                    }
                }, [a("nav-tabs-table")], 1), a("md-tab", {
                    attrs: {
                        id: "tab-pages",
                        "md-label": "Website",
                        "md-icon": "code"
                    }
                }, [a("nav-tabs-table")], 1), a("md-tab", {
                    attrs: {
                        id: "tab-posts",
                        "md-label": "server",
                        "md-icon": "cloud"
                    }
                }, [a("nav-tabs-table")], 1)], 1)], 1)], 2)], 1)])])
            },
            q = [],
            Z = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("md-card", [a("md-card-header", {
                    staticClass: "card-chart",
                    attrs: {
                        "data-background-color": t.dataBackgroundColor
                    }
                }, [a("div", {
                    staticClass: "ct-chart",
                    attrs: {
                        id: t.chartId
                    }
                })]), a("md-card-content", [t._t("content")], 2), a("md-card-actions", {
                    attrs: {
                        "md-alignment": "left"
                    }
                }, [t._t("footer")], 2)], 1)
            },
            tt = [],
            et = (a("d3b7"), a("25f0"), {
                name: "chart-card",
                props: {
                    footerText: {
                        type: String,
                        default: ""
                    },
                    headerTitle: {
                        type: String,
                        default: "Chart title"
                    },
                    chartType: {
                        type: String,
                        default: "Line"
                    },
                    chartOptions: {
                        type: Object,
                        default: function() {
                            return {}
                        }
                    },
                    chartResponsiveOptions: {
                        type: Array,
                        default: function() {
                            return []
                        }
                    },
                    chartData: {
                        type: Object,
                        default: function() {
                            return {
                                labels: [],
                                series: []
                            }
                        }
                    },
                    dataBackgroundColor: {
                        type: String,
                        default: ""
                    }
                },
                data: function() {
                    return {
                        chartId: "no-id"
                    }
                },
                methods: {
                    initChart: function(t) {
                        var e = "#".concat(this.chartId);
                        t[this.chartType](e, this.chartData, this.chartOptions)
                    },
                    updateChartId: function() {
                        var t = (new Date).getTime().toString(),
                            e = this.getRandomInt(0, t);
                        this.chartId = "div_".concat(e)
                    },
                    getRandomInt: function(t, e) {
                        return Math.floor(Math.random() * (e - t + 1)) + t
                    }
                },
                mounted: function() {
                    var t = this;
                    this.updateChartId(), Promise.resolve().then(a.t.bind(null, "ba48", 7)).then((function(e) {
                        var a = e.default || e;
                        t.$nextTick((function() {
                            t.initChart(a)
                        }))
                    }))
                }
            }),
            at = et,
            st = Object(c["a"])(at, Z, tt, !1, null, null, null),
            it = st.exports,
            nt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("md-card", {
                    staticClass: "md-card-nav-tabs"
                }, [a("md-card-content", [t._t("content")], 2)], 1)
            },
            ot = [],
            rt = {
                name: "nav-tabs-card"
            },
            lt = rt,
            ct = Object(c["a"])(lt, nt, ot, !1, null, null, null),
            dt = ct.exports,
            mt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("md-card", {
                    staticClass: "md-card-stats"
                }, [a("md-card-header", {
                    attrs: {
                        "data-background-color": t.dataBackgroundColor
                    }
                }, [t._t("header")], 2), a("md-card-content", [t._t("content")], 2), a("md-card-actions", {
                    attrs: {
                        "md-alignment": "left"
                    }
                }, [t._t("footer")], 2)], 1)
            },
            ut = [],
            pt = {
                name: "stats-card",
                props: {
                    dataBackgroundColor: {
                        type: String,
                        default: ""
                    }
                }
            },
            ft = pt,
            ht = Object(c["a"])(ft, mt, ut, !1, null, null, null),
            vt = ht.exports,
            bt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("md-table", {
                    on: {
                        "md-selected": t.onSelect
                    },
                    scopedSlots: t._u([{
                        key: "md-table-row",
                        fn: function(e) {
                            var s = e.item;
                            return a("md-table-row", {
                                attrs: {
                                    "md-selectable": "multiple",
                                    "md-auto-select": ""
                                }
                            }, [a("md-table-cell", [t._v(t._s(s.name))]), a("md-table-cell", [a("md-button", {
                                staticClass: "md-just-icon md-simple md-primary"
                            }, [a("md-icon", [t._v("edit")]), a("md-tooltip", {
                                attrs: {
                                    "md-direction": "top"
                                }
                            }, [t._v("Edit")])], 1), a("md-button", {
                                staticClass: "md-just-icon md-simple md-danger"
                            }, [a("md-icon", [t._v("close")]), a("md-tooltip", {
                                attrs: {
                                    "md-direction": "top"
                                }
                            }, [t._v("Close")])], 1)], 1)], 1)
                        }
                    }]),
                    model: {
                        value: t.users,
                        callback: function(e) {
                            t.users = e
                        },
                        expression: "users"
                    }
                })], 1)
            },
            gt = [],
            yt = {
                name: "nav-tabs-table",
                data: function() {
                    return {
                        selected: [],
                        users: [{
                            name: 'Sign contract for "What are conference organizers afraid of?"'
                        }, {
                            name: "Lines From Great Russian Literature? Or E-mails From My Boss?"
                        }, {
                            name: "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit"
                        }]
                    }
                },
                methods: {
                    onSelect: function(t) {
                        this.selected = t
                    }
                }
            },
            Ct = yt,
            _t = Object(c["a"])(Ct, bt, gt, !1, null, null, null),
            wt = _t.exports,
            kt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("md-table", {
                    attrs: {
                        "table-header-color": t.tableHeaderColor
                    },
                    scopedSlots: t._u([{
                        key: "md-table-row",
                        fn: function(e) {
                            var s = e.item;
                            return a("md-table-row", {}, [a("md-table-cell", {
                                attrs: {
                                    "md-label": "ID"
                                }
                            }, [t._v(t._s(s.id))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "Name"
                                }
                            }, [t._v(t._s(s.name))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "Salary"
                                }
                            }, [t._v(t._s(s.salary))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "Country"
                                }
                            }, [t._v(t._s(s.country))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "City"
                                }
                            }, [t._v(t._s(s.city))])], 1)
                        }
                    }]),
                    model: {
                        value: t.users,
                        callback: function(e) {
                            t.users = e
                        },
                        expression: "users"
                    }
                })], 1)
            },
            xt = [],
            St = {
                name: "ordered-table",
                props: {
                    tableHeaderColor: {
                        type: String,
                        default: ""
                    }
                },
                data: function() {
                    return {
                        selected: [],
                        users: [{
                            id: 1,
                            name: "Dakota Rice",
                            salary: "$36,738",
                            country: "Niger",
                            city: "Oud-Turnhout"
                        }, {
                            id: 2,
                            name: "Minerva Hooper",
                            salary: "$23,738",
                            country: "Curaçao",
                            city: "Sinaai-Waas"
                        }, {
                            id: 3,
                            name: "Sage Rodriguez",
                            salary: "$56,142",
                            country: "Netherlands",
                            city: "Overland Park"
                        }, {
                            id: 4,
                            name: "Philip Chaney",
                            salary: "$38,735",
                            country: "Korea, South",
                            city: "Gloucester"
                        }]
                    }
                }
            },
            Tt = St,
            Ot = Object(c["a"])(Tt, kt, xt, !1, null, null, null),
            zt = Ot.exports,
            $t = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("md-table", {
                    attrs: {
                        "table-header-color": t.tableHeaderColor
                    },
                    scopedSlots: t._u([{
                        key: "md-table-row",
                        fn: function(e) {
                            var s = e.item;
                            return a("md-table-row", {}, [a("md-table-cell", {
                                attrs: {
                                    "md-label": "Name"
                                }
                            }, [t._v(t._s(s.name))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "Country"
                                }
                            }, [t._v(t._s(s.country))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "City"
                                }
                            }, [t._v(t._s(s.city))]), a("md-table-cell", {
                                attrs: {
                                    "md-label": "Salary"
                                }
                            }, [t._v(t._s(s.salary))])], 1)
                        }
                    }]),
                    model: {
                        value: t.users,
                        callback: function(e) {
                            t.users = e
                        },
                        expression: "users"
                    }
                })], 1)
            },
            It = [],
            jt = {
                name: "simple-table",
                props: {
                    tableHeaderColor: {
                        type: String,
                        default: ""
                    }
                },
                data: function() {
                    return {
                        selected: [],
                        users: [{
                            name: "Dakota Rice",
                            salary: "$36,738",
                            country: "Niger",
                            city: "Oud-Turnhout"
                        }, {
                            name: "Minerva Hooper",
                            salary: "$23,738",
                            country: "Curaçao",
                            city: "Sinaai-Waas"
                        }, {
                            name: "Sage Rodriguez",
                            salary: "$56,142",
                            country: "Netherlands",
                            city: "Overland Park"
                        }, {
                            name: "Philip Chaney",
                            salary: "$38,735",
                            country: "Korea, South",
                            city: "Gloucester"
                        }, {
                            name: "Doris Greene",
                            salary: "$63,542",
                            country: "Malawi",
                            city: "Feldkirchen in Kārnten"
                        }, {
                            name: "Mason Porter",
                            salary: "$78,615",
                            country: "Chile",
                            city: "Gloucester"
                        }]
                    }
                }
            },
            Dt = jt,
            Mt = Object(c["a"])(Dt, $t, It, !1, null, null, null),
            Pt = Mt.exports,
            Et = {
                components: {
                    StatsCard: vt,
                    ChartCard: it,
                    NavTabsCard: dt,
                    NavTabsTable: wt,
                    OrderedTable: zt
                },
                data: function() {
                    return {
                        dailySalesChart: {
                            data: {
                                labels: ["M", "T", "W", "T", "F", "S", "S"],
                                series: [
                                    [12, 17, 7, 17, 23, 18, 38]
                                ]
                            },
                            options: {
                                lineSmooth: this.$Chartist.Interpolation.cardinal({
                                    tension: 0
                                }),
                                low: 0,
                                high: 50,
                                chartPadding: {
                                    top: 0,
                                    right: 0,
                                    bottom: 0,
                                    left: 0
                                }
                            }
                        },
                        dataCompletedTasksChart: {
                            data: {
                                labels: ["12am", "3pm", "6pm", "9pm", "12pm", "3am", "6am", "9am"],
                                series: [
                                    [230, 750, 450, 300, 280, 240, 200, 190]
                                ]
                            },
                            options: {
                                lineSmooth: this.$Chartist.Interpolation.cardinal({
                                    tension: 0
                                }),
                                low: 0,
                                high: 1e3,
                                chartPadding: {
                                    top: 0,
                                    right: 0,
                                    bottom: 0,
                                    left: 0
                                }
                            }
                        },
                        emailsSubscriptionChart: {
                            data: {
                                labels: ["Ja", "Fe", "Ma", "Ap", "Mai", "Ju", "Jul", "Au", "Se", "Oc", "No", "De"],
                                series: [
                                    [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]
                                ]
                            },
                            options: {
                                axisX: {
                                    showGrid: !1
                                },
                                low: 0,
                                high: 1e3,
                                chartPadding: {
                                    top: 0,
                                    right: 5,
                                    bottom: 0,
                                    left: 0
                                }
                            },
                            responsiveOptions: [
                                ["screen and (max-width: 640px)", {
                                    seriesBarDistance: 5,
                                    axisX: {
                                        labelInterpolationFnc: function(t) {
                                            return t[0]
                                        }
                                    }
                                }]
                            ]
                        }
                    }
                }
            },
            At = Et,
            Nt = Object(c["a"])(At, X, q, !1, null, null, null),
            Bt = Nt.exports,
            Lt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-size-66"
                }, [a("edit-profile-form", {
                    attrs: {
                        "data-background-color": "green"
                    }
                })], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-size-33"
                }, [a("user-card")], 1)])])
            },
            Ht = [],
            Ft = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("md-card", {
                    staticClass: "md-card-profile"
                }, [a("div", {
                    staticClass: "md-card-avatar"
                }, [a("vuetim/static/tte/img", {
                    staticClass: "vuetim/static/tte/img",
                    attrs: {
                        src: t.cardUserImage
                    }
                })]), a("md-card-content", [a("h6", {
                    staticClass: "category text-gray"
                }, [t._v("CEO / Co-Founder")]), a("h4", {
                    staticClass: "card-title"
                }, [t._v("Alec Thompson")]), a("p", {
                    staticClass: "card-description"
                }, [t._v(" Don't be scared of the truth because we need to restart the human foundation in truth And I love you like Kanye loves Kanye I love Rick Owens’ bed design but the back is... ")]), a("md-button", {
                    staticClass: "md-round md-success"
                }, [t._v("Follow")])], 1)], 1)
            },
            Rt = [],
            Ut = {
                name: "user-card",
                props: {
                    cardUserImage: {
                        type: String,
                        default: a("a180")
                    }
                },
                data: function() {
                    return {}
                }
            },
            Vt = Ut,
            Kt = Object(c["a"])(Vt, Ft, Rt, !1, null, null, null),
            Gt = Kt.exports,
            Jt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("form", [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": t.dataBackgroundColor
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Edit Profile")]), a("p", {
                    staticClass: "category"
                }, [t._v("Complete your profile")])]), a("md-card-content", [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("Company (disabled)")]), a("md-input", {
                    attrs: {
                        disabled: ""
                    },
                    model: {
                        value: t.disabled,
                        callback: function(e) {
                            t.disabled = e
                        },
                        expression: "disabled"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("User Name")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.username,
                        callback: function(e) {
                            t.username = e
                        },
                        expression: "username"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("Email Address")]), a("md-input", {
                    attrs: {
                        type: "email"
                    },
                    model: {
                        value: t.emailadress,
                        callback: function(e) {
                            t.emailadress = e
                        },
                        expression: "emailadress"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-50"
                }, [a("md-field", [a("label", [t._v("First Name")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.firstname,
                        callback: function(e) {
                            t.firstname = e
                        },
                        expression: "firstname"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-50"
                }, [a("md-field", [a("label", [t._v("Last Name")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.lastname,
                        callback: function(e) {
                            t.lastname = e
                        },
                        expression: "lastname"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-100"
                }, [a("md-field", [a("label", [t._v("Adress")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.address,
                        callback: function(e) {
                            t.address = e
                        },
                        expression: "address"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("City")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.city,
                        callback: function(e) {
                            t.city = e
                        },
                        expression: "city"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("Country")]), a("md-input", {
                    attrs: {
                        type: "text"
                    },
                    model: {
                        value: t.country,
                        callback: function(e) {
                            t.country = e
                        },
                        expression: "country"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-small-size-100 md-size-33"
                }, [a("md-field", [a("label", [t._v("Postal Code")]), a("md-input", {
                    attrs: {
                        type: "number"
                    },
                    model: {
                        value: t.code,
                        callback: function(e) {
                            t.code = e
                        },
                        expression: "code"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-size-100"
                }, [a("md-field", {
                    attrs: {
                        maxlength: "5"
                    }
                }, [a("label", [t._v("About Me")]), a("md-textarea", {
                    model: {
                        value: t.aboutme,
                        callback: function(e) {
                            t.aboutme = e
                        },
                        expression: "aboutme"
                    }
                })], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-size-100 text-right"
                }, [a("md-button", {
                    staticClass: "md-raised md-success"
                }, [t._v("Update Profile")])], 1)])])], 1)], 1)
            },
            Wt = [],
            Yt = {
                name: "edit-profile-form",
                props: {
                    dataBackgroundColor: {
                        type: String,
                        default: ""
                    }
                },
                data: function() {
                    return {
                        username: null,
                        disabled: null,
                        emailadress: null,
                        lastname: null,
                        firstname: null,
                        address: null,
                        city: null,
                        country: null,
                        code: null,
                        aboutme: "Lamborghini Mercy, Your chick she so thirsty, I'm in that two seat Lambo."
                    }
                }
            },
            Qt = Yt,
            Xt = Object(c["a"])(Qt, Jt, Wt, !1, null, null, null),
            qt = Xt.exports,
            Zt = {
                components: {
                    EditProfileForm: qt,
                    UserCard: Gt
                }
            },
            te = Zt,
            ee = Object(c["a"])(te, Lt, Ht, !1, null, null, null),
            ae = ee.exports,
            se = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
                }, [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Simple Table")]), a("p", {
                    staticClass: "category"
                }, [t._v("Here is a subtitle for this table")])]), a("md-card-content", [a("simple-table", {
                    attrs: {
                        "table-header-color": "green"
                    }
                })], 1)], 1)], 1), a("div", {
                    staticClass: "md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
                }, [a("md-card", {
                    staticClass: "md-card-plain"
                }, [a("md-card-header", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Table on Plain Background")]), a("p", {
                    staticClass: "category"
                }, [t._v("Here is a subtitle for this table")])]), a("md-card-content", [a("ordered-table")], 1)], 1)], 1)])])
            },
            ie = [],
            ne = {
                components: {
                    OrderedTable: zt,
                    SimpleTable: Pt
                }
            },
            oe = ne,
            re = Object(c["a"])(oe, se, ie, !1, null, null, null),
            le = re.exports,
            ce = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item"
                }, [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Material Dashboard Heading")]), a("p", {
                    staticClass: "category"
                }, [t._v("Created using Roboto Font Family")])]), a("md-card-content", [a("div", {
                    attrs: {
                        id: "typography"
                    }
                }, [a("div", {
                    staticClass: "title"
                }, [a("h2", [t._v("Typography")])]), a("div", {
                    staticClass: "row"
                }, [a("div", {
                    staticClass: "tim-typo"
                }, [a("h1", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 1")]), t._v("The Life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h2", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 2")]), t._v("The life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h3", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 3")]), t._v("The life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h4", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 4")]), t._v("The life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h5", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 5")]), t._v("The life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h6", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Header 6")]), t._v("The life of Material Dashboard ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("p", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Paragraph")]), t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers. I understand culture. I am the nucleus. I think that’s a responsibility that I have, to push possibilities, to show people, this is the level that things could be at. ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Quote")]), a("blockquote", [a("p", [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers. I understand culture. I am the nucleus. I think that’s a responsibility that I have, to push possibilities, to show people, this is the level that things could be at. ")]), a("small", [t._v(" Kanye West, Musician ")])])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Muted Text")]), a("p", {
                    staticClass: "text-muted"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Primary Text")]), a("p", {
                    staticClass: "text-primary"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Info Text")]), a("p", {
                    staticClass: "text-info"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Success Text")]), a("p", {
                    staticClass: "text-success"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Warning Text")]), a("p", {
                    staticClass: "text-warning"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Danger Text")]), a("p", {
                    staticClass: "text-danger"
                }, [t._v(" I will be the leader of a company that ends up being worth billions of dollars, because I got the answers... ")])]), a("div", {
                    staticClass: "tim-typo"
                }, [a("h2", [a("span", {
                    staticClass: "tim-note"
                }, [t._v("Small Tag")]), t._v(" Header with small subtitle "), a("br"), a("small", [t._v('Use "small" tag for the headers')])])])])])])], 1)], 1)])])
            },
            de = [],
            me = {
                props: {
                    dataBackgroundColor: {
                        type: String,
                        default: ""
                    }
                }
            },
            ue = me,
            pe = Object(c["a"])(ue, ce, de, !1, null, null, null),
            fe = pe.exports,
            he = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item"
                }, [a("md-card", {
                    staticClass: "md-card-plain"
                }, [a("md-card-header", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Material Design Icons")]), a("p", {
                    staticClass: "category"
                }, [t._v(" Handcrafted by our friends from "), a("a", {
                    attrs: {
                        target: "_blank",
                        href: "https://design.google.com/icons/"
                    }
                }, [t._v("Google")])])]), a("md-card-content", [a("div", {
                    staticClass: "iframe-container hidden-sm"
                }, [a("iframe", {
                    attrs: {
                        src: "https://vuematerial.io/components/icon"
                    }
                }, [a("p", [t._v("Your browser does not support iframes.")])])]), a("div", {
                    staticClass: "hidden-md"
                }, [a("h5", [t._v(" The icons are visible on Desktop mode inside an iframe. Since the iframe is not working on Mobile and Tablets please visit the icons on their original page on Google. Check the "), a("a", {
                    attrs: {
                        href: "https://design.google.com/icons/",
                        target: "_blank"
                    }
                }, [t._v("Material Icons")])])])])], 1)], 1)])])
            },
            ve = [],
            be = {},
            ge = be,
            ye = Object(c["a"])(ge, he, ve, !1, null, null, null),
            Ce = ye.exports,
            _e = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    attrs: {
                        id: "map"
                    }
                })
            },
            we = [],
            ke = "AIzaSyB2Yno10-YTnLjjn_Vtk0V8cdcY5lC4plU",
            xe = a("6344"),
            Se = new xe["Loader"](ke),
            Te = {
                mounted: function() {
                    Se.load().then((function(t) {
                        var e = new t.maps.LatLng(40.748817, -73.985428),
                            a = {
                                zoom: 13,
                                center: e,
                                scrollwheel: !1,
                                styles: [{
                                    featureType: "water",
                                    stylers: [{
                                        saturation: 43
                                    }, {
                                        lightness: -11
                                    }, {
                                        hue: "#0088ff"
                                    }]
                                }, {
                                    featureType: "road",
                                    elementType: "geometry.fill",
                                    stylers: [{
                                        hue: "#ff0000"
                                    }, {
                                        saturation: -100
                                    }, {
                                        lightness: 99
                                    }]
                                }, {
                                    featureType: "road",
                                    elementType: "geometry.stroke",
                                    stylers: [{
                                        color: "#808080"
                                    }, {
                                        lightness: 54
                                    }]
                                }, {
                                    featureType: "landscape.man_made",
                                    elementType: "geometry.fill",
                                    stylers: [{
                                        color: "#ece2d9"
                                    }]
                                }, {
                                    featureType: "poi.park",
                                    elementType: "geometry.fill",
                                    stylers: [{
                                        color: "#ccdca1"
                                    }]
                                }, {
                                    featureType: "road",
                                    elementType: "labels.text.fill",
                                    stylers: [{
                                        color: "#767676"
                                    }]
                                }, {
                                    featureType: "road",
                                    elementType: "labels.text.stroke",
                                    stylers: [{
                                        color: "#ffffff"
                                    }]
                                }, {
                                    featureType: "poi",
                                    stylers: [{
                                        visibility: "off"
                                    }]
                                }, {
                                    featureType: "landscape.natural",
                                    elementType: "geometry.fill",
                                    stylers: [{
                                        visibility: "on"
                                    }, {
                                        color: "#b8cb93"
                                    }]
                                }, {
                                    featureType: "poi.park",
                                    stylers: [{
                                        visibility: "on"
                                    }]
                                }, {
                                    featureType: "poi.sports_complex",
                                    stylers: [{
                                        visibility: "on"
                                    }]
                                }, {
                                    featureType: "poi.medical",
                                    stylers: [{
                                        visibility: "on"
                                    }]
                                }, {
                                    featureType: "poi.business",
                                    stylers: [{
                                        visibility: "simplified"
                                    }]
                                }]
                            },
                            s = new t.maps.Map(document.getElementById("map"), a),
                            i = new t.maps.Marker({
                                position: e,
                                title: "Hello World!"
                            });
                        i.setMap(s)
                    }))
                }
            },
            Oe = Te,
            ze = Object(c["a"])(Oe, _e, we, !1, null, null, null),
            $e = ze.exports,
            Ie = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item"
                }, [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": "green"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Notifications")]), a("p", {
                    staticClass: "category"
                }, [t._v(" Handcrafted by us with "), a("i", {
                    staticClass: "fa fa-heart heart"
                })])]), a("md-card-content", [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-medium-size-100"
                }, [a("h5", [t._v("Notifications Style")]), a("div", {
                    staticClass: "alert alert-info"
                }, [a("span", [t._v("This is a plain notification")])]), a("div", {
                    staticClass: "alert alert-info"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [t._v("This is a notification with close button.")])]), a("div", {
                    staticClass: "alert alert-info alert-with-icon",
                    attrs: {
                        "data-notify": "container"
                    }
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("i", {
                    staticClass: "material-icons",
                    attrs: {
                        "data-notify": "icon"
                    }
                }, [t._v("add_alert")]), a("span", {
                    attrs: {
                        "data-notify": "message"
                    }
                }, [t._v("This is a notification with close button and icon.")])]), a("div", {
                    staticClass: "alert alert-info alert-with-icon",
                    attrs: {
                        "data-notify": "container"
                    }
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("i", {
                    staticClass: "material-icons",
                    attrs: {
                        "data-notify": "icon"
                    }
                }, [t._v("add_alert")]), a("span", {
                    attrs: {
                        "data-notify": "message"
                    }
                }, [t._v("This is a notification with close button and icon and have many lines. You can see that the icon and the close button are always vertically aligned. This is a beautiful notification. So you don't have to worry about the style.")])])]), a("div", {
                    staticClass: "md-layout-item md-medium-size-100"
                }, [a("h5", [t._v("Notification states")]), a("div", {
                    staticClass: "alert alert-info"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [a("b", [t._v(" Info - ")]), t._v(' This is a regular notification made with ".alert-info"')])]), a("div", {
                    staticClass: "alert alert-success"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [a("b", [t._v(" Success - ")]), t._v(' This is a regular notification made with ".alert-success"')])]), a("div", {
                    staticClass: "alert alert-warning"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [a("b", [t._v(" Warning - ")]), t._v(' This is a regular notification made with ".alert-warning"')])]), a("div", {
                    staticClass: "alert alert-danger"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [a("b", [t._v(" Danger - ")]), t._v(' This is a regular notification made with ".alert-danger"')])]), a("div", {
                    staticClass: "alert alert-primary"
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true"
                    }
                }, [t._v(" × ")]), a("span", [a("b", [t._v(" Primary - ")]), t._v(' This is a regular notification made with ".alert-primary"')])])]), a("div", {
                    staticClass: "md-layout-item md-size-100"
                }, [a("div", {
                    staticClass: "places-buttons text-center"
                }, [a("h5", {
                    staticClass: "text-center"
                }, [t._v(" Notifications Places "), a("p", {
                    staticClass: "category"
                }, [t._v("Click to view notifications")])]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("top", "left")
                        }
                    }
                }, [t._v("Top Left")]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("top", "center")
                        }
                    }
                }, [t._v("Top Center")]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("top", "right")
                        }
                    }
                }, [t._v("Top Right")]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("bottom", "left")
                        }
                    }
                }, [t._v("Bottom Left")]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("bottom", "center")
                        }
                    }
                }, [t._v("Bottom Center")]), a("md-button", {
                    staticClass: "md-primary",
                    on: {
                        click: function(e) {
                            return t.notifyVue("bottom", "right")
                        }
                    }
                }, [t._v("Bottom Right")])], 1)])])])], 1)], 1)])])
            },
            je = [],
            De = {
                data: function() {
                    return {
                        type: ["", "info", "success", "warning", "danger"],
                        notifications: {
                            topCenter: !1
                        }
                    }
                },
                methods: {
                    notifyVue: function(t, e) {
                        var a = Math.floor(4 * Math.random() + 1);
                        this.$notify({
                            message: "Welcome to <b>Material Dashboard</b> - a beautiful freebie for every web developer.",
                            icon: "add_alert",
                            horizontalAlign: e,
                            verticalAlign: t,
                            type: this.type[a]
                        })
                    }
                }
            },
            Me = De,
            Pe = Object(c["a"])(Me, Ie, je, !1, null, null, null),
            Ee = Pe.exports,
            Ae = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "content"
                }, [a("div", {
                    staticClass: "md-layout"
                }, [a("div", {
                    staticClass: "md-layout-item md-size-66 mx-auto md-small-size-100"
                }, [a("md-card", [a("md-card-header", {
                    attrs: {
                        "data-background-color": "purple"
                    }
                }, [a("h4", {
                    staticClass: "title"
                }, [t._v("Vue Material Dashboard PRO")]), a("p", {
                    staticClass: "category"
                }, [t._v(" Are you looking for more components? Please check our Premium Version of Vue Material Dashboard. ")])]), a("md-card-content", [a("div", {
                    staticClass: "table-responsive table-upgrade"
                }, [a("table", {
                    staticClass: "table",
                    attrs: {
                        cellspacing: "0"
                    }
                }, [a("thead", [a("tr", [a("th"), a("th", {
                    staticClass: "text-center"
                }, [t._v("Free")]), a("th", {
                    staticClass: "text-center"
                }, [t._v("PRO")])])]), a("tbody", [a("tr", [a("td", [t._v("Components")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("60")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("200")])]), a("tr", [a("td", [t._v("Plugins")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("2")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("15")])]), a("tr", [a("td", [t._v("Example Pages")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("3")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("27")])]), a("tr", [a("td", [t._v("Login, Register, Pricing, Lock Pages")]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-times text-danger"
                })]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-check text-success"
                })])]), a("tr", [a("td", [t._v(" DataTables, VectorMap, SweetAlert, Wizard, jQueryValidation, FullCalendar etc... ")]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-times text-danger"
                })]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-check text-success"
                })])]), a("tr", [a("td", [t._v("Mini Sidebar")]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-times text-danger"
                })]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-check text-success"
                })])]), a("tr", [a("td", [t._v("Premium Support")]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-times text-danger"
                })]), a("td", {
                    staticClass: "text-center"
                }, [a("i", {
                    staticClass: "fa fa-check text-success"
                })])]), a("tr", [a("td"), a("td", {
                    staticClass: "text-center"
                }, [t._v("Free")]), a("td", {
                    staticClass: "text-center"
                }, [t._v("Just $59")])]), a("tr", [a("td", {
                    staticClass: "text-center"
                }), a("td", {
                    staticClass: "text-center"
                }, [a("md-button", {
                    staticClass: "md-default md-round",
                    attrs: {
                        href: "#",
                        disabled: ""
                    }
                }, [t._v("Current Version")])], 1), a("td", {
                    staticClass: "text-center"
                }, [a("md-button", {
                    staticClass: "md-info md-round",
                    attrs: {
                        target: "_blank",
                        href: "https://www.creative-tim.com/product/vue-material-dashboard-pro/?ref=vue-md-free-upgrade-live"
                    }
                }, [t._v("Upgrade to PRO")])], 1)])])])])])], 1)], 1)])])
            },
            Ne = [],
            Be = {},
            Le = Be,
            He = (a("4b83"), Object(c["a"])(Le, Ae, Ne, !1, null, "86fef1a4", null)),
            Fe = He.exports,
            Re = [{
                path: "/",
                component: Q,
                redirect: "/dashboard",
                children: [{
                    path: "dashboard",
                    name: "Dashboard",
                    component: Bt
                }, {
                    path: "user",
                    name: "User Profile",
                    component: ae
                }, {
                    path: "table",
                    name: "Table List",
                    component: le
                }, {
                    path: "typography",
                    name: "Typography",
                    component: fe
                }, {
                    path: "icons",
                    name: "Icons",
                    component: Ce
                }, {
                    path: "maps",
                    name: "Maps",
                    meta: {
                        hideFooter: !0
                    },
                    component: $e
                }, {
                    path: "notifications",
                    name: "Notifications",
                    component: Ee
                }, {
                    path: "upgrade",
                    name: "Upgrade to PRO",
                    component: Fe
                }]
            }],
            Ue = Re,
            Ve = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    directives: [{
                        name: "click-outside",
                        rawName: "v-click-outside",
                        value: t.closeDropDown,
                        expression: "closeDropDown"
                    }],
                    staticClass: "dropdown",
                    class: {
                        open: t.isOpen
                    },
                    on: {
                        click: t.toggleDropDown
                    }
                }, [t._t("title", [a("a", {
                    staticClass: "dropdown-toggle",
                    attrs: {
                        "data-toggle": "dropdown",
                        href: "javascript:void(0)"
                    }
                }, [a("i", {
                    class: t.icon
                }), a("p", {
                    staticClass: "notification"
                }, [t._v(" " + t._s(t.title) + " "), a("b", {
                    staticClass: "caret"
                })])])]), t._t("default")], 2)
            },
            Ke = [],
            Ge = {
                name: "drop-down",
                props: {
                    title: String,
                    icon: String
                },
                data: function() {
                    return {
                        isOpen: !1
                    }
                },
                methods: {
                    toggleDropDown: function() {
                        this.isOpen = !this.isOpen
                    },
                    closeDropDown: function() {
                        this.isOpen = !1
                    }
                }
            },
            Je = Ge,
            We = Object(c["a"])(Je, Ve, Ke, !1, null, null, null),
            Ye = We.exports,
            Qe = {
                install: function(t) {
                    t.component("drop-down", Ye)
                }
            },
            Xe = Qe,
            qe = a("c7db"),
            Ze = {
                install: function(t) {
                    t.directive("click-outside", qe["directive"])
                }
            },
            ta = Ze,
            ea = (a("c740"), a("a434"), function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "notifications"
                }, [a("transition-group", {
                    attrs: {
                        name: "list"
                    }
                }, t._l(t.notifications, (function(e) {
                    return a("notification", {
                        key: e.timestamp.getTime(),
                        attrs: {
                            message: e.message,
                            icon: e.icon,
                            type: e.type,
                            timestamp: e.timestamp,
                            "vertical-align": e.verticalAlign,
                            "horizontal-align": e.horizontalAlign
                        },
                        on: {
                            "on-close": t.removeNotification
                        }
                    })
                })), 1)], 1)
            }),
            aa = [],
            sa = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "alert open alert-with-icon",
                    class: [t.verticalAlign, t.horizontalAlign, t.alertType],
                    style: t.customPosition,
                    attrs: {
                        "data-notify": "container",
                        role: "alert",
                        "data-notify-position": "top-center"
                    },
                    on: {
                        click: function(e) {
                            return t.close()
                        }
                    }
                }, [a("button", {
                    staticClass: "close",
                    attrs: {
                        type: "button",
                        "aria-hidden": "true",
                        "data-notify": "dismiss"
                    },
                    on: {
                        click: t.close
                    }
                }, [t._v(" × ")]), a("i", {
                    staticClass: "material-icons",
                    attrs: {
                        "data-notify": "icon"
                    }
                }, [t._v(t._s(t.icon))]), a("span", {
                    attrs: {
                        "data-notify": "message"
                    },
                    domProps: {
                        innerHTML: t._s(t.message)
                    }
                })])
            },
            ia = [],
            na = (a("4de4"), a("a9e3"), {
                name: "notification",
                props: {
                    message: String,
                    icon: String,
                    verticalAlign: {
                        type: String,
                        default: "top"
                    },
                    horizontalAlign: {
                        type: String,
                        default: "center"
                    },
                    type: {
                        type: String,
                        default: "info"
                    },
                    timeout: {
                        type: Number,
                        default: 2500
                    },
                    timestamp: {
                        type: Date,
                        default: function() {
                            return new Date
                        }
                    }
                },
                data: function() {
                    return {
                        elmHeight: 0
                    }
                },
                computed: {
                    hasIcon: function() {
                        return this.icon && this.icon.length > 0
                    },
                    alertType: function() {
                        return "alert-".concat(this.type)
                    },
                    customPosition: function() {
                        var t = this,
                            e = 20,
                            a = this.elmHeight + 10,
                            s = this.$notifications.state.filter((function(e) {
                                return e.horizontalAlign === t.horizontalAlign && e.verticalAlign === t.verticalAlign && e.timestamp <= t.timestamp
                            })).length,
                            i = (s - 1) * a + e,
                            n = {};
                        return "top" === this.verticalAlign ? n.top = "".concat(i, "px") : n.bottom = "".concat(i, "px"), n
                    }
                },
                methods: {
                    close: function() {
                        this.$emit("on-close", this.timestamp)
                    }
                },
                mounted: function() {
                    this.elmHeight = this.$el.clientHeight, this.timeout && setTimeout(this.close, this.timeout)
                }
            }),
            oa = na,
            ra = (a("7b35"), Object(c["a"])(oa, sa, ia, !1, null, "3b98be06", null)),
            la = ra.exports,
            ca = {
                components: {
                    Notification: la
                },
                data: function() {
                    return {
                        notifications: this.$notifications.state
                    }
                },
                methods: {
                    removeNotification: function(t) {
                        this.$notifications.removeNotification(t)
                    }
                }
            },
            da = ca,
            ma = (a("6ae5"), Object(c["a"])(da, ea, aa, !1, null, null, null)),
            ua = ma.exports,
            pa = {
                state: [],
                removeNotification: function(t) {
                    var e = this.state.findIndex((function(e) {
                        return e.timestamp === t
                    })); - 1 !== e && this.state.splice(e, 1)
                },
                addNotification: function(t) {
                    t.timestamp = new Date, t.timestamp.setMilliseconds(t.timestamp.getMilliseconds() + this.state.length), this.state.push(t)
                },
                notify: function(t) {
                    var e = this;
                    Array.isArray(t) ? t.forEach((function(t) {
                        e.addNotification(t)
                    })) : this.addNotification(t)
                }
            },
            fa = {
                install: function(t) {
                    t.mixin({
                        data: function() {
                            return {
                                notificationStore: pa
                            }
                        },
                        methods: {
                            notify: function(t) {
                                this.notificationStore.notify(t)
                            }
                        }
                    }), Object.defineProperty(t.prototype, "$notify", {
                        get: function() {
                            return this.$root.notify
                        }
                    }), Object.defineProperty(t.prototype, "$notifications", {
                        get: function() {
                            return this.$root.notificationStore
                        }
                    }), t.component("Notifications", ua)
                }
            },
            ha = fa,
            va = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "sidebar",
                    style: t.sidebarStyle,
                    attrs: {
                        "data-color": t.sidebarItemColor,
                        "data-image": t.sidebarBackgroundImage
                    }
                }, [a("div", {
                    staticClass: "logo"
                }, [a("a", {
                    staticClass: "simple-text logo-mini",
                    attrs: {
                        href: "#"
                    }
                }, [a("div", {
                    staticClass: "logo-img"
                }, [a("vuetim/static/tte/img", {
                    attrs: {
                        src: t.imgLogo,
                        alt: ""
                    }
                })])]), a("a", {
                    staticClass: "simple-text logo-normal",
                    attrs: {
                        href: "https://www.creative-tim.com/product/vue-material-dashboard",
                        target: "_blank"
                    }
                }, [t._v(" " + t._s(t.title) + " ")])]), a("div", {
                    staticClass: "sidebar-wrapper"
                }, [t._t("content"), a("md-list", {
                    staticClass: "nav"
                }, [t._t("default", t._l(t.sidebarLinks, (function(t, e) {
                    return a("sidebar-link", {
                        key: t.name + e,
                        attrs: {
                            to: t.path,
                            link: t
                        }
                    })
                })))], 2)], 2)])
            },
            ba = [],
            ga = (a("c975"), function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "md-list-item"
                }, [a("router-link", t._b({
                    staticClass: "md-list-item-router md-list-item-container md-button-clean",
                    on: {
                        click: t.hideSidebar
                    }
                }, "router-link", t.$attrs, !1), [a("div", {
                    staticClass: "md-list-item-content md-ripple"
                }, [t._t("default", [a("md-icon", [t._v(t._s(t.link.icon))]), a("p", [t._v(t._s(t.link.name))])])], 2)])], 1)
            }),
            ya = [],
            Ca = {
                inject: {
                    autoClose: {
                        default: !0
                    }
                },
                props: {
                    link: {
                        type: [String, Object],
                        default: function() {
                            return {
                                name: "",
                                path: "",
                                icon: ""
                            }
                        }
                    },
                    tag: {
                        type: String,
                        default: "router-link"
                    }
                },
                methods: {
                    hideSidebar: function() {
                        this.autoClose && this.$sidebar && !0 === this.$sidebar.showSidebar && this.$sidebar.displaySidebar(!1)
                    }
                }
            },
            _a = Ca,
            wa = Object(c["a"])(_a, ga, ya, !1, null, null, null),
            ka = wa.exports,
            xa = {
                components: {
                    SidebarLink: ka
                },
                props: {
                    title: {
                        type: String,
                        default: "Vue MD"
                    },
                    sidebarBackgroundImage: {
                        type: String,
                        default: a("9524")
                    },
                    imgLogo: {
                        type: String,
                        default: a("fdbce")
                    },
                    sidebarItemColor: {
                        type: String,
                        default: "green",
                        validator: function(t) {
                            var e = ["", "purple", "blue", "green", "orange", "red"];
                            return -1 !== e.indexOf(t)
                        }
                    },
                    sidebarLinks: {
                        type: Array,
                        default: function() {
                            return []
                        }
                    },
                    autoClose: {
                        type: Boolean,
                        default: !0
                    }
                },
                provide: function() {
                    return {
                        autoClose: this.autoClose
                    }
                },
                computed: {
                    sidebarStyle: function() {
                        return {
                            backgroundImage: "url(".concat(this.sidebarBackgroundImage, ")")
                        }
                    }
                }
            },
            Sa = xa,
            Ta = (a("0efd"), Object(c["a"])(Sa, va, ba, !1, null, null, null)),
            Oa = Ta.exports,
            za = {
                showSidebar: !1,
                displaySidebar: function(t) {
                    this.showSidebar = t
                }
            },
            $a = {
                install: function(t) {
                    t.mixin({
                        data: function() {
                            return {
                                sidebarStore: za
                            }
                        }
                    }), Object.defineProperty(t.prototype, "$sidebar", {
                        get: function() {
                            return this.$root.sidebarStore
                        }
                    }), t.component("side-bar", Oa), t.component("sidebar-link", ka)
                }
            },
            Ia = $a,
            ja = a("43f9"),
            Da = a.n(ja),
            Ma = (a("43f4"), a("9e17"), a("54ba"), {
                install: function(t) {
                    t.use(Ia), t.use(Da.a)
                }
            }),
            Pa = a("ba48"),
            Ea = a.n(Pa),
            Aa = new i["a"]({
                routes: Ue,
                linkExactActiveClass: "nav-item active"
            });
        s["default"].prototype.$Chartist = Ea.a, s["default"].use(i["a"]), s["default"].use(Ma), s["default"].use(Xe), s["default"].use(ta), s["default"].use(ha), new s["default"]({
            el: "#app",
            render: function(t) {
                return t(m)
            },
            router: Aa,
            data: {
                Chartist: Ea.a
            }
        })
    },
    "6ae5": function(t, e, a) {
        "use strict";
        var s = a("b5b2"),
            i = a.n(s);
        i.a
    },
    "6de7": function(t, e, a) {},
    "738c": function(t, e, a) {},
    "7b35": function(t, e, a) {
        "use strict";
        var s = a("4ba2"),
            i = a.n(s);
        i.a
    },
    "7d6d": function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/sidebar-1.23832d31.jpg"
    },
    9524: function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/sidebar-2.32103624.jpg"
    },
    "9e17": function(t, e, a) {},
    a180: function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/marc.aba54d65.jpg"
    },
    aeef: function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/sidebar-3.3a54f533.jpg"
    },
    b51f: function(t, e, a) {},
    b5b2: function(t, e, a) {},
    cd1f: function(t, e, a) {},
    dac3: function(t, e, a) {
        "use strict";
        var s = a("b51f"),
            i = a.n(s);
        i.a
    },
    eb9e: function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/sidebar-4.3b7e38ed.jpg"
    },
    fdbce: function(t, e, a) {
        t.exports = a.p + "vuetim/static/tte/img/vue-logo.c2a605fb.png"
    }
});
