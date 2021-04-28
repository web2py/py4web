/*!

=========================================================
* Vue Notus - v1.0.0 based on Tailwind Starter Kit by Creative Tim
=========================================================

* Product Page: https://www.creative-tim.com/product/vue-notus
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/vue-notus/blob/master/LICENSE.md)

* Tailwind Starter Kit Page: https://www.creative-tim.com/learning-lab/tailwind-starter-kit/presentation

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
(function(t) {
    function e(e) {
        for (var s, i, o = e[0], n = e[1], c = e[2], p = 0, f = []; p < o.length; p++) i = o[p], Object.prototype.hasOwnProperty.call(l, i) && l[i] && f.push(l[i][0]), l[i] = 0;
        for (s in n) Object.prototype.hasOwnProperty.call(n, s) && (t[s] = n[s]);
        d && d(e);
        while (f.length) f.shift()();
        return r.push.apply(r, c || []), a()
    }

    function a() {
        for (var t, e = 0; e < r.length; e++) {
            for (var a = r[e], s = !0, o = 1; o < a.length; o++) {
                var n = a[o];
                0 !== l[n] && (s = !1)
            }
            s && (r.splice(e--, 1), t = i(i.s = a[0]))
        }
        return t
    }
    var s = {},
        l = {
            app: 0
        },
        r = [];

    function i(e) {
        if (s[e]) return s[e].exports;
        var a = s[e] = {
            i: e,
            l: !1,
            exports: {}
        };
        return t[e].call(a.exports, a, a.exports, i), a.l = !0, a.exports
    }
    i.m = t, i.c = s, i.d = function(t, e, a) {
        i.o(t, e) || Object.defineProperty(t, e, {
            enumerable: !0,
            get: a
        })
    }, i.r = function(t) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(t, "__esModule", {
            value: !0
        })
    }, i.t = function(t, e) {
        if (1 & e && (t = i(t)), 8 & e) return t;
        if (4 & e && "object" === typeof t && t && t.__esModule) return t;
        var a = Object.create(null);
        if (i.r(a), Object.defineProperty(a, "default", {
                enumerable: !0,
                value: t
            }), 2 & e && "string" != typeof t)
            for (var s in t) i.d(a, s, function(e) {
                return t[e]
            }.bind(null, s));
        return a
    }, i.n = function(t) {
        var e = t && t.__esModule ? function() {
            return t["default"]
        } : function() {
            return t
        };
        return i.d(e, "a", e), e
    }, i.o = function(t, e) {
        return Object.prototype.hasOwnProperty.call(t, e)
    }, i.p = "/";
    var o = window["webpackJsonp"] = window["webpackJsonp"] || [],
        n = o.push.bind(o);
    o.push = e, o = o.slice();
    for (var c = 0; c < o.length; c++) e(o[c]);
    var d = n;
    r.push([0, "chunk-vendors"]), a()
})({
    0: function(t, e, a) {
        t.exports = a("56d7")
    },
    "0b08": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-info-card.66aa97ea.png"
    },
    1454: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/angular.368685db.jpg"
    },
    "191e": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/documentation.e889cedc.png"
    },
    "1ac6": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/pattern_vue.d203753c.png"
    },
    "228c": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/team-1-800x800.53033970.jpg"
    },
    4250: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-btn-pink.d7124f46.png"
    },
    4424: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/login.a6f0905b.jpg"
    },
    4678: function(t, e, a) {
        var s = {
            "./af": "2bfb",
            "./af.js": "2bfb",
            "./ar": "8e73",
            "./ar-dz": "a356",
            "./ar-dz.js": "a356",
            "./ar-kw": "423e",
            "./ar-kw.js": "423e",
            "./ar-ly": "1cfd",
            "./ar-ly.js": "1cfd",
            "./ar-ma": "0a84",
            "./ar-ma.js": "0a84",
            "./ar-sa": "8230",
            "./ar-sa.js": "8230",
            "./ar-tn": "6d83",
            "./ar-tn.js": "6d83",
            "./ar.js": "8e73",
            "./az": "485c",
            "./az.js": "485c",
            "./be": "1fc1",
            "./be.js": "1fc1",
            "./bg": "84aa",
            "./bg.js": "84aa",
            "./bm": "a7fa",
            "./bm.js": "a7fa",
            "./bn": "9043",
            "./bn-bd": "9686",
            "./bn-bd.js": "9686",
            "./bn.js": "9043",
            "./bo": "d26a",
            "./bo.js": "d26a",
            "./br": "6887",
            "./br.js": "6887",
            "./bs": "2554",
            "./bs.js": "2554",
            "./ca": "d716",
            "./ca.js": "d716",
            "./cs": "3c0d",
            "./cs.js": "3c0d",
            "./cv": "03ec",
            "./cv.js": "03ec",
            "./cy": "9797",
            "./cy.js": "9797",
            "./da": "0f14",
            "./da.js": "0f14",
            "./de": "b469",
            "./de-at": "b3eb",
            "./de-at.js": "b3eb",
            "./de-ch": "bb71",
            "./de-ch.js": "bb71",
            "./de.js": "b469",
            "./dv": "598a",
            "./dv.js": "598a",
            "./el": "8d47",
            "./el.js": "8d47",
            "./en-au": "0e6b",
            "./en-au.js": "0e6b",
            "./en-ca": "3886",
            "./en-ca.js": "3886",
            "./en-gb": "39a6",
            "./en-gb.js": "39a6",
            "./en-ie": "e1d3",
            "./en-ie.js": "e1d3",
            "./en-il": "7333",
            "./en-il.js": "7333",
            "./en-in": "ec2e",
            "./en-in.js": "ec2e",
            "./en-nz": "6f50",
            "./en-nz.js": "6f50",
            "./en-sg": "b7e9",
            "./en-sg.js": "b7e9",
            "./eo": "65db",
            "./eo.js": "65db",
            "./es": "898b",
            "./es-do": "0a3c",
            "./es-do.js": "0a3c",
            "./es-mx": "b5b7",
            "./es-mx.js": "b5b7",
            "./es-us": "55c9",
            "./es-us.js": "55c9",
            "./es.js": "898b",
            "./et": "ec18",
            "./et.js": "ec18",
            "./eu": "0ff2",
            "./eu.js": "0ff2",
            "./fa": "8df4",
            "./fa.js": "8df4",
            "./fi": "81e9",
            "./fi.js": "81e9",
            "./fil": "d69a",
            "./fil.js": "d69a",
            "./fo": "0721",
            "./fo.js": "0721",
            "./fr": "9f26",
            "./fr-ca": "d9f8",
            "./fr-ca.js": "d9f8",
            "./fr-ch": "0e49",
            "./fr-ch.js": "0e49",
            "./fr.js": "9f26",
            "./fy": "7118",
            "./fy.js": "7118",
            "./ga": "5120",
            "./ga.js": "5120",
            "./gd": "f6b4",
            "./gd.js": "f6b4",
            "./gl": "8840",
            "./gl.js": "8840",
            "./gom-deva": "aaf2",
            "./gom-deva.js": "aaf2",
            "./gom-latn": "0caa",
            "./gom-latn.js": "0caa",
            "./gu": "e0c5",
            "./gu.js": "e0c5",
            "./he": "c7aa",
            "./he.js": "c7aa",
            "./hi": "dc4d",
            "./hi.js": "dc4d",
            "./hr": "4ba9",
            "./hr.js": "4ba9",
            "./hu": "5b14",
            "./hu.js": "5b14",
            "./hy-am": "d6b6",
            "./hy-am.js": "d6b6",
            "./id": "5038",
            "./id.js": "5038",
            "./is": "0558",
            "./is.js": "0558",
            "./it": "6e98",
            "./it-ch": "6f12",
            "./it-ch.js": "6f12",
            "./it.js": "6e98",
            "./ja": "079e",
            "./ja.js": "079e",
            "./jv": "b540",
            "./jv.js": "b540",
            "./ka": "201b",
            "./ka.js": "201b",
            "./kk": "6d79",
            "./kk.js": "6d79",
            "./km": "e81d",
            "./km.js": "e81d",
            "./kn": "3e92",
            "./kn.js": "3e92",
            "./ko": "22f8",
            "./ko.js": "22f8",
            "./ku": "2421",
            "./ku.js": "2421",
            "./ky": "9609",
            "./ky.js": "9609",
            "./lb": "440c",
            "./lb.js": "440c",
            "./lo": "b29d",
            "./lo.js": "b29d",
            "./lt": "26f9",
            "./lt.js": "26f9",
            "./lv": "b97c",
            "./lv.js": "b97c",
            "./me": "293c",
            "./me.js": "293c",
            "./mi": "688b",
            "./mi.js": "688b",
            "./mk": "6909",
            "./mk.js": "6909",
            "./ml": "02fb",
            "./ml.js": "02fb",
            "./mn": "958b",
            "./mn.js": "958b",
            "./mr": "39bd",
            "./mr.js": "39bd",
            "./ms": "ebe4",
            "./ms-my": "6403",
            "./ms-my.js": "6403",
            "./ms.js": "ebe4",
            "./mt": "1b45",
            "./mt.js": "1b45",
            "./my": "8689",
            "./my.js": "8689",
            "./nb": "6ce3",
            "./nb.js": "6ce3",
            "./ne": "3a39",
            "./ne.js": "3a39",
            "./nl": "facd",
            "./nl-be": "db29",
            "./nl-be.js": "db29",
            "./nl.js": "facd",
            "./nn": "b84c",
            "./nn.js": "b84c",
            "./oc-lnc": "167b",
            "./oc-lnc.js": "167b",
            "./pa-in": "f3ff",
            "./pa-in.js": "f3ff",
            "./pl": "8d57",
            "./pl.js": "8d57",
            "./pt": "f260",
            "./pt-br": "d2d4",
            "./pt-br.js": "d2d4",
            "./pt.js": "f260",
            "./ro": "972c",
            "./ro.js": "972c",
            "./ru": "957c",
            "./ru.js": "957c",
            "./sd": "6784",
            "./sd.js": "6784",
            "./se": "ffff",
            "./se.js": "ffff",
            "./si": "eda5",
            "./si.js": "eda5",
            "./sk": "7be6",
            "./sk.js": "7be6",
            "./sl": "8155",
            "./sl.js": "8155",
            "./sq": "c8f3",
            "./sq.js": "c8f3",
            "./sr": "cf1e",
            "./sr-cyrl": "13e9",
            "./sr-cyrl.js": "13e9",
            "./sr.js": "cf1e",
            "./ss": "52bd",
            "./ss.js": "52bd",
            "./sv": "5fbd",
            "./sv.js": "5fbd",
            "./sw": "74dc",
            "./sw.js": "74dc",
            "./ta": "3de5",
            "./ta.js": "3de5",
            "./te": "5cbb",
            "./te.js": "5cbb",
            "./tet": "576c",
            "./tet.js": "576c",
            "./tg": "3b1b",
            "./tg.js": "3b1b",
            "./th": "10e8",
            "./th.js": "10e8",
            "./tk": "5aff",
            "./tk.js": "5aff",
            "./tl-ph": "0f38",
            "./tl-ph.js": "0f38",
            "./tlh": "cf75",
            "./tlh.js": "cf75",
            "./tr": "0e81",
            "./tr.js": "0e81",
            "./tzl": "cf51",
            "./tzl.js": "cf51",
            "./tzm": "c109",
            "./tzm-latn": "b53d",
            "./tzm-latn.js": "b53d",
            "./tzm.js": "c109",
            "./ug-cn": "6117",
            "./ug-cn.js": "6117",
            "./uk": "ada2",
            "./uk.js": "ada2",
            "./ur": "5294",
            "./ur.js": "5294",
            "./uz": "2e8c",
            "./uz-latn": "010e",
            "./uz-latn.js": "010e",
            "./uz.js": "2e8c",
            "./vi": "2921",
            "./vi.js": "2921",
            "./x-pseudo": "fd7e",
            "./x-pseudo.js": "fd7e",
            "./yo": "7f33",
            "./yo.js": "7f33",
            "./zh-cn": "5c3a",
            "./zh-cn.js": "5c3a",
            "./zh-hk": "49ab",
            "./zh-hk.js": "49ab",
            "./zh-mo": "3a6c",
            "./zh-mo.js": "3a6c",
            "./zh-tw": "90ea",
            "./zh-tw.js": "90ea"
        };

        function l(t) {
            var e = r(t);
            return a(e)
        }

        function r(t) {
            if (!a.o(s, t)) {
                var e = new Error("Cannot find module '" + t + "'");
                throw e.code = "MODULE_NOT_FOUND", e
            }
            return s[t]
        }
        l.keys = function() {
            return Object.keys(s)
        }, l.resolve = r, t.exports = l, l.id = "4678"
    },
    5393: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-profile-card.51088525.png"
    },
    "56d7": function(t, e, a) {
        "use strict";
        a.r(e);
        a("e260"), a("e6cf"), a("cca6"), a("a79d");
        var s = a("a026"),
            l = a("8c4f"),
            r = (a("becf"), a("9c9e"), function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    attrs: {
                        id: "app"
                    }
                }, [a("router-view")], 1)
            }),
            i = [],
            o = a("2877"),
            n = {},
            c = Object(o["a"])(n, r, i, !1, null, null, null),
            d = c.exports,
            p = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("sidebar"), a("div", {
                    staticClass: "relative md:ml-64 bg-gray-200"
                }, [a("admin-navbar"), a("header-stats"), a("div", {
                    staticClass: "px-4 md:px-10 mx-auto w-full -m-24"
                }, [a("router-view"), a("footer-admin")], 1)], 1)], 1)
            },
            f = [],
            u = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("nav", {
                    staticClass: "absolute top-0 left-0 w-full z-10 bg-transparent md:flex-row md:flex-no-wrap md:justify-start flex items-center p-4"
                }, [a("div", {
                    staticClass: "w-full mx-autp items-center flex justify-between md:flex-no-wrap flex-wrap md:px-10 px-4"
                }, [a("a", {
                    staticClass: "text-white text-sm uppercase hidden lg:inline-block font-semibold",
                    attrs: {
                        href: "javascript:void(0)"
                    }
                }, [t._v(" Dashboard ")]), t._m(0), a("ul", {
                    staticClass: "flex-col md:flex-row list-none items-center hidden md:flex"
                }, [a("user-dropdown")], 1)])])
            },
            x = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("form", {
                    staticClass: "md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"
                }, [a("div", {
                    staticClass: "relative flex w-full flex-wrap items-stretch"
                }, [a("span", {
                    staticClass: "z-10 h-full leading-snug font-normal absolute text-center text-gray-400 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
                }, [a("i", {
                    staticClass: "fas fa-search"
                })]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:shadow-outline w-full pl-10",
                    attrs: {
                        type: "text",
                        placeholder: "Search here..."
                    }
                })])])
            }],
            m = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("a", {
                    ref: "btnDropdownRef",
                    staticClass: "text-gray-600 block",
                    attrs: {
                        href: "#pablo"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleDropdown(e)
                        }
                    }
                }, [a("div", {
                    staticClass: "items-center flex"
                }, [a("span", {
                    staticClass: "w-12 h-12 text-sm text-white bg-gray-300 inline-flex items-center justify-center rounded-full"
                }, [a("img", {
                    staticClass: "w-full rounded-full align-middle border-none shadow-lg",
                    attrs: {
                        alt: "...",
                        src: t.image
                    }
                })])])]), a("div", {
                    ref: "popoverDropdownRef",
                    staticClass: "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",
                    class: {
                        hidden: !t.dropdownPopoverShow, block: t.dropdownPopoverShow
                    }
                }, [a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Another action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Something else here ")]), a("div", {
                    staticClass: "h-0 my-2 border border-solid border-gray-200"
                }), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Seprated link ")])])])
            },
            b = [],
            g = a("39c3"),
            w = a("228c"),
            h = a.n(w),
            v = {
                data: function() {
                    return {
                        dropdownPopoverShow: !1,
                        image: h.a
                    }
                },
                methods: {
                    toggleDropdown: function(t) {
                        t.preventDefault(), this.dropdownPopoverShow ? this.dropdownPopoverShow = !1 : (this.dropdownPopoverShow = !0, Object(g["a"])(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
                            placement: "bottom-start"
                        }))
                    }
                }
            },
            C = v,
            y = Object(o["a"])(C, m, b, !1, null, null, null),
            _ = y.exports,
            k = {
                components: {
                    UserDropdown: _
                }
            },
            j = k,
            S = Object(o["a"])(j, u, x, !1, null, null, null),
            E = S.exports,
            $ = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("nav", {
                    staticClass: "md:left-0 md:block md:fixed md:top-0 md:bottom-0 md:overflow-y-auto md:flex-row md:flex-no-wrap md:overflow-hidden shadow-xl bg-white flex flex-wrap items-center justify-between relative md:w-64 z-10 py-4 px-6"
                }, [a("div", {
                    staticClass: "md:flex-col md:items-stretch md:min-h-full md:flex-no-wrap px-0 flex flex-wrap items-center justify-between w-full mx-auto"
                }, [a("button", {
                    staticClass: "cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent",
                    attrs: {
                        type: "button"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleCollapseShow("bg-white m-2 py-3 px-6")
                        }
                    }
                }, [a("i", {
                    staticClass: "fas fa-bars"
                })]), a("router-link", {
                    staticClass: "md:block text-left md:pb-2 text-gray-700 mr-0 inline-block whitespace-no-wrap text-sm uppercase font-bold p-4 px-0",
                    attrs: {
                        to: "/"
                    }
                }, [t._v(" Vue Notus ")]), a("ul", {
                    staticClass: "md:hidden items-center flex flex-wrap list-none"
                }, [a("li", {
                    staticClass: "inline-block relative"
                }, [a("notification-dropdown")], 1), a("li", {
                    staticClass: "inline-block relative"
                }, [a("user-dropdown")], 1)]), a("div", {
                    staticClass: "md:flex md:flex-col md:items-stretch md:opacity-100 md:relative md:mt-4 md:shadow-none shadow absolute top-0 left-0 right-0 z-40 overflow-y-auto overflow-x-hidden h-auto items-center flex-1 rounded",
                    class: t.collapseShow
                }, [a("div", {
                    staticClass: "md:min-w-full md:hidden block pb-4 mb-4 border-b border-solid border-gray-300"
                }, [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-6/12"
                }, [a("router-link", {
                    staticClass: "md:block text-left md:pb-2 text-gray-700 mr-0 inline-block whitespace-no-wrap text-sm uppercase font-bold p-4 px-0",
                    attrs: {
                        to: "/"
                    }
                }, [t._v(" Vue Notus ")])], 1), a("div", {
                    staticClass: "w-6/12 flex justify-end"
                }, [a("button", {
                    staticClass: "cursor-pointer text-black opacity-50 md:hidden px-3 py-1 text-xl leading-none bg-transparent rounded border border-solid border-transparent",
                    attrs: {
                        type: "button"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleCollapseShow("hidden")
                        }
                    }
                }, [a("i", {
                    staticClass: "fas fa-times"
                })])])])]), t._m(0), a("hr", {
                    staticClass: "my-4 md:min-w-full"
                }), a("h6", {
                    staticClass: "md:min-w-full text-gray-600 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
                }, [t._v(" Admin Layout Pages ")]), a("ul", {
                    staticClass: "md:flex-col md:min-w-full flex flex-col list-none"
                }, [a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    attrs: {
                        to: "/admin/dashboard"
                    },
                    scopedSlots: t._u([{
                        key: "default",
                        fn: function(e) {
                            var s = e.href,
                                l = (e.route, e.navigate),
                                r = e.isActive;
                            return [a("a", {
                                staticClass: "text-xs uppercase py-3 font-bold block",
                                class: [r ? "text-green-500 hover:text-green-600" : "text-gray-800 hover:text-gray-600"],
                                attrs: {
                                    href: s
                                },
                                on: {
                                    click: l
                                }
                            }, [a("i", {
                                staticClass: "fas fa-tv mr-2 text-sm",
                                class: [r ? "opacity-75" : "text-gray-400"]
                            }), t._v(" Dashboard ")])]
                        }
                    }])
                })], 1), a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    attrs: {
                        to: "/admin/settings"
                    },
                    scopedSlots: t._u([{
                        key: "default",
                        fn: function(e) {
                            var s = e.href,
                                l = (e.route, e.navigate),
                                r = e.isActive;
                            return [a("a", {
                                staticClass: "text-xs uppercase py-3 font-bold block",
                                class: [r ? "text-green-500 hover:text-green-600" : "text-gray-800 hover:text-gray-600"],
                                attrs: {
                                    href: s
                                },
                                on: {
                                    click: l
                                }
                            }, [a("i", {
                                staticClass: "fas fa-tools mr-2 text-sm",
                                class: [r ? "opacity-75" : "text-gray-400"]
                            }), t._v(" Settings ")])]
                        }
                    }])
                })], 1), a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    attrs: {
                        to: "/admin/tables"
                    },
                    scopedSlots: t._u([{
                        key: "default",
                        fn: function(e) {
                            var s = e.href,
                                l = (e.route, e.navigate),
                                r = e.isActive;
                            return [a("a", {
                                staticClass: "text-xs uppercase py-3 font-bold block",
                                class: [r ? "text-green-500 hover:text-green-600" : "text-gray-800 hover:text-gray-600"],
                                attrs: {
                                    href: s
                                },
                                on: {
                                    click: l
                                }
                            }, [a("i", {
                                staticClass: "fas fa-table mr-2 text-sm",
                                class: [r ? "opacity-75" : "text-gray-400"]
                            }), t._v(" Tables ")])]
                        }
                    }])
                })], 1), a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    attrs: {
                        to: "/admin/maps"
                    },
                    scopedSlots: t._u([{
                        key: "default",
                        fn: function(e) {
                            var s = e.href,
                                l = (e.route, e.navigate),
                                r = e.isActive;
                            return [a("a", {
                                staticClass: "text-xs uppercase py-3 font-bold block",
                                class: [r ? "text-green-500 hover:text-green-600" : "text-gray-800 hover:text-gray-600"],
                                attrs: {
                                    href: s
                                },
                                on: {
                                    click: l
                                }
                            }, [a("i", {
                                staticClass: "fas fa-map-marked mr-2 text-sm",
                                class: [r ? "opacity-75" : "text-gray-400"]
                            }), t._v(" Maps ")])]
                        }
                    }])
                })], 1)]), a("hr", {
                    staticClass: "my-4 md:min-w-full"
                }), a("h6", {
                    staticClass: "md:min-w-full text-gray-600 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
                }, [t._v(" Auth Layout Pages ")]), a("ul", {
                    staticClass: "md:flex-col md:min-w-full flex flex-col list-none md:mb-4"
                }, [a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-xs uppercase py-3 font-bold block",
                    attrs: {
                        to: "/auth/login"
                    }
                }, [a("i", {
                    staticClass: "fas fa-fingerprint text-gray-400 mr-2 text-sm"
                }), t._v(" Login ")])], 1), a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-xs uppercase py-3 font-bold block",
                    attrs: {
                        to: "/auth/register"
                    }
                }, [a("i", {
                    staticClass: "fas fa-clipboard-list text-gray-400 mr-2 text-sm"
                }), t._v(" Register ")])], 1)]), a("hr", {
                    staticClass: "my-4 md:min-w-full"
                }), a("h6", {
                    staticClass: "md:min-w-full text-gray-600 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
                }, [t._v(" No Layout Pages ")]), a("ul", {
                    staticClass: "md:flex-col md:min-w-full flex flex-col list-none md:mb-4"
                }, [a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-xs uppercase py-3 font-bold block",
                    attrs: {
                        to: "/landing"
                    }
                }, [a("i", {
                    staticClass: "fas fa-newspaper text-gray-400 mr-2 text-sm"
                }), t._v(" Landing Page ")])], 1), a("li", {
                    staticClass: "items-center"
                }, [a("router-link", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-xs uppercase py-3 font-bold block",
                    attrs: {
                        to: "/profile"
                    }
                }, [a("i", {
                    staticClass: "fas fa-user-circle text-gray-400 mr-2 text-sm"
                }), t._v(" Profile Page ")])], 1)]), a("hr", {
                    staticClass: "my-4 md:min-w-full"
                }), a("h6", {
                    staticClass: "md:min-w-full text-gray-600 text-xs uppercase font-bold block pt-1 pb-4 no-underline"
                }, [t._v(" Documentation ")]), t._m(1)])], 1)])
            },
            D = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("form", {
                    staticClass: "mt-6 mb-4 md:hidden"
                }, [a("div", {
                    staticClass: "mb-3 pt-0"
                }, [a("input", {
                    staticClass: "px-3 py-2 h-12 border border-solid border-gray-600 placeholder-gray-400 text-gray-700 bg-white rounded text-base leading-snug shadow-none outline-none focus:outline-none w-full font-normal",
                    attrs: {
                        type: "text",
                        placeholder: "Search"
                    }
                })])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("ul", {
                    staticClass: "md:flex-col md:min-w-full flex flex-col list-none md:mb-4"
                }, [a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/colors/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fas fa-paint-brush mr-2 text-gray-400 text-base"
                }), t._v(" Styles ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/alerts/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-css3-alt mr-2 text-gray-400 text-base"
                }), t._v(" CSS Components ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/angular/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-angular mr-2 text-gray-400 text-base"
                }), t._v(" Angular ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/js/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-js-square mr-2 text-gray-400 text-base"
                }), t._v(" Javascript ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/nextjs/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-react mr-2 text-gray-400 text-base"
                }), t._v(" NextJS ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/react/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-react mr-2 text-gray-400 text-base"
                }), t._v(" React ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/svelte/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fas fa-link mr-2 text-gray-400 text-base"
                }), t._v(" Svelte ")])]), a("li", {
                    staticClass: "inline-flex"
                }, [a("a", {
                    staticClass: "text-gray-800 hover:text-gray-600 text-sm block mb-4 no-underline font-semibold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-vuejs mr-2 text-gray-400 text-base"
                }), t._v(" VueJS ")])])])
            }],
            O = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("a", {
                    ref: "btnDropdownRef",
                    staticClass: "text-gray-600 block py-1 px-3",
                    on: {
                        click: function(e) {
                            return t.toggleDropdown(e)
                        }
                    }
                }, [a("i", {
                    staticClass: "fas fa-bell"
                })]), a("div", {
                    ref: "popoverDropdownRef",
                    staticClass: "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",
                    class: {
                        hidden: !t.dropdownPopoverShow, block: t.dropdownPopoverShow
                    }
                }, [a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Another action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Something else here ")]), a("div", {
                    staticClass: "h-0 my-2 border border-solid border-gray-200"
                }), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Seprated link ")])])])
            },
            P = [],
            A = {
                data: function() {
                    return {
                        dropdownPopoverShow: !1
                    }
                },
                methods: {
                    toggleDropdown: function(t) {
                        t.preventDefault(), this.dropdownPopoverShow ? this.dropdownPopoverShow = !1 : (this.dropdownPopoverShow = !0, Object(g["a"])(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
                            placement: "bottom-start"
                        }))
                    }
                }
            },
            T = A,
            F = Object(o["a"])(T, O, P, !1, null, null, null),
            L = F.exports,
            N = {
                data: function() {
                    return {
                        collapseShow: "hidden"
                    }
                },
                methods: {
                    toggleCollapseShow: function(t) {
                        this.collapseShow = t
                    }
                },
                components: {
                    NotificationDropdown: L,
                    UserDropdown: _
                }
            },
            z = N,
            R = Object(o["a"])(z, $, D, !1, null, null, null),
            B = R.exports,
            I = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative bg-green-600 md:pt-32 pb-32 pt-12"
                }, [a("div", {
                    staticClass: "px-4 md:px-10 mx-auto w-full"
                }, [a("div", [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 xl:w-3/12 px-4"
                }, [a("card-stats", {
                    attrs: {
                        statSubtitle: "TRAFFIC",
                        statTitle: "350,897",
                        statArrow: "up",
                        statPercent: "3.48",
                        statPercentColor: "text-green-500",
                        statDescripiron: "Since last month",
                        statIconName: "far fa-chart-bar",
                        statIconColor: "bg-red-500"
                    }
                })], 1), a("div", {
                    staticClass: "w-full lg:w-6/12 xl:w-3/12 px-4"
                }, [a("card-stats", {
                    attrs: {
                        statSubtitle: "NEW USERS",
                        statTitle: "2,356",
                        statArrow: "down",
                        statPercent: "3.48",
                        statPercentColor: "text-red-500",
                        statDescripiron: "Since last week",
                        statIconName: "fas fa-chart-pie",
                        statIconColor: "bg-orange-500"
                    }
                })], 1), a("div", {
                    staticClass: "w-full lg:w-6/12 xl:w-3/12 px-4"
                }, [a("card-stats", {
                    attrs: {
                        statSubtitle: "SALES",
                        statTitle: "924",
                        statArrow: "down",
                        statPercent: "1.10",
                        statPercentColor: "text-orange-500",
                        statDescripiron: "Since yesterday",
                        statIconName: "fas fa-users",
                        statIconColor: "bg-pink-500"
                    }
                })], 1), a("div", {
                    staticClass: "w-full lg:w-6/12 xl:w-3/12 px-4"
                }, [a("card-stats", {
                    attrs: {
                        statSubtitle: "PERFORMANCE",
                        statTitle: "49,65%",
                        statArrow: "up",
                        statPercent: "12",
                        statPercentColor: "text-green-500",
                        statDescripiron: "Since last month",
                        statIconName: "fas fa-percent",
                        statIconColor: "bg-green-500"
                    }
                })], 1)])])])])
            },
            M = [],
            J = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
                }, [a("div", {
                    staticClass: "flex-auto p-4"
                }, [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "relative w-full pr-4 max-w-full flex-grow flex-1"
                }, [a("h5", {
                    staticClass: "text-gray-500 uppercase font-bold text-xs"
                }, [t._v(" " + t._s(t.statSubtitle) + " ")]), a("span", {
                    staticClass: "font-semibold text-xl text-gray-800"
                }, [t._v(" " + t._s(t.statTitle) + " ")])]), a("div", {
                    staticClass: "relative w-auto pl-4 flex-initial"
                }, [a("div", {
                    staticClass: "text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full",
                    class: [t.statIconColor]
                }, [a("i", {
                    class: [t.statIconName]
                })])])]), a("p", {
                    staticClass: "text-sm text-gray-500 mt-4"
                }, [a("span", {
                    staticClass: "mr-2",
                    class: [t.statPercentColor]
                }, [a("i", {
                    class: ["up" === t.statArrow ? "fas fa-arrow-up" : "fas fa-arrow-down"]
                }), t._v(" " + t._s(t.statPercent) + "% ")]), a("span", {
                    staticClass: "whitespace-no-wrap"
                }, [t._v(t._s(t.statDescripiron))])])])])
            },
            V = [],
            U = (a("c975"), {
                name: "card-stats",
                props: {
                    statSubtitle: {
                        type: String,
                        default: "Traffic"
                    },
                    statTitle: {
                        type: String,
                        default: "350,897"
                    },
                    statArrow: {
                        default: "up",
                        validator: function(t) {
                            return -1 !== ["up", "down"].indexOf(t)
                        }
                    },
                    statPercent: {
                        type: String,
                        default: "3.48"
                    },
                    statPercentColor: {
                        type: String,
                        default: "text-green-500"
                    },
                    statDescripiron: {
                        type: String,
                        default: "Since last month"
                    },
                    statIconName: {
                        type: String,
                        default: "far fa-chart-bar"
                    },
                    statIconColor: {
                        type: String,
                        default: "bg-red-500"
                    }
                }
            }),
            q = U,
            Y = Object(o["a"])(q, J, V, !1, null, null, null),
            W = Y.exports,
            G = {
                components: {
                    CardStats: W
                }
            },
            H = G,
            K = Object(o["a"])(H, I, M, !1, null, null, null),
            Z = K.exports,
            Q = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("footer", {
                    staticClass: "block py-4"
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [a("hr", {
                    staticClass: "mb-4 border-b-1 border-gray-300"
                }), a("div", {
                    staticClass: "flex flex-wrap items-center md:justify-between justify-center"
                }, [a("div", {
                    staticClass: "w-full md:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "text-sm text-gray-600 font-semibold py-1 text-center md:text-left"
                }, [t._v(" Copyright © " + t._s(t.date) + " "), a("a", {
                    staticClass: "text-gray-600 hover:text-gray-800 text-sm font-semibold py-1",
                    attrs: {
                        href: "https://www.creative-tim.com?ref=vn-footer-admin"
                    }
                }, [t._v(" Creative Tim ")])])]), t._m(0)])])])
            },
            X = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full md:w-8/12 px-4"
                }, [a("ul", {
                    staticClass: "flex flex-wrap list-none md:justify-end justify-center"
                }, [a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://www.creative-tim.com?ref=vn-footer-admin"
                    }
                }, [t._v(" Creative Tim ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://www.creative-tim.com/presentation?ref=vn-footer-admin"
                    }
                }, [t._v(" About Us ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "http://blog.creative-tim.com?ref=vn-footer-admin"
                    }
                }, [t._v(" Blog ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus/blob/master/LICENSE.md?ref=vn-footer-admin"
                    }
                }, [t._v(" MIT License ")])])])])
            }],
            tt = {
                data: function() {
                    return {
                        date: (new Date).getFullYear()
                    }
                }
            },
            et = tt,
            at = Object(o["a"])(et, Q, X, !1, null, null, null),
            st = at.exports,
            lt = {
                name: "admin-layout",
                components: {
                    AdminNavbar: E,
                    Sidebar: B,
                    HeaderStats: Z,
                    FooterAdmin: st
                }
            },
            rt = lt,
            it = Object(o["a"])(rt, p, f, !1, null, null, null),
            ot = it.exports,
            nt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("navbar"), a("main", [a("section", {
                    staticClass: "relative w-full h-full py-40 min-h-screen"
                }, [a("div", {
                    staticClass: "absolute top-0 w-full h-full bg-gray-900 bg-no-repeat bg-full",
                    style: "background-image: url('" + t.registerBg2 + "');"
                }), a("router-view"), a("footer-small", {
                    attrs: {
                        absolute: ""
                    }
                })], 1)])], 1)
            },
            ct = [],
            dt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("nav", {
                    staticClass: "top-0 absolute z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg"
                }, [a("div", {
                    staticClass: "container px-4 mx-auto flex flex-wrap items-center justify-between"
                }, [a("div", {
                    staticClass: "w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start"
                }, [a("router-link", {
                    staticClass: "text-white text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-no-wrap uppercase",
                    attrs: {
                        to: "/"
                    }
                }, [t._v(" Vue Notus ")]), a("button", {
                    staticClass: "cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none",
                    attrs: {
                        type: "button"
                    },
                    on: {
                        click: t.setNavbarOpen
                    }
                }, [a("i", {
                    staticClass: "text-white fas fa-bars"
                })])], 1), a("div", {
                    staticClass: "lg:flex flex-grow items-center bg-white lg:bg-transparent lg:shadow-none",
                    class: [t.navbarOpen ? "block rounded shadow-lg" : "hidden"],
                    attrs: {
                        id: "example-navbar-warning"
                    }
                }, [t._m(0), a("ul", {
                    staticClass: "flex flex-col lg:flex-row list-none lg:ml-auto"
                }, [a("li", {
                    staticClass: "flex items-center"
                }, [a("PagesDropdown")], 1), t._m(1), t._m(2), t._m(3), t._m(4)])])])])
            },
            pt = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("ul", {
                    staticClass: "flex flex-col lg:flex-row list-none mr-auto"
                }, [a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "lg:text-white lg:hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-auth-navbar"
                    }
                }, [a("i", {
                    staticClass: "lg:text-gray-300 text-gray-500 far fa-file-alt text-lg leading-lg mr-2"
                }), t._v(" Docs ")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "lg:text-white lg:hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "lg:text-gray-300 text-gray-500 fab fa-facebook text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Share")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "lg:text-white lg:hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://twitter.com/intent/tweet?url=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F&text=Start%20your%20development%20with%20a%20Free%20Tailwind%20CSS%20and%20VueJS%20UI%20Kit%20and%20Admin.%20Let%20Vue%20Notus%20amaze%20you%20with%20its%20cool%20features%20and%20build%20tools%20and%20get%20your%20project%20to%20a%20whole%20new%20level.%20",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "lg:text-gray-300 text-gray-500 fab fa-twitter text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Tweet")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "lg:text-white lg:hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus?ref=vn-auth-navbar",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "lg:text-gray-300 text-gray-500 fab fa-github text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Star")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("button", {
                    staticClass: "bg-white text-gray-800 active:bg-gray-100 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fas fa-arrow-alt-circle-down"
                }), t._v(" Download ")])])
            }],
            ft = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("a", {
                    ref: "btnDropdownRef",
                    staticClass: "lg:text-white lg:hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "#pablo"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleDropdown(e)
                        }
                    }
                }, [t._v(" Demo Pages ")]), a("div", {
                    ref: "popoverDropdownRef",
                    staticClass: "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",
                    class: {
                        hidden: !t.dropdownPopoverShow, block: t.dropdownPopoverShow
                    }
                }, [a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" Admin Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/dashboard"
                    }
                }, [t._v(" Dashboard ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/settings"
                    }
                }, [t._v(" Settings ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/tables"
                    }
                }, [t._v(" Tables ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/maps"
                    }
                }, [t._v(" Maps ")]), a("div", {
                    staticClass: "h-0 mx-4 my-2 border border-solid border-gray-200"
                }), a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" Auth Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/auth/login"
                    }
                }, [t._v(" Login ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/auth/register"
                    }
                }, [t._v(" Register ")]), a("div", {
                    staticClass: "h-0 mx-4 my-2 border border-solid border-gray-200"
                }), a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" No Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/landing"
                    }
                }, [t._v(" Lading ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/profile"
                    }
                }, [t._v(" Profile ")])], 1)])
            },
            ut = [],
            xt = {
                data: function() {
                    return {
                        dropdownPopoverShow: !1
                    }
                },
                methods: {
                    toggleDropdown: function(t) {
                        t.preventDefault(), this.dropdownPopoverShow ? this.dropdownPopoverShow = !1 : (this.dropdownPopoverShow = !0, Object(g["a"])(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
                            placement: "bottom-start"
                        }))
                    }
                }
            },
            mt = xt,
            bt = Object(o["a"])(mt, ft, ut, !1, null, null, null),
            gt = bt.exports,
            wt = {
                data: function() {
                    return {
                        navbarOpen: !1
                    }
                },
                methods: {
                    setNavbarOpen: function() {
                        this.navbarOpen = !this.navbarOpen
                    }
                },
                components: {
                    PagesDropdown: gt
                }
            },
            ht = wt,
            vt = Object(o["a"])(ht, dt, pt, !1, null, null, null),
            Ct = vt.exports,
            yt = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("footer", {
                    staticClass: "pb-6",
                    class: [t.absolute ? "absolute w-full bottom-0 bg-gray-900" : "relative"]
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [a("hr", {
                    staticClass: "mb-6 border-b-1 border-gray-700"
                }), a("div", {
                    staticClass: "flex flex-wrap items-center md:justify-between justify-center"
                }, [a("div", {
                    staticClass: "w-full md:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "text-sm text-gray-600 font-semibold py-1 text-center md:text-left"
                }, [t._v(" Copyright © " + t._s(t.date) + " "), a("a", {
                    staticClass: "text-white hover:text-gray-400 text-sm font-semibold py-1",
                    attrs: {
                        href: "https://www.creative-tim.com?ref=vn-footer-small"
                    }
                }, [t._v(" Creative Tim ")])])]), t._m(0)])])])
            },
            _t = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full md:w-8/12 px-4"
                }, [a("ul", {
                    staticClass: "flex flex-wrap list-none md:justify-end justify-center"
                }, [a("li", [a("a", {
                    staticClass: "text-white hover:text-gray-400 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://www.creative-tim.com?ref=vn-footer-small"
                    }
                }, [t._v(" Creative Tim ")])]), a("li", [a("a", {
                    staticClass: "text-white hover:text-gray-400 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://www.creative-tim.com/presentation?ref=vn-footer-small"
                    }
                }, [t._v(" About Us ")])]), a("li", [a("a", {
                    staticClass: "text-white hover:text-gray-400 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "http://blog.creative-tim.com?ref=vn-footer-small"
                    }
                }, [t._v(" Blog ")])]), a("li", [a("a", {
                    staticClass: "text-white hover:text-gray-400 text-sm font-semibold block py-1 px-3",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus/blob/master/LICENSE.md?ref=vn-footer-small"
                    }
                }, [t._v(" MIT License ")])])])])
            }],
            kt = {
                data: function() {
                    return {
                        date: (new Date).getFullYear()
                    }
                },
                props: {
                    absolute: {
                        type: Boolean,
                        default: !1
                    }
                }
            },
            jt = kt,
            St = Object(o["a"])(jt, yt, _t, !1, null, null, null),
            Et = St.exports,
            $t = a("7017"),
            Dt = a.n($t),
            Ot = {
                data: function() {
                    return {
                        registerBg2: Dt.a
                    }
                },
                components: {
                    Navbar: Ct,
                    FooterSmall: Et
                }
            },
            Pt = Ot,
            At = Object(o["a"])(Pt, nt, ct, !1, null, null, null),
            Tt = At.exports,
            Ft = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full xl:w-8/12 mb-12 xl:mb-0 px-4"
                }, [a("card-line-chart")], 1), a("div", {
                    staticClass: "w-full xl:w-4/12 px-4"
                }, [a("card-bar-chart")], 1)]), a("div", {
                    staticClass: "flex flex-wrap mt-4"
                }, [a("div", {
                    staticClass: "w-full xl:w-8/12 mb-12 xl:mb-0 px-4"
                }, [a("card-page-visits")], 1), a("div", {
                    staticClass: "w-full xl:w-4/12 px-4"
                }, [a("card-social-traffic")], 1)])])
            },
            Lt = [],
            Nt = function() {
                var t = this,
                    e = t.$createElement;
                t._self._c;
                return t._m(0)
            },
            zt = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-gray-800"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-4 py-3 bg-transparent"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "relative w-full max-w-full flex-grow flex-1"
                }, [a("h6", {
                    staticClass: "uppercase text-gray-200 mb-1 text-xs font-semibold"
                }, [t._v(" Overview ")]), a("h2", {
                    staticClass: "text-white text-xl font-semibold"
                }, [t._v(" Sales value ")])])])]), a("div", {
                    staticClass: "p-4 flex-auto"
                }, [a("div", {
                    staticClass: "relative h-350-px"
                }, [a("canvas", {
                    attrs: {
                        id: "line-chart"
                    }
                })])])])
            }],
            Rt = a("30ef"),
            Bt = a.n(Rt),
            It = {
                mounted: function() {
                    this.$nextTick((function() {
                        var t = {
                                type: "line",
                                data: {
                                    labels: ["January", "February", "March", "April", "May", "June", "July"],
                                    datasets: [{
                                        label: (new Date).getFullYear(),
                                        backgroundColor: "#4c51bf",
                                        borderColor: "#4c51bf",
                                        data: [65, 78, 66, 44, 56, 67, 75],
                                        fill: !1
                                    }, {
                                        label: (new Date).getFullYear() - 1,
                                        fill: !1,
                                        backgroundColor: "#fff",
                                        borderColor: "#fff",
                                        data: [40, 68, 86, 74, 56, 60, 87]
                                    }]
                                },
                                options: {
                                    maintainAspectRatio: !1,
                                    responsive: !0,
                                    title: {
                                        display: !1,
                                        text: "Sales Charts",
                                        fontColor: "white"
                                    },
                                    legend: {
                                        labels: {
                                            fontColor: "white"
                                        },
                                        align: "end",
                                        position: "bottom"
                                    },
                                    tooltips: {
                                        mode: "index",
                                        intersect: !1
                                    },
                                    hover: {
                                        mode: "nearest",
                                        intersect: !0
                                    },
                                    scales: {
                                        xAxes: [{
                                            ticks: {
                                                fontColor: "rgba(255,255,255,.7)"
                                            },
                                            display: !0,
                                            scaleLabel: {
                                                display: !1,
                                                labelString: "Month",
                                                fontColor: "white"
                                            },
                                            gridLines: {
                                                display: !1,
                                                borderDash: [2],
                                                borderDashOffset: [2],
                                                color: "rgba(33, 37, 41, 0.3)",
                                                zeroLineColor: "rgba(0, 0, 0, 0)",
                                                zeroLineBorderDash: [2],
                                                zeroLineBorderDashOffset: [2]
                                            }
                                        }],
                                        yAxes: [{
                                            ticks: {
                                                fontColor: "rgba(255,255,255,.7)"
                                            },
                                            display: !0,
                                            scaleLabel: {
                                                display: !1,
                                                labelString: "Value",
                                                fontColor: "white"
                                            },
                                            gridLines: {
                                                borderDash: [3],
                                                borderDashOffset: [3],
                                                drawBorder: !1,
                                                color: "rgba(255, 255, 255, 0.15)",
                                                zeroLineColor: "rgba(33, 37, 41, 0)",
                                                zeroLineBorderDash: [2],
                                                zeroLineBorderDashOffset: [2]
                                            }
                                        }]
                                    }
                                }
                            },
                            e = document.getElementById("line-chart").getContext("2d");
                        window.myLine = new Bt.a(e, t)
                    }))
                }
            },
            Mt = It,
            Jt = Object(o["a"])(Mt, Nt, zt, !1, null, null, null),
            Vt = Jt.exports,
            Ut = function() {
                var t = this,
                    e = t.$createElement;
                t._self._c;
                return t._m(0)
            },
            qt = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-4 py-3 bg-transparent"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "relative w-full max-w-full flex-grow flex-1"
                }, [a("h6", {
                    staticClass: "uppercase text-gray-500 mb-1 text-xs font-semibold"
                }, [t._v(" Performance ")]), a("h2", {
                    staticClass: "text-gray-800 text-xl font-semibold"
                }, [t._v(" Total orders ")])])])]), a("div", {
                    staticClass: "p-4 flex-auto"
                }, [a("div", {
                    staticClass: "relative h-350-px"
                }, [a("canvas", {
                    attrs: {
                        id: "bar-chart"
                    }
                })])])])
            }],
            Yt = {
                mounted: function() {
                    this.$nextTick((function() {
                        var t = {
                                type: "bar",
                                data: {
                                    labels: ["January", "February", "March", "April", "May", "June", "July"],
                                    datasets: [{
                                        label: (new Date).getFullYear(),
                                        backgroundColor: "#ed64a6",
                                        borderColor: "#ed64a6",
                                        data: [30, 78, 56, 34, 100, 45, 13],
                                        fill: !1,
                                        barThickness: 8
                                    }, {
                                        label: (new Date).getFullYear() - 1,
                                        fill: !1,
                                        backgroundColor: "#4c51bf",
                                        borderColor: "#4c51bf",
                                        data: [27, 68, 86, 74, 10, 4, 87],
                                        barThickness: 8
                                    }]
                                },
                                options: {
                                    maintainAspectRatio: !1,
                                    responsive: !0,
                                    title: {
                                        display: !1,
                                        text: "Orders Chart"
                                    },
                                    tooltips: {
                                        mode: "index",
                                        intersect: !1
                                    },
                                    hover: {
                                        mode: "nearest",
                                        intersect: !0
                                    },
                                    legend: {
                                        labels: {
                                            fontColor: "rgba(0,0,0,.4)"
                                        },
                                        align: "end",
                                        position: "bottom"
                                    },
                                    scales: {
                                        xAxes: [{
                                            display: !1,
                                            scaleLabel: {
                                                display: !0,
                                                labelString: "Month"
                                            },
                                            gridLines: {
                                                borderDash: [2],
                                                borderDashOffset: [2],
                                                color: "rgba(33, 37, 41, 0.3)",
                                                zeroLineColor: "rgba(33, 37, 41, 0.3)",
                                                zeroLineBorderDash: [2],
                                                zeroLineBorderDashOffset: [2]
                                            }
                                        }],
                                        yAxes: [{
                                            display: !0,
                                            scaleLabel: {
                                                display: !1,
                                                labelString: "Value"
                                            },
                                            gridLines: {
                                                borderDash: [2],
                                                drawBorder: !1,
                                                borderDashOffset: [2],
                                                color: "rgba(33, 37, 41, 0.2)",
                                                zeroLineColor: "rgba(33, 37, 41, 0.15)",
                                                zeroLineBorderDash: [2],
                                                zeroLineBorderDashOffset: [2]
                                            }
                                        }]
                                    }
                                }
                            },
                            e = document.getElementById("bar-chart").getContext("2d");
                        window.myBar = new Bt.a(e, t)
                    }))
                }
            },
            Wt = Yt,
            Gt = Object(o["a"])(Wt, Ut, qt, !1, null, null, null),
            Ht = Gt.exports,
            Kt = function() {
                var t = this,
                    e = t.$createElement;
                t._self._c;
                return t._m(0)
            },
            Zt = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-4 py-3 border-0"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "relative w-full px-4 max-w-full flex-grow flex-1"
                }, [a("h3", {
                    staticClass: "font-semibold text-base text-gray-800"
                }, [t._v(" Page visits ")])]), a("div", {
                    staticClass: "relative w-full px-4 max-w-full flex-grow flex-1 text-right"
                }, [a("button", {
                    staticClass: "bg-indigo-500 text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" See all ")])])])]), a("div", {
                    staticClass: "block w-full overflow-x-auto"
                }, [a("table", {
                    staticClass: "items-center w-full bg-transparent border-collapse"
                }, [a("thead", [a("tr", [a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Page name ")]), a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Visitors ")]), a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Unique users ")]), a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Bounce rate ")])])]), a("tbody", [a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" /argon/ ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 4,569 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 340 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-arrow-up text-green-500 mr-4"
                }), t._v(" 46,53% ")])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" /argon/index.html ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 3,985 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 319 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-arrow-down text-orange-500 mr-4"
                }), t._v(" 46,53% ")])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" /argon/charts.html ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 3,513 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 294 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-arrow-down text-orange-500 mr-4"
                }), t._v(" 36,49% ")])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" /argon/tables.html ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 2,050 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 147 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-arrow-up text-green-500 mr-4"
                }), t._v(" 50,87% ")])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" /argon/profile.html ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 1,795 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 190 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-arrow-down text-red-500 mr-4"
                }), t._v(" 46,53% ")])])])])])])
            }],
            Qt = {},
            Xt = Object(o["a"])(Qt, Kt, Zt, !1, null, null, null),
            te = Xt.exports,
            ee = function() {
                var t = this,
                    e = t.$createElement;
                t._self._c;
                return t._m(0)
            },
            ae = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-4 py-3 border-0"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "relative w-full px-4 max-w-full flex-grow flex-1"
                }, [a("h3", {
                    staticClass: "font-semibold text-base text-gray-800"
                }, [t._v(" Social traffic ")])]), a("div", {
                    staticClass: "relative w-full px-4 max-w-full flex-grow flex-1 text-right"
                }, [a("button", {
                    staticClass: "bg-indigo-500 text-white active:bg-indigo-600 text-xs font-bold uppercase px-3 py-1 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" See all ")])])])]), a("div", {
                    staticClass: "block w-full overflow-x-auto"
                }, [a("table", {
                    staticClass: "items-center w-full bg-transparent border-collapse"
                }, [a("thead", {
                    staticClass: "thead-light"
                }, [a("tr", [a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Referral ")]), a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left"
                }, [t._v(" Visitors ")]), a("th", {
                    staticClass: "px-6 bg-gray-100 text-gray-600 align-middle border border-solid border-gray-200 py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left min-w-140-px"
                })])]), a("tbody", [a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" Facebook ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 1,480 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("60%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-red-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-red-500",
                    staticStyle: {
                        width: "60%"
                    }
                })])])])])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" Facebook ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 5,480 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("70%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-green-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500",
                    staticStyle: {
                        width: "70%"
                    }
                })])])])])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" Google ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 4,807 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("80%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-purple-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-purple-500",
                    staticStyle: {
                        width: "80%"
                    }
                })])])])])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" Instagram ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 3,678 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("75%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-blue-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500",
                    staticStyle: {
                        width: "75%"
                    }
                })])])])])]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left"
                }, [t._v(" twitter ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" 2,645 ")]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("30%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-orange-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500",
                    staticStyle: {
                        width: "30%"
                    }
                })])])])])])])])])])
            }],
            se = {},
            le = Object(o["a"])(se, ee, ae, !1, null, null, null),
            re = le.exports,
            ie = {
                name: "dashboard-page",
                components: {
                    CardLineChart: Vt,
                    CardBarChart: Ht,
                    CardPageVisits: te,
                    CardSocialTraffic: re
                }
            },
            oe = ie,
            ne = Object(o["a"])(oe, Ft, Lt, !1, null, null, null),
            ce = ne.exports,
            de = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-8/12 px-4"
                }, [a("CardSettings")], 1), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("CardProfile")], 1)])
            },
            pe = [],
            fe = function() {
                var t = this,
                    e = t.$createElement;
                t._self._c;
                return t._m(0)
            },
            ue = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-200 border-0"
                }, [a("div", {
                    staticClass: "rounded-t bg-white mb-0 px-6 py-6"
                }, [a("div", {
                    staticClass: "text-center flex justify-between"
                }, [a("h6", {
                    staticClass: "text-gray-800 text-xl font-bold"
                }, [t._v("My account")]), a("button", {
                    staticClass: "bg-green-500 text-white active:bg-green-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" Settings ")])])]), a("div", {
                    staticClass: "flex-auto px-4 lg:px-10 py-10 pt-0"
                }, [a("form", [a("h6", {
                    staticClass: "text-gray-500 text-sm mt-3 mb-6 font-bold uppercase"
                }, [t._v(" User Information ")]), a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Username ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "lucky.jesse"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Email address ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        value: "jesse@example.com"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" First Name ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "Lucky"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Last Name ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "Jesse"
                    }
                })])])]), a("hr", {
                    staticClass: "mt-6 border-b-1 border-gray-400"
                }), a("h6", {
                    staticClass: "text-gray-500 text-sm mt-3 mb-6 font-bold uppercase"
                }, [t._v(" Contact Information ")]), a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-12/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Address ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" City ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        value: "New York"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Country ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "United States"
                    }
                })])]), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Postal Code ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        value: "Postal Code"
                    }
                })])])]), a("hr", {
                    staticClass: "mt-6 border-b-1 border-gray-400"
                }), a("h6", {
                    staticClass: "text-gray-500 text-sm mt-3 mb-6 font-bold uppercase"
                }, [t._v(" About Me ")]), a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-12/12 px-4"
                }, [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" About me ")]), a("textarea", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        rows: "4"
                    }
                }, [t._v(" A beautiful UI Kit and Admin for VueJS & Tailwind CSS. It is Free and Open Source. ")])])])])])])])
            }],
            xe = {},
            me = Object(o["a"])(xe, fe, ue, !1, null, null, null),
            be = me.exports,
            ge = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg mt-16"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center"
                }, [a("div", {
                    staticClass: "w-full px-4 flex justify-center"
                }, [a("div", {
                    staticClass: "relative"
                }, [a("img", {
                    staticClass: "shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px",
                    attrs: {
                        alt: "...",
                        src: t.team2
                    }
                })])]), t._m(0)]), t._m(1), t._m(2)])])
            },
            we = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full px-4 text-center mt-20"
                }, [a("div", {
                    staticClass: "flex justify-center py-4 lg:pt-4 pt-8"
                }, [a("div", {
                    staticClass: "mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 22 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Friends")])]), a("div", {
                    staticClass: "mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 10 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Photos")])]), a("div", {
                    staticClass: "lg:mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 89 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Comments")])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "text-center mt-12"
                }, [a("h3", {
                    staticClass: "text-xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
                }, [t._v(" Jenna Stones ")]), a("div", {
                    staticClass: "text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
                }, [a("i", {
                    staticClass: "fas fa-map-marker-alt mr-2 text-lg text-gray-500"
                }), t._v(" Los Angeles, California ")]), a("div", {
                    staticClass: "mb-2 text-gray-700 mt-10"
                }, [a("i", {
                    staticClass: "fas fa-briefcase mr-2 text-lg text-gray-500"
                }), t._v(" Solution Manager - Creative Tim Officer ")]), a("div", {
                    staticClass: "mb-2 text-gray-700"
                }, [a("i", {
                    staticClass: "fas fa-university mr-2 text-lg text-gray-500"
                }), t._v(" University of Computer Science ")])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "mt-10 py-10 border-t border-gray-300 text-center"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center"
                }, [a("div", {
                    staticClass: "w-full lg:w-9/12 px-4"
                }, [a("p", {
                    staticClass: "mb-4 text-lg leading-relaxed text-gray-800"
                }, [t._v(" An artist of considerable range, Jenna the name taken by Melbourne-raised, Brooklyn-based Nick Murphy writes, performs and records all of his own music, giving it a warm, intimate feel with a solid groove structure. An artist of considerable range. ")]), a("a", {
                    staticClass: "font-normal text-green-500",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Show more ")])])])])
            }],
            he = a("9b47"),
            ve = a.n(he),
            Ce = {
                data: function() {
                    return {
                        team2: ve.a
                    }
                }
            },
            ye = Ce,
            _e = Object(o["a"])(ye, ge, we, !1, null, null, null),
            ke = _e.exports,
            je = {
                components: {
                    CardSettings: be,
                    CardProfile: ke
                }
            },
            Se = je,
            Ee = Object(o["a"])(Se, de, pe, !1, null, null, null),
            $e = Ee.exports,
            De = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap mt-4"
                }, [a("div", {
                    staticClass: "w-full mb-12 px-4"
                }, [a("card-table")], 1), a("div", {
                    staticClass: "w-full mb-12 px-4"
                }, [a("card-table", {
                    attrs: {
                        color: "dark"
                    }
                })], 1)])
            },
            Oe = [],
            Pe = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded",
                    class: ["light" === t.color ? "bg-white" : "bg-green-900 text-white"]
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-4 py-3 border-0"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "relative w-full px-4 max-w-full flex-grow flex-1"
                }, [a("h3", {
                    staticClass: "font-semibold text-lg",
                    class: ["light" === t.color ? "text-gray-800" : "text-white"]
                }, [t._v(" Card Tables ")])])])]), a("div", {
                    staticClass: "block w-full overflow-x-auto"
                }, [a("table", {
                    staticClass: "items-center w-full bg-transparent border-collapse"
                }, [a("thead", [a("tr", [a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                }, [t._v(" Project ")]), a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                }, [t._v(" Budget ")]), a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                }, [t._v(" Status ")]), a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                }, [t._v(" Users ")]), a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                }, [t._v(" Completion ")]), a("th", {
                    staticClass: "px-6 align-middle border border-solid py-3 text-xs uppercase border-l-0 border-r-0 whitespace-no-wrap font-semibold text-left",
                    class: ["light" === t.color ? "bg-gray-100 text-gray-600 border-gray-200" : "bg-green-800 text-green-300 border-green-700"]
                })])]), a("tbody", [a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left flex items-center"
                }, [a("img", {
                    staticClass: "h-12 w-12 bg-white rounded-full border",
                    attrs: {
                        src: t.bootstrap,
                        alt: "..."
                    }
                }), a("span", {
                    staticClass: "ml-3 font-bold",
                    class: ["light" === t.color ? "text-gray-700" : "text-white"]
                }, [t._v(" Argon Design System ")])]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" $2,500 USD ")]), t._m(0), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex"
                }, [a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow",
                    attrs: {
                        src: t.team1,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team2,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team3,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team4,
                        alt: "..."
                    }
                })])]), t._m(1), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-right"
                }, [a("table-dropdown")], 1)]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left flex items-center"
                }, [a("img", {
                    staticClass: "h-12 w-12 bg-white rounded-full border",
                    attrs: {
                        src: t.angular,
                        alt: "..."
                    }
                }), a("span", {
                    staticClass: "ml-3 font-bold",
                    class: ["light" === t.color ? "text-gray-700" : "text-white"]
                }, [t._v(" Angular Now UI Kit PRO ")])]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" $1,800 USD ")]), t._m(2), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex"
                }, [a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow",
                    attrs: {
                        src: t.team1,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team2,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team3,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team4,
                        alt: "..."
                    }
                })])]), t._m(3), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-right"
                }, [a("table-dropdown")], 1)]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left flex items-center"
                }, [a("img", {
                    staticClass: "h-12 w-12 bg-white rounded-full border",
                    attrs: {
                        src: t.sketch,
                        alt: "..."
                    }
                }), a("span", {
                    staticClass: "ml-3 font-bold",
                    class: ["light" === t.color ? "text-gray-700" : "text-white"]
                }, [t._v(" Black Dashboard Sketch ")])]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" $3,150 USD ")]), t._m(4), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex"
                }, [a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow",
                    attrs: {
                        src: t.team1,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team2,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team3,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team4,
                        alt: "..."
                    }
                })])]), t._m(5), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-right"
                }, [a("table-dropdown")], 1)]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left flex items-center"
                }, [a("img", {
                    staticClass: "h-12 w-12 bg-white rounded-full border",
                    attrs: {
                        src: t.react,
                        alt: "..."
                    }
                }), a("span", {
                    staticClass: "ml-3 font-bold",
                    class: ["light" === t.color ? "text-gray-700" : "text-white"]
                }, [t._v(" React Material Dashboard ")])]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" $4,400 USD ")]), t._m(6), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex"
                }, [a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow",
                    attrs: {
                        src: t.team1,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team2,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team3,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team4,
                        alt: "..."
                    }
                })])]), t._m(7), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-right"
                }, [a("table-dropdown")], 1)]), a("tr", [a("th", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-left flex items-center"
                }, [a("img", {
                    staticClass: "h-12 w-12 bg-white rounded-full border",
                    attrs: {
                        src: t.vue,
                        alt: "..."
                    }
                }), a("span", {
                    staticClass: "ml-3 font-bold",
                    class: ["light" === t.color ? "text-gray-700" : "text-white"]
                }, [t._v(" React Material Dashboard ")])]), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [t._v(" $2,200 USD ")]), t._m(8), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex"
                }, [a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow",
                    attrs: {
                        src: t.team1,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team2,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team3,
                        alt: "..."
                    }
                }), a("img", {
                    staticClass: "w-10 h-10 rounded-full border-2 border-gray-100 shadow -ml-4",
                    attrs: {
                        src: t.team4,
                        alt: "..."
                    }
                })])]), t._m(9), a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4 text-right"
                }, [a("table-dropdown")], 1)])])])])])
            },
            Ae = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-circle text-orange-500 mr-2"
                }), t._v(" pending ")])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("60%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-red-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-red-500",
                    staticStyle: {
                        width: "60%"
                    }
                })])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-circle text-green-500 mr-2"
                }), t._v(" completed ")])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("100%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-green-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500",
                    staticStyle: {
                        width: "100%"
                    }
                })])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-circle text-red-500 mr-2"
                }), t._v(" delayed ")])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("73%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-red-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-red-500",
                    staticStyle: {
                        width: "73%"
                    }
                })])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-circle text-teal-500 mr-2"
                }), t._v(" on schedule ")])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("90%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-teal-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-teal-500",
                    staticStyle: {
                        width: "90%"
                    }
                })])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("i", {
                    staticClass: "fas fa-circle text-green-500 mr-2"
                }), t._v(" completed ")])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("td", {
                    staticClass: "border-t-0 px-6 align-middle border-l-0 border-r-0 text-xs whitespace-no-wrap p-4"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("span", {
                    staticClass: "mr-2"
                }, [t._v("100%")]), a("div", {
                    staticClass: "relative w-full"
                }, [a("div", {
                    staticClass: "overflow-hidden h-2 text-xs flex rounded bg-green-200"
                }, [a("div", {
                    staticClass: "shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500",
                    staticStyle: {
                        width: "100%"
                    }
                })])])])])
            }],
            Te = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("a", {
                    ref: "btnDropdownRef",
                    staticClass: "text-gray-600 py-1 px-3",
                    attrs: {
                        href: "#pablo"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleDropdown(e)
                        }
                    }
                }, [a("i", {
                    staticClass: "fas fa-ellipsis-v"
                })]), a("div", {
                    ref: "popoverDropdownRef",
                    staticClass: "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",
                    class: {
                        hidden: !t.dropdownPopoverShow, block: t.dropdownPopoverShow
                    }
                }, [a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Another action ")]), a("a", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        href: "javascript:void(0);"
                    }
                }, [t._v(" Something else here ")])])])
            },
            Fe = [],
            Le = {
                data: function() {
                    return {
                        dropdownPopoverShow: !1
                    }
                },
                methods: {
                    toggleDropdown: function(t) {
                        t.preventDefault(), this.dropdownPopoverShow ? this.dropdownPopoverShow = !1 : (this.dropdownPopoverShow = !0, Object(g["a"])(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
                            placement: "bottom-start"
                        }))
                    }
                }
            },
            Ne = Le,
            ze = Object(o["a"])(Ne, Te, Fe, !1, null, null, null),
            Re = ze.exports,
            Be = a("f61f"),
            Ie = a.n(Be),
            Me = a("1454"),
            Je = a.n(Me),
            Ve = a("c1c9"),
            Ue = a.n(Ve),
            qe = a("8cac"),
            Ye = a.n(qe),
            We = a("9cda"),
            Ge = a.n(We),
            He = a("8d31"),
            Ke = a.n(He),
            Ze = {
                data: function() {
                    return {
                        bootstrap: Ie.a,
                        angular: Je.a,
                        sketch: Ue.a,
                        react: Ye.a,
                        vue: Ye.a,
                        team1: h.a,
                        team2: ve.a,
                        team3: Ge.a,
                        team4: Ke.a
                    }
                },
                components: {
                    TableDropdown: Re
                },
                props: {
                    color: {
                        default: "light",
                        validator: function(t) {
                            return -1 !== ["light", "dark"].indexOf(t)
                        }
                    }
                }
            },
            Qe = Ze,
            Xe = Object(o["a"])(Qe, Pe, Ae, !1, null, null, null),
            ta = Xe.exports,
            ea = {
                components: {
                    CardTable: ta
                }
            },
            aa = ea,
            sa = Object(o["a"])(aa, De, Oe, !1, null, null, null),
            la = sa.exports,
            ra = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
                }, [a("map-example")], 1)])])
            },
            ia = [],
            oa = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "relative w-full rounded h-600-px",
                    attrs: {
                        id: "map-canvas",
                        "data-lat": "40.748817",
                        "data-lng": "-73.985428"
                    }
                })
            },
            na = [],
            ca = {
                mounted: function() {
                    var t = window.google,
                        e = document.getElementById("map-canvas"),
                        a = e.getAttribute("data-lat"),
                        s = e.getAttribute("data-lng"),
                        l = new t.maps.LatLng(a, s),
                        r = {
                            zoom: 12,
                            scrollwheel: !1,
                            center: l,
                            mapTypeId: t.maps.MapTypeId.ROADMAP,
                            styles: [{
                                featureType: "administrative",
                                elementType: "labels.text.fill",
                                stylers: [{
                                    color: "#444444"
                                }]
                            }, {
                                featureType: "landscape",
                                elementType: "all",
                                stylers: [{
                                    color: "#f2f2f2"
                                }]
                            }, {
                                featureType: "poi",
                                elementType: "all",
                                stylers: [{
                                    visibility: "off"
                                }]
                            }, {
                                featureType: "road",
                                elementType: "all",
                                stylers: [{
                                    saturation: -100
                                }, {
                                    lightness: 45
                                }]
                            }, {
                                featureType: "road.highway",
                                elementType: "all",
                                stylers: [{
                                    visibility: "simplified"
                                }]
                            }, {
                                featureType: "road.arterial",
                                elementType: "labels.icon",
                                stylers: [{
                                    visibility: "off"
                                }]
                            }, {
                                featureType: "transit",
                                elementType: "all",
                                stylers: [{
                                    visibility: "off"
                                }]
                            }, {
                                featureType: "water",
                                elementType: "all",
                                stylers: [{
                                    color: "#5e72e4"
                                }, {
                                    visibility: "on"
                                }]
                            }]
                        };
                    e = new t.maps.Map(e, r);
                    var i = new t.maps.Marker({
                            position: l,
                            map: e,
                            animation: t.maps.Animation.DROP,
                            title: "Hello World!"
                        }),
                        o = '<div class="info-window-content"><h2>Vue Notus</h2><p>A beautiful UI Kit and Admin for Tailwind CSS. It is Free and Open Source.</p></div>',
                        n = new t.maps.InfoWindow({
                            content: o
                        });
                    t.maps.event.addListener(i, "click", (function() {
                        n.open(e, i)
                    }))
                }
            },
            da = ca,
            pa = Object(o["a"])(da, oa, na, !1, null, null, null),
            fa = pa.exports,
            ua = {
                components: {
                    MapExample: fa
                }
            },
            xa = ua,
            ma = Object(o["a"])(xa, ra, ia, !1, null, null, null),
            ba = ma.exports,
            ga = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto px-4 h-full"
                }, [a("div", {
                    staticClass: "flex content-center items-center justify-center h-full"
                }, [a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-6 py-6"
                }, [t._m(0), a("div", {
                    staticClass: "btn-wrapper text-center"
                }, [a("button", {
                    staticClass: "bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-2 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("img", {
                    staticClass: "w-5 mr-1",
                    attrs: {
                        alt: "...",
                        src: t.github
                    }
                }), t._v(" Github ")]), a("button", {
                    staticClass: "bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("img", {
                    staticClass: "w-5 mr-1",
                    attrs: {
                        alt: "...",
                        src: t.google
                    }
                }), t._v(" Google ")])]), a("hr", {
                    staticClass: "mt-6 border-b-1 border-gray-400"
                })]), t._m(1)]), a("div", {
                    staticClass: "flex flex-wrap mt-6 relative"
                }, [t._m(2), a("div", {
                    staticClass: "w-1/2 text-right"
                }, [a("router-link", {
                    staticClass: "text-gray-300",
                    attrs: {
                        to: "/auth/register"
                    }
                }, [a("small", [t._v("Create new account")])])], 1)])])])])
            },
            wa = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "text-center mb-3"
                }, [a("h6", {
                    staticClass: "text-gray-600 text-sm font-bold"
                }, [t._v(" Sign in with ")])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex-auto px-4 lg:px-10 py-10 pt-0"
                }, [a("div", {
                    staticClass: "text-gray-500 text-center mb-3 font-bold"
                }, [a("small", [t._v("Or sign in with credentials")])]), a("form", [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Email ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        placeholder: "Email"
                    }
                })]), a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Password ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "password",
                        placeholder: "Password"
                    }
                })]), a("div", [a("label", {
                    staticClass: "inline-flex items-center cursor-pointer"
                }, [a("input", {
                    staticClass: "form-checkbox text-gray-800 ml-1 w-5 h-5 ease-linear transition-all duration-150",
                    attrs: {
                        id: "customCheckLogin",
                        type: "checkbox"
                    }
                }), a("span", {
                    staticClass: "ml-2 text-sm font-semibold text-gray-700"
                }, [t._v(" Remember me ")])])]), a("div", {
                    staticClass: "text-center mt-6"
                }, [a("button", {
                    staticClass: "bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" Sign In ")])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-1/2"
                }, [a("a", {
                    staticClass: "text-gray-300",
                    attrs: {
                        href: "javascript:void(0)"
                    }
                }, [a("small", [t._v("Forgot password?")])])])
            }],
            ha = a("6bff"),
            va = a.n(ha),
            Ca = a("ccc8"),
            ya = a.n(Ca),
            _a = {
                data: function() {
                    return {
                        github: va.a,
                        google: ya.a
                    }
                }
            },
            ka = _a,
            ja = Object(o["a"])(ka, ga, wa, !1, null, null, null),
            Sa = ja.exports,
            Ea = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto px-4 h-full"
                }, [a("div", {
                    staticClass: "flex content-center items-center justify-center h-full"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0"
                }, [a("div", {
                    staticClass: "rounded-t mb-0 px-6 py-6"
                }, [t._m(0), a("div", {
                    staticClass: "btn-wrapper text-center"
                }, [a("button", {
                    staticClass: "bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-2 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("img", {
                    staticClass: "w-5 mr-1",
                    attrs: {
                        alt: "...",
                        src: t.github
                    }
                }), t._v(" Github ")]), a("button", {
                    staticClass: "bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("img", {
                    staticClass: "w-5 mr-1",
                    attrs: {
                        alt: "...",
                        src: t.google
                    }
                }), t._v(" Google ")])]), a("hr", {
                    staticClass: "mt-6 border-b-1 border-gray-400"
                })]), t._m(1)])])])])
            },
            $a = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "text-center mb-3"
                }, [a("h6", {
                    staticClass: "text-gray-600 text-sm font-bold"
                }, [t._v(" Sign up with ")])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex-auto px-4 lg:px-10 py-10 pt-0"
                }, [a("div", {
                    staticClass: "text-gray-500 text-center mb-3 font-bold"
                }, [a("small", [t._v("Or sign up with credentials")])]), a("form", [a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Name ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        placeholder: "Name"
                    }
                })]), a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Email ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        placeholder: "Email"
                    }
                })]), a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "grid-password"
                    }
                }, [t._v(" Password ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "password",
                        placeholder: "Password"
                    }
                })]), a("div", [a("label", {
                    staticClass: "inline-flex items-center cursor-pointer"
                }, [a("input", {
                    staticClass: "form-checkbox text-gray-800 ml-1 w-5 h-5 ease-linear transition-all duration-150",
                    attrs: {
                        id: "customCheckLogin",
                        type: "checkbox"
                    }
                }), a("span", {
                    staticClass: "ml-2 text-sm font-semibold text-gray-700"
                }, [t._v(" I agree with the "), a("a", {
                    staticClass: "text-green-500",
                    attrs: {
                        href: "javascript:void(0)"
                    }
                }, [t._v(" Privacy Policy ")])])])]), a("div", {
                    staticClass: "text-center mt-6"
                }, [a("button", {
                    staticClass: "bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" Create Account ")])])])])
            }],
            Da = {
                data: function() {
                    return {
                        github: va.a,
                        google: ya.a
                    }
                }
            },
            Oa = Da,
            Pa = Object(o["a"])(Oa, Ea, $a, !1, null, null, null),
            Aa = Pa.exports,
            Ta = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("navbar"), a("main", [a("div", {
                    staticClass: "relative pt-16 pb-32 flex content-center items-center justify-center min-h-screen-75"
                }, [t._m(0), t._m(1), a("div", {
                    staticClass: "top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-300 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])])]), a("section", {
                    staticClass: "pb-20 bg-gray-300 -mt-24"
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [t._m(2), a("div", {
                    staticClass: "flex flex-wrap items-center mt-32"
                }, [a("div", {
                    staticClass: "w-full md:w-5/12 px-4 mr-auto ml-auto"
                }, [t._m(3), a("h3", {
                    staticClass: "text-3xl mb-2 font-semibold leading-normal"
                }, [t._v(" Working with us is a pleasure ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-4 mb-4 text-gray-700"
                }, [t._v(" Don't let your uses guess by attaching tooltips and popoves to any element. Just make sure you enable them first via JavaScript. ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-0 mb-4 text-gray-700"
                }, [t._v(" The kit comes with three pre-built pages to help you get started faster. You can change the text and images and you're good to go. Just make sure you enable them first via JavaScript. ")]), a("router-link", {
                    staticClass: "font-bold text-gray-800 mt-8",
                    attrs: {
                        to: "/"
                    }
                }, [t._v(" Check Vue Notus! ")])], 1), a("div", {
                    staticClass: "w-full md:w-4/12 px-4 mr-auto ml-auto"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg bg-green-600"
                }, [a("img", {
                    staticClass: "w-full align-middle rounded-t-lg",
                    attrs: {
                        alt: "...",
                        src: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1051&q=80"
                    }
                }), a("blockquote", {
                    staticClass: "relative p-8 mb-4"
                }, [a("svg", {
                    staticClass: "absolute left-0 w-full block h-95-px -top-94-px",
                    attrs: {
                        preserveAspectRatio: "none",
                        xmlns: "http://www.w3.org/2000/svg",
                        viewBox: "0 0 583 95"
                    }
                }, [a("polygon", {
                    staticClass: "text-green-600 fill-current",
                    attrs: {
                        points: "-30,95 583,95 583,65"
                    }
                })]), a("h4", {
                    staticClass: "text-xl font-bold text-white"
                }, [t._v(" Top Notch Services ")]), a("p", {
                    staticClass: "text-md font-light mt-2 text-white"
                }, [t._v(" The Arctic Ocean freezes every winter and much of the sea-ice then thaws every summer, and that process will continue whatever happens. ")])])])])])])]), a("section", {
                    staticClass: "relative py-20"
                }, [a("div", {
                    staticClass: "bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-white fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])]), t._m(4)]), a("section", {
                    staticClass: "pt-20 pb-48"
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [t._m(5), a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("img", {
                    staticClass: "shadow-lg rounded-full mx-auto max-w-120-px",
                    attrs: {
                        alt: "...",
                        src: t.team1
                    }
                }), t._m(6)])]), a("div", {
                    staticClass: "w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("img", {
                    staticClass: "shadow-lg rounded-full mx-auto max-w-120-px",
                    attrs: {
                        alt: "...",
                        src: t.team2
                    }
                }), t._m(7)])]), a("div", {
                    staticClass: "w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("img", {
                    staticClass: "shadow-lg rounded-full mx-auto max-w-120-px",
                    attrs: {
                        alt: "...",
                        src: t.team3
                    }
                }), t._m(8)])]), a("div", {
                    staticClass: "w-full md:w-6/12 lg:w-3/12 lg:mb-0 mb-12 px-4"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("img", {
                    staticClass: "shadow-lg rounded-full mx-auto max-w-120-px",
                    attrs: {
                        alt: "...",
                        src: t.team4
                    }
                }), t._m(9)])])])])]), a("section", {
                    staticClass: "pb-20 relative block bg-gray-900"
                }, [a("div", {
                    staticClass: "bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-900 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])]), t._m(10)]), t._m(11)]), a("footer-component")], 1)
            },
            Fa = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "absolute top-0 w-full h-full bg-center bg-cover",
                    staticStyle: {
                        "background-image": "url('https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80')"
                    }
                }, [a("span", {
                    staticClass: "w-full h-full absolute opacity-75 bg-black",
                    attrs: {
                        id: "blackOverlay"
                    }
                })])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container relative mx-auto"
                }, [a("div", {
                    staticClass: "items-center flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4 ml-auto mr-auto text-center"
                }, [a("div", {
                    staticClass: "pr-12"
                }, [a("h1", {
                    staticClass: "text-white font-semibold text-5xl"
                }, [t._v(" Your story starts with us. ")]), a("p", {
                    staticClass: "mt-4 text-lg text-gray-300"
                }, [t._v(" This is a simple example of a Landing Page you can build using Vue Notus. It features multiple CSS components based on the Tailwind CSS design system. ")])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "lg:pt-12 pt-6 w-full md:w-4/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-red-400"
                }, [a("i", {
                    staticClass: "fas fa-award"
                })]), a("h6", {
                    staticClass: "text-xl font-semibold"
                }, [t._v("Awarded Agency")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-600"
                }, [t._v(" Divide details about your product or agency work into parts. A paragraph describing a feature will be enough. ")])])])]), a("div", {
                    staticClass: "w-full md:w-4/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-blue-400"
                }, [a("i", {
                    staticClass: "fas fa-retweet"
                })]), a("h6", {
                    staticClass: "text-xl font-semibold"
                }, [t._v("Free Revisions")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-600"
                }, [t._v(" Keep you user engaged by providing meaningful information. Remember that by this time, the user is curious. ")])])])]), a("div", {
                    staticClass: "pt-6 w-full md:w-4/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-green-400"
                }, [a("i", {
                    staticClass: "fas fa-fingerprint"
                })]), a("h6", {
                    staticClass: "text-xl font-semibold"
                }, [t._v("Verified Company")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-600"
                }, [t._v(" Write a few lines about each one. A paragraph describing a feature will be enough. Keep you user engaged! ")])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-gray-100"
                }, [a("i", {
                    staticClass: "fas fa-user-friends text-xl"
                })])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto px-4"
                }, [a("div", {
                    staticClass: "items-center flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full md:w-4/12 ml-auto mr-auto px-4"
                }, [a("img", {
                    staticClass: "max-w-full rounded-lg shadow-lg",
                    attrs: {
                        alt: "...",
                        src: "https://images.unsplash.com/photo-1555212697-194d092e3b8f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"
                    }
                })]), a("div", {
                    staticClass: "w-full md:w-5/12 ml-auto mr-auto px-4"
                }, [a("div", {
                    staticClass: "md:pr-12"
                }, [a("div", {
                    staticClass: "text-green-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-green-300"
                }, [a("i", {
                    staticClass: "fas fa-rocket text-xl"
                })]), a("h3", {
                    staticClass: "text-3xl font-semibold"
                }, [t._v("A growing company")]), a("p", {
                    staticClass: "mt-4 text-lg leading-relaxed text-gray-600"
                }, [t._v(" The extension comes with three pre-built pages to help you get started faster. You can change the text and images and you're good to go. ")]), a("ul", {
                    staticClass: "list-none mt-6"
                }, [a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-green-600 bg-green-200 mr-3"
                }, [a("i", {
                    staticClass: "fas fa-fingerprint"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v(" Carefully crafted components ")])])])]), a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-green-600 bg-green-200 mr-3"
                }, [a("i", {
                    staticClass: "fab fa-html5"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v(" Amazing page examples ")])])])]), a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-green-600 bg-green-200 mr-3"
                }, [a("i", {
                    staticClass: "far fa-paper-plane"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v("Dynamic components")])])])])])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap justify-center text-center mb-24"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("h2", {
                    staticClass: "text-4xl font-semibold"
                }, [t._v("Here are our heroes")]), a("p", {
                    staticClass: "text-lg leading-relaxed m-4 text-gray-600"
                }, [t._v(" According to the National Oceanic and Atmospheric Administration, Ted, Scambos, NSIDClead scentist, puts the potentially record maximum. ")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "pt-6 text-center"
                }, [a("h5", {
                    staticClass: "text-xl font-bold"
                }, [t._v("Ryan Tompson")]), a("p", {
                    staticClass: "mt-1 text-sm text-gray-500 uppercase font-semibold"
                }, [t._v(" Web Developer ")]), a("div", {
                    staticClass: "mt-6"
                }, [a("button", {
                    staticClass: "bg-blue-400 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-twitter"
                })]), a("button", {
                    staticClass: "bg-blue-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-facebook-f"
                })]), a("button", {
                    staticClass: "bg-pink-500 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-dribbble"
                })])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "pt-6 text-center"
                }, [a("h5", {
                    staticClass: "text-xl font-bold"
                }, [t._v("Romina Hadid")]), a("p", {
                    staticClass: "mt-1 text-sm text-gray-500 uppercase font-semibold"
                }, [t._v(" Marketing Specialist ")]), a("div", {
                    staticClass: "mt-6"
                }, [a("button", {
                    staticClass: "bg-red-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-google"
                })]), a("button", {
                    staticClass: "bg-blue-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-facebook-f"
                })])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "pt-6 text-center"
                }, [a("h5", {
                    staticClass: "text-xl font-bold"
                }, [t._v("Alexa Smith")]), a("p", {
                    staticClass: "mt-1 text-sm text-gray-500 uppercase font-semibold"
                }, [t._v(" UI/UX Designer ")]), a("div", {
                    staticClass: "mt-6"
                }, [a("button", {
                    staticClass: "bg-red-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-google"
                })]), a("button", {
                    staticClass: "bg-blue-400 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-twitter"
                })]), a("button", {
                    staticClass: "bg-gray-800 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-instagram"
                })])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "pt-6 text-center"
                }, [a("h5", {
                    staticClass: "text-xl font-bold"
                }, [t._v("Jenna Kardi")]), a("p", {
                    staticClass: "mt-1 text-sm text-gray-500 uppercase font-semibold"
                }, [t._v(" Founder and CEO ")]), a("div", {
                    staticClass: "mt-6"
                }, [a("button", {
                    staticClass: "bg-pink-500 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-dribbble"
                })]), a("button", {
                    staticClass: "bg-red-600 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-google"
                })]), a("button", {
                    staticClass: "bg-blue-400 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-twitter"
                })]), a("button", {
                    staticClass: "bg-gray-800 text-white w-8 h-8 rounded-full outline-none focus:outline-none mr-1 mb-1",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-instagram"
                })])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto px-4 lg:pt-24 lg:pb-64"
                }, [a("div", {
                    staticClass: "flex flex-wrap text-center justify-center"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("h2", {
                    staticClass: "text-4xl font-semibold text-white"
                }, [t._v(" Build something ")]), a("p", {
                    staticClass: "text-lg leading-relaxed mt-4 mb-4 text-gray-500"
                }, [t._v(" Put the potentially record low maximum sea ice extent tihs year down to low ice. According to the National Oceanic and Atmospheric Administration, Ted, Scambos. ")])])]), a("div", {
                    staticClass: "flex flex-wrap mt-12 justify-center"
                }, [a("div", {
                    staticClass: "w-full lg:w-3/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "text-gray-900 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
                }, [a("i", {
                    staticClass: "fas fa-medal text-xl"
                })]), a("h6", {
                    staticClass: "text-xl mt-5 font-semibold text-white"
                }, [t._v(" Excelent Services ")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-500"
                }, [t._v(" Some quick example text to build on the card title and make up the bulk of the card's content. ")])]), a("div", {
                    staticClass: "w-full lg:w-3/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "text-gray-900 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
                }, [a("i", {
                    staticClass: "fas fa-poll text-xl"
                })]), a("h5", {
                    staticClass: "text-xl mt-5 font-semibold text-white"
                }, [t._v(" Grow your market ")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-500"
                }, [t._v(" Some quick example text to build on the card title and make up the bulk of the card's content. ")])]), a("div", {
                    staticClass: "w-full lg:w-3/12 px-4 text-center"
                }, [a("div", {
                    staticClass: "text-gray-900 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
                }, [a("i", {
                    staticClass: "fas fa-lightbulb text-xl"
                })]), a("h5", {
                    staticClass: "text-xl mt-5 font-semibold text-white"
                }, [t._v(" Launch time ")]), a("p", {
                    staticClass: "mt-2 mb-4 text-gray-500"
                }, [t._v(" Some quick example text to build on the card title and make up the bulk of the card's content. ")])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("section", {
                    staticClass: "relative block py-24 lg:pt-0 bg-gray-900"
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center lg:-mt-64 -mt-48"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300"
                }, [a("div", {
                    staticClass: "flex-auto p-5 lg:p-10"
                }, [a("h4", {
                    staticClass: "text-2xl font-semibold"
                }, [t._v(" Want to work with us? ")]), a("p", {
                    staticClass: "leading-relaxed mt-1 mb-4 text-gray-600"
                }, [t._v(" Complete this form and we will get back to you in 24 hours. ")]), a("div", {
                    staticClass: "relative w-full mb-3 mt-8"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "full-name"
                    }
                }, [t._v(" Full Name ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "text",
                        placeholder: "Full Name"
                    }
                })]), a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "email"
                    }
                }, [t._v(" Email ")]), a("input", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full ease-linear transition-all duration-150",
                    attrs: {
                        type: "email",
                        placeholder: "Email"
                    }
                })]), a("div", {
                    staticClass: "relative w-full mb-3"
                }, [a("label", {
                    staticClass: "block uppercase text-gray-700 text-xs font-bold mb-2",
                    attrs: {
                        htmlFor: "message"
                    }
                }, [t._v(" Message ")]), a("textarea", {
                    staticClass: "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full",
                    attrs: {
                        rows: "4",
                        cols: "80",
                        placeholder: "Type a message..."
                    }
                })]), a("div", {
                    staticClass: "text-center mt-6"
                }, [a("button", {
                    staticClass: "bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" Send Message ")])])])])])])])])
            }],
            La = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("footer", {
                    staticClass: "relative bg-gray-300 pt-8 pb-6"
                }, [a("div", {
                    staticClass: "bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-300 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])]), a("div", {
                    staticClass: "container mx-auto px-4"
                }, [t._m(0), a("hr", {
                    staticClass: "my-6 border-gray-400"
                }), a("div", {
                    staticClass: "flex flex-wrap items-center md:justify-between justify-center"
                }, [a("div", {
                    staticClass: "w-full md:w-4/12 px-4 mx-auto text-center"
                }, [a("div", {
                    staticClass: "text-sm text-gray-600 font-semibold py-1"
                }, [t._v(" Copyright © " + t._s(t.date) + " Vue Notus by "), a("a", {
                    staticClass: "text-gray-600 hover:text-gray-900",
                    attrs: {
                        href: "https://www.creative-tim.com?ref=vn-footer"
                    }
                }, [t._v(" Creative Tim ")]), t._v(" . ")])])])])])
            },
            Na = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap text-center lg:text-left"
                }, [a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("h4", {
                    staticClass: "text-3xl font-semibold"
                }, [t._v("Let's keep in touch!")]), a("h5", {
                    staticClass: "text-lg mt-0 mb-2 text-gray-700"
                }, [t._v(" Find us on any of these platforms, we respond 1-2 business days. ")]), a("div", {
                    staticClass: "mt-6 lg:mb-0 mb-6"
                }, [a("button", {
                    staticClass: "bg-white text-blue-400 shadow-lg font-normal h-10 w-10 items-center justify-center align-center rounded-full outline-none focus:outline-none mr-2",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-twitter"
                })]), a("button", {
                    staticClass: "bg-white text-blue-600 shadow-lg font-normal h-10 w-10 items-center justify-center align-center rounded-full outline-none focus:outline-none mr-2",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-facebook-square"
                })]), a("button", {
                    staticClass: "bg-white text-pink-400 shadow-lg font-normal h-10 w-10 items-center justify-center align-center rounded-full outline-none focus:outline-none mr-2",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-dribbble"
                })]), a("button", {
                    staticClass: "bg-white text-gray-900 shadow-lg font-normal h-10 w-10 items-center justify-center align-center rounded-full outline-none focus:outline-none mr-2",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fab fa-github"
                })])])]), a("div", {
                    staticClass: "w-full lg:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-top mb-6"
                }, [a("div", {
                    staticClass: "w-full lg:w-4/12 px-4 ml-auto"
                }, [a("span", {
                    staticClass: "block uppercase text-gray-600 text-sm font-semibold mb-2"
                }, [t._v(" Useful Links ")]), a("ul", {
                    staticClass: "list-unstyled"
                }, [a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://www.creative-tim.com/presentation?ref=vn-footer"
                    }
                }, [t._v(" About Us ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://blog.creative-tim.com?ref=vn-footer"
                    }
                }, [t._v(" Blog ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://www.github.com/creativetimofficial?ref=vn-footer"
                    }
                }, [t._v(" Github ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://www.creative-tim.com/bootstrap-themes/free?ref=vn-footer"
                    }
                }, [t._v(" Free Products ")])])])]), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("span", {
                    staticClass: "block uppercase text-gray-600 text-sm font-semibold mb-2"
                }, [t._v(" Other Resources ")]), a("ul", {
                    staticClass: "list-unstyled"
                }, [a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus/blob/master/LICENSE.md?ref=vn-footer"
                    }
                }, [t._v(" MIT License ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://creative-tim.com/terms?ref=vn-footer"
                    }
                }, [t._v(" Terms & Conditions ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://creative-tim.com/privacy?ref=vn-footer"
                    }
                }, [t._v(" Privacy Policy ")])]), a("li", [a("a", {
                    staticClass: "text-gray-700 hover:text-gray-900 font-semibold block pb-2 text-sm",
                    attrs: {
                        href: "https://creative-tim.com/contact-us?ref=vn-footer"
                    }
                }, [t._v(" Contact Us ")])])])])])])])
            }],
            za = {
                data: function() {
                    return {
                        date: (new Date).getFullYear()
                    }
                }
            },
            Ra = za,
            Ba = Object(o["a"])(Ra, La, Na, !1, null, null, null),
            Ia = Ba.exports,
            Ma = {
                data: function() {
                    return {
                        team1: h.a,
                        team2: ve.a,
                        team3: Ge.a,
                        team4: Ke.a
                    }
                },
                components: {
                    Navbar: Ct,
                    FooterComponent: Ia
                }
            },
            Ja = Ma,
            Va = Object(o["a"])(Ja, Ta, Fa, !1, null, null, null),
            Ua = Va.exports,
            qa = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("navbar"), a("main", {
                    staticClass: "profile-page"
                }, [a("section", {
                    staticClass: "relative block h-500-px"
                }, [t._m(0), a("div", {
                    staticClass: "top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-300 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])])]), a("section", {
                    staticClass: "relative py-16 bg-gray-300"
                }, [a("div", {
                    staticClass: "container mx-auto px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"
                }, [a("div", {
                    staticClass: "px-6"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center"
                }, [a("div", {
                    staticClass: "w-full lg:w-3/12 px-4 lg:order-2 flex justify-center"
                }, [a("div", {
                    staticClass: "relative"
                }, [a("img", {
                    staticClass: "shadow-xl rounded-full h-auto align-middle border-none absolute -m-16 -ml-20 lg:-ml-16 max-w-150-px",
                    attrs: {
                        alt: "...",
                        src: t.team2
                    }
                })])]), t._m(1), t._m(2)]), t._m(3), t._m(4)])])])])]), a("footer-component")], 1)
            },
            Ya = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "absolute top-0 w-full h-full bg-center bg-cover",
                    staticStyle: {
                        "background-image": "url('https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2710&q=80')"
                    }
                }, [a("span", {
                    staticClass: "w-full h-full absolute opacity-50 bg-black",
                    attrs: {
                        id: "blackOverlay"
                    }
                })])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full lg:w-4/12 px-4 lg:order-3 lg:text-right lg:self-center"
                }, [a("div", {
                    staticClass: "py-6 px-3 mt-32 sm:mt-0"
                }, [a("button", {
                    staticClass: "bg-green-500 active:bg-green-600 uppercase text-white font-bold hover:shadow-md shadow text-xs px-4 py-2 rounded outline-none focus:outline-none sm:mr-2 mb-1 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [t._v(" Connect ")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full lg:w-4/12 px-4 lg:order-1"
                }, [a("div", {
                    staticClass: "flex justify-center py-4 lg:pt-4 pt-8"
                }, [a("div", {
                    staticClass: "mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 22 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Friends")])]), a("div", {
                    staticClass: "mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 10 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Photos")])]), a("div", {
                    staticClass: "lg:mr-4 p-3 text-center"
                }, [a("span", {
                    staticClass: "text-xl font-bold block uppercase tracking-wide text-gray-700"
                }, [t._v(" 89 ")]), a("span", {
                    staticClass: "text-sm text-gray-500"
                }, [t._v("Comments")])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "text-center mt-12"
                }, [a("h3", {
                    staticClass: "text-4xl font-semibold leading-normal mb-2 text-gray-800 mb-2"
                }, [t._v(" Jenna Stones ")]), a("div", {
                    staticClass: "text-sm leading-normal mt-0 mb-2 text-gray-500 font-bold uppercase"
                }, [a("i", {
                    staticClass: "fas fa-map-marker-alt mr-2 text-lg text-gray-500"
                }), t._v(" Los Angeles, California ")]), a("div", {
                    staticClass: "mb-2 text-gray-700 mt-10"
                }, [a("i", {
                    staticClass: "fas fa-briefcase mr-2 text-lg text-gray-500"
                }), t._v(" Solution Manager - Creative Tim Officer ")]), a("div", {
                    staticClass: "mb-2 text-gray-700"
                }, [a("i", {
                    staticClass: "fas fa-university mr-2 text-lg text-gray-500"
                }), t._v(" University of Computer Science ")])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "mt-10 py-10 border-t border-gray-300 text-center"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center"
                }, [a("div", {
                    staticClass: "w-full lg:w-9/12 px-4"
                }, [a("p", {
                    staticClass: "mb-4 text-lg leading-relaxed text-gray-800"
                }, [t._v(" An artist of considerable range, Jenna the name taken by Melbourne-raised, Brooklyn-based Nick Murphy writes, performs and records all of his own music, giving it a warm, intimate feel with a solid groove structure. An artist of considerable range. ")]), a("a", {
                    staticClass: "font-normal text-green-500",
                    attrs: {
                        href: "javascript:void(0)"
                    }
                }, [t._v(" Show more ")])])])])
            }],
            Wa = {
                data: function() {
                    return {
                        team2: ve.a
                    }
                },
                components: {
                    Navbar: Ct,
                    FooterComponent: Ia
                }
            },
            Ga = Wa,
            Ha = Object(o["a"])(Ga, qa, Ya, !1, null, null, null),
            Ka = Ha.exports,
            Za = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("index-navbar"), a("section", {
                    staticClass: "header relative pt-16 items-center flex h-screen max-h-860-px"
                }, [t._m(0), a("img", {
                    staticClass: "absolute top-0 b-auto right-0 pt-16 sm:w-6/12 -mt-48 sm:mt-0 w-10/12 max-h-860-px",
                    attrs: {
                        src: t.patternVue,
                        alt: "..."
                    }
                })]), a("section", {
                    staticClass: "mt-48 md:mt-40 pb-40 relative bg-gray-200"
                }, [a("div", {
                    staticClass: "-mt-20 top-0 bottom-auto left-0 right-0 w-full absolute h-20",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-200 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])]), a("div", {
                    staticClass: "container mx-auto"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [a("div", {
                    staticClass: "w-10/12 md:w-6/12 lg:w-4/12 px-12 md:px-4 mr-auto ml-auto -mt-32"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg bg-green-600"
                }, [a("img", {
                    staticClass: "w-full align-middle rounded-t-lg",
                    attrs: {
                        alt: "...",
                        src: "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80"
                    }
                }), a("blockquote", {
                    staticClass: "relative p-8 mb-4"
                }, [a("svg", {
                    staticClass: "absolute left-0 w-full block h-95-px -top-94-px",
                    attrs: {
                        preserveAspectRatio: "none",
                        xmlns: "http://www.w3.org/2000/svg",
                        viewBox: "0 0 583 95"
                    }
                }, [a("polygon", {
                    staticClass: "text-green-600 fill-current",
                    attrs: {
                        points: "-30,95 583,95 583,65"
                    }
                })]), a("h4", {
                    staticClass: "text-xl font-bold text-white"
                }, [t._v(" Great for your awesome project ")]), a("p", {
                    staticClass: "text-md font-light mt-2 text-white"
                }, [t._v(" Putting together a page has never been easier than matching together pre-made components. From landing pages presentation to login areas, you can easily customise and built your pages. ")])])])]), t._m(1)])]), a("div", {
                    staticClass: "container mx-auto overflow-hidden pb-20"
                }, [a("div", {
                    staticClass: "flex flex-wrap items-center"
                }, [t._m(2), a("div", {
                    staticClass: "w-full md:w-5/12 px-4 mr-auto ml-auto mt-32"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 w-full mb-6 mt-48 md:mt-0"
                }, [a("img", {
                    staticClass: "w-full align-middle rounded absolute shadow-lg max-w-100-px left-145-px -top-29-px z-3",
                    attrs: {
                        alt: "...",
                        src: t.componentBtn
                    }
                }), a("img", {
                    staticClass: "w-full align-middle rounded-lg absolute shadow-lg max-w-210-px left-260-px -top-160-px",
                    attrs: {
                        alt: "...",
                        src: t.componentProfileCard
                    }
                }), a("img", {
                    staticClass: "w-full align-middle rounded-lg absolute shadow-lg max-w-180-px left-40-px -top-225-px z-2",
                    attrs: {
                        alt: "...",
                        src: t.componentInfoCard
                    }
                }), a("img", {
                    staticClass: "w-full align-middle rounded-lg absolute shadow-2xl max-w-200-px -left-50-px top-25-px",
                    attrs: {
                        alt: "...",
                        src: t.componentInfo2
                    }
                }), a("img", {
                    staticClass: "w-full align-middle rounded absolute shadow-lg max-w-580-px -left-20-px top-210-px",
                    attrs: {
                        alt: "...",
                        src: t.componentMenu
                    }
                }), a("img", {
                    staticClass: "w-full align-middle rounded absolute shadow-xl max-w-120-px left-195-px top-95-px",
                    attrs: {
                        alt: "...",
                        src: t.componentBtnPink
                    }
                })])])]), t._m(3)]), a("div", {
                    staticClass: "container mx-auto px-4 pb-32 pt-48"
                }, [a("div", {
                    staticClass: "items-center flex flex-wrap"
                }, [t._m(4), a("div", {
                    staticClass: "w-full md:w-6/12 mr-auto px-4 pt-24 md:pt-0"
                }, [a("img", {
                    staticClass: "max-w-full rounded-lg shadow-xl",
                    staticStyle: {
                        transform: "scale(1) perspective(1040px) rotateY(-11deg)"
                    },
                    attrs: {
                        alt: "...",
                        src: t.documentation
                    }
                })])])]), t._m(5)]), a("section", {
                    staticClass: "block relative z-1 bg-gray-700"
                }, [a("div", {
                    staticClass: "container mx-auto"
                }, [a("div", {
                    staticClass: "justify-center flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-12/12 px-4 -mt-24"
                }, [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("h5", {
                    staticClass: "text-xl font-semibold pb-4 text-center"
                }, [t._v(" Login Page ")]), a("router-link", {
                    attrs: {
                        to: "/auth/login"
                    }
                }, [a("div", {
                    staticClass: "hover:-mt-4 relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg ease-linear transition-all duration-150"
                }, [a("img", {
                    staticClass: "align-middle border-none max-w-full h-auto rounded-lg",
                    attrs: {
                        alt: "...",
                        src: t.login
                    }
                })])])], 1), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("h5", {
                    staticClass: "text-xl font-semibold pb-4 text-center"
                }, [t._v(" Profile Page ")]), a("router-link", {
                    attrs: {
                        to: "/profile"
                    }
                }, [a("div", {
                    staticClass: "hover:-mt-4 relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg ease-linear transition-all duration-150"
                }, [a("img", {
                    staticClass: "align-middle border-none max-w-full h-auto rounded-lg",
                    attrs: {
                        alt: "...",
                        src: t.profile
                    }
                })])])], 1), a("div", {
                    staticClass: "w-full lg:w-4/12 px-4"
                }, [a("h5", {
                    staticClass: "text-xl font-semibold pb-4 text-center"
                }, [t._v(" Landing Page ")]), a("router-link", {
                    attrs: {
                        to: "/landing"
                    }
                }, [a("div", {
                    staticClass: "hover:-mt-4 relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg ease-linear transition-all duration-150"
                }, [a("img", {
                    staticClass: "align-middle border-none max-w-full h-auto rounded-lg",
                    attrs: {
                        alt: "...",
                        src: t.landing
                    }
                })])])], 1)])])])])]), t._m(6), a("section", {
                    staticClass: "pb-16 bg-gray-300 relative pt-32"
                }, [a("div", {
                    staticClass: "-mt-20 top-0 bottom-auto left-0 right-0 w-full absolute h-20",
                    staticStyle: {
                        transform: "translateZ(0)"
                    }
                }, [a("svg", {
                    staticClass: "absolute bottom-0 overflow-hidden",
                    attrs: {
                        xmlns: "http://www.w3.org/2000/svg",
                        preserveAspectRatio: "none",
                        version: "1.1",
                        viewBox: "0 0 2560 100",
                        x: "0",
                        y: "0"
                    }
                }, [a("polygon", {
                    staticClass: "text-gray-300 fill-current",
                    attrs: {
                        points: "2560 0 2560 100 0 100"
                    }
                })])]), t._m(7)]), a("footer-component")], 1)
            },
            Qa = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto items-center flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "pt-32 sm:pt-0"
                }, [a("h2", {
                    staticClass: "font-semibold text-4xl text-gray-700"
                }, [t._v(" Vue Notus - A beautiful extension for Tailwind CSS. ")]), a("p", {
                    staticClass: "mt-4 text-lg leading-relaxed text-gray-600"
                }, [t._v(" Vue Notus is Free and Open Source. It does not change or add any CSS to the already one from "), a("a", {
                    staticClass: "text-gray-700",
                    attrs: {
                        href: "https://tailwindcss.com/?ref=creativetim",
                        target: "_blank"
                    }
                }, [t._v(" Tailwind CSS ")]), t._v(" . It features multiple HTML elements and it comes with dynamic components for ReactJS, Vue and Angular. ")]), a("div", {
                    staticClass: "mt-12"
                }, [a("a", {
                    staticClass: "get-started text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1 bg-green-500 active:bg-green-600 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" Get started ")]), a("a", {
                    staticClass: "github-star ml-1 text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1 bg-gray-800 active:bg-gray-700 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" Github Star ")])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full md:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "flex flex-wrap"
                }, [a("div", {
                    staticClass: "w-full md:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col mt-4"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-sitemap"
                })]), a("h6", {
                    staticClass: "text-xl mb-1 font-semibold"
                }, [t._v(" CSS Components ")]), a("p", {
                    staticClass: "mb-4 text-gray-600"
                }, [t._v(" Vue Notus comes with a huge number of Fully Coded CSS components. ")])])]), a("div", {
                    staticClass: "relative flex flex-col min-w-0"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-drafting-compass"
                })]), a("h6", {
                    staticClass: "text-xl mb-1 font-semibold"
                }, [t._v(" JavaScript Components ")]), a("p", {
                    staticClass: "mb-4 text-gray-600"
                }, [t._v(" We also feature many dynamic components for React, NextJS, Vue and Angular. ")])])])]), a("div", {
                    staticClass: "w-full md:w-6/12 px-4"
                }, [a("div", {
                    staticClass: "relative flex flex-col min-w-0 mt-4"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-newspaper"
                })]), a("h6", {
                    staticClass: "text-xl mb-1 font-semibold"
                }, [t._v("Pages")]), a("p", {
                    staticClass: "mb-4 text-gray-600"
                }, [t._v(" This extension also comes with 3 sample pages. They are fully coded so you can start working instantly. ")])])]), a("div", {
                    staticClass: "relative flex flex-col min-w-0"
                }, [a("div", {
                    staticClass: "px-4 py-5 flex-auto"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-file-alt"
                })]), a("h6", {
                    staticClass: "text-xl mb-1 font-semibold"
                }, [t._v(" Documentation ")]), a("p", {
                    staticClass: "mb-4 text-gray-600"
                }, [t._v(" Built by developers for developers. You will love how easy is to to work with Vue Notus. ")])])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full md:w-4/12 px-12 md:px-4 ml-auto mr-auto mt-48"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-sitemap text-xl"
                })]), a("h3", {
                    staticClass: "text-3xl mb-2 font-semibold leading-normal"
                }, [t._v(" CSS Components ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-4 mb-4 text-gray-700"
                }, [t._v(" Every element that you need in a product comes built in as a component. All components fit perfectly with each other and can have different colours. ")]), a("div", {
                    staticClass: "block pb-6"
                }, [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Buttons ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Inputs ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Labels ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Menus ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Navbars ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Pagination ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Progressbars ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Typography ")])]), a("a", {
                    staticClass: "font-bold text-gray-800 hover:text-gray-600 ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" View All "), a("i", {
                    staticClass: "fa fa-angle-double-right ml-1 leading-relaxed"
                })])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "flex flex-wrap items-center pt-32"
                }, [a("div", {
                    staticClass: "w-full md:w-6/12 px-4 mr-auto ml-auto mt-32"
                }, [a("div", {
                    staticClass: "justify-center flex flex-wrap relative"
                }, [a("div", {
                    staticClass: "my-4 w-full lg:w-6/12 px-4"
                }, [a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/svelte/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-red-600 shadow-lg rounded-lg text-center p-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/svelte.jpg"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" Svelte ")])])]), a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/react/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-blue-500 shadow-lg rounded-lg text-center p-8 mt-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/react.jpg"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" ReactJS ")])])]), a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/nextjs/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-gray-800 shadow-lg rounded-lg text-center p-8 mt-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/nextjs.jpg"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" NextJS ")])])])]), a("div", {
                    staticClass: "my-4 w-full lg:w-6/12 px-4 lg:mt-16"
                }, [a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/js/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-yellow-500 shadow-lg rounded-lg text-center p-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/js.png"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" JavaScript ")])])]), a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/angular/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-red-700 shadow-lg rounded-lg text-center p-8 mt-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/angular.jpg"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" Angular ")])])]), a("a", {
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("div", {
                    staticClass: "bg-green-500 shadow-lg rounded-lg text-center p-8 mt-8"
                }, [a("img", {
                    staticClass: "shadow-md rounded-full max-w-full w-16 mx-auto p-2 bg-white",
                    attrs: {
                        alt: "...",
                        src: "https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/vue.jpg"
                    }
                }), a("p", {
                    staticClass: "text-lg text-white mt-4 font-semibold"
                }, [t._v(" Vue.js ")])])])])])]), a("div", {
                    staticClass: "w-full md:w-4/12 px-12 md:px-4 ml-auto mr-auto mt-48"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-drafting-compass text-xl"
                })]), a("h3", {
                    staticClass: "text-3xl mb-2 font-semibold leading-normal"
                }, [t._v(" Javascript Components ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-4 mb-4 text-gray-700"
                }, [t._v(" In order to create a great User Experience some components require JavaScript. In this way you can manipulate the elements on the page and give more options to your users. ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-4 mb-4 text-gray-700"
                }, [t._v(" We created a set of Components that are dynamic and come to help you. ")]), a("div", {
                    staticClass: "block pb-6"
                }, [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Alerts ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Dropdowns ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Menus ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Modals ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Navbars ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Popovers ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Tabs ")]), a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-white uppercase last:mr-0 mr-2 mt-2"
                }, [t._v(" Tooltips ")])]), a("a", {
                    staticClass: "font-bold text-gray-800 hover:text-gray-600 ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/alerts/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" View all "), a("i", {
                    staticClass: "fa fa-angle-double-right ml-1 leading-relaxed"
                })])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "w-full md:w-5/12 ml-auto px-12 md:px-4"
                }, [a("div", {
                    staticClass: "md:pr-12"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-file-alt text-xl"
                })]), a("h3", {
                    staticClass: "text-3xl font-semibold"
                }, [t._v(" Complex Documentation ")]), a("p", {
                    staticClass: "mt-4 text-lg leading-relaxed text-gray-600"
                }, [t._v(" This extension comes a lot of fully coded examples that help you get started faster. You can adjust the colors and also the programming language. You can change the text and images and you're good to go. ")]), a("ul", {
                    staticClass: "list-none mt-6"
                }, [a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-gray-100 mr-3"
                }, [a("i", {
                    staticClass: "fas fa-fingerprint"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v(" Built by Developers for Developers ")])])])]), a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-gray-100 mr-3"
                }, [a("i", {
                    staticClass: "fab fa-html5"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v(" Carefully crafted code for Components ")])])])]), a("li", {
                    staticClass: "py-2"
                }, [a("div", {
                    staticClass: "flex items-center"
                }, [a("div", [a("span", {
                    staticClass: "text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-gray-600 bg-gray-100 mr-3"
                }, [a("i", {
                    staticClass: "far fa-paper-plane"
                })])]), a("div", [a("h4", {
                    staticClass: "text-gray-600"
                }, [t._v(" Dynamic Javascript Components ")])])])])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "justify-center text-center flex flex-wrap mt-24"
                }, [a("div", {
                    staticClass: "w-full md:w-6/12 px-12 md:px-4"
                }, [a("h2", {
                    staticClass: "font-semibold text-4xl"
                }, [t._v("Beautiful Example Pages")]), a("p", {
                    staticClass: "text-lg leading-relaxed mt-4 mb-4 text-gray-600"
                }, [t._v(" Vue Notus is a completly new product built using our past experience in web templates. Take the examples we made for you and start playing with them. ")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("section", {
                    staticClass: "py-20 bg-gray-700 overflow-hidden"
                }, [a("div", {
                    staticClass: "container mx-auto pb-64"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center"
                }, [a("div", {
                    staticClass: "w-full md:w-5/12 px-12 md:px-4 ml-auto mr-auto md:mt-64"
                }, [a("div", {
                    staticClass: "text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
                }, [a("i", {
                    staticClass: "fas fa-code-branch text-xl"
                })]), a("h3", {
                    staticClass: "text-3xl mb-2 font-semibold leading-normal text-white"
                }, [t._v(" Open Source ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-4 mb-4 text-gray-500"
                }, [t._v(" Since "), a("a", {
                    staticClass: "text-gray-400",
                    attrs: {
                        href: "https://tailwindcss.com/?ref=creativetim",
                        target: "_blank"
                    }
                }, [t._v(" Tailwind CSS ")]), t._v(" is an open source project we wanted to continue this movement too. You can give this version a try to feel the design and also test the quality of the code! ")]), a("p", {
                    staticClass: "text-lg font-light leading-relaxed mt-0 mb-4 text-gray-500"
                }, [t._v(" Get it free on Github and please help us spread the news with a Star! ")]), a("a", {
                    staticClass: "github-star mt-4 inline-block text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1 bg-gray-800 active:bg-gray-700 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" Github Star ")])]), a("div", {
                    staticClass: "w-full md:w-4/12 px-4 mr-auto ml-auto mt-32 relative"
                }, [a("i", {
                    staticClass: "fab fa-github text-gray-800 text-55 absolute -top-150-px -right-100 left-auto opacity-80"
                })])])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", {
                    staticClass: "container mx-auto"
                }, [a("div", {
                    staticClass: "flex flex-wrap justify-center bg-white shadow-xl rounded-lg -mt-64 py-16 px-12 relative z-10"
                }, [a("div", {
                    staticClass: "w-full text-center lg:w-8/12"
                }, [a("p", {
                    staticClass: "text-4xl text-center"
                }, [a("span", {
                    attrs: {
                        role: "img",
                        "aria-label": "love"
                    }
                }, [t._v(" 😍 ")])]), a("h3", {
                    staticClass: "font-semibold text-3xl"
                }, [t._v(" Do you love this Starter Kit? ")]), a("p", {
                    staticClass: "text-gray-600 text-lg leading-relaxed mt-4 mb-4"
                }, [t._v(" Cause if you do, it can be yours now. Hit the buttons below to navigate to get the Free version for your next project. Build a new web app or give an old project a new look! ")]), a("div", {
                    staticClass: "sm:block flex flex-col mt-10"
                }, [a("a", {
                    staticClass: "get-started text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-2 bg-green-500 active:bg-green-600 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [t._v(" Get started ")]), a("a", {
                    staticClass: "github-star sm:ml-1 text-white font-bold px-6 py-4 rounded outline-none focus:outline-none mr-1 mb-1 bg-gray-800 active:bg-gray-700 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus?ref=vn-index",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "fab fa-github text-lg mr-1"
                }), a("span", [t._v("Help With a Star")])])]), a("div", {
                    staticClass: "text-center mt-16"
                })])])])
            }],
            Xa = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("nav", {
                    staticClass: "top-0 fixed z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg bg-white shadow"
                }, [a("div", {
                    staticClass: "container px-4 mx-auto flex flex-wrap items-center justify-between"
                }, [a("div", {
                    staticClass: "w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start"
                }, [a("router-link", {
                    attrs: {
                        to: "/"
                    }
                }, [a("a", {
                    staticClass: "text-gray-800 text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-no-wrap uppercase",
                    attrs: {
                        href: "#pablo"
                    }
                }, [t._v(" Vue Notus ")])]), a("button", {
                    staticClass: "cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none",
                    attrs: {
                        type: "button"
                    },
                    on: {
                        click: t.setNavbarOpen
                    }
                }, [a("i", {
                    staticClass: "fas fa-bars"
                })])], 1), a("div", {
                    staticClass: "lg:flex flex-grow items-center",
                    class: [t.navbarOpen ? "block" : "hidden"],
                    attrs: {
                        id: "example-navbar-warning"
                    }
                }, [t._m(0), a("ul", {
                    staticClass: "flex flex-col lg:flex-row list-none lg:ml-auto"
                }, [a("li", {
                    staticClass: "flex items-center"
                }, [a("index-dropdown")], 1), t._m(1), t._m(2), t._m(3), t._m(4)])])])])
            },
            ts = [function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("ul", {
                    staticClass: "flex flex-col lg:flex-row list-none mr-auto"
                }, [a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "hover:text-gray-600 text-gray-800 px-3 py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://www.creative-tim.com/learning-lab/tailwind/vue/overview/notus?ref=vn-index-navbar"
                    }
                }, [a("i", {
                    staticClass: "text-gray-500 far fa-file-alt text-lg leading-lg mr-2"
                }), t._v(" Docs ")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "hover:text-gray-600 text-gray-800 px-3 py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "text-gray-500 fab fa-facebook text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Share")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "hover:text-gray-600 text-gray-800 px-3 py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://twitter.com/intent/tweet?url=https%3A%2F%2Fdemos.creative-tim.com%2Fvue-notus%2F%23%2F&text=Start%20your%20development%20with%20a%20Free%20Tailwind%20CSS%20and%20VueJS%20UI%20Kit%20and%20Admin.%20Let%20Vue%20Notus%20amaze%20you%20with%20its%20cool%20features%20and%20build%20tools%20and%20get%20your%20project%20to%20a%20whole%20new%20level.%20",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "text-gray-500 fab fa-twitter text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Tweet")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("a", {
                    staticClass: "hover:text-gray-600 text-gray-800 px-3 py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "https://github.com/creativetimofficial/vue-notus?ref=vn-index-navbar",
                        target: "_blank"
                    }
                }, [a("i", {
                    staticClass: "text-gray-500 fab fa-github text-lg leading-lg"
                }), a("span", {
                    staticClass: "lg:hidden inline-block ml-2"
                }, [t._v("Star")])])])
            }, function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("li", {
                    staticClass: "flex items-center"
                }, [a("button", {
                    staticClass: "bg-green-500 text-white active:bg-green-600 text-xs font-bold uppercase px-4 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none lg:mr-1 lg:mb-0 ml-3 mb-3 ease-linear transition-all duration-150",
                    attrs: {
                        type: "button"
                    }
                }, [a("i", {
                    staticClass: "fas fa-arrow-alt-circle-down"
                }), t._v(" Download ")])])
            }],
            es = function() {
                var t = this,
                    e = t.$createElement,
                    a = t._self._c || e;
                return a("div", [a("a", {
                    ref: "btnDropdownRef",
                    staticClass: "hover:text-gray-600 text-gray-800 px-3 py-2 flex items-center text-xs uppercase font-bold",
                    attrs: {
                        href: "#pablo"
                    },
                    on: {
                        click: function(e) {
                            return t.toggleDropdown(e)
                        }
                    }
                }, [t._v(" Demo Pages ")]), a("div", {
                    ref: "popoverDropdownRef",
                    staticClass: "bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48",
                    class: {
                        hidden: !t.dropdownPopoverShow, block: t.dropdownPopoverShow
                    }
                }, [a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" Admin Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/dashboard"
                    }
                }, [t._v(" Dashboard ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/settings"
                    }
                }, [t._v(" Settings ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/tables"
                    }
                }, [t._v(" Tables ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/admin/maps"
                    }
                }, [t._v(" Maps ")]), a("div", {
                    staticClass: "h-0 mx-4 my-2 border border-solid border-gray-200"
                }), a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" Auth Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/auth/login"
                    }
                }, [t._v(" Login ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/auth/register"
                    }
                }, [t._v(" Register ")]), a("div", {
                    staticClass: "h-0 mx-4 my-2 border border-solid border-gray-200"
                }), a("span", {
                    staticClass: "text-sm pt-2 pb-0 px-4 font-bold block w-full whitespace-no-wrap bg-transparent text-gray-500"
                }, [t._v(" No Layout ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/landing"
                    }
                }, [t._v(" Lading ")]), a("router-link", {
                    staticClass: "text-sm py-2 px-4 font-normal block w-full whitespace-no-wrap bg-transparent text-gray-800",
                    attrs: {
                        to: "/profile"
                    }
                }, [t._v(" Profile ")])], 1)])
            },
            as = [],
            ss = {
                data: function() {
                    return {
                        dropdownPopoverShow: !1
                    }
                },
                methods: {
                    toggleDropdown: function(t) {
                        t.preventDefault(), this.dropdownPopoverShow ? this.dropdownPopoverShow = !1 : (this.dropdownPopoverShow = !0, Object(g["a"])(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
                            placement: "bottom-start"
                        }))
                    }
                }
            },
            ls = ss,
            rs = Object(o["a"])(ls, es, as, !1, null, null, null),
            is = rs.exports,
            os = {
                data: function() {
                    return {
                        navbarOpen: !1
                    }
                },
                methods: {
                    setNavbarOpen: function() {
                        this.navbarOpen = !this.navbarOpen
                    }
                },
                components: {
                    IndexDropdown: is
                }
            },
            ns = os,
            cs = Object(o["a"])(ns, Xa, ts, !1, null, null, null),
            ds = cs.exports,
            ps = a("1ac6"),
            fs = a.n(ps),
            us = a("80b3"),
            xs = a.n(us),
            ms = a("5393"),
            bs = a.n(ms),
            gs = a("0b08"),
            ws = a.n(gs),
            hs = a("7032"),
            vs = a.n(hs),
            Cs = a("e54d"),
            ys = a.n(Cs),
            _s = a("4250"),
            ks = a.n(_s),
            js = a("191e"),
            Ss = a.n(js),
            Es = a("4424"),
            $s = a.n(Es),
            Ds = a("707c"),
            Os = a.n(Ds),
            Ps = a("6265"),
            As = a.n(Ps),
            Ts = {
                data: function() {
                    return {
                        patternVue: fs.a,
                        componentBtn: xs.a,
                        componentProfileCard: bs.a,
                        componentInfoCard: ws.a,
                        componentInfo2: vs.a,
                        componentMenu: ys.a,
                        componentBtnPink: ks.a,
                        documentation: Ss.a,
                        login: $s.a,
                        profile: Os.a,
                        landing: As.a
                    }
                },
                components: {
                    IndexNavbar: ds,
                    FooterComponent: Ia
                }
            },
            Fs = Ts,
            Ls = Object(o["a"])(Fs, Za, Qa, !1, null, null, null),
            Ns = Ls.exports,
            zs = [{
                path: "/admin",
                redirect: "/admin/dashboard",
                component: ot,
                children: [{
                    path: "/admin/dashboard",
                    component: ce
                }, {
                    path: "/admin/settings",
                    component: $e
                }, {
                    path: "/admin/tables",
                    component: la
                }, {
                    path: "/admin/maps",
                    component: ba
                }]
            }, {
                path: "/auth",
                redirect: "/auth/login",
                component: Tt,
                children: [{
                    path: "/auth/login",
                    component: Sa
                }, {
                    path: "/auth/register",
                    component: Aa
                }]
            }, {
                path: "/landing",
                component: Ua
            }, {
                path: "/profile",
                component: Ka
            }, {
                path: "/",
                component: Ns
            }, {
                path: "*",
                redirect: "/"
            }];
        s["a"].config.productionTip = !1, s["a"].use(l["a"]);
        var Rs = new l["a"]({
            routes: zs
        });
        new s["a"]({
            router: Rs,
            render: function(t) {
                return t(d)
            }
        }).$mount("#app")
    },
    6265: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/landing.37b6ed3b.jpg"
    },
    "6bff": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/github.4ffd4fe7.svg"
    },
    7017: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/register_bg_2.2fee0b50.png"
    },
    7032: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-info-2.4c7eaa62.png"
    },
    "707c": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/profile.056db542.jpg"
    },
    "80b3": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-btn.75fe9b24.png"
    },
    "8cac": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/react.c4eb3d0b.jpg"
    },
    "8d31": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/team-4-470x470.7d13384c.png"
    },
    "9b47": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/team-2-800x800.dcfcf3b7.jpg"
    },
    "9c9e": function(t, e, a) {},
    "9cda": function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/team-3-800x800.5a0e395b.jpg"
    },
    c1c9: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/sketch.e7c82e5c.jpg"
    },
    ccc8: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/google.87be59a1.svg"
    },
    e54d: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/component-menu.c72479a3.png"
    },
    f61f: function(t, e, a) {
        t.exports = a.p + "vuenotus/static/tte/img/bootstrap.ab904daa.jpg"
    }
});
