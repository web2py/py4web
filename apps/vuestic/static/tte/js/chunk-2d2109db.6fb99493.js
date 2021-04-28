(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-2d2109db"], {
        b93a: function(a, t, e) {
            "use strict";
            e.r(t);
            var o = function() {
                    var a = this,
                        t = a.$createElement,
                        e = a._self._c || t;
                    return e("div", {
                        staticClass: "yandex-maps-page"
                    }, [e("div", {
                        staticClass: "row"
                    }, [e("div", {
                        staticClass: "flex md12 xs12"
                    }, [e("va-card", {
                        staticClass: "yandex-maps-page__widget",
                        attrs: {
                            title: "Yandex Maps"
                        }
                    }, [e("yandex-map", {
                        staticStyle: {
                            width: "100%",
                            height: "65vh"
                        },
                        attrs: {
                            "use-object-manager:": !0,
                            coords: [55.2, 38.8],
                            zoom: 8,
                            behaviors: ["default"],
                            controls: ["trafficControl", "zoomControl", "geolocationControl", "fullscreenControl", "searchControl"],
                            placemarks: a.placemarks,
                            "map-type": "hybrid"
                        }
                    })], 1)], 1)])])
                },
                s = [],
                n = e("5490"),
                l = {
                    name: "yandex-maps-page",
                    components: {
                        yandexMap: n["b"]
                    },
                    data: function() {
                        return {
                            placemarks: [{
                                coords: [54.8, 38.9],
                                properties: {},
                                options: {},
                                clusterName: "1",
                                balloonTemplate: '<div>"Your custom template"</div>',
                                callbacks: {
                                    click: function() {}
                                }
                            }]
                        }
                    }
                },
                c = l,
                r = e("2877"),
                i = Object(r["a"])(c, o, s, !1, null, null, null);
            t["default"] = i.exports
        }
    }
]);
