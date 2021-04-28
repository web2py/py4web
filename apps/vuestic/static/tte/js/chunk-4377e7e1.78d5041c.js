(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-4377e7e1"], {
        8570: function(a, e, t) {
            "use strict";
            t.r(e);
            var i = function() {
                    var a = this,
                        e = a.$createElement,
                        t = a._self._c || e;
                    return t("div", {
                        staticClass: "lists"
                    }, [t("div", {
                        staticClass: "row"
                    }, [t("div", {
                        staticClass: "flex xs12 lg6"
                    }, [t("va-list", {
                        staticClass: "mb-2",
                        attrs: {
                            fit: ""
                        }
                    }, [t("va-list-label", [a._v(" " + a._s(a.$t("lists.customers")) + " ")]), a._l(a.customers, (function(e, i) {
                        return [t("va-item", {
                            key: "item" + e.id,
                            attrs: {
                                clickable: ""
                            },
                            on: {
                                click: function(t) {
                                    return a.notify(e.name)
                                }
                            }
                        }, [t("va-item-section", {
                            attrs: {
                                avatar: ""
                            }
                        }, [t("va-avatar", [t("img", {
                            attrs: {
                                src: e.picture,
                                alt: e.name
                            }
                        })])], 1), t("va-item-section", [t("va-item-label", [a._v(" " + a._s(e.name) + " ")]), t("va-item-label", {
                            attrs: {
                                caption: ""
                            }
                        }, [a._v(" " + a._s(e.address) + " ")])], 1), t("va-item-section", {
                            attrs: {
                                side: ""
                            }
                        }, [t("va-icon", {
                            attrs: {
                                name: "fa fa-eye",
                                color: "gray"
                            }
                        })], 1)], 1), i < a.customers.length - 1 ? t("va-list-separator", {
                            key: "separator" + e.id
                        }) : a._e()]
                    }))], 2), t("va-list", {
                        attrs: {
                            fit: ""
                        }
                    }, [t("va-list-label", [a._v(" " + a._s(a.$t("lists.recentMessages")) + " ")]), a._l(a.customers, (function(e, i) {
                        return [t("va-item", {
                            key: "item" + e.id,
                            attrs: {
                                clickable: ""
                            },
                            on: {
                                click: function(t) {
                                    return a.toggleStar(e)
                                }
                            }
                        }, [t("va-item-section", {
                            attrs: {
                                side: ""
                            }
                        }, [e.starred ? t("va-icon", {
                            attrs: {
                                name: "fa fa-star",
                                color: "warning"
                            }
                        }) : a._e()], 1), t("va-item-section", {
                            attrs: {
                                avatar: ""
                            }
                        }, [t("va-avatar", [t("img", {
                            attrs: {
                                src: e.picture,
                                alt: e.name
                            }
                        })])], 1), t("va-item-section", [t("va-item-label", [a._v(" " + a._s(e.name) + " ")])], 1), t("va-item-section", {
                            attrs: {
                                side: ""
                            }
                        }, [t("va-icon", {
                            attrs: {
                                name: a.getGenderIcon(e.gender),
                                color: a.getGenderColor(e.gender)
                            }
                        })], 1)], 1), i < a.customers.length - 1 ? t("va-list-separator", {
                            key: "separator" + e.id
                        }) : a._e()]
                    })), t("va-list-separator", {
                        attrs: {
                            fit: "",
                            spaced: ""
                        }
                    }), t("va-list-label", {
                        attrs: {
                            color: "gray"
                        }
                    }, [a._v(" " + a._s(a.$t("lists.archieved")) + " ")]), a._l(a.archived, (function(e, i) {
                        return [t("va-item", {
                            key: "item" + e.id
                        }, [t("va-item-section", {
                            attrs: {
                                side: ""
                            }
                        }, [e.starred ? t("va-icon", {
                            attrs: {
                                name: "fa fa-star",
                                color: "warning"
                            }
                        }) : a._e()], 1), t("va-item-section", {
                            attrs: {
                                avatar: ""
                            }
                        }, [t("va-avatar", [t("img", {
                            attrs: {
                                src: e.picture,
                                alt: e.name
                            }
                        })])], 1), t("va-item-section", [t("va-item-label", [a._v(" " + a._s(e.name) + " ")])], 1)], 1), i < a.archived.length - 1 ? t("va-list-separator", {
                            key: "separator" + e.id
                        }) : a._e()]
                    }))], 2)], 1), t("div", {
                        staticClass: "flex xs12 lg6"
                    }, [t("va-list", {
                        staticClass: "mb-2",
                        attrs: {
                            fit: ""
                        }
                    }, [t("va-list-label", [a._v(" " + a._s(a.$t("lists.starterKit")) + " ")]), t("va-item", {
                        attrs: {
                            clickable: ""
                        }
                    }, [t("va-item-section", [t("va-item-label", [a._v(" Add profile images ")]), t("va-item-label", {
                        attrs: {
                            caption: ""
                        }
                    }, [a._v(" You can use PNG or JPG files. ")])], 1)], 1), t("va-item", {
                        attrs: {
                            clickable: ""
                        }
                    }, [t("va-item-section", [t("va-item-label", [a._v(" Invite friends ")]), t("va-item-label", {
                        attrs: {
                            caption: ""
                        }
                    }, [a._v(" You can send invitations via email or any messenger. ")])], 1)], 1), t("va-list-separator", {
                        attrs: {
                            fit: "",
                            spaced: ""
                        }
                    }), t("va-list-label", [a._v(" " + a._s(a.$t("lists.notifications")) + " ")]), t("va-item", [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-checkbox", {
                        model: {
                            value: a.appBanners,
                            callback: function(e) {
                                a.appBanners = e
                            },
                            expression: "appBanners"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v(" Application Banners ")]), t("va-item-label", {
                        attrs: {
                            caption: ""
                        }
                    }, [a._v(" You can send invitations via email or any messenger. ")])], 1)], 1), t("va-item", [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-checkbox", {
                        model: {
                            value: a.banners,
                            callback: function(e) {
                                a.banners = e
                            },
                            expression: "banners"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v(" Banners ")]), t("va-item-label", {
                        attrs: {
                            caption: ""
                        }
                    }, [a._v(" You can send invitations via email or any messenger. ")])], 1)], 1), t("va-item", [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-checkbox", {
                        model: {
                            value: a.notifications,
                            callback: function(e) {
                                a.notifications = e
                            },
                            expression: "notifications"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v(" Midnight Notifications ")])], 1)], 1)], 1), t("va-list", {
                        attrs: {
                            fit: ""
                        }
                    }, [t("va-list-label", [a._v(" " + a._s(a.$t("lists.routerSupport")) + " ")]), t("va-item", {
                        attrs: {
                            to: {
                                name: "google-maps"
                            }
                        }
                    }, [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-icon", {
                        attrs: {
                            name: "fa fa-google",
                            color: "red"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v("Google Maps")])], 1)], 1), t("va-item", {
                        attrs: {
                            to: {
                                name: "yandex-maps"
                            }
                        }
                    }, [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-icon", {
                        attrs: {
                            name: "fa fa-map",
                            color: "red"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v("Yandex Maps")])], 1)], 1), t("va-item", {
                        attrs: {
                            to: {
                                name: "leaflet-maps"
                            }
                        }
                    }, [t("va-item-section", {
                        attrs: {
                            side: ""
                        }
                    }, [t("va-icon", {
                        attrs: {
                            name: "fa fa-map-marker",
                            color: "red"
                        }
                    })], 1), t("va-item-section", [t("va-item-label", [a._v("Leaflet Maps")])], 1)], 1)], 1)], 1)])])
                },
                s = [],
                r = t("e674"),
                n = {
                    data: function() {
                        return {
                            customers: r.slice(0, 5),
                            archived: r.slice(5, 8),
                            appBanners: !1,
                            banners: !1,
                            notifications: !0
                        }
                    },
                    methods: {
                        getGenderIcon: function(a) {
                            return "male" === a ? "fa fa-mars" : "fa fa-venus"
                        },
                        getGenderColor: function(a) {
                            return "male" === a ? "blue" : "pink"
                        },
                        notify: function(a) {
                            this.showToast("Clicked ".concat(a), {
                                position: "bottom-right"
                            })
                        },
                        toggleStar: function(a) {
                            a.starred = !a.starred
                        }
                    }
                },
                o = n,
                l = t("2877"),
                c = Object(l["a"])(o, i, s, !1, null, null, null);
            e["default"] = c.exports
        },
        e674: function(a) {
            a.exports = JSON.parse('[{"id":"5d318282400cc272d72ff744","starred":true,"balance":"$3,210.05","picture":"https://randomuser.me/api/portraits/women/1.jpg","age":30,"name":"Marcia Neal","gender":"female","company":"BLUEGRAIN","email":"marcianeal@bluegrain.com","phone":"+1 (950) 575-2330","address":"642 Overbaugh Place, Loretto, Rhode Island, 3756"},{"id":"5d318282da3af2a9bda573b7","starred":false,"balance":"$3,961.47","picture":"https://randomuser.me/api/portraits/women/2.jpg","age":21,"name":"Corrine Oliver","gender":"female","company":"QUALITERN","email":"corrineoliver@qualitern.com","phone":"+1 (955) 402-3254","address":"532 Colin Place, Talpa, Connecticut, 7461"},{"id":"5d31828232ea44346bd45ee9","starred":true,"balance":"$1,874.06","picture":"https://randomuser.me/api/portraits/men/1.jpg","age":27,"name":"Tucker Kaufman","gender":"male","company":"PREMIANT","email":"tuckerkaufman@premiant.com","phone":"+1 (954) 475-2928","address":"887 Winthrop Street, Tryon, Florida, 3912"},{"id":"5d3182822ebdb5c989bb3364","starred":false,"balance":"$1,797.76","picture":"https://randomuser.me/api/portraits/women/3.jpg","age":32,"name":"Daisy Kramer","gender":"female","company":"ORBIN","email":"daisykramer@orbin.com","phone":"+1 (858) 416-3088","address":"821 Louise Terrace, Waterview, Indiana, 6960"},{"id":"5d318282e1e716000b687943","starred":false,"balance":"$2,538.94","picture":"https://randomuser.me/api/portraits/women/4.jpg","age":26,"name":"Mindy Potts","gender":"female","company":"SNACKTION","email":"mindypotts@snacktion.com","phone":"+1 (835) 508-2695","address":"418 Broadway , Whitehaven, New York, 7690"},{"id":"5d318282a9a4a59adf96cdd0","starred":false,"balance":"$3,143.43","picture":"https://randomuser.me/api/portraits/men/2.jpg","age":35,"name":"Dotson Franks","gender":"male","company":"SATIANCE","email":"dotsonfranks@satiance.com","phone":"+1 (869) 559-3971","address":"156 Lyme Avenue, Lupton, California, 1221"},{"id":"5d3182823227c20aabc4993f","starred":false,"balance":"$2,601.91","picture":"https://randomuser.me/api/portraits/women/5.jpg","age":29,"name":"Audrey Clay","gender":"female","company":"MIRACLIS","email":"audreyclay@miraclis.com","phone":"+1 (860) 565-2697","address":"644 Vermont Court, Freelandville, Kentucky, 2619"},{"id":"5d318282b5127412e1761466","starred":false,"balance":"$1,718.36","picture":"https://randomuser.me/api/portraits/men/3.jpg","age":37,"name":"Aguirre Klein","gender":"male","company":"CALCU","email":"aguirreklein@calcu.com","phone":"+1 (924) 555-3247","address":"626 Carroll Street, Roulette, Ohio, 1477"}]')
        }
    }
]);
