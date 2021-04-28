(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d22c838"], {
        f40d: function(t, e, s) {
            "use strict";
            s.r(e);
            var r = function() {
                    var t = this,
                        e = t.$createElement,
                        s = t._self._c || e;
                    return s("form", {
                        staticClass: "login",
                        on: {
                            submit: function(e) {
                                return e.preventDefault(), t.onsubmit(e)
                            }
                        }
                    }, [s("div", {
                        staticClass: "row mb-2"
                    }, [s("va-input", {
                        attrs: {
                            type: "email",
                            label: t.$t("auth.email"),
                            error: !!t.emailErrors.length,
                            "error-messages": t.emailErrors
                        },
                        model: {
                            value: t.email,
                            callback: function(e) {
                                t.email = e
                            },
                            expression: "email"
                        }
                    })], 1), s("div", {
                        staticClass: "row justify--center"
                    }, [s("va-button", {
                        staticClass: "my-0",
                        attrs: {
                            type: "submit"
                        }
                    }, [t._v(t._s(t.$t("auth.reset_password")))])], 1)])
                },
                a = [],
                i = {
                    name: "recover-password",
                    data: function() {
                        return {
                            email: "",
                            emailErrors: []
                        }
                    },
                    methods: {
                        onsubmit: function() {
                            this.email ? this.$router.push("/") : this.emailErrors = ["Email is required"]
                        }
                    }
                },
                n = i,
                l = s("2877"),
                o = Object(l["a"])(n, r, a, !1, null, null, null);
            e["default"] = o.exports
        }
    }
]);
