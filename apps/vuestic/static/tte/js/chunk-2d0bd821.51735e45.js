(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d0bd821"], {
        "2bfa": function(t, e, i) {
            "use strict";
            i.r(e);
            var a = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "medium-editor"
                    }, [i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex md12"
                    }, [i("va-card", {
                        attrs: {
                            title: t.$t("forms.mediumEditor.title")
                        }
                    }, [i("div", {
                        staticClass: "d-flex flex-center"
                    }, [i("va-medium-editor", {
                        on: {
                            initialized: t.handleEditorInitialization
                        }
                    }, [i("h1", [t._v("Select Text To Open Editor")]), i("p", [t._v(" You enter into your favorite local bar looking "), i("span", {
                        staticClass: "default-selection"
                    }, [i("b", [t._v("good")])]), t._v(" as hell, but you know the only heads you want to turn—spicy & stylish alpha bitches — are heavily fixated on the D. The hot girl talks to you, but she only wants to be your best friend. Her nonthreatening and attentive best friend. Receiver of sexy selfies, listener of stories. Meanwhile, you attract unwanted attention from straight men, pudgy and greasy moths to your emotionally distant flame. ")]), i("p", [t._v(" Read the full article on "), i("a", {
                        attrs: {
                            href: "https://medium.com/@dorn.anna/girl-no-you-dont-2e21e826c62c"
                        }
                    }, [t._v("Medium")])])])], 1)])], 1)])])
                },
                n = [],
                o = {
                    name: "medium-editor",
                    methods: {
                        handleEditorInitialization: function(t) {
                            var e = this;
                            this.editor = t, this.$nextTick((function() {
                                e.highlightSampleText()
                            }))
                        },
                        highlightSampleText: function() {
                            var t = document.getElementsByClassName("default-selection")[0];
                            this.editor.selectElement(t)
                        }
                    }
                },
                s = o,
                l = i("2877"),
                r = Object(l["a"])(s, a, n, !1, null, null, null);
            e["default"] = r.exports
        }
    }
]);
