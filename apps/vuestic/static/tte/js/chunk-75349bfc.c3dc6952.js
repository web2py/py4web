(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["chunk-75349bfc"], {
        "3abe": function(t, e, i) {
            var n = i("e11e");

            function o(t) {
                t = t || {
                    defaultStyle: !0
                }, t.defaultStyle && (n.Icon.Default.imagePath = "//cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/images", s());
                var e = document.createElement("div");
                return e.setAttribute("style", "width:100%;height:100%;position:inherit;"), document.body.appendChild(e), n.map(e)
            }

            function s() {
                document.documentElement.style.height = "100%", document.body.style.height = "100%", document.body.style.margin = "0";
                var t = document.createElement("link");
                t.setAttribute("rel", "stylesheet"), t.setAttribute("href", "//cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.3/leaflet.css"), document.body.appendChild(t)
            }
            t.exports = o
        },
        8107: function(t, e, i) {
            "use strict";
            var n = i("9f6e"),
                o = i.n(n);
            o.a
        },
        "9f6e": function(t, e, i) {},
        a75f: function(t, e, i) {
            "use strict";
            i.r(e);
            var n = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "leaflet-maps-page"
                    }, [i("div", {
                        staticClass: "row"
                    }, [i("div", {
                        staticClass: "flex md12 xs12"
                    }, [i("va-card", {
                        staticClass: "leaflet-maps-page__widget",
                        attrs: {
                            title: "Leaflet Maps"
                        }
                    }, [i("leaflet-map", {
                        staticStyle: {
                            height: "65vh"
                        }
                    })], 1)], 1)])])
                },
                o = [],
                s = function() {
                    var t = this,
                        e = t.$createElement,
                        i = t._self._c || e;
                    return i("div", {
                        staticClass: "leaflet-map fill-height"
                    })
                },
                a = [],
                r = (i("3abe"), i("e11e")),
                h = {
                    name: "leaflet-map",
                    mounted: function() {
                        r["Icon"].Default.imagePath = "https://unpkg.com/leaflet@1.0.3/dist/images";
                        var t = r["map"](this.$el).setView([51.505, -.09], 13);
                        r["tileLayer"]("https://{s}.tile.osm.org/{z}/{x}/{y}.png", {
                            attribution: '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
                        }).addTo(t), r["marker"]([51.5, -.09]).addTo(t).bindPopup("A pretty CSS3 popup.<br> Easily customizable.").openPopup()
                    }
                },
                l = h,
                u = (i("8107"), i("2877")),
                c = Object(u["a"])(l, s, a, !1, null, null, null),
                p = c.exports,
                d = {
                    name: "leaflet-maps-page",
                    components: {
                        LeafletMap: p
                    }
                },
                _ = d,
                m = Object(u["a"])(_, n, o, !1, null, null, null);
            e["default"] = m.exports
        },
        e11e: function(t, e, i) {
            var n, o;
            (function(s, a, r) {
                var h = s.L,
                    l = {
                        version: "0.7.7"
                    };
                "object" === typeof t.exports ? t.exports = l : (n = l, o = "function" === typeof n ? n.call(e, i, e, t) : n, o === r || (t.exports = o)), l.noConflict = function() {
                        return s.L = h, this
                    }, s.L = l, l.Util = {
                        extend: function(t) {
                            var e, i, n, o, s = Array.prototype.slice.call(arguments, 1);
                            for (i = 0, n = s.length; i < n; i++)
                                for (e in o = s[i] || {}, o) o.hasOwnProperty(e) && (t[e] = o[e]);
                            return t
                        },
                        bind: function(t, e) {
                            var i = arguments.length > 2 ? Array.prototype.slice.call(arguments, 2) : null;
                            return function() {
                                return t.apply(e, i || arguments)
                            }
                        },
                        stamp: function() {
                            var t = 0,
                                e = "_leaflet_id";
                            return function(i) {
                                return i[e] = i[e] || ++t, i[e]
                            }
                        }(),
                        invokeEach: function(t, e, i) {
                            var n, o;
                            if ("object" === typeof t) {
                                for (n in o = Array.prototype.slice.call(arguments, 3), t) e.apply(i, [n, t[n]].concat(o));
                                return !0
                            }
                            return !1
                        },
                        limitExecByInterval: function(t, e, i) {
                            var n, o;
                            return function s() {
                                var a = arguments;
                                n ? o = !0 : (n = !0, setTimeout((function() {
                                    n = !1, o && (s.apply(i, a), o = !1)
                                }), e), t.apply(i, a))
                            }
                        },
                        falseFn: function() {
                            return !1
                        },
                        formatNum: function(t, e) {
                            var i = Math.pow(10, e || 5);
                            return Math.round(t * i) / i
                        },
                        trim: function(t) {
                            return t.trim ? t.trim() : t.replace(/^\s+|\s+$/g, "")
                        },
                        splitWords: function(t) {
                            return l.Util.trim(t).split(/\s+/)
                        },
                        setOptions: function(t, e) {
                            return t.options = l.extend({}, t.options, e), t.options
                        },
                        getParamString: function(t, e, i) {
                            var n = [];
                            for (var o in t) n.push(encodeURIComponent(i ? o.toUpperCase() : o) + "=" + encodeURIComponent(t[o]));
                            return (e && -1 !== e.indexOf("?") ? "&" : "?") + n.join("&")
                        },
                        template: function(t, e) {
                            return t.replace(/\{ *([\w_]+) *\}/g, (function(t, i) {
                                var n = e[i];
                                if (n === r) throw new Error("No value provided for variable " + t);
                                return "function" === typeof n && (n = n(e)), n
                            }))
                        },
                        isArray: Array.isArray || function(t) {
                            return "[object Array]" === Object.prototype.toString.call(t)
                        },
                        emptyImageUrl: "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="
                    },
                    function() {
                        function t(t) {
                            var e, i, n = ["webkit", "moz", "o", "ms"];
                            for (e = 0; e < n.length && !i; e++) i = s[n[e] + t];
                            return i
                        }
                        var e = 0;

                        function i(t) {
                            var i = +new Date,
                                n = Math.max(0, 16 - (i - e));
                            return e = i + n, s.setTimeout(t, n)
                        }
                        var n = s.requestAnimationFrame || t("RequestAnimationFrame") || i,
                            o = s.cancelAnimationFrame || t("CancelAnimationFrame") || t("CancelRequestAnimationFrame") || function(t) {
                                s.clearTimeout(t)
                            };
                        l.Util.requestAnimFrame = function(t, e, o, a) {
                            if (t = l.bind(t, e), !o || n !== i) return n.call(s, t, a);
                            t()
                        }, l.Util.cancelAnimFrame = function(t) {
                            t && o.call(s, t)
                        }
                    }(), l.extend = l.Util.extend, l.bind = l.Util.bind, l.stamp = l.Util.stamp, l.setOptions = l.Util.setOptions, l.Class = function() {}, l.Class.extend = function(t) {
                        var e = function() {
                                this.initialize && this.initialize.apply(this, arguments), this._initHooks && this.callInitHooks()
                            },
                            i = function() {};
                        i.prototype = this.prototype;
                        var n = new i;
                        for (var o in n.constructor = e, e.prototype = n, this) this.hasOwnProperty(o) && "prototype" !== o && (e[o] = this[o]);
                        t.statics && (l.extend(e, t.statics), delete t.statics), t.includes && (l.Util.extend.apply(null, [n].concat(t.includes)), delete t.includes), t.options && n.options && (t.options = l.extend({}, n.options, t.options)), l.extend(n, t), n._initHooks = [];
                        var s = this;
                        return e.__super__ = s.prototype, n.callInitHooks = function() {
                            if (!this._initHooksCalled) {
                                s.prototype.callInitHooks && s.prototype.callInitHooks.call(this), this._initHooksCalled = !0;
                                for (var t = 0, e = n._initHooks.length; t < e; t++) n._initHooks[t].call(this)
                            }
                        }, e
                    }, l.Class.include = function(t) {
                        l.extend(this.prototype, t)
                    }, l.Class.mergeOptions = function(t) {
                        l.extend(this.prototype.options, t)
                    }, l.Class.addInitHook = function(t) {
                        var e = Array.prototype.slice.call(arguments, 1),
                            i = "function" === typeof t ? t : function() {
                                this[t].apply(this, e)
                            };
                        this.prototype._initHooks = this.prototype._initHooks || [], this.prototype._initHooks.push(i)
                    };
                var u = "_leaflet_events";
                l.Mixin = {}, l.Mixin.Events = {
                        addEventListener: function(t, e, i) {
                            if (l.Util.invokeEach(t, this.addEventListener, this, e, i)) return this;
                            var n, o, s, a, r, h, c, p = this[u] = this[u] || {},
                                d = i && i !== this && l.stamp(i);
                            for (t = l.Util.splitWords(t), n = 0, o = t.length; n < o; n++) s = {
                                action: e,
                                context: i || this
                            }, a = t[n], d ? (r = a + "_idx", h = r + "_len", c = p[r] = p[r] || {}, c[d] || (c[d] = [], p[h] = (p[h] || 0) + 1), c[d].push(s)) : (p[a] = p[a] || [], p[a].push(s));
                            return this
                        },
                        hasEventListeners: function(t) {
                            var e = this[u];
                            return !!e && (t in e && e[t].length > 0 || t + "_idx" in e && e[t + "_idx_len"] > 0)
                        },
                        removeEventListener: function(t, e, i) {
                            if (!this[u]) return this;
                            if (!t) return this.clearAllEventListeners();
                            if (l.Util.invokeEach(t, this.removeEventListener, this, e, i)) return this;
                            var n, o, s, a, r, h, c, p, d, _ = this[u],
                                m = i && i !== this && l.stamp(i);
                            for (t = l.Util.splitWords(t), n = 0, o = t.length; n < o; n++)
                                if (s = t[n], h = s + "_idx", c = h + "_len", p = _[h], e) {
                                    if (a = m && p ? p[m] : _[s], a) {
                                        for (r = a.length - 1; r >= 0; r--) a[r].action !== e || i && a[r].context !== i || (d = a.splice(r, 1), d[0].action = l.Util.falseFn);
                                        i && p && 0 === a.length && (delete p[m], _[c]--)
                                    }
                                } else delete _[s], delete _[h], delete _[c];
                            return this
                        },
                        clearAllEventListeners: function() {
                            return delete this[u], this
                        },
                        fireEvent: function(t, e) {
                            if (!this.hasEventListeners(t)) return this;
                            var i, n, o, s, a, r = l.Util.extend({}, e, {
                                    type: t,
                                    target: this
                                }),
                                h = this[u];
                            if (h[t])
                                for (i = h[t].slice(), n = 0, o = i.length; n < o; n++) i[n].action.call(i[n].context, r);
                            for (a in s = h[t + "_idx"], s)
                                if (i = s[a].slice(), i)
                                    for (n = 0, o = i.length; n < o; n++) i[n].action.call(i[n].context, r);
                            return this
                        },
                        addOneTimeEventListener: function(t, e, i) {
                            if (l.Util.invokeEach(t, this.addOneTimeEventListener, this, e, i)) return this;
                            var n = l.bind((function() {
                                this.removeEventListener(t, e, i).removeEventListener(t, n, i)
                            }), this);
                            return this.addEventListener(t, e, i).addEventListener(t, n, i)
                        }
                    }, l.Mixin.Events.on = l.Mixin.Events.addEventListener, l.Mixin.Events.off = l.Mixin.Events.removeEventListener, l.Mixin.Events.once = l.Mixin.Events.addOneTimeEventListener, l.Mixin.Events.fire = l.Mixin.Events.fireEvent,
                    function() {
                        var t = "ActiveXObject" in s,
                            e = t && !a.addEventListener,
                            i = navigator.userAgent.toLowerCase(),
                            n = -1 !== i.indexOf("webkit"),
                            o = -1 !== i.indexOf("chrome"),
                            h = -1 !== i.indexOf("phantom"),
                            u = -1 !== i.indexOf("android"),
                            c = -1 !== i.search("android [23]"),
                            p = -1 !== i.indexOf("gecko"),
                            d = typeof orientation !== r + "",
                            _ = !s.PointerEvent && s.MSPointerEvent,
                            m = s.PointerEvent && s.navigator.pointerEnabled || _,
                            f = "devicePixelRatio" in s && s.devicePixelRatio > 1 || "matchMedia" in s && s.matchMedia("(min-resolution:144dpi)") && s.matchMedia("(min-resolution:144dpi)").matches,
                            g = a.documentElement,
                            v = t && "transition" in g.style,
                            y = "WebKitCSSMatrix" in s && "m11" in new s.WebKitCSSMatrix && !c,
                            P = "MozPerspective" in g.style,
                            L = "OTransition" in g.style,
                            x = !s.L_DISABLE_3D && (v || y || P || L) && !h,
                            w = !s.L_NO_TOUCH && !h && (m || "ontouchstart" in s || s.DocumentTouch && a instanceof s.DocumentTouch);
                        l.Browser = {
                            ie: t,
                            ielt9: e,
                            webkit: n,
                            gecko: p && !n && !s.opera && !t,
                            android: u,
                            android23: c,
                            chrome: o,
                            ie3d: v,
                            webkit3d: y,
                            gecko3d: P,
                            opera3d: L,
                            any3d: x,
                            mobile: d,
                            mobileWebkit: d && n,
                            mobileWebkit3d: d && y,
                            mobileOpera: d && s.opera,
                            touch: w,
                            msPointer: _,
                            pointer: m,
                            retina: f
                        }
                    }(), l.Point = function(t, e, i) {
                        this.x = i ? Math.round(t) : t, this.y = i ? Math.round(e) : e
                    }, l.Point.prototype = {
                        clone: function() {
                            return new l.Point(this.x, this.y)
                        },
                        add: function(t) {
                            return this.clone()._add(l.point(t))
                        },
                        _add: function(t) {
                            return this.x += t.x, this.y += t.y, this
                        },
                        subtract: function(t) {
                            return this.clone()._subtract(l.point(t))
                        },
                        _subtract: function(t) {
                            return this.x -= t.x, this.y -= t.y, this
                        },
                        divideBy: function(t) {
                            return this.clone()._divideBy(t)
                        },
                        _divideBy: function(t) {
                            return this.x /= t, this.y /= t, this
                        },
                        multiplyBy: function(t) {
                            return this.clone()._multiplyBy(t)
                        },
                        _multiplyBy: function(t) {
                            return this.x *= t, this.y *= t, this
                        },
                        round: function() {
                            return this.clone()._round()
                        },
                        _round: function() {
                            return this.x = Math.round(this.x), this.y = Math.round(this.y), this
                        },
                        floor: function() {
                            return this.clone()._floor()
                        },
                        _floor: function() {
                            return this.x = Math.floor(this.x), this.y = Math.floor(this.y), this
                        },
                        distanceTo: function(t) {
                            t = l.point(t);
                            var e = t.x - this.x,
                                i = t.y - this.y;
                            return Math.sqrt(e * e + i * i)
                        },
                        equals: function(t) {
                            return t = l.point(t), t.x === this.x && t.y === this.y
                        },
                        contains: function(t) {
                            return t = l.point(t), Math.abs(t.x) <= Math.abs(this.x) && Math.abs(t.y) <= Math.abs(this.y)
                        },
                        toString: function() {
                            return "Point(" + l.Util.formatNum(this.x) + ", " + l.Util.formatNum(this.y) + ")"
                        }
                    }, l.point = function(t, e, i) {
                        return t instanceof l.Point ? t : l.Util.isArray(t) ? new l.Point(t[0], t[1]) : t === r || null === t ? t : new l.Point(t, e, i)
                    }, l.Bounds = function(t, e) {
                        if (t)
                            for (var i = e ? [t, e] : t, n = 0, o = i.length; n < o; n++) this.extend(i[n])
                    }, l.Bounds.prototype = {
                        extend: function(t) {
                            return t = l.point(t), this.min || this.max ? (this.min.x = Math.min(t.x, this.min.x), this.max.x = Math.max(t.x, this.max.x), this.min.y = Math.min(t.y, this.min.y), this.max.y = Math.max(t.y, this.max.y)) : (this.min = t.clone(), this.max = t.clone()), this
                        },
                        getCenter: function(t) {
                            return new l.Point((this.min.x + this.max.x) / 2, (this.min.y + this.max.y) / 2, t)
                        },
                        getBottomLeft: function() {
                            return new l.Point(this.min.x, this.max.y)
                        },
                        getTopRight: function() {
                            return new l.Point(this.max.x, this.min.y)
                        },
                        getSize: function() {
                            return this.max.subtract(this.min)
                        },
                        contains: function(t) {
                            var e, i;
                            return t = "number" === typeof t[0] || t instanceof l.Point ? l.point(t) : l.bounds(t), t instanceof l.Bounds ? (e = t.min, i = t.max) : e = i = t, e.x >= this.min.x && i.x <= this.max.x && e.y >= this.min.y && i.y <= this.max.y
                        },
                        intersects: function(t) {
                            t = l.bounds(t);
                            var e = this.min,
                                i = this.max,
                                n = t.min,
                                o = t.max,
                                s = o.x >= e.x && n.x <= i.x,
                                a = o.y >= e.y && n.y <= i.y;
                            return s && a
                        },
                        isValid: function() {
                            return !(!this.min || !this.max)
                        }
                    }, l.bounds = function(t, e) {
                        return !t || t instanceof l.Bounds ? t : new l.Bounds(t, e)
                    }, l.Transformation = function(t, e, i, n) {
                        this._a = t, this._b = e, this._c = i, this._d = n
                    }, l.Transformation.prototype = {
                        transform: function(t, e) {
                            return this._transform(t.clone(), e)
                        },
                        _transform: function(t, e) {
                            return e = e || 1, t.x = e * (this._a * t.x + this._b), t.y = e * (this._c * t.y + this._d), t
                        },
                        untransform: function(t, e) {
                            return e = e || 1, new l.Point((t.x / e - this._b) / this._a, (t.y / e - this._d) / this._c)
                        }
                    }, l.DomUtil = {
                        get: function(t) {
                            return "string" === typeof t ? a.getElementById(t) : t
                        },
                        getStyle: function(t, e) {
                            var i = t.style[e];
                            if (!i && t.currentStyle && (i = t.currentStyle[e]), (!i || "auto" === i) && a.defaultView) {
                                var n = a.defaultView.getComputedStyle(t, null);
                                i = n ? n[e] : null
                            }
                            return "auto" === i ? null : i
                        },
                        getViewportOffset: function(t) {
                            var e, i = 0,
                                n = 0,
                                o = t,
                                s = a.body,
                                r = a.documentElement;
                            do {
                                if (i += o.offsetTop || 0, n += o.offsetLeft || 0, i += parseInt(l.DomUtil.getStyle(o, "borderTopWidth"), 10) || 0, n += parseInt(l.DomUtil.getStyle(o, "borderLeftWidth"), 10) || 0, e = l.DomUtil.getStyle(o, "position"), o.offsetParent === s && "absolute" === e) break;
                                if ("fixed" === e) {
                                    i += s.scrollTop || r.scrollTop || 0, n += s.scrollLeft || r.scrollLeft || 0;
                                    break
                                }
                                if ("relative" === e && !o.offsetLeft) {
                                    var h = l.DomUtil.getStyle(o, "width"),
                                        u = l.DomUtil.getStyle(o, "max-width"),
                                        c = o.getBoundingClientRect();
                                    "none" === h && "none" === u || (n += c.left + o.clientLeft), i += c.top + (s.scrollTop || r.scrollTop || 0);
                                    break
                                }
                                o = o.offsetParent
                            } while (o);
                            o = t;
                            do {
                                if (o === s) break;
                                i -= o.scrollTop || 0, n -= o.scrollLeft || 0, o = o.parentNode
                            } while (o);
                            return new l.Point(n, i)
                        },
                        documentIsLtr: function() {
                            return l.DomUtil._docIsLtrCached || (l.DomUtil._docIsLtrCached = !0, l.DomUtil._docIsLtr = "ltr" === l.DomUtil.getStyle(a.body, "direction")), l.DomUtil._docIsLtr
                        },
                        create: function(t, e, i) {
                            var n = a.createElement(t);
                            return n.className = e, i && i.appendChild(n), n
                        },
                        hasClass: function(t, e) {
                            if (t.classList !== r) return t.classList.contains(e);
                            var i = l.DomUtil._getClass(t);
                            return i.length > 0 && new RegExp("(^|\\s)" + e + "(\\s|$)").test(i)
                        },
                        addClass: function(t, e) {
                            if (t.classList !== r)
                                for (var i = l.Util.splitWords(e), n = 0, o = i.length; n < o; n++) t.classList.add(i[n]);
                            else if (!l.DomUtil.hasClass(t, e)) {
                                var s = l.DomUtil._getClass(t);
                                l.DomUtil._setClass(t, (s ? s + " " : "") + e)
                            }
                        },
                        removeClass: function(t, e) {
                            t.classList !== r ? t.classList.remove(e) : l.DomUtil._setClass(t, l.Util.trim((" " + l.DomUtil._getClass(t) + " ").replace(" " + e + " ", " ")))
                        },
                        _setClass: function(t, e) {
                            t.className.baseVal === r ? t.className = e : t.className.baseVal = e
                        },
                        _getClass: function(t) {
                            return t.className.baseVal === r ? t.className : t.className.baseVal
                        },
                        setOpacity: function(t, e) {
                            if ("opacity" in t.style) t.style.opacity = e;
                            else if ("filter" in t.style) {
                                var i = !1,
                                    n = "DXImageTransform.Microsoft.Alpha";
                                try {
                                    i = t.filters.item(n)
                                } catch (o) {
                                    if (1 === e) return
                                }
                                e = Math.round(100 * e), i ? (i.Enabled = 100 !== e, i.Opacity = e) : t.style.filter += " progid:" + n + "(opacity=" + e + ")"
                            }
                        },
                        testProp: function(t) {
                            for (var e = a.documentElement.style, i = 0; i < t.length; i++)
                                if (t[i] in e) return t[i];
                            return !1
                        },
                        getTranslateString: function(t) {
                            var e = l.Browser.webkit3d,
                                i = "translate" + (e ? "3d" : "") + "(",
                                n = (e ? ",0" : "") + ")";
                            return i + t.x + "px," + t.y + "px" + n
                        },
                        getScaleString: function(t, e) {
                            var i = l.DomUtil.getTranslateString(e.add(e.multiplyBy(-1 * t))),
                                n = " scale(" + t + ") ";
                            return i + n
                        },
                        setPosition: function(t, e, i) {
                            t._leaflet_pos = e, !i && l.Browser.any3d ? t.style[l.DomUtil.TRANSFORM] = l.DomUtil.getTranslateString(e) : (t.style.left = e.x + "px", t.style.top = e.y + "px")
                        },
                        getPosition: function(t) {
                            return t._leaflet_pos
                        }
                    }, l.DomUtil.TRANSFORM = l.DomUtil.testProp(["transform", "WebkitTransform", "OTransform", "MozTransform", "msTransform"]), l.DomUtil.TRANSITION = l.DomUtil.testProp(["webkitTransition", "transition", "OTransition", "MozTransition", "msTransition"]), l.DomUtil.TRANSITION_END = "webkitTransition" === l.DomUtil.TRANSITION || "OTransition" === l.DomUtil.TRANSITION ? l.DomUtil.TRANSITION + "End" : "transitionend",
                    function() {
                        if ("onselectstart" in a) l.extend(l.DomUtil, {
                            disableTextSelection: function() {
                                l.DomEvent.on(s, "selectstart", l.DomEvent.preventDefault)
                            },
                            enableTextSelection: function() {
                                l.DomEvent.off(s, "selectstart", l.DomEvent.preventDefault)
                            }
                        });
                        else {
                            var t = l.DomUtil.testProp(["userSelect", "WebkitUserSelect", "OUserSelect", "MozUserSelect", "msUserSelect"]);
                            l.extend(l.DomUtil, {
                                disableTextSelection: function() {
                                    if (t) {
                                        var e = a.documentElement.style;
                                        this._userSelect = e[t], e[t] = "none"
                                    }
                                },
                                enableTextSelection: function() {
                                    t && (a.documentElement.style[t] = this._userSelect, delete this._userSelect)
                                }
                            })
                        }
                        l.extend(l.DomUtil, {
                            disableImageDrag: function() {
                                l.DomEvent.on(s, "dragstart", l.DomEvent.preventDefault)
                            },
                            enableImageDrag: function() {
                                l.DomEvent.off(s, "dragstart", l.DomEvent.preventDefault)
                            }
                        })
                    }(), l.LatLng = function(t, e, i) {
                        if (t = parseFloat(t), e = parseFloat(e), isNaN(t) || isNaN(e)) throw new Error("Invalid LatLng object: (" + t + ", " + e + ")");
                        this.lat = t, this.lng = e, i !== r && (this.alt = parseFloat(i))
                    }, l.extend(l.LatLng, {
                        DEG_TO_RAD: Math.PI / 180,
                        RAD_TO_DEG: 180 / Math.PI,
                        MAX_MARGIN: 1e-9
                    }), l.LatLng.prototype = {
                        equals: function(t) {
                            if (!t) return !1;
                            t = l.latLng(t);
                            var e = Math.max(Math.abs(this.lat - t.lat), Math.abs(this.lng - t.lng));
                            return e <= l.LatLng.MAX_MARGIN
                        },
                        toString: function(t) {
                            return "LatLng(" + l.Util.formatNum(this.lat, t) + ", " + l.Util.formatNum(this.lng, t) + ")"
                        },
                        distanceTo: function(t) {
                            t = l.latLng(t);
                            var e = 6378137,
                                i = l.LatLng.DEG_TO_RAD,
                                n = (t.lat - this.lat) * i,
                                o = (t.lng - this.lng) * i,
                                s = this.lat * i,
                                a = t.lat * i,
                                r = Math.sin(n / 2),
                                h = Math.sin(o / 2),
                                u = r * r + h * h * Math.cos(s) * Math.cos(a);
                            return 2 * e * Math.atan2(Math.sqrt(u), Math.sqrt(1 - u))
                        },
                        wrap: function(t, e) {
                            var i = this.lng;
                            return t = t || -180, e = e || 180, i = (i + e) % (e - t) + (i < t || i === e ? e : t), new l.LatLng(this.lat, i)
                        }
                    }, l.latLng = function(t, e) {
                        return t instanceof l.LatLng ? t : l.Util.isArray(t) ? "number" === typeof t[0] || "string" === typeof t[0] ? new l.LatLng(t[0], t[1], t[2]) : null : t === r || null === t ? t : "object" === typeof t && "lat" in t ? new l.LatLng(t.lat, "lng" in t ? t.lng : t.lon) : e === r ? null : new l.LatLng(t, e)
                    }, l.LatLngBounds = function(t, e) {
                        if (t)
                            for (var i = e ? [t, e] : t, n = 0, o = i.length; n < o; n++) this.extend(i[n])
                    }, l.LatLngBounds.prototype = {
                        extend: function(t) {
                            if (!t) return this;
                            var e = l.latLng(t);
                            return t = null !== e ? e : l.latLngBounds(t), t instanceof l.LatLng ? this._southWest || this._northEast ? (this._southWest.lat = Math.min(t.lat, this._southWest.lat), this._southWest.lng = Math.min(t.lng, this._southWest.lng), this._northEast.lat = Math.max(t.lat, this._northEast.lat), this._northEast.lng = Math.max(t.lng, this._northEast.lng)) : (this._southWest = new l.LatLng(t.lat, t.lng), this._northEast = new l.LatLng(t.lat, t.lng)) : t instanceof l.LatLngBounds && (this.extend(t._southWest), this.extend(t._northEast)), this
                        },
                        pad: function(t) {
                            var e = this._southWest,
                                i = this._northEast,
                                n = Math.abs(e.lat - i.lat) * t,
                                o = Math.abs(e.lng - i.lng) * t;
                            return new l.LatLngBounds(new l.LatLng(e.lat - n, e.lng - o), new l.LatLng(i.lat + n, i.lng + o))
                        },
                        getCenter: function() {
                            return new l.LatLng((this._southWest.lat + this._northEast.lat) / 2, (this._southWest.lng + this._northEast.lng) / 2)
                        },
                        getSouthWest: function() {
                            return this._southWest
                        },
                        getNorthEast: function() {
                            return this._northEast
                        },
                        getNorthWest: function() {
                            return new l.LatLng(this.getNorth(), this.getWest())
                        },
                        getSouthEast: function() {
                            return new l.LatLng(this.getSouth(), this.getEast())
                        },
                        getWest: function() {
                            return this._southWest.lng
                        },
                        getSouth: function() {
                            return this._southWest.lat
                        },
                        getEast: function() {
                            return this._northEast.lng
                        },
                        getNorth: function() {
                            return this._northEast.lat
                        },
                        contains: function(t) {
                            t = "number" === typeof t[0] || t instanceof l.LatLng ? l.latLng(t) : l.latLngBounds(t);
                            var e, i, n = this._southWest,
                                o = this._northEast;
                            return t instanceof l.LatLngBounds ? (e = t.getSouthWest(), i = t.getNorthEast()) : e = i = t, e.lat >= n.lat && i.lat <= o.lat && e.lng >= n.lng && i.lng <= o.lng
                        },
                        intersects: function(t) {
                            t = l.latLngBounds(t);
                            var e = this._southWest,
                                i = this._northEast,
                                n = t.getSouthWest(),
                                o = t.getNorthEast(),
                                s = o.lat >= e.lat && n.lat <= i.lat,
                                a = o.lng >= e.lng && n.lng <= i.lng;
                            return s && a
                        },
                        toBBoxString: function() {
                            return [this.getWest(), this.getSouth(), this.getEast(), this.getNorth()].join(",")
                        },
                        equals: function(t) {
                            return !!t && (t = l.latLngBounds(t), this._southWest.equals(t.getSouthWest()) && this._northEast.equals(t.getNorthEast()))
                        },
                        isValid: function() {
                            return !(!this._southWest || !this._northEast)
                        }
                    }, l.latLngBounds = function(t, e) {
                        return !t || t instanceof l.LatLngBounds ? t : new l.LatLngBounds(t, e)
                    }, l.Projection = {}, l.Projection.SphericalMercator = {
                        MAX_LATITUDE: 85.0511287798,
                        project: function(t) {
                            var e = l.LatLng.DEG_TO_RAD,
                                i = this.MAX_LATITUDE,
                                n = Math.max(Math.min(i, t.lat), -i),
                                o = t.lng * e,
                                s = n * e;
                            return s = Math.log(Math.tan(Math.PI / 4 + s / 2)), new l.Point(o, s)
                        },
                        unproject: function(t) {
                            var e = l.LatLng.RAD_TO_DEG,
                                i = t.x * e,
                                n = (2 * Math.atan(Math.exp(t.y)) - Math.PI / 2) * e;
                            return new l.LatLng(n, i)
                        }
                    }, l.Projection.LonLat = {
                        project: function(t) {
                            return new l.Point(t.lng, t.lat)
                        },
                        unproject: function(t) {
                            return new l.LatLng(t.y, t.x)
                        }
                    }, l.CRS = {
                        latLngToPoint: function(t, e) {
                            var i = this.projection.project(t),
                                n = this.scale(e);
                            return this.transformation._transform(i, n)
                        },
                        pointToLatLng: function(t, e) {
                            var i = this.scale(e),
                                n = this.transformation.untransform(t, i);
                            return this.projection.unproject(n)
                        },
                        project: function(t) {
                            return this.projection.project(t)
                        },
                        scale: function(t) {
                            return 256 * Math.pow(2, t)
                        },
                        getSize: function(t) {
                            var e = this.scale(t);
                            return l.point(e, e)
                        }
                    }, l.CRS.Simple = l.extend({}, l.CRS, {
                        projection: l.Projection.LonLat,
                        transformation: new l.Transformation(1, 0, -1, 0),
                        scale: function(t) {
                            return Math.pow(2, t)
                        }
                    }), l.CRS.EPSG3857 = l.extend({}, l.CRS, {
                        code: "EPSG:3857",
                        projection: l.Projection.SphericalMercator,
                        transformation: new l.Transformation(.5 / Math.PI, .5, -.5 / Math.PI, .5),
                        project: function(t) {
                            var e = this.projection.project(t),
                                i = 6378137;
                            return e.multiplyBy(i)
                        }
                    }), l.CRS.EPSG900913 = l.extend({}, l.CRS.EPSG3857, {
                        code: "EPSG:900913"
                    }), l.CRS.EPSG4326 = l.extend({}, l.CRS, {
                        code: "EPSG:4326",
                        projection: l.Projection.LonLat,
                        transformation: new l.Transformation(1 / 360, .5, -1 / 360, .5)
                    }), l.Map = l.Class.extend({
                        includes: l.Mixin.Events,
                        options: {
                            crs: l.CRS.EPSG3857,
                            fadeAnimation: l.DomUtil.TRANSITION && !l.Browser.android23,
                            trackResize: !0,
                            markerZoomAnimation: l.DomUtil.TRANSITION && l.Browser.any3d
                        },
                        initialize: function(t, e) {
                            e = l.setOptions(this, e), this._initContainer(t), this._initLayout(), this._onResize = l.bind(this._onResize, this), this._initEvents(), e.maxBounds && this.setMaxBounds(e.maxBounds), e.center && e.zoom !== r && this.setView(l.latLng(e.center), e.zoom, {
                                reset: !0
                            }), this._handlers = [], this._layers = {}, this._zoomBoundLayers = {}, this._tileLayersNum = 0, this.callInitHooks(), this._addLayers(e.layers)
                        },
                        setView: function(t, e) {
                            return e = e === r ? this.getZoom() : e, this._resetView(l.latLng(t), this._limitZoom(e)), this
                        },
                        setZoom: function(t, e) {
                            return this._loaded ? this.setView(this.getCenter(), t, {
                                zoom: e
                            }) : (this._zoom = this._limitZoom(t), this)
                        },
                        zoomIn: function(t, e) {
                            return this.setZoom(this._zoom + (t || 1), e)
                        },
                        zoomOut: function(t, e) {
                            return this.setZoom(this._zoom - (t || 1), e)
                        },
                        setZoomAround: function(t, e, i) {
                            var n = this.getZoomScale(e),
                                o = this.getSize().divideBy(2),
                                s = t instanceof l.Point ? t : this.latLngToContainerPoint(t),
                                a = s.subtract(o).multiplyBy(1 - 1 / n),
                                r = this.containerPointToLatLng(o.add(a));
                            return this.setView(r, e, {
                                zoom: i
                            })
                        },
                        fitBounds: function(t, e) {
                            e = e || {}, t = t.getBounds ? t.getBounds() : l.latLngBounds(t);
                            var i = l.point(e.paddingTopLeft || e.padding || [0, 0]),
                                n = l.point(e.paddingBottomRight || e.padding || [0, 0]),
                                o = this.getBoundsZoom(t, !1, i.add(n));
                            o = e.maxZoom ? Math.min(e.maxZoom, o) : o;
                            var s = n.subtract(i).divideBy(2),
                                a = this.project(t.getSouthWest(), o),
                                r = this.project(t.getNorthEast(), o),
                                h = this.unproject(a.add(r).divideBy(2).add(s), o);
                            return this.setView(h, o, e)
                        },
                        fitWorld: function(t) {
                            return this.fitBounds([
                                [-90, -180],
                                [90, 180]
                            ], t)
                        },
                        panTo: function(t, e) {
                            return this.setView(t, this._zoom, {
                                pan: e
                            })
                        },
                        panBy: function(t) {
                            return this.fire("movestart"), this._rawPanBy(l.point(t)), this.fire("move"), this.fire("moveend")
                        },
                        setMaxBounds: function(t) {
                            return t = l.latLngBounds(t), this.options.maxBounds = t, t ? (this._loaded && this._panInsideMaxBounds(), this.on("moveend", this._panInsideMaxBounds, this)) : this.off("moveend", this._panInsideMaxBounds, this)
                        },
                        panInsideBounds: function(t, e) {
                            var i = this.getCenter(),
                                n = this._limitCenter(i, this._zoom, t);
                            return i.equals(n) ? this : this.panTo(n, e)
                        },
                        addLayer: function(t) {
                            var e = l.stamp(t);
                            return this._layers[e] ? this : (this._layers[e] = t, !t.options || isNaN(t.options.maxZoom) && isNaN(t.options.minZoom) || (this._zoomBoundLayers[e] = t, this._updateZoomLevels()), this.options.zoomAnimation && l.TileLayer && t instanceof l.TileLayer && (this._tileLayersNum++, this._tileLayersToLoad++, t.on("load", this._onTileLayerLoad, this)), this._loaded && this._layerAdd(t), this)
                        },
                        removeLayer: function(t) {
                            var e = l.stamp(t);
                            return this._layers[e] ? (this._loaded && t.onRemove(this), delete this._layers[e], this._loaded && this.fire("layerremove", {
                                layer: t
                            }), this._zoomBoundLayers[e] && (delete this._zoomBoundLayers[e], this._updateZoomLevels()), this.options.zoomAnimation && l.TileLayer && t instanceof l.TileLayer && (this._tileLayersNum--, this._tileLayersToLoad--, t.off("load", this._onTileLayerLoad, this)), this) : this
                        },
                        hasLayer: function(t) {
                            return !!t && l.stamp(t) in this._layers
                        },
                        eachLayer: function(t, e) {
                            for (var i in this._layers) t.call(e, this._layers[i]);
                            return this
                        },
                        invalidateSize: function(t) {
                            if (!this._loaded) return this;
                            t = l.extend({
                                animate: !1,
                                pan: !0
                            }, !0 === t ? {
                                animate: !0
                            } : t);
                            var e = this.getSize();
                            this._sizeChanged = !0, this._initialCenter = null;
                            var i = this.getSize(),
                                n = e.divideBy(2).round(),
                                o = i.divideBy(2).round(),
                                s = n.subtract(o);
                            return s.x || s.y ? (t.animate && t.pan ? this.panBy(s) : (t.pan && this._rawPanBy(s), this.fire("move"), t.debounceMoveend ? (clearTimeout(this._sizeTimer), this._sizeTimer = setTimeout(l.bind(this.fire, this, "moveend"), 200)) : this.fire("moveend")), this.fire("resize", {
                                oldSize: e,
                                newSize: i
                            })) : this
                        },
                        addHandler: function(t, e) {
                            if (!e) return this;
                            var i = this[t] = new e(this);
                            return this._handlers.push(i), this.options[t] && i.enable(), this
                        },
                        remove: function() {
                            this._loaded && this.fire("unload"), this._initEvents("off");
                            try {
                                delete this._container._leaflet
                            } catch (t) {
                                this._container._leaflet = r
                            }
                            return this._clearPanes(), this._clearControlPos && this._clearControlPos(), this._clearHandlers(), this
                        },
                        getCenter: function() {
                            return this._checkIfLoaded(), this._initialCenter && !this._moved() ? this._initialCenter : this.layerPointToLatLng(this._getCenterLayerPoint())
                        },
                        getZoom: function() {
                            return this._zoom
                        },
                        getBounds: function() {
                            var t = this.getPixelBounds(),
                                e = this.unproject(t.getBottomLeft()),
                                i = this.unproject(t.getTopRight());
                            return new l.LatLngBounds(e, i)
                        },
                        getMinZoom: function() {
                            return this.options.minZoom === r ? this._layersMinZoom === r ? 0 : this._layersMinZoom : this.options.minZoom
                        },
                        getMaxZoom: function() {
                            return this.options.maxZoom === r ? this._layersMaxZoom === r ? 1 / 0 : this._layersMaxZoom : this.options.maxZoom
                        },
                        getBoundsZoom: function(t, e, i) {
                            t = l.latLngBounds(t);
                            var n, o = this.getMinZoom() - (e ? 1 : 0),
                                s = this.getMaxZoom(),
                                a = this.getSize(),
                                r = t.getNorthWest(),
                                h = t.getSouthEast(),
                                u = !0;
                            i = l.point(i || [0, 0]);
                            do {
                                o++, n = this.project(h, o).subtract(this.project(r, o)).add(i), u = e ? n.x < a.x || n.y < a.y : a.contains(n)
                            } while (u && o <= s);
                            return u && e ? null : e ? o : o - 1
                        },
                        getSize: function() {
                            return this._size && !this._sizeChanged || (this._size = new l.Point(this._container.clientWidth, this._container.clientHeight), this._sizeChanged = !1), this._size.clone()
                        },
                        getPixelBounds: function() {
                            var t = this._getTopLeftPoint();
                            return new l.Bounds(t, t.add(this.getSize()))
                        },
                        getPixelOrigin: function() {
                            return this._checkIfLoaded(), this._initialTopLeftPoint
                        },
                        getPanes: function() {
                            return this._panes
                        },
                        getContainer: function() {
                            return this._container
                        },
                        getZoomScale: function(t) {
                            var e = this.options.crs;
                            return e.scale(t) / e.scale(this._zoom)
                        },
                        getScaleZoom: function(t) {
                            return this._zoom + Math.log(t) / Math.LN2
                        },
                        project: function(t, e) {
                            return e = e === r ? this._zoom : e, this.options.crs.latLngToPoint(l.latLng(t), e)
                        },
                        unproject: function(t, e) {
                            return e = e === r ? this._zoom : e, this.options.crs.pointToLatLng(l.point(t), e)
                        },
                        layerPointToLatLng: function(t) {
                            var e = l.point(t).add(this.getPixelOrigin());
                            return this.unproject(e)
                        },
                        latLngToLayerPoint: function(t) {
                            var e = this.project(l.latLng(t))._round();
                            return e._subtract(this.getPixelOrigin())
                        },
                        containerPointToLayerPoint: function(t) {
                            return l.point(t).subtract(this._getMapPanePos())
                        },
                        layerPointToContainerPoint: function(t) {
                            return l.point(t).add(this._getMapPanePos())
                        },
                        containerPointToLatLng: function(t) {
                            var e = this.containerPointToLayerPoint(l.point(t));
                            return this.layerPointToLatLng(e)
                        },
                        latLngToContainerPoint: function(t) {
                            return this.layerPointToContainerPoint(this.latLngToLayerPoint(l.latLng(t)))
                        },
                        mouseEventToContainerPoint: function(t) {
                            return l.DomEvent.getMousePosition(t, this._container)
                        },
                        mouseEventToLayerPoint: function(t) {
                            return this.containerPointToLayerPoint(this.mouseEventToContainerPoint(t))
                        },
                        mouseEventToLatLng: function(t) {
                            return this.layerPointToLatLng(this.mouseEventToLayerPoint(t))
                        },
                        _initContainer: function(t) {
                            var e = this._container = l.DomUtil.get(t);
                            if (!e) throw new Error("Map container not found.");
                            if (e._leaflet) throw new Error("Map container is already initialized.");
                            e._leaflet = !0
                        },
                        _initLayout: function() {
                            var t = this._container;
                            l.DomUtil.addClass(t, "leaflet-container" + (l.Browser.touch ? " leaflet-touch" : "") + (l.Browser.retina ? " leaflet-retina" : "") + (l.Browser.ielt9 ? " leaflet-oldie" : "") + (this.options.fadeAnimation ? " leaflet-fade-anim" : ""));
                            var e = l.DomUtil.getStyle(t, "position");
                            "absolute" !== e && "relative" !== e && "fixed" !== e && (t.style.position = "relative"), this._initPanes(), this._initControlPos && this._initControlPos()
                        },
                        _initPanes: function() {
                            var t = this._panes = {};
                            this._mapPane = t.mapPane = this._createPane("leaflet-map-pane", this._container), this._tilePane = t.tilePane = this._createPane("leaflet-tile-pane", this._mapPane), t.objectsPane = this._createPane("leaflet-objects-pane", this._mapPane), t.shadowPane = this._createPane("leaflet-shadow-pane"), t.overlayPane = this._createPane("leaflet-overlay-pane"), t.markerPane = this._createPane("leaflet-marker-pane"), t.popupPane = this._createPane("leaflet-popup-pane");
                            var e = " leaflet-zoom-hide";
                            this.options.markerZoomAnimation || (l.DomUtil.addClass(t.markerPane, e), l.DomUtil.addClass(t.shadowPane, e), l.DomUtil.addClass(t.popupPane, e))
                        },
                        _createPane: function(t, e) {
                            return l.DomUtil.create("div", t, e || this._panes.objectsPane)
                        },
                        _clearPanes: function() {
                            this._container.removeChild(this._mapPane)
                        },
                        _addLayers: function(t) {
                            t = t ? l.Util.isArray(t) ? t : [t] : [];
                            for (var e = 0, i = t.length; e < i; e++) this.addLayer(t[e])
                        },
                        _resetView: function(t, e, i, n) {
                            var o = this._zoom !== e;
                            n || (this.fire("movestart"), o && this.fire("zoomstart")), this._zoom = e, this._initialCenter = t, this._initialTopLeftPoint = this._getNewTopLeftPoint(t), i ? this._initialTopLeftPoint._add(this._getMapPanePos()) : l.DomUtil.setPosition(this._mapPane, new l.Point(0, 0)), this._tileLayersToLoad = this._tileLayersNum;
                            var s = !this._loaded;
                            this._loaded = !0, this.fire("viewreset", {
                                hard: !i
                            }), s && (this.fire("load"), this.eachLayer(this._layerAdd, this)), this.fire("move"), (o || n) && this.fire("zoomend"), this.fire("moveend", {
                                hard: !i
                            })
                        },
                        _rawPanBy: function(t) {
                            l.DomUtil.setPosition(this._mapPane, this._getMapPanePos().subtract(t))
                        },
                        _getZoomSpan: function() {
                            return this.getMaxZoom() - this.getMinZoom()
                        },
                        _updateZoomLevels: function() {
                            var t, e = 1 / 0,
                                i = -1 / 0,
                                n = this._getZoomSpan();
                            for (t in this._zoomBoundLayers) {
                                var o = this._zoomBoundLayers[t];
                                isNaN(o.options.minZoom) || (e = Math.min(e, o.options.minZoom)), isNaN(o.options.maxZoom) || (i = Math.max(i, o.options.maxZoom))
                            }
                            t === r ? this._layersMaxZoom = this._layersMinZoom = r : (this._layersMaxZoom = i, this._layersMinZoom = e), n !== this._getZoomSpan() && this.fire("zoomlevelschange")
                        },
                        _panInsideMaxBounds: function() {
                            this.panInsideBounds(this.options.maxBounds)
                        },
                        _checkIfLoaded: function() {
                            if (!this._loaded) throw new Error("Set map center and zoom first.")
                        },
                        _initEvents: function(t) {
                            if (l.DomEvent) {
                                t = t || "on", l.DomEvent[t](this._container, "click", this._onMouseClick, this);
                                var e, i, n = ["dblclick", "mousedown", "mouseup", "mouseenter", "mouseleave", "mousemove", "contextmenu"];
                                for (e = 0, i = n.length; e < i; e++) l.DomEvent[t](this._container, n[e], this._fireMouseEvent, this);
                                this.options.trackResize && l.DomEvent[t](s, "resize", this._onResize, this)
                            }
                        },
                        _onResize: function() {
                            l.Util.cancelAnimFrame(this._resizeRequest), this._resizeRequest = l.Util.requestAnimFrame((function() {
                                this.invalidateSize({
                                    debounceMoveend: !0
                                })
                            }), this, !1, this._container)
                        },
                        _onMouseClick: function(t) {
                            !this._loaded || !t._simulated && (this.dragging && this.dragging.moved() || this.boxZoom && this.boxZoom.moved()) || l.DomEvent._skipped(t) || (this.fire("preclick"), this._fireMouseEvent(t))
                        },
                        _fireMouseEvent: function(t) {
                            if (this._loaded && !l.DomEvent._skipped(t)) {
                                var e = t.type;
                                if (e = "mouseenter" === e ? "mouseover" : "mouseleave" === e ? "mouseout" : e, this.hasEventListeners(e)) {
                                    "contextmenu" === e && l.DomEvent.preventDefault(t);
                                    var i = this.mouseEventToContainerPoint(t),
                                        n = this.containerPointToLayerPoint(i),
                                        o = this.layerPointToLatLng(n);
                                    this.fire(e, {
                                        latlng: o,
                                        layerPoint: n,
                                        containerPoint: i,
                                        originalEvent: t
                                    })
                                }
                            }
                        },
                        _onTileLayerLoad: function() {
                            this._tileLayersToLoad--, this._tileLayersNum && !this._tileLayersToLoad && this.fire("tilelayersload")
                        },
                        _clearHandlers: function() {
                            for (var t = 0, e = this._handlers.length; t < e; t++) this._handlers[t].disable()
                        },
                        whenReady: function(t, e) {
                            return this._loaded ? t.call(e || this, this) : this.on("load", t, e), this
                        },
                        _layerAdd: function(t) {
                            t.onAdd(this), this.fire("layeradd", {
                                layer: t
                            })
                        },
                        _getMapPanePos: function() {
                            return l.DomUtil.getPosition(this._mapPane)
                        },
                        _moved: function() {
                            var t = this._getMapPanePos();
                            return t && !t.equals([0, 0])
                        },
                        _getTopLeftPoint: function() {
                            return this.getPixelOrigin().subtract(this._getMapPanePos())
                        },
                        _getNewTopLeftPoint: function(t, e) {
                            var i = this.getSize()._divideBy(2);
                            return this.project(t, e)._subtract(i)._round()
                        },
                        _latLngToNewLayerPoint: function(t, e, i) {
                            var n = this._getNewTopLeftPoint(i, e).add(this._getMapPanePos());
                            return this.project(t, e)._subtract(n)
                        },
                        _getCenterLayerPoint: function() {
                            return this.containerPointToLayerPoint(this.getSize()._divideBy(2))
                        },
                        _getCenterOffset: function(t) {
                            return this.latLngToLayerPoint(t).subtract(this._getCenterLayerPoint())
                        },
                        _limitCenter: function(t, e, i) {
                            if (!i) return t;
                            var n = this.project(t, e),
                                o = this.getSize().divideBy(2),
                                s = new l.Bounds(n.subtract(o), n.add(o)),
                                a = this._getBoundsOffset(s, i, e);
                            return this.unproject(n.add(a), e)
                        },
                        _limitOffset: function(t, e) {
                            if (!e) return t;
                            var i = this.getPixelBounds(),
                                n = new l.Bounds(i.min.add(t), i.max.add(t));
                            return t.add(this._getBoundsOffset(n, e))
                        },
                        _getBoundsOffset: function(t, e, i) {
                            var n = this.project(e.getNorthWest(), i).subtract(t.min),
                                o = this.project(e.getSouthEast(), i).subtract(t.max),
                                s = this._rebound(n.x, -o.x),
                                a = this._rebound(n.y, -o.y);
                            return new l.Point(s, a)
                        },
                        _rebound: function(t, e) {
                            return t + e > 0 ? Math.round(t - e) / 2 : Math.max(0, Math.ceil(t)) - Math.max(0, Math.floor(e))
                        },
                        _limitZoom: function(t) {
                            var e = this.getMinZoom(),
                                i = this.getMaxZoom();
                            return Math.max(e, Math.min(i, t))
                        }
                    }), l.map = function(t, e) {
                        return new l.Map(t, e)
                    }, l.Projection.Mercator = {
                        MAX_LATITUDE: 85.0840591556,
                        R_MINOR: 6356752.314245179,
                        R_MAJOR: 6378137,
                        project: function(t) {
                            var e = l.LatLng.DEG_TO_RAD,
                                i = this.MAX_LATITUDE,
                                n = Math.max(Math.min(i, t.lat), -i),
                                o = this.R_MAJOR,
                                s = this.R_MINOR,
                                a = t.lng * e * o,
                                r = n * e,
                                h = s / o,
                                u = Math.sqrt(1 - h * h),
                                c = u * Math.sin(r);
                            c = Math.pow((1 - c) / (1 + c), .5 * u);
                            var p = Math.tan(.5 * (.5 * Math.PI - r)) / c;
                            return r = -o * Math.log(p), new l.Point(a, r)
                        },
                        unproject: function(t) {
                            var e, i = l.LatLng.RAD_TO_DEG,
                                n = this.R_MAJOR,
                                o = this.R_MINOR,
                                s = t.x * i / n,
                                a = o / n,
                                r = Math.sqrt(1 - a * a),
                                h = Math.exp(-t.y / n),
                                u = Math.PI / 2 - 2 * Math.atan(h),
                                c = 15,
                                p = 1e-7,
                                d = c,
                                _ = .1;
                            while (Math.abs(_) > p && --d > 0) e = r * Math.sin(u), _ = Math.PI / 2 - 2 * Math.atan(h * Math.pow((1 - e) / (1 + e), .5 * r)) - u, u += _;
                            return new l.LatLng(u * i, s)
                        }
                    }, l.CRS.EPSG3395 = l.extend({}, l.CRS, {
                        code: "EPSG:3395",
                        projection: l.Projection.Mercator,
                        transformation: function() {
                            var t = l.Projection.Mercator,
                                e = t.R_MAJOR,
                                i = .5 / (Math.PI * e);
                            return new l.Transformation(i, .5, -i, .5)
                        }()
                    }), l.TileLayer = l.Class.extend({
                        includes: l.Mixin.Events,
                        options: {
                            minZoom: 0,
                            maxZoom: 18,
                            tileSize: 256,
                            subdomains: "abc",
                            errorTileUrl: "",
                            attribution: "",
                            zoomOffset: 0,
                            opacity: 1,
                            unloadInvisibleTiles: l.Browser.mobile,
                            updateWhenIdle: l.Browser.mobile
                        },
                        initialize: function(t, e) {
                            e = l.setOptions(this, e), e.detectRetina && l.Browser.retina && e.maxZoom > 0 && (e.tileSize = Math.floor(e.tileSize / 2), e.zoomOffset++, e.minZoom > 0 && e.minZoom--, this.options.maxZoom--), e.bounds && (e.bounds = l.latLngBounds(e.bounds)), this._url = t;
                            var i = this.options.subdomains;
                            "string" === typeof i && (this.options.subdomains = i.split(""))
                        },
                        onAdd: function(t) {
                            this._map = t, this._animated = t._zoomAnimated, this._initContainer(), t.on({
                                viewreset: this._reset,
                                moveend: this._update
                            }, this), this._animated && t.on({
                                zoomanim: this._animateZoom,
                                zoomend: this._endZoomAnim
                            }, this), this.options.updateWhenIdle || (this._limitedUpdate = l.Util.limitExecByInterval(this._update, 150, this), t.on("move", this._limitedUpdate, this)), this._reset(), this._update()
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        onRemove: function(t) {
                            this._container.parentNode.removeChild(this._container), t.off({
                                viewreset: this._reset,
                                moveend: this._update
                            }, this), this._animated && t.off({
                                zoomanim: this._animateZoom,
                                zoomend: this._endZoomAnim
                            }, this), this.options.updateWhenIdle || t.off("move", this._limitedUpdate, this), this._container = null, this._map = null
                        },
                        bringToFront: function() {
                            var t = this._map._panes.tilePane;
                            return this._container && (t.appendChild(this._container), this._setAutoZIndex(t, Math.max)), this
                        },
                        bringToBack: function() {
                            var t = this._map._panes.tilePane;
                            return this._container && (t.insertBefore(this._container, t.firstChild), this._setAutoZIndex(t, Math.min)), this
                        },
                        getAttribution: function() {
                            return this.options.attribution
                        },
                        getContainer: function() {
                            return this._container
                        },
                        setOpacity: function(t) {
                            return this.options.opacity = t, this._map && this._updateOpacity(), this
                        },
                        setZIndex: function(t) {
                            return this.options.zIndex = t, this._updateZIndex(), this
                        },
                        setUrl: function(t, e) {
                            return this._url = t, e || this.redraw(), this
                        },
                        redraw: function() {
                            return this._map && (this._reset({
                                hard: !0
                            }), this._update()), this
                        },
                        _updateZIndex: function() {
                            this._container && this.options.zIndex !== r && (this._container.style.zIndex = this.options.zIndex)
                        },
                        _setAutoZIndex: function(t, e) {
                            var i, n, o, s = t.children,
                                a = -e(1 / 0, -1 / 0);
                            for (n = 0, o = s.length; n < o; n++) s[n] !== this._container && (i = parseInt(s[n].style.zIndex, 10), isNaN(i) || (a = e(a, i)));
                            this.options.zIndex = this._container.style.zIndex = (isFinite(a) ? a : 0) + e(1, -1)
                        },
                        _updateOpacity: function() {
                            var t, e = this._tiles;
                            if (l.Browser.ielt9)
                                for (t in e) l.DomUtil.setOpacity(e[t], this.options.opacity);
                            else l.DomUtil.setOpacity(this._container, this.options.opacity)
                        },
                        _initContainer: function() {
                            var t = this._map._panes.tilePane;
                            if (!this._container) {
                                if (this._container = l.DomUtil.create("div", "leaflet-layer"), this._updateZIndex(), this._animated) {
                                    var e = "leaflet-tile-container";
                                    this._bgBuffer = l.DomUtil.create("div", e, this._container), this._tileContainer = l.DomUtil.create("div", e, this._container)
                                } else this._tileContainer = this._container;
                                t.appendChild(this._container), this.options.opacity < 1 && this._updateOpacity()
                            }
                        },
                        _reset: function(t) {
                            for (var e in this._tiles) this.fire("tileunload", {
                                tile: this._tiles[e]
                            });
                            this._tiles = {}, this._tilesToLoad = 0, this.options.reuseTiles && (this._unusedTiles = []), this._tileContainer.innerHTML = "", this._animated && t && t.hard && this._clearBgBuffer(), this._initContainer()
                        },
                        _getTileSize: function() {
                            var t = this._map,
                                e = t.getZoom() + this.options.zoomOffset,
                                i = this.options.maxNativeZoom,
                                n = this.options.tileSize;
                            return i && e > i && (n = Math.round(t.getZoomScale(e) / t.getZoomScale(i) * n)), n
                        },
                        _update: function() {
                            if (this._map) {
                                var t = this._map,
                                    e = t.getPixelBounds(),
                                    i = t.getZoom(),
                                    n = this._getTileSize();
                                if (!(i > this.options.maxZoom || i < this.options.minZoom)) {
                                    var o = l.bounds(e.min.divideBy(n)._floor(), e.max.divideBy(n)._floor());
                                    this._addTilesFromCenterOut(o), (this.options.unloadInvisibleTiles || this.options.reuseTiles) && this._removeOtherTiles(o)
                                }
                            }
                        },
                        _addTilesFromCenterOut: function(t) {
                            var e, i, n, o = [],
                                s = t.getCenter();
                            for (e = t.min.y; e <= t.max.y; e++)
                                for (i = t.min.x; i <= t.max.x; i++) n = new l.Point(i, e), this._tileShouldBeLoaded(n) && o.push(n);
                            var r = o.length;
                            if (0 !== r) {
                                o.sort((function(t, e) {
                                    return t.distanceTo(s) - e.distanceTo(s)
                                }));
                                var h = a.createDocumentFragment();
                                for (this._tilesToLoad || this.fire("loading"), this._tilesToLoad += r, i = 0; i < r; i++) this._addTile(o[i], h);
                                this._tileContainer.appendChild(h)
                            }
                        },
                        _tileShouldBeLoaded: function(t) {
                            if (t.x + ":" + t.y in this._tiles) return !1;
                            var e = this.options;
                            if (!e.continuousWorld) {
                                var i = this._getWrapTileNum();
                                if (e.noWrap && (t.x < 0 || t.x >= i.x) || t.y < 0 || t.y >= i.y) return !1
                            }
                            if (e.bounds) {
                                var n = this._getTileSize(),
                                    o = t.multiplyBy(n),
                                    s = o.add([n, n]),
                                    a = this._map.unproject(o),
                                    r = this._map.unproject(s);
                                if (e.continuousWorld || e.noWrap || (a = a.wrap(), r = r.wrap()), !e.bounds.intersects([a, r])) return !1
                            }
                            return !0
                        },
                        _removeOtherTiles: function(t) {
                            var e, i, n, o;
                            for (o in this._tiles) e = o.split(":"), i = parseInt(e[0], 10), n = parseInt(e[1], 10), (i < t.min.x || i > t.max.x || n < t.min.y || n > t.max.y) && this._removeTile(o)
                        },
                        _removeTile: function(t) {
                            var e = this._tiles[t];
                            this.fire("tileunload", {
                                tile: e,
                                url: e.src
                            }), this.options.reuseTiles ? (l.DomUtil.removeClass(e, "leaflet-tile-loaded"), this._unusedTiles.push(e)) : e.parentNode === this._tileContainer && this._tileContainer.removeChild(e), l.Browser.android || (e.onload = null, e.src = l.Util.emptyImageUrl), delete this._tiles[t]
                        },
                        _addTile: function(t, e) {
                            var i = this._getTilePos(t),
                                n = this._getTile();
                            l.DomUtil.setPosition(n, i, l.Browser.chrome), this._tiles[t.x + ":" + t.y] = n, this._loadTile(n, t), n.parentNode !== this._tileContainer && e.appendChild(n)
                        },
                        _getZoomForUrl: function() {
                            var t = this.options,
                                e = this._map.getZoom();
                            return t.zoomReverse && (e = t.maxZoom - e), e += t.zoomOffset, t.maxNativeZoom ? Math.min(e, t.maxNativeZoom) : e
                        },
                        _getTilePos: function(t) {
                            var e = this._map.getPixelOrigin(),
                                i = this._getTileSize();
                            return t.multiplyBy(i).subtract(e)
                        },
                        getTileUrl: function(t) {
                            return l.Util.template(this._url, l.extend({
                                s: this._getSubdomain(t),
                                z: t.z,
                                x: t.x,
                                y: t.y
                            }, this.options))
                        },
                        _getWrapTileNum: function() {
                            var t = this._map.options.crs,
                                e = t.getSize(this._map.getZoom());
                            return e.divideBy(this._getTileSize())._floor()
                        },
                        _adjustTilePoint: function(t) {
                            var e = this._getWrapTileNum();
                            this.options.continuousWorld || this.options.noWrap || (t.x = (t.x % e.x + e.x) % e.x), this.options.tms && (t.y = e.y - t.y - 1), t.z = this._getZoomForUrl()
                        },
                        _getSubdomain: function(t) {
                            var e = Math.abs(t.x + t.y) % this.options.subdomains.length;
                            return this.options.subdomains[e]
                        },
                        _getTile: function() {
                            if (this.options.reuseTiles && this._unusedTiles.length > 0) {
                                var t = this._unusedTiles.pop();
                                return this._resetTile(t), t
                            }
                            return this._createTile()
                        },
                        _resetTile: function() {},
                        _createTile: function() {
                            var t = l.DomUtil.create("img", "leaflet-tile");
                            return t.style.width = t.style.height = this._getTileSize() + "px", t.galleryimg = "no", t.onselectstart = t.onmousemove = l.Util.falseFn, l.Browser.ielt9 && this.options.opacity !== r && l.DomUtil.setOpacity(t, this.options.opacity), l.Browser.mobileWebkit3d && (t.style.WebkitBackfaceVisibility = "hidden"), t
                        },
                        _loadTile: function(t, e) {
                            t._layer = this, t.onload = this._tileOnLoad, t.onerror = this._tileOnError, this._adjustTilePoint(e), t.src = this.getTileUrl(e), this.fire("tileloadstart", {
                                tile: t,
                                url: t.src
                            })
                        },
                        _tileLoaded: function() {
                            this._tilesToLoad--, this._animated && l.DomUtil.addClass(this._tileContainer, "leaflet-zoom-animated"), this._tilesToLoad || (this.fire("load"), this._animated && (clearTimeout(this._clearBgBufferTimer), this._clearBgBufferTimer = setTimeout(l.bind(this._clearBgBuffer, this), 500)))
                        },
                        _tileOnLoad: function() {
                            var t = this._layer;
                            this.src !== l.Util.emptyImageUrl && (l.DomUtil.addClass(this, "leaflet-tile-loaded"), t.fire("tileload", {
                                tile: this,
                                url: this.src
                            })), t._tileLoaded()
                        },
                        _tileOnError: function() {
                            var t = this._layer;
                            t.fire("tileerror", {
                                tile: this,
                                url: this.src
                            });
                            var e = t.options.errorTileUrl;
                            e && (this.src = e), t._tileLoaded()
                        }
                    }), l.tileLayer = function(t, e) {
                        return new l.TileLayer(t, e)
                    }, l.TileLayer.WMS = l.TileLayer.extend({
                        defaultWmsParams: {
                            service: "WMS",
                            request: "GetMap",
                            version: "1.1.1",
                            layers: "",
                            styles: "",
                            format: "image/jpeg",
                            transparent: !1
                        },
                        initialize: function(t, e) {
                            this._url = t;
                            var i = l.extend({}, this.defaultWmsParams),
                                n = e.tileSize || this.options.tileSize;
                            for (var o in e.detectRetina && l.Browser.retina ? i.width = i.height = 2 * n : i.width = i.height = n, e) this.options.hasOwnProperty(o) || "crs" === o || (i[o] = e[o]);
                            this.wmsParams = i, l.setOptions(this, e)
                        },
                        onAdd: function(t) {
                            this._crs = this.options.crs || t.options.crs, this._wmsVersion = parseFloat(this.wmsParams.version);
                            var e = this._wmsVersion >= 1.3 ? "crs" : "srs";
                            this.wmsParams[e] = this._crs.code, l.TileLayer.prototype.onAdd.call(this, t)
                        },
                        getTileUrl: function(t) {
                            var e = this._map,
                                i = this.options.tileSize,
                                n = t.multiplyBy(i),
                                o = n.add([i, i]),
                                s = this._crs.project(e.unproject(n, t.z)),
                                a = this._crs.project(e.unproject(o, t.z)),
                                r = this._wmsVersion >= 1.3 && this._crs === l.CRS.EPSG4326 ? [a.y, s.x, s.y, a.x].join(",") : [s.x, a.y, a.x, s.y].join(","),
                                h = l.Util.template(this._url, {
                                    s: this._getSubdomain(t)
                                });
                            return h + l.Util.getParamString(this.wmsParams, h, !0) + "&BBOX=" + r
                        },
                        setParams: function(t, e) {
                            return l.extend(this.wmsParams, t), e || this.redraw(), this
                        }
                    }), l.tileLayer.wms = function(t, e) {
                        return new l.TileLayer.WMS(t, e)
                    }, l.TileLayer.Canvas = l.TileLayer.extend({
                        options: {
                            async: !1
                        },
                        initialize: function(t) {
                            l.setOptions(this, t)
                        },
                        redraw: function() {
                            for (var t in this._map && (this._reset({
                                    hard: !0
                                }), this._update()), this._tiles) this._redrawTile(this._tiles[t]);
                            return this
                        },
                        _redrawTile: function(t) {
                            this.drawTile(t, t._tilePoint, this._map._zoom)
                        },
                        _createTile: function() {
                            var t = l.DomUtil.create("canvas", "leaflet-tile");
                            return t.width = t.height = this.options.tileSize, t.onselectstart = t.onmousemove = l.Util.falseFn, t
                        },
                        _loadTile: function(t, e) {
                            t._layer = this, t._tilePoint = e, this._redrawTile(t), this.options.async || this.tileDrawn(t)
                        },
                        drawTile: function() {},
                        tileDrawn: function(t) {
                            this._tileOnLoad.call(t)
                        }
                    }), l.tileLayer.canvas = function(t) {
                        return new l.TileLayer.Canvas(t)
                    }, l.ImageOverlay = l.Class.extend({
                        includes: l.Mixin.Events,
                        options: {
                            opacity: 1
                        },
                        initialize: function(t, e, i) {
                            this._url = t, this._bounds = l.latLngBounds(e), l.setOptions(this, i)
                        },
                        onAdd: function(t) {
                            this._map = t, this._image || this._initImage(), t._panes.overlayPane.appendChild(this._image), t.on("viewreset", this._reset, this), t.options.zoomAnimation && l.Browser.any3d && t.on("zoomanim", this._animateZoom, this), this._reset()
                        },
                        onRemove: function(t) {
                            t.getPanes().overlayPane.removeChild(this._image), t.off("viewreset", this._reset, this), t.options.zoomAnimation && t.off("zoomanim", this._animateZoom, this)
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        setOpacity: function(t) {
                            return this.options.opacity = t, this._updateOpacity(), this
                        },
                        bringToFront: function() {
                            return this._image && this._map._panes.overlayPane.appendChild(this._image), this
                        },
                        bringToBack: function() {
                            var t = this._map._panes.overlayPane;
                            return this._image && t.insertBefore(this._image, t.firstChild), this
                        },
                        setUrl: function(t) {
                            this._url = t, this._image.src = this._url
                        },
                        getAttribution: function() {
                            return this.options.attribution
                        },
                        _initImage: function() {
                            this._image = l.DomUtil.create("img", "leaflet-image-layer"), this._map.options.zoomAnimation && l.Browser.any3d ? l.DomUtil.addClass(this._image, "leaflet-zoom-animated") : l.DomUtil.addClass(this._image, "leaflet-zoom-hide"), this._updateOpacity(), l.extend(this._image, {
                                galleryimg: "no",
                                onselectstart: l.Util.falseFn,
                                onmousemove: l.Util.falseFn,
                                onload: l.bind(this._onImageLoad, this),
                                src: this._url
                            })
                        },
                        _animateZoom: function(t) {
                            var e = this._map,
                                i = this._image,
                                n = e.getZoomScale(t.zoom),
                                o = this._bounds.getNorthWest(),
                                s = this._bounds.getSouthEast(),
                                a = e._latLngToNewLayerPoint(o, t.zoom, t.center),
                                r = e._latLngToNewLayerPoint(s, t.zoom, t.center)._subtract(a),
                                h = a._add(r._multiplyBy(.5 * (1 - 1 / n)));
                            i.style[l.DomUtil.TRANSFORM] = l.DomUtil.getTranslateString(h) + " scale(" + n + ") "
                        },
                        _reset: function() {
                            var t = this._image,
                                e = this._map.latLngToLayerPoint(this._bounds.getNorthWest()),
                                i = this._map.latLngToLayerPoint(this._bounds.getSouthEast())._subtract(e);
                            l.DomUtil.setPosition(t, e), t.style.width = i.x + "px", t.style.height = i.y + "px"
                        },
                        _onImageLoad: function() {
                            this.fire("load")
                        },
                        _updateOpacity: function() {
                            l.DomUtil.setOpacity(this._image, this.options.opacity)
                        }
                    }), l.imageOverlay = function(t, e, i) {
                        return new l.ImageOverlay(t, e, i)
                    }, l.Icon = l.Class.extend({
                        options: {
                            className: ""
                        },
                        initialize: function(t) {
                            l.setOptions(this, t)
                        },
                        createIcon: function(t) {
                            return this._createIcon("icon", t)
                        },
                        createShadow: function(t) {
                            return this._createIcon("shadow", t)
                        },
                        _createIcon: function(t, e) {
                            var i, n = this._getIconUrl(t);
                            if (!n) {
                                if ("icon" === t) throw new Error("iconUrl not set in Icon options (see the docs).");
                                return null
                            }
                            return i = e && "IMG" === e.tagName ? this._createImg(n, e) : this._createImg(n), this._setIconStyles(i, t), i
                        },
                        _setIconStyles: function(t, e) {
                            var i, n = this.options,
                                o = l.point(n[e + "Size"]);
                            i = "shadow" === e ? l.point(n.shadowAnchor || n.iconAnchor) : l.point(n.iconAnchor), !i && o && (i = o.divideBy(2, !0)), t.className = "leaflet-marker-" + e + " " + n.className, i && (t.style.marginLeft = -i.x + "px", t.style.marginTop = -i.y + "px"), o && (t.style.width = o.x + "px", t.style.height = o.y + "px")
                        },
                        _createImg: function(t, e) {
                            return e = e || a.createElement("img"), e.src = t, e
                        },
                        _getIconUrl: function(t) {
                            return l.Browser.retina && this.options[t + "RetinaUrl"] ? this.options[t + "RetinaUrl"] : this.options[t + "Url"]
                        }
                    }), l.icon = function(t) {
                        return new l.Icon(t)
                    }, l.Icon.Default = l.Icon.extend({
                        options: {
                            iconSize: [25, 41],
                            iconAnchor: [12, 41],
                            popupAnchor: [1, -34],
                            shadowSize: [41, 41]
                        },
                        _getIconUrl: function(t) {
                            var e = t + "Url";
                            if (this.options[e]) return this.options[e];
                            l.Browser.retina && "icon" === t && (t += "-2x");
                            var i = l.Icon.Default.imagePath;
                            if (!i) throw new Error("Couldn't autodetect L.Icon.Default.imagePath, set it manually.");
                            return i + "/marker-" + t + ".png"
                        }
                    }), l.Icon.Default.imagePath = function() {
                        var t, e, i, n, o, s = a.getElementsByTagName("script"),
                            r = /[\/^]leaflet[\-\._]?([\w\-\._]*)\.js\??/;
                        for (t = 0, e = s.length; t < e; t++)
                            if (i = s[t].src, n = i.match(r), n) return o = i.split(r)[0], (o ? o + "/" : "") + "images"
                    }(), l.Marker = l.Class.extend({
                        includes: l.Mixin.Events,
                        options: {
                            icon: new l.Icon.Default,
                            title: "",
                            alt: "",
                            clickable: !0,
                            draggable: !1,
                            keyboard: !0,
                            zIndexOffset: 0,
                            opacity: 1,
                            riseOnHover: !1,
                            riseOffset: 250
                        },
                        initialize: function(t, e) {
                            l.setOptions(this, e), this._latlng = l.latLng(t)
                        },
                        onAdd: function(t) {
                            this._map = t, t.on("viewreset", this.update, this), this._initIcon(), this.update(), this.fire("add"), t.options.zoomAnimation && t.options.markerZoomAnimation && t.on("zoomanim", this._animateZoom, this)
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        onRemove: function(t) {
                            this.dragging && this.dragging.disable(), this._removeIcon(), this._removeShadow(), this.fire("remove"), t.off({
                                viewreset: this.update,
                                zoomanim: this._animateZoom
                            }, this), this._map = null
                        },
                        getLatLng: function() {
                            return this._latlng
                        },
                        setLatLng: function(t) {
                            return this._latlng = l.latLng(t), this.update(), this.fire("move", {
                                latlng: this._latlng
                            })
                        },
                        setZIndexOffset: function(t) {
                            return this.options.zIndexOffset = t, this.update(), this
                        },
                        setIcon: function(t) {
                            return this.options.icon = t, this._map && (this._initIcon(), this.update()), this._popup && this.bindPopup(this._popup), this
                        },
                        update: function() {
                            return this._icon && this._setPos(this._map.latLngToLayerPoint(this._latlng).round()), this
                        },
                        _initIcon: function() {
                            var t = this.options,
                                e = this._map,
                                i = e.options.zoomAnimation && e.options.markerZoomAnimation,
                                n = i ? "leaflet-zoom-animated" : "leaflet-zoom-hide",
                                o = t.icon.createIcon(this._icon),
                                s = !1;
                            o !== this._icon && (this._icon && this._removeIcon(), s = !0, t.title && (o.title = t.title), t.alt && (o.alt = t.alt)), l.DomUtil.addClass(o, n), t.keyboard && (o.tabIndex = "0"), this._icon = o, this._initInteraction(), t.riseOnHover && l.DomEvent.on(o, "mouseover", this._bringToFront, this).on(o, "mouseout", this._resetZIndex, this);
                            var a = t.icon.createShadow(this._shadow),
                                r = !1;
                            a !== this._shadow && (this._removeShadow(), r = !0), a && l.DomUtil.addClass(a, n), this._shadow = a, t.opacity < 1 && this._updateOpacity();
                            var h = this._map._panes;
                            s && h.markerPane.appendChild(this._icon), a && r && h.shadowPane.appendChild(this._shadow)
                        },
                        _removeIcon: function() {
                            this.options.riseOnHover && l.DomEvent.off(this._icon, "mouseover", this._bringToFront).off(this._icon, "mouseout", this._resetZIndex), this._map._panes.markerPane.removeChild(this._icon), this._icon = null
                        },
                        _removeShadow: function() {
                            this._shadow && this._map._panes.shadowPane.removeChild(this._shadow), this._shadow = null
                        },
                        _setPos: function(t) {
                            l.DomUtil.setPosition(this._icon, t), this._shadow && l.DomUtil.setPosition(this._shadow, t), this._zIndex = t.y + this.options.zIndexOffset, this._resetZIndex()
                        },
                        _updateZIndex: function(t) {
                            this._icon.style.zIndex = this._zIndex + t
                        },
                        _animateZoom: function(t) {
                            var e = this._map._latLngToNewLayerPoint(this._latlng, t.zoom, t.center).round();
                            this._setPos(e)
                        },
                        _initInteraction: function() {
                            if (this.options.clickable) {
                                var t = this._icon,
                                    e = ["dblclick", "mousedown", "mouseover", "mouseout", "contextmenu"];
                                l.DomUtil.addClass(t, "leaflet-clickable"), l.DomEvent.on(t, "click", this._onMouseClick, this), l.DomEvent.on(t, "keypress", this._onKeyPress, this);
                                for (var i = 0; i < e.length; i++) l.DomEvent.on(t, e[i], this._fireMouseEvent, this);
                                l.Handler.MarkerDrag && (this.dragging = new l.Handler.MarkerDrag(this), this.options.draggable && this.dragging.enable())
                            }
                        },
                        _onMouseClick: function(t) {
                            var e = this.dragging && this.dragging.moved();
                            (this.hasEventListeners(t.type) || e) && l.DomEvent.stopPropagation(t), e || (this.dragging && this.dragging._enabled || !this._map.dragging || !this._map.dragging.moved()) && this.fire(t.type, {
                                originalEvent: t,
                                latlng: this._latlng
                            })
                        },
                        _onKeyPress: function(t) {
                            13 === t.keyCode && this.fire("click", {
                                originalEvent: t,
                                latlng: this._latlng
                            })
                        },
                        _fireMouseEvent: function(t) {
                            this.fire(t.type, {
                                originalEvent: t,
                                latlng: this._latlng
                            }), "contextmenu" === t.type && this.hasEventListeners(t.type) && l.DomEvent.preventDefault(t), "mousedown" !== t.type ? l.DomEvent.stopPropagation(t) : l.DomEvent.preventDefault(t)
                        },
                        setOpacity: function(t) {
                            return this.options.opacity = t, this._map && this._updateOpacity(), this
                        },
                        _updateOpacity: function() {
                            l.DomUtil.setOpacity(this._icon, this.options.opacity), this._shadow && l.DomUtil.setOpacity(this._shadow, this.options.opacity)
                        },
                        _bringToFront: function() {
                            this._updateZIndex(this.options.riseOffset)
                        },
                        _resetZIndex: function() {
                            this._updateZIndex(0)
                        }
                    }), l.marker = function(t, e) {
                        return new l.Marker(t, e)
                    }, l.DivIcon = l.Icon.extend({
                        options: {
                            iconSize: [12, 12],
                            className: "leaflet-div-icon",
                            html: !1
                        },
                        createIcon: function(t) {
                            var e = t && "DIV" === t.tagName ? t : a.createElement("div"),
                                i = this.options;
                            return !1 !== i.html ? e.innerHTML = i.html : e.innerHTML = "", i.bgPos && (e.style.backgroundPosition = -i.bgPos.x + "px " + -i.bgPos.y + "px"), this._setIconStyles(e, "icon"), e
                        },
                        createShadow: function() {
                            return null
                        }
                    }), l.divIcon = function(t) {
                        return new l.DivIcon(t)
                    }, l.Map.mergeOptions({
                        closePopupOnClick: !0
                    }), l.Popup = l.Class.extend({
                        includes: l.Mixin.Events,
                        options: {
                            minWidth: 50,
                            maxWidth: 300,
                            autoPan: !0,
                            closeButton: !0,
                            offset: [0, 7],
                            autoPanPadding: [5, 5],
                            keepInView: !1,
                            className: "",
                            zoomAnimation: !0
                        },
                        initialize: function(t, e) {
                            l.setOptions(this, t), this._source = e, this._animated = l.Browser.any3d && this.options.zoomAnimation, this._isOpen = !1
                        },
                        onAdd: function(t) {
                            this._map = t, this._container || this._initLayout();
                            var e = t.options.fadeAnimation;
                            e && l.DomUtil.setOpacity(this._container, 0), t._panes.popupPane.appendChild(this._container), t.on(this._getEvents(), this), this.update(), e && l.DomUtil.setOpacity(this._container, 1), this.fire("open"), t.fire("popupopen", {
                                popup: this
                            }), this._source && this._source.fire("popupopen", {
                                popup: this
                            })
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        openOn: function(t) {
                            return t.openPopup(this), this
                        },
                        onRemove: function(t) {
                            t._panes.popupPane.removeChild(this._container), l.Util.falseFn(this._container.offsetWidth), t.off(this._getEvents(), this), t.options.fadeAnimation && l.DomUtil.setOpacity(this._container, 0), this._map = null, this.fire("close"), t.fire("popupclose", {
                                popup: this
                            }), this._source && this._source.fire("popupclose", {
                                popup: this
                            })
                        },
                        getLatLng: function() {
                            return this._latlng
                        },
                        setLatLng: function(t) {
                            return this._latlng = l.latLng(t), this._map && (this._updatePosition(), this._adjustPan()), this
                        },
                        getContent: function() {
                            return this._content
                        },
                        setContent: function(t) {
                            return this._content = t, this.update(), this
                        },
                        update: function() {
                            this._map && (this._container.style.visibility = "hidden", this._updateContent(), this._updateLayout(), this._updatePosition(), this._container.style.visibility = "", this._adjustPan())
                        },
                        _getEvents: function() {
                            var t = {
                                viewreset: this._updatePosition
                            };
                            return this._animated && (t.zoomanim = this._zoomAnimation), ("closeOnClick" in this.options ? this.options.closeOnClick : this._map.options.closePopupOnClick) && (t.preclick = this._close), this.options.keepInView && (t.moveend = this._adjustPan), t
                        },
                        _close: function() {
                            this._map && this._map.closePopup(this)
                        },
                        _initLayout: function() {
                            var t, e = "leaflet-popup",
                                i = e + " " + this.options.className + " leaflet-zoom-" + (this._animated ? "animated" : "hide"),
                                n = this._container = l.DomUtil.create("div", i);
                            this.options.closeButton && (t = this._closeButton = l.DomUtil.create("a", e + "-close-button", n), t.href = "#close", t.innerHTML = "&#215;", l.DomEvent.disableClickPropagation(t), l.DomEvent.on(t, "click", this._onCloseButtonClick, this));
                            var o = this._wrapper = l.DomUtil.create("div", e + "-content-wrapper", n);
                            l.DomEvent.disableClickPropagation(o), this._contentNode = l.DomUtil.create("div", e + "-content", o), l.DomEvent.disableScrollPropagation(this._contentNode), l.DomEvent.on(o, "contextmenu", l.DomEvent.stopPropagation), this._tipContainer = l.DomUtil.create("div", e + "-tip-container", n), this._tip = l.DomUtil.create("div", e + "-tip", this._tipContainer)
                        },
                        _updateContent: function() {
                            if (this._content) {
                                if ("string" === typeof this._content) this._contentNode.innerHTML = this._content;
                                else {
                                    while (this._contentNode.hasChildNodes()) this._contentNode.removeChild(this._contentNode.firstChild);
                                    this._contentNode.appendChild(this._content)
                                }
                                this.fire("contentupdate")
                            }
                        },
                        _updateLayout: function() {
                            var t = this._contentNode,
                                e = t.style;
                            e.width = "", e.whiteSpace = "nowrap";
                            var i = t.offsetWidth;
                            i = Math.min(i, this.options.maxWidth), i = Math.max(i, this.options.minWidth), e.width = i + 1 + "px", e.whiteSpace = "", e.height = "";
                            var n = t.offsetHeight,
                                o = this.options.maxHeight,
                                s = "leaflet-popup-scrolled";
                            o && n > o ? (e.height = o + "px", l.DomUtil.addClass(t, s)) : l.DomUtil.removeClass(t, s), this._containerWidth = this._container.offsetWidth
                        },
                        _updatePosition: function() {
                            if (this._map) {
                                var t = this._map.latLngToLayerPoint(this._latlng),
                                    e = this._animated,
                                    i = l.point(this.options.offset);
                                e && l.DomUtil.setPosition(this._container, t), this._containerBottom = -i.y - (e ? 0 : t.y), this._containerLeft = -Math.round(this._containerWidth / 2) + i.x + (e ? 0 : t.x), this._container.style.bottom = this._containerBottom + "px", this._container.style.left = this._containerLeft + "px"
                            }
                        },
                        _zoomAnimation: function(t) {
                            var e = this._map._latLngToNewLayerPoint(this._latlng, t.zoom, t.center);
                            l.DomUtil.setPosition(this._container, e)
                        },
                        _adjustPan: function() {
                            if (this.options.autoPan) {
                                var t = this._map,
                                    e = this._container.offsetHeight,
                                    i = this._containerWidth,
                                    n = new l.Point(this._containerLeft, -e - this._containerBottom);
                                this._animated && n._add(l.DomUtil.getPosition(this._container));
                                var o = t.layerPointToContainerPoint(n),
                                    s = l.point(this.options.autoPanPadding),
                                    a = l.point(this.options.autoPanPaddingTopLeft || s),
                                    r = l.point(this.options.autoPanPaddingBottomRight || s),
                                    h = t.getSize(),
                                    u = 0,
                                    c = 0;
                                o.x + i + r.x > h.x && (u = o.x + i - h.x + r.x), o.x - u - a.x < 0 && (u = o.x - a.x), o.y + e + r.y > h.y && (c = o.y + e - h.y + r.y), o.y - c - a.y < 0 && (c = o.y - a.y), (u || c) && t.fire("autopanstart").panBy([u, c])
                            }
                        },
                        _onCloseButtonClick: function(t) {
                            this._close(), l.DomEvent.stop(t)
                        }
                    }), l.popup = function(t, e) {
                        return new l.Popup(t, e)
                    }, l.Map.include({
                        openPopup: function(t, e, i) {
                            if (this.closePopup(), !(t instanceof l.Popup)) {
                                var n = t;
                                t = new l.Popup(i).setLatLng(e).setContent(n)
                            }
                            return t._isOpen = !0, this._popup = t, this.addLayer(t)
                        },
                        closePopup: function(t) {
                            return t && t !== this._popup || (t = this._popup, this._popup = null), t && (this.removeLayer(t), t._isOpen = !1), this
                        }
                    }), l.Marker.include({
                        openPopup: function() {
                            return this._popup && this._map && !this._map.hasLayer(this._popup) && (this._popup.setLatLng(this._latlng), this._map.openPopup(this._popup)), this
                        },
                        closePopup: function() {
                            return this._popup && this._popup._close(), this
                        },
                        togglePopup: function() {
                            return this._popup && (this._popup._isOpen ? this.closePopup() : this.openPopup()), this
                        },
                        bindPopup: function(t, e) {
                            var i = l.point(this.options.icon.options.popupAnchor || [0, 0]);
                            return i = i.add(l.Popup.prototype.options.offset), e && e.offset && (i = i.add(e.offset)), e = l.extend({
                                offset: i
                            }, e), this._popupHandlersAdded || (this.on("click", this.togglePopup, this).on("remove", this.closePopup, this).on("move", this._movePopup, this), this._popupHandlersAdded = !0), t instanceof l.Popup ? (l.setOptions(t, e), this._popup = t, t._source = this) : this._popup = new l.Popup(e, this).setContent(t), this
                        },
                        setPopupContent: function(t) {
                            return this._popup && this._popup.setContent(t), this
                        },
                        unbindPopup: function() {
                            return this._popup && (this._popup = null, this.off("click", this.togglePopup, this).off("remove", this.closePopup, this).off("move", this._movePopup, this), this._popupHandlersAdded = !1), this
                        },
                        getPopup: function() {
                            return this._popup
                        },
                        _movePopup: function(t) {
                            this._popup.setLatLng(t.latlng)
                        }
                    }), l.LayerGroup = l.Class.extend({
                        initialize: function(t) {
                            var e, i;
                            if (this._layers = {}, t)
                                for (e = 0, i = t.length; e < i; e++) this.addLayer(t[e])
                        },
                        addLayer: function(t) {
                            var e = this.getLayerId(t);
                            return this._layers[e] = t, this._map && this._map.addLayer(t), this
                        },
                        removeLayer: function(t) {
                            var e = t in this._layers ? t : this.getLayerId(t);
                            return this._map && this._layers[e] && this._map.removeLayer(this._layers[e]), delete this._layers[e], this
                        },
                        hasLayer: function(t) {
                            return !!t && (t in this._layers || this.getLayerId(t) in this._layers)
                        },
                        clearLayers: function() {
                            return this.eachLayer(this.removeLayer, this), this
                        },
                        invoke: function(t) {
                            var e, i, n = Array.prototype.slice.call(arguments, 1);
                            for (e in this._layers) i = this._layers[e], i[t] && i[t].apply(i, n);
                            return this
                        },
                        onAdd: function(t) {
                            this._map = t, this.eachLayer(t.addLayer, t)
                        },
                        onRemove: function(t) {
                            this.eachLayer(t.removeLayer, t), this._map = null
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        eachLayer: function(t, e) {
                            for (var i in this._layers) t.call(e, this._layers[i]);
                            return this
                        },
                        getLayer: function(t) {
                            return this._layers[t]
                        },
                        getLayers: function() {
                            var t = [];
                            for (var e in this._layers) t.push(this._layers[e]);
                            return t
                        },
                        setZIndex: function(t) {
                            return this.invoke("setZIndex", t)
                        },
                        getLayerId: function(t) {
                            return l.stamp(t)
                        }
                    }), l.layerGroup = function(t) {
                        return new l.LayerGroup(t)
                    }, l.FeatureGroup = l.LayerGroup.extend({
                        includes: l.Mixin.Events,
                        statics: {
                            EVENTS: "click dblclick mouseover mouseout mousemove contextmenu popupopen popupclose"
                        },
                        addLayer: function(t) {
                            return this.hasLayer(t) ? this : ("on" in t && t.on(l.FeatureGroup.EVENTS, this._propagateEvent, this), l.LayerGroup.prototype.addLayer.call(this, t), this._popupContent && t.bindPopup && t.bindPopup(this._popupContent, this._popupOptions), this.fire("layeradd", {
                                layer: t
                            }))
                        },
                        removeLayer: function(t) {
                            return this.hasLayer(t) ? (t in this._layers && (t = this._layers[t]), "off" in t && t.off(l.FeatureGroup.EVENTS, this._propagateEvent, this), l.LayerGroup.prototype.removeLayer.call(this, t), this._popupContent && this.invoke("unbindPopup"), this.fire("layerremove", {
                                layer: t
                            })) : this
                        },
                        bindPopup: function(t, e) {
                            return this._popupContent = t, this._popupOptions = e, this.invoke("bindPopup", t, e)
                        },
                        openPopup: function(t) {
                            for (var e in this._layers) {
                                this._layers[e].openPopup(t);
                                break
                            }
                            return this
                        },
                        setStyle: function(t) {
                            return this.invoke("setStyle", t)
                        },
                        bringToFront: function() {
                            return this.invoke("bringToFront")
                        },
                        bringToBack: function() {
                            return this.invoke("bringToBack")
                        },
                        getBounds: function() {
                            var t = new l.LatLngBounds;
                            return this.eachLayer((function(e) {
                                t.extend(e instanceof l.Marker ? e.getLatLng() : e.getBounds())
                            })), t
                        },
                        _propagateEvent: function(t) {
                            t = l.extend({
                                layer: t.target,
                                target: this
                            }, t), this.fire(t.type, t)
                        }
                    }), l.featureGroup = function(t) {
                        return new l.FeatureGroup(t)
                    }, l.Path = l.Class.extend({
                        includes: [l.Mixin.Events],
                        statics: {
                            CLIP_PADDING: function() {
                                var t = l.Browser.mobile ? 1280 : 2e3,
                                    e = (t / Math.max(s.outerWidth, s.outerHeight) - 1) / 2;
                                return Math.max(0, Math.min(.5, e))
                            }()
                        },
                        options: {
                            stroke: !0,
                            color: "#0033ff",
                            dashArray: null,
                            lineCap: null,
                            lineJoin: null,
                            weight: 5,
                            opacity: .5,
                            fill: !1,
                            fillColor: null,
                            fillOpacity: .2,
                            clickable: !0
                        },
                        initialize: function(t) {
                            l.setOptions(this, t)
                        },
                        onAdd: function(t) {
                            this._map = t, this._container || (this._initElements(), this._initEvents()), this.projectLatlngs(), this._updatePath(), this._container && this._map._pathRoot.appendChild(this._container), this.fire("add"), t.on({
                                viewreset: this.projectLatlngs,
                                moveend: this._updatePath
                            }, this)
                        },
                        addTo: function(t) {
                            return t.addLayer(this), this
                        },
                        onRemove: function(t) {
                            t._pathRoot.removeChild(this._container), this.fire("remove"), this._map = null, l.Browser.vml && (this._container = null, this._stroke = null, this._fill = null), t.off({
                                viewreset: this.projectLatlngs,
                                moveend: this._updatePath
                            }, this)
                        },
                        projectLatlngs: function() {},
                        setStyle: function(t) {
                            return l.setOptions(this, t), this._container && this._updateStyle(), this
                        },
                        redraw: function() {
                            return this._map && (this.projectLatlngs(), this._updatePath()), this
                        }
                    }), l.Map.include({
                        _updatePathViewport: function() {
                            var t = l.Path.CLIP_PADDING,
                                e = this.getSize(),
                                i = l.DomUtil.getPosition(this._mapPane),
                                n = i.multiplyBy(-1)._subtract(e.multiplyBy(t)._round()),
                                o = n.add(e.multiplyBy(1 + 2 * t)._round());
                            this._pathViewport = new l.Bounds(n, o)
                        }
                    }), l.Path.SVG_NS = "http://www.w3.org/2000/svg", l.Browser.svg = !(!a.createElementNS || !a.createElementNS(l.Path.SVG_NS, "svg").createSVGRect), l.Path = l.Path.extend({
                        statics: {
                            SVG: l.Browser.svg
                        },
                        bringToFront: function() {
                            var t = this._map._pathRoot,
                                e = this._container;
                            return e && t.lastChild !== e && t.appendChild(e), this
                        },
                        bringToBack: function() {
                            var t = this._map._pathRoot,
                                e = this._container,
                                i = t.firstChild;
                            return e && i !== e && t.insertBefore(e, i), this
                        },
                        getPathString: function() {},
                        _createElement: function(t) {
                            return a.createElementNS(l.Path.SVG_NS, t)
                        },
                        _initElements: function() {
                            this._map._initPathRoot(), this._initPath(), this._initStyle()
                        },
                        _initPath: function() {
                            this._container = this._createElement("g"), this._path = this._createElement("path"), this.options.className && l.DomUtil.addClass(this._path, this.options.className), this._container.appendChild(this._path)
                        },
                        _initStyle: function() {
                            this.options.stroke && (this._path.setAttribute("stroke-linejoin", "round"), this._path.setAttribute("stroke-linecap", "round")), this.options.fill && this._path.setAttribute("fill-rule", "evenodd"), this.options.pointerEvents && this._path.setAttribute("pointer-events", this.options.pointerEvents), this.options.clickable || this.options.pointerEvents || this._path.setAttribute("pointer-events", "none"), this._updateStyle()
                        },
                        _updateStyle: function() {
                            this.options.stroke ? (this._path.setAttribute("stroke", this.options.color), this._path.setAttribute("stroke-opacity", this.options.opacity), this._path.setAttribute("stroke-width", this.options.weight), this.options.dashArray ? this._path.setAttribute("stroke-dasharray", this.options.dashArray) : this._path.removeAttribute("stroke-dasharray"), this.options.lineCap && this._path.setAttribute("stroke-linecap", this.options.lineCap), this.options.lineJoin && this._path.setAttribute("stroke-linejoin", this.options.lineJoin)) : this._path.setAttribute("stroke", "none"), this.options.fill ? (this._path.setAttribute("fill", this.options.fillColor || this.options.color), this._path.setAttribute("fill-opacity", this.options.fillOpacity)) : this._path.setAttribute("fill", "none")
                        },
                        _updatePath: function() {
                            var t = this.getPathString();
                            t || (t = "M0 0"), this._path.setAttribute("d", t)
                        },
                        _initEvents: function() {
                            if (this.options.clickable) {
                                !l.Browser.svg && l.Browser.vml || l.DomUtil.addClass(this._path, "leaflet-clickable"), l.DomEvent.on(this._container, "click", this._onMouseClick, this);
                                for (var t = ["dblclick", "mousedown", "mouseover", "mouseout", "mousemove", "contextmenu"], e = 0; e < t.length; e++) l.DomEvent.on(this._container, t[e], this._fireMouseEvent, this)
                            }
                        },
                        _onMouseClick: function(t) {
                            this._map.dragging && this._map.dragging.moved() || this._fireMouseEvent(t)
                        },
                        _fireMouseEvent: function(t) {
                            if (this._map && this.hasEventListeners(t.type)) {
                                var e = this._map,
                                    i = e.mouseEventToContainerPoint(t),
                                    n = e.containerPointToLayerPoint(i),
                                    o = e.layerPointToLatLng(n);
                                this.fire(t.type, {
                                    latlng: o,
                                    layerPoint: n,
                                    containerPoint: i,
                                    originalEvent: t
                                }), "contextmenu" === t.type && l.DomEvent.preventDefault(t), "mousemove" !== t.type && l.DomEvent.stopPropagation(t)
                            }
                        }
                    }), l.Map.include({
                        _initPathRoot: function() {
                            this._pathRoot || (this._pathRoot = l.Path.prototype._createElement("svg"), this._panes.overlayPane.appendChild(this._pathRoot), this.options.zoomAnimation && l.Browser.any3d ? (l.DomUtil.addClass(this._pathRoot, "leaflet-zoom-animated"), this.on({
                                zoomanim: this._animatePathZoom,
                                zoomend: this._endPathZoom
                            })) : l.DomUtil.addClass(this._pathRoot, "leaflet-zoom-hide"), this.on("moveend", this._updateSvgViewport), this._updateSvgViewport())
                        },
                        _animatePathZoom: function(t) {
                            var e = this.getZoomScale(t.zoom),
                                i = this._getCenterOffset(t.center)._multiplyBy(-e)._add(this._pathViewport.min);
                            this._pathRoot.style[l.DomUtil.TRANSFORM] = l.DomUtil.getTranslateString(i) + " scale(" + e + ") ", this._pathZooming = !0
                        },
                        _endPathZoom: function() {
                            this._pathZooming = !1
                        },
                        _updateSvgViewport: function() {
                            if (!this._pathZooming) {
                                this._updatePathViewport();
                                var t = this._pathViewport,
                                    e = t.min,
                                    i = t.max,
                                    n = i.x - e.x,
                                    o = i.y - e.y,
                                    s = this._pathRoot,
                                    a = this._panes.overlayPane;
                                l.Browser.mobileWebkit && a.removeChild(s), l.DomUtil.setPosition(s, e), s.setAttribute("width", n), s.setAttribute("height", o), s.setAttribute("viewBox", [e.x, e.y, n, o].join(" ")), l.Browser.mobileWebkit && a.appendChild(s)
                            }
                        }
                    }), l.Path.include({
                        bindPopup: function(t, e) {
                            return t instanceof l.Popup ? this._popup = t : (this._popup && !e || (this._popup = new l.Popup(e, this)), this._popup.setContent(t)), this._popupHandlersAdded || (this.on("click", this._openPopup, this).on("remove", this.closePopup, this), this._popupHandlersAdded = !0), this
                        },
                        unbindPopup: function() {
                            return this._popup && (this._popup = null, this.off("click", this._openPopup).off("remove", this.closePopup), this._popupHandlersAdded = !1), this
                        },
                        openPopup: function(t) {
                            return this._popup && (t = t || this._latlng || this._latlngs[Math.floor(this._latlngs.length / 2)], this._openPopup({
                                latlng: t
                            })), this
                        },
                        closePopup: function() {
                            return this._popup && this._popup._close(), this
                        },
                        _openPopup: function(t) {
                            this._popup.setLatLng(t.latlng), this._map.openPopup(this._popup)
                        }
                    }), l.Browser.vml = !l.Browser.svg && function() {
                        try {
                            var t = a.createElement("div");
                            t.innerHTML = '<v:shape adj="1"/>';
                            var e = t.firstChild;
                            return e.style.behavior = "url(#default#VML)", e && "object" === typeof e.adj
                        } catch (i) {
                            return !1
                        }
                    }(), l.Path = l.Browser.svg || !l.Browser.vml ? l.Path : l.Path.extend({
                        statics: {
                            VML: !0,
                            CLIP_PADDING: .02
                        },
                        _createElement: function() {
                            try {
                                return a.namespaces.add("lvml", "urn:schemas-microsoft-com:vml"),
                                    function(t) {
                                        return a.createElement("<lvml:" + t + ' class="lvml">')
                                    }
                            } catch (t) {
                                return function(t) {
                                    return a.createElement("<" + t + ' xmlns="urn:schemas-microsoft.com:vml" class="lvml">')
                                }
                            }
                        }(),
                        _initPath: function() {
                            var t = this._container = this._createElement("shape");
                            l.DomUtil.addClass(t, "leaflet-vml-shape" + (this.options.className ? " " + this.options.className : "")), this.options.clickable && l.DomUtil.addClass(t, "leaflet-clickable"), t.coordsize = "1 1", this._path = this._createElement("path"), t.appendChild(this._path), this._map._pathRoot.appendChild(t)
                        },
                        _initStyle: function() {
                            this._updateStyle()
                        },
                        _updateStyle: function() {
                            var t = this._stroke,
                                e = this._fill,
                                i = this.options,
                                n = this._container;
                            n.stroked = i.stroke, n.filled = i.fill, i.stroke ? (t || (t = this._stroke = this._createElement("stroke"), t.endcap = "round", n.appendChild(t)), t.weight = i.weight + "px", t.color = i.color, t.opacity = i.opacity, i.dashArray ? t.dashStyle = l.Util.isArray(i.dashArray) ? i.dashArray.join(" ") : i.dashArray.replace(/( *, *)/g, " ") : t.dashStyle = "", i.lineCap && (t.endcap = i.lineCap.replace("butt", "flat")), i.lineJoin && (t.joinstyle = i.lineJoin)) : t && (n.removeChild(t), this._stroke = null), i.fill ? (e || (e = this._fill = this._createElement("fill"), n.appendChild(e)), e.color = i.fillColor || i.color, e.opacity = i.fillOpacity) : e && (n.removeChild(e), this._fill = null)
                        },
                        _updatePath: function() {
                            var t = this._container.style;
                            t.display = "none", this._path.v = this.getPathString() + " ", t.display = ""
                        }
                    }), l.Map.include(l.Browser.svg || !l.Browser.vml ? {} : {
                        _initPathRoot: function() {
                            if (!this._pathRoot) {
                                var t = this._pathRoot = a.createElement("div");
                                t.className = "leaflet-vml-container", this._panes.overlayPane.appendChild(t), this.on("moveend", this._updatePathViewport), this._updatePathViewport()
                            }
                        }
                    }), l.Browser.canvas = function() {
                        return !!a.createElement("canvas").getContext
                    }(), l.Path = l.Path.SVG && !s.L_PREFER_CANVAS || !l.Browser.canvas ? l.Path : l.Path.extend({
                        statics: {
                            CANVAS: !0,
                            SVG: !1
                        },
                        redraw: function() {
                            return this._map && (this.projectLatlngs(), this._requestUpdate()), this
                        },
                        setStyle: function(t) {
                            return l.setOptions(this, t), this._map && (this._updateStyle(), this._requestUpdate()), this
                        },
                        onRemove: function(t) {
                            t.off("viewreset", this.projectLatlngs, this).off("moveend", this._updatePath, this), this.options.clickable && (this._map.off("click", this._onClick, this), this._map.off("mousemove", this._onMouseMove, this)), this._requestUpdate(), this.fire("remove"), this._map = null
                        },
                        _requestUpdate: function() {
                            this._map && !l.Path._updateRequest && (l.Path._updateRequest = l.Util.requestAnimFrame(this._fireMapMoveEnd, this._map))
                        },
                        _fireMapMoveEnd: function() {
                            l.Path._updateRequest = null, this.fire("moveend")
                        },
                        _initElements: function() {
                            this._map._initPathRoot(), this._ctx = this._map._canvasCtx
                        },
                        _updateStyle: function() {
                            var t = this.options;
                            t.stroke && (this._ctx.lineWidth = t.weight, this._ctx.strokeStyle = t.color), t.fill && (this._ctx.fillStyle = t.fillColor || t.color), t.lineCap && (this._ctx.lineCap = t.lineCap), t.lineJoin && (this._ctx.lineJoin = t.lineJoin)
                        },
                        _drawPath: function() {
                            var t, e, i, n, o, s;
                            for (this._ctx.beginPath(), t = 0, i = this._parts.length; t < i; t++) {
                                for (e = 0, n = this._parts[t].length; e < n; e++) o = this._parts[t][e], s = (0 === e ? "move" : "line") + "To", this._ctx[s](o.x, o.y);
                                this instanceof l.Polygon && this._ctx.closePath()
                            }
                        },
                        _checkIfEmpty: function() {
                            return !this._parts.length
                        },
                        _updatePath: function() {
                            if (!this._checkIfEmpty()) {
                                var t = this._ctx,
                                    e = this.options;
                                this._drawPath(), t.save(), this._updateStyle(), e.fill && (t.globalAlpha = e.fillOpacity, t.fill(e.fillRule || "evenodd")), e.stroke && (t.globalAlpha = e.opacity, t.stroke()), t.restore()
                            }
                        },
                        _initEvents: function() {
                            this.options.clickable && (this._map.on("mousemove", this._onMouseMove, this), this._map.on("click dblclick contextmenu", this._fireMouseEvent, this))
                        },
                        _fireMouseEvent: function(t) {
                            this._containsPoint(t.layerPoint) && this.fire(t.type, t)
                        },
                        _onMouseMove: function(t) {
                            this._map && !this._map._animatingZoom && (this._containsPoint(t.layerPoint) ? (this._ctx.canvas.style.cursor = "pointer", this._mouseInside = !0, this.fire("mouseover", t)) : this._mouseInside && (this._ctx.canvas.style.cursor = "", this._mouseInside = !1, this.fire("mouseout", t)))
                        }
                    }), l.Map.include(l.Path.SVG && !s.L_PREFER_CANVAS || !l.Browser.canvas ? {} : {
                        _initPathRoot: function() {
                            var t, e = this._pathRoot;
                            e || (e = this._pathRoot = a.createElement("canvas"), e.style.position = "absolute", t = this._canvasCtx = e.getContext("2d"), t.lineCap = "round", t.lineJoin = "round", this._panes.overlayPane.appendChild(e), this.options.zoomAnimation && (this._pathRoot.className = "leaflet-zoom-animated", this.on("zoomanim", this._animatePathZoom), this.on("zoomend", this._endPathZoom)), this.on("moveend", this._updateCanvasViewport), this._updateCanvasViewport())
                        },
                        _updateCanvasViewport: function() {
                            if (!this._pathZooming) {
                                this._updatePathViewport();
                                var t = this._pathViewport,
                                    e = t.min,
                                    i = t.max.subtract(e),
                                    n = this._pathRoot;
                                l.DomUtil.setPosition(n, e), n.width = i.x, n.height = i.y, n.getContext("2d").translate(-e.x, -e.y)
                            }
                        }
                    }), l.LineUtil = {
                        simplify: function(t, e) {
                            if (!e || !t.length) return t.slice();
                            var i = e * e;
                            return t = this._reducePoints(t, i), t = this._simplifyDP(t, i), t
                        },
                        pointToSegmentDistance: function(t, e, i) {
                            return Math.sqrt(this._sqClosestPointOnSegment(t, e, i, !0))
                        },
                        closestPointOnSegment: function(t, e, i) {
                            return this._sqClosestPointOnSegment(t, e, i)
                        },
                        _simplifyDP: function(t, e) {
                            var i = t.length,
                                n = typeof Uint8Array !== r + "" ? Uint8Array : Array,
                                o = new n(i);
                            o[0] = o[i - 1] = 1, this._simplifyDPStep(t, o, e, 0, i - 1);
                            var s, a = [];
                            for (s = 0; s < i; s++) o[s] && a.push(t[s]);
                            return a
                        },
                        _simplifyDPStep: function(t, e, i, n, o) {
                            var s, a, r, h = 0;
                            for (a = n + 1; a <= o - 1; a++) r = this._sqClosestPointOnSegment(t[a], t[n], t[o], !0), r > h && (s = a, h = r);
                            h > i && (e[s] = 1, this._simplifyDPStep(t, e, i, n, s), this._simplifyDPStep(t, e, i, s, o))
                        },
                        _reducePoints: function(t, e) {
                            for (var i = [t[0]], n = 1, o = 0, s = t.length; n < s; n++) this._sqDist(t[n], t[o]) > e && (i.push(t[n]), o = n);
                            return o < s - 1 && i.push(t[s - 1]), i
                        },
                        clipSegment: function(t, e, i, n) {
                            var o, s, a, r = n ? this._lastCode : this._getBitCode(t, i),
                                h = this._getBitCode(e, i);
                            this._lastCode = h;
                            while (1) {
                                if (!(r | h)) return [t, e];
                                if (r & h) return !1;
                                o = r || h, s = this._getEdgeIntersection(t, e, o, i), a = this._getBitCode(s, i), o === r ? (t = s, r = a) : (e = s, h = a)
                            }
                        },
                        _getEdgeIntersection: function(t, e, i, n) {
                            var o = e.x - t.x,
                                s = e.y - t.y,
                                a = n.min,
                                r = n.max;
                            return 8 & i ? new l.Point(t.x + o * (r.y - t.y) / s, r.y) : 4 & i ? new l.Point(t.x + o * (a.y - t.y) / s, a.y) : 2 & i ? new l.Point(r.x, t.y + s * (r.x - t.x) / o) : 1 & i ? new l.Point(a.x, t.y + s * (a.x - t.x) / o) : void 0
                        },
                        _getBitCode: function(t, e) {
                            var i = 0;
                            return t.x < e.min.x ? i |= 1 : t.x > e.max.x && (i |= 2), t.y < e.min.y ? i |= 4 : t.y > e.max.y && (i |= 8), i
                        },
                        _sqDist: function(t, e) {
                            var i = e.x - t.x,
                                n = e.y - t.y;
                            return i * i + n * n
                        },
                        _sqClosestPointOnSegment: function(t, e, i, n) {
                            var o, s = e.x,
                                a = e.y,
                                r = i.x - s,
                                h = i.y - a,
                                u = r * r + h * h;
                            return u > 0 && (o = ((t.x - s) * r + (t.y - a) * h) / u, o > 1 ? (s = i.x, a = i.y) : o > 0 && (s += r * o, a += h * o)), r = t.x - s, h = t.y - a, n ? r * r + h * h : new l.Point(s, a)
                        }
                    }, l.Polyline = l.Path.extend({
                        initialize: function(t, e) {
                            l.Path.prototype.initialize.call(this, e), this._latlngs = this._convertLatLngs(t)
                        },
                        options: {
                            smoothFactor: 1,
                            noClip: !1
                        },
                        projectLatlngs: function() {
                            this._originalPoints = [];
                            for (var t = 0, e = this._latlngs.length; t < e; t++) this._originalPoints[t] = this._map.latLngToLayerPoint(this._latlngs[t])
                        },
                        getPathString: function() {
                            for (var t = 0, e = this._parts.length, i = ""; t < e; t++) i += this._getPathPartStr(this._parts[t]);
                            return i
                        },
                        getLatLngs: function() {
                            return this._latlngs
                        },
                        setLatLngs: function(t) {
                            return this._latlngs = this._convertLatLngs(t), this.redraw()
                        },
                        addLatLng: function(t) {
                            return this._latlngs.push(l.latLng(t)), this.redraw()
                        },
                        spliceLatLngs: function() {
                            var t = [].splice.apply(this._latlngs, arguments);
                            return this._convertLatLngs(this._latlngs, !0), this.redraw(), t
                        },
                        closestLayerPoint: function(t) {
                            for (var e, i, n = 1 / 0, o = this._parts, s = null, a = 0, r = o.length; a < r; a++)
                                for (var h = o[a], u = 1, c = h.length; u < c; u++) {
                                    e = h[u - 1], i = h[u];
                                    var p = l.LineUtil._sqClosestPointOnSegment(t, e, i, !0);
                                    p < n && (n = p, s = l.LineUtil._sqClosestPointOnSegment(t, e, i))
                                }
                            return s && (s.distance = Math.sqrt(n)), s
                        },
                        getBounds: function() {
                            return new l.LatLngBounds(this.getLatLngs())
                        },
                        _convertLatLngs: function(t, e) {
                            var i, n, o = e ? t : [];
                            for (i = 0, n = t.length; i < n; i++) {
                                if (l.Util.isArray(t[i]) && "number" !== typeof t[i][0]) return;
                                o[i] = l.latLng(t[i])
                            }
                            return o
                        },
                        _initEvents: function() {
                            l.Path.prototype._initEvents.call(this)
                        },
                        _getPathPartStr: function(t) {
                            for (var e, i = l.Path.VML, n = 0, o = t.length, s = ""; n < o; n++) e = t[n], i && e._round(), s += (n ? "L" : "M") + e.x + " " + e.y;
                            return s
                        },
                        _clipPoints: function() {
                            var t, e, i, n = this._originalPoints,
                                o = n.length;
                            if (this.options.noClip) this._parts = [n];
                            else {
                                this._parts = [];
                                var s = this._parts,
                                    a = this._map._pathViewport,
                                    r = l.LineUtil;
                                for (t = 0, e = 0; t < o - 1; t++) i = r.clipSegment(n[t], n[t + 1], a, t), i && (s[e] = s[e] || [], s[e].push(i[0]), i[1] === n[t + 1] && t !== o - 2 || (s[e].push(i[1]), e++))
                            }
                        },
                        _simplifyPoints: function() {
                            for (var t = this._parts, e = l.LineUtil, i = 0, n = t.length; i < n; i++) t[i] = e.simplify(t[i], this.options.smoothFactor)
                        },
                        _updatePath: function() {
                            this._map && (this._clipPoints(), this._simplifyPoints(), l.Path.prototype._updatePath.call(this))
                        }
                    }), l.polyline = function(t, e) {
                        return new l.Polyline(t, e)
                    }, l.PolyUtil = {}, l.PolyUtil.clipPolygon = function(t, e) {
                        var i, n, o, s, a, r, h, u, c, p = [1, 4, 2, 8],
                            d = l.LineUtil;
                        for (n = 0, h = t.length; n < h; n++) t[n]._code = d._getBitCode(t[n], e);
                        for (s = 0; s < 4; s++) {
                            for (u = p[s], i = [], n = 0, h = t.length, o = h - 1; n < h; o = n++) a = t[n], r = t[o], a._code & u ? r._code & u || (c = d._getEdgeIntersection(r, a, u, e), c._code = d._getBitCode(c, e), i.push(c)) : (r._code & u && (c = d._getEdgeIntersection(r, a, u, e), c._code = d._getBitCode(c, e), i.push(c)), i.push(a));
                            t = i
                        }
                        return t
                    }, l.Polygon = l.Polyline.extend({
                        options: {
                            fill: !0
                        },
                        initialize: function(t, e) {
                            l.Polyline.prototype.initialize.call(this, t, e), this._initWithHoles(t)
                        },
                        _initWithHoles: function(t) {
                            var e, i, n;
                            if (t && l.Util.isArray(t[0]) && "number" !== typeof t[0][0])
                                for (this._latlngs = this._convertLatLngs(t[0]), this._holes = t.slice(1), e = 0, i = this._holes.length; e < i; e++) n = this._holes[e] = this._convertLatLngs(this._holes[e]), n[0].equals(n[n.length - 1]) && n.pop();
                            t = this._latlngs, t.length >= 2 && t[0].equals(t[t.length - 1]) && t.pop()
                        },
                        projectLatlngs: function() {
                            var t, e, i, n;
                            if (l.Polyline.prototype.projectLatlngs.call(this), this._holePoints = [], this._holes)
                                for (t = 0, i = this._holes.length; t < i; t++)
                                    for (this._holePoints[t] = [], e = 0, n = this._holes[t].length; e < n; e++) this._holePoints[t][e] = this._map.latLngToLayerPoint(this._holes[t][e])
                        },
                        setLatLngs: function(t) {
                            return t && l.Util.isArray(t[0]) && "number" !== typeof t[0][0] ? (this._initWithHoles(t), this.redraw()) : l.Polyline.prototype.setLatLngs.call(this, t)
                        },
                        _clipPoints: function() {
                            var t = this._originalPoints,
                                e = [];
                            if (this._parts = [t].concat(this._holePoints), !this.options.noClip) {
                                for (var i = 0, n = this._parts.length; i < n; i++) {
                                    var o = l.PolyUtil.clipPolygon(this._parts[i], this._map._pathViewport);
                                    o.length && e.push(o)
                                }
                                this._parts = e
                            }
                        },
                        _getPathPartStr: function(t) {
                            var e = l.Polyline.prototype._getPathPartStr.call(this, t);
                            return e + (l.Browser.svg ? "z" : "x")
                        }
                    }), l.polygon = function(t, e) {
                        return new l.Polygon(t, e)
                    },
                    function() {
                        function t(t) {
                            return l.FeatureGroup.extend({
                                initialize: function(t, e) {
                                    this._layers = {}, this._options = e, this.setLatLngs(t)
                                },
                                setLatLngs: function(e) {
                                    var i = 0,
                                        n = e.length;
                                    this.eachLayer((function(t) {
                                        i < n ? t.setLatLngs(e[i++]) : this.removeLayer(t)
                                    }), this);
                                    while (i < n) this.addLayer(new t(e[i++], this._options));
                                    return this
                                },
                                getLatLngs: function() {
                                    var t = [];
                                    return this.eachLayer((function(e) {
                                        t.push(e.getLatLngs())
                                    })), t
                                }
                            })
                        }
                        l.MultiPolyline = t(l.Polyline), l.MultiPolygon = t(l.Polygon), l.multiPolyline = function(t, e) {
                            return new l.MultiPolyline(t, e)
                        }, l.multiPolygon = function(t, e) {
                            return new l.MultiPolygon(t, e)
                        }
                    }(), l.Rectangle = l.Polygon.extend({
                        initialize: function(t, e) {
                            l.Polygon.prototype.initialize.call(this, this._boundsToLatLngs(t), e)
                        },
                        setBounds: function(t) {
                            this.setLatLngs(this._boundsToLatLngs(t))
                        },
                        _boundsToLatLngs: function(t) {
                            return t = l.latLngBounds(t), [t.getSouthWest(), t.getNorthWest(), t.getNorthEast(), t.getSouthEast()]
                        }
                    }), l.rectangle = function(t, e) {
                        return new l.Rectangle(t, e)
                    }, l.Circle = l.Path.extend({
                        initialize: function(t, e, i) {
                            l.Path.prototype.initialize.call(this, i), this._latlng = l.latLng(t), this._mRadius = e
                        },
                        options: {
                            fill: !0
                        },
                        setLatLng: function(t) {
                            return this._latlng = l.latLng(t), this.redraw()
                        },
                        setRadius: function(t) {
                            return this._mRadius = t, this.redraw()
                        },
                        projectLatlngs: function() {
                            var t = this._getLngRadius(),
                                e = this._latlng,
                                i = this._map.latLngToLayerPoint([e.lat, e.lng - t]);
                            this._point = this._map.latLngToLayerPoint(e), this._radius = Math.max(this._point.x - i.x, 1)
                        },
                        getBounds: function() {
                            var t = this._getLngRadius(),
                                e = this._mRadius / 40075017 * 360,
                                i = this._latlng;
                            return new l.LatLngBounds([i.lat - e, i.lng - t], [i.lat + e, i.lng + t])
                        },
                        getLatLng: function() {
                            return this._latlng
                        },
                        getPathString: function() {
                            var t = this._point,
                                e = this._radius;
                            return this._checkIfEmpty() ? "" : l.Browser.svg ? "M" + t.x + "," + (t.y - e) + "A" + e + "," + e + ",0,1,1," + (t.x - .1) + "," + (t.y - e) + " z" : (t._round(), e = Math.round(e), "AL " + t.x + "," + t.y + " " + e + "," + e + " 0,23592600")
                        },
                        getRadius: function() {
                            return this._mRadius
                        },
                        _getLatRadius: function() {
                            return this._mRadius / 40075017 * 360
                        },
                        _getLngRadius: function() {
                            return this._getLatRadius() / Math.cos(l.LatLng.DEG_TO_RAD * this._latlng.lat)
                        },
                        _checkIfEmpty: function() {
                            if (!this._map) return !1;
                            var t = this._map._pathViewport,
                                e = this._radius,
                                i = this._point;
                            return i.x - e > t.max.x || i.y - e > t.max.y || i.x + e < t.min.x || i.y + e < t.min.y
                        }
                    }), l.circle = function(t, e, i) {
                        return new l.Circle(t, e, i)
                    }, l.CircleMarker = l.Circle.extend({
                        options: {
                            radius: 10,
                            weight: 2
                        },
                        initialize: function(t, e) {
                            l.Circle.prototype.initialize.call(this, t, null, e), this._radius = this.options.radius
                        },
                        projectLatlngs: function() {
                            this._point = this._map.latLngToLayerPoint(this._latlng)
                        },
                        _updateStyle: function() {
                            l.Circle.prototype._updateStyle.call(this), this.setRadius(this.options.radius)
                        },
                        setLatLng: function(t) {
                            return l.Circle.prototype.setLatLng.call(this, t), this._popup && this._popup._isOpen && this._popup.setLatLng(t), this
                        },
                        setRadius: function(t) {
                            return this.options.radius = this._radius = t, this.redraw()
                        },
                        getRadius: function() {
                            return this._radius
                        }
                    }), l.circleMarker = function(t, e) {
                        return new l.CircleMarker(t, e)
                    }, l.Polyline.include(l.Path.CANVAS ? {
                        _containsPoint: function(t, e) {
                            var i, n, o, s, a, r, h, u = this.options.weight / 2;
                            for (l.Browser.touch && (u += 10), i = 0, s = this._parts.length; i < s; i++)
                                for (h = this._parts[i], n = 0, a = h.length, o = a - 1; n < a; o = n++)
                                    if ((e || 0 !== n) && (r = l.LineUtil.pointToSegmentDistance(t, h[o], h[n]), r <= u)) return !0;
                            return !1
                        }
                    } : {}), l.Polygon.include(l.Path.CANVAS ? {
                        _containsPoint: function(t) {
                            var e, i, n, o, s, a, r, h, u = !1;
                            if (l.Polyline.prototype._containsPoint.call(this, t, !0)) return !0;
                            for (o = 0, r = this._parts.length; o < r; o++)
                                for (e = this._parts[o], s = 0, h = e.length, a = h - 1; s < h; a = s++) i = e[s], n = e[a], i.y > t.y !== n.y > t.y && t.x < (n.x - i.x) * (t.y - i.y) / (n.y - i.y) + i.x && (u = !u);
                            return u
                        }
                    } : {}), l.Circle.include(l.Path.CANVAS ? {
                        _drawPath: function() {
                            var t = this._point;
                            this._ctx.beginPath(), this._ctx.arc(t.x, t.y, this._radius, 0, 2 * Math.PI, !1)
                        },
                        _containsPoint: function(t) {
                            var e = this._point,
                                i = this.options.stroke ? this.options.weight / 2 : 0;
                            return t.distanceTo(e) <= this._radius + i
                        }
                    } : {}), l.CircleMarker.include(l.Path.CANVAS ? {
                        _updateStyle: function() {
                            l.Path.prototype._updateStyle.call(this)
                        }
                    } : {}), l.GeoJSON = l.FeatureGroup.extend({
                        initialize: function(t, e) {
                            l.setOptions(this, e), this._layers = {}, t && this.addData(t)
                        },
                        addData: function(t) {
                            var e, i, n, o = l.Util.isArray(t) ? t : t.features;
                            if (o) {
                                for (e = 0, i = o.length; e < i; e++) n = o[e], (n.geometries || n.geometry || n.features || n.coordinates) && this.addData(o[e]);
                                return this
                            }
                            var s = this.options;
                            if (!s.filter || s.filter(t)) {
                                var a = l.GeoJSON.geometryToLayer(t, s.pointToLayer, s.coordsToLatLng, s);
                                return a.feature = l.GeoJSON.asFeature(t), a.defaultOptions = a.options, this.resetStyle(a), s.onEachFeature && s.onEachFeature(t, a), this.addLayer(a)
                            }
                        },
                        resetStyle: function(t) {
                            var e = this.options.style;
                            e && (l.Util.extend(t.options, t.defaultOptions), this._setLayerStyle(t, e))
                        },
                        setStyle: function(t) {
                            this.eachLayer((function(e) {
                                this._setLayerStyle(e, t)
                            }), this)
                        },
                        _setLayerStyle: function(t, e) {
                            "function" === typeof e && (e = e(t.feature)), t.setStyle && t.setStyle(e)
                        }
                    }), l.extend(l.GeoJSON, {
                        geometryToLayer: function(t, e, i, n) {
                            var o, s, a, r, h = "Feature" === t.type ? t.geometry : t,
                                u = h.coordinates,
                                c = [];
                            switch (i = i || this.coordsToLatLng, h.type) {
                                case "Point":
                                    return o = i(u), e ? e(t, o) : new l.Marker(o);
                                case "MultiPoint":
                                    for (a = 0, r = u.length; a < r; a++) o = i(u[a]), c.push(e ? e(t, o) : new l.Marker(o));
                                    return new l.FeatureGroup(c);
                                case "LineString":
                                    return s = this.coordsToLatLngs(u, 0, i), new l.Polyline(s, n);
                                case "Polygon":
                                    if (2 === u.length && !u[1].length) throw new Error("Invalid GeoJSON object.");
                                    return s = this.coordsToLatLngs(u, 1, i), new l.Polygon(s, n);
                                case "MultiLineString":
                                    return s = this.coordsToLatLngs(u, 1, i), new l.MultiPolyline(s, n);
                                case "MultiPolygon":
                                    return s = this.coordsToLatLngs(u, 2, i), new l.MultiPolygon(s, n);
                                case "GeometryCollection":
                                    for (a = 0, r = h.geometries.length; a < r; a++) c.push(this.geometryToLayer({
                                        geometry: h.geometries[a],
                                        type: "Feature",
                                        properties: t.properties
                                    }, e, i, n));
                                    return new l.FeatureGroup(c);
                                default:
                                    throw new Error("Invalid GeoJSON object.")
                            }
                        },
                        coordsToLatLng: function(t) {
                            return new l.LatLng(t[1], t[0], t[2])
                        },
                        coordsToLatLngs: function(t, e, i) {
                            var n, o, s, a = [];
                            for (o = 0, s = t.length; o < s; o++) n = e ? this.coordsToLatLngs(t[o], e - 1, i) : (i || this.coordsToLatLng)(t[o]), a.push(n);
                            return a
                        },
                        latLngToCoords: function(t) {
                            var e = [t.lng, t.lat];
                            return t.alt !== r && e.push(t.alt), e
                        },
                        latLngsToCoords: function(t) {
                            for (var e = [], i = 0, n = t.length; i < n; i++) e.push(l.GeoJSON.latLngToCoords(t[i]));
                            return e
                        },
                        getFeature: function(t, e) {
                            return t.feature ? l.extend({}, t.feature, {
                                geometry: e
                            }) : l.GeoJSON.asFeature(e)
                        },
                        asFeature: function(t) {
                            return "Feature" === t.type ? t : {
                                type: "Feature",
                                properties: {},
                                geometry: t
                            }
                        }
                    });
                var c = {
                    toGeoJSON: function() {
                        return l.GeoJSON.getFeature(this, {
                            type: "Point",
                            coordinates: l.GeoJSON.latLngToCoords(this.getLatLng())
                        })
                    }
                };
                l.Marker.include(c), l.Circle.include(c), l.CircleMarker.include(c), l.Polyline.include({
                        toGeoJSON: function() {
                            return l.GeoJSON.getFeature(this, {
                                type: "LineString",
                                coordinates: l.GeoJSON.latLngsToCoords(this.getLatLngs())
                            })
                        }
                    }), l.Polygon.include({
                        toGeoJSON: function() {
                            var t, e, i, n = [l.GeoJSON.latLngsToCoords(this.getLatLngs())];
                            if (n[0].push(n[0][0]), this._holes)
                                for (t = 0, e = this._holes.length; t < e; t++) i = l.GeoJSON.latLngsToCoords(this._holes[t]), i.push(i[0]), n.push(i);
                            return l.GeoJSON.getFeature(this, {
                                type: "Polygon",
                                coordinates: n
                            })
                        }
                    }),
                    function() {
                        function t(t) {
                            return function() {
                                var e = [];
                                return this.eachLayer((function(t) {
                                    e.push(t.toGeoJSON().geometry.coordinates)
                                })), l.GeoJSON.getFeature(this, {
                                    type: t,
                                    coordinates: e
                                })
                            }
                        }
                        l.MultiPolyline.include({
                            toGeoJSON: t("MultiLineString")
                        }), l.MultiPolygon.include({
                            toGeoJSON: t("MultiPolygon")
                        }), l.LayerGroup.include({
                            toGeoJSON: function() {
                                var e, i = this.feature && this.feature.geometry,
                                    n = [];
                                if (i && "MultiPoint" === i.type) return t("MultiPoint").call(this);
                                var o = i && "GeometryCollection" === i.type;
                                return this.eachLayer((function(t) {
                                    t.toGeoJSON && (e = t.toGeoJSON(), n.push(o ? e.geometry : l.GeoJSON.asFeature(e)))
                                })), o ? l.GeoJSON.getFeature(this, {
                                    geometries: n,
                                    type: "GeometryCollection"
                                }) : {
                                    type: "FeatureCollection",
                                    features: n
                                }
                            }
                        })
                    }(), l.geoJson = function(t, e) {
                        return new l.GeoJSON(t, e)
                    }, l.DomEvent = {
                        addListener: function(t, e, i, n) {
                            var o, s, a, r = l.stamp(i),
                                h = "_leaflet_" + e + r;
                            return t[h] ? this : (o = function(e) {
                                return i.call(n || t, e || l.DomEvent._getEvent())
                            }, l.Browser.pointer && 0 === e.indexOf("touch") ? this.addPointerListener(t, e, o, r) : (l.Browser.touch && "dblclick" === e && this.addDoubleTapListener && this.addDoubleTapListener(t, o, r), "addEventListener" in t ? "mousewheel" === e ? (t.addEventListener("DOMMouseScroll", o, !1), t.addEventListener(e, o, !1)) : "mouseenter" === e || "mouseleave" === e ? (s = o, a = "mouseenter" === e ? "mouseover" : "mouseout", o = function(e) {
                                if (l.DomEvent._checkMouse(t, e)) return s(e)
                            }, t.addEventListener(a, o, !1)) : "click" === e && l.Browser.android ? (s = o, o = function(t) {
                                return l.DomEvent._filterClick(t, s)
                            }, t.addEventListener(e, o, !1)) : t.addEventListener(e, o, !1) : "attachEvent" in t && t.attachEvent("on" + e, o), t[h] = o, this))
                        },
                        removeListener: function(t, e, i) {
                            var n = l.stamp(i),
                                o = "_leaflet_" + e + n,
                                s = t[o];
                            return s ? (l.Browser.pointer && 0 === e.indexOf("touch") ? this.removePointerListener(t, e, n) : l.Browser.touch && "dblclick" === e && this.removeDoubleTapListener ? this.removeDoubleTapListener(t, n) : "removeEventListener" in t ? "mousewheel" === e ? (t.removeEventListener("DOMMouseScroll", s, !1), t.removeEventListener(e, s, !1)) : "mouseenter" === e || "mouseleave" === e ? t.removeEventListener("mouseenter" === e ? "mouseover" : "mouseout", s, !1) : t.removeEventListener(e, s, !1) : "detachEvent" in t && t.detachEvent("on" + e, s), t[o] = null, this) : this
                        },
                        stopPropagation: function(t) {
                            return t.stopPropagation ? t.stopPropagation() : t.cancelBubble = !0, l.DomEvent._skipped(t), this
                        },
                        disableScrollPropagation: function(t) {
                            var e = l.DomEvent.stopPropagation;
                            return l.DomEvent.on(t, "mousewheel", e).on(t, "MozMousePixelScroll", e)
                        },
                        disableClickPropagation: function(t) {
                            for (var e = l.DomEvent.stopPropagation, i = l.Draggable.START.length - 1; i >= 0; i--) l.DomEvent.on(t, l.Draggable.START[i], e);
                            return l.DomEvent.on(t, "click", l.DomEvent._fakeStop).on(t, "dblclick", e)
                        },
                        preventDefault: function(t) {
                            return t.preventDefault ? t.preventDefault() : t.returnValue = !1, this
                        },
                        stop: function(t) {
                            return l.DomEvent.preventDefault(t).stopPropagation(t)
                        },
                        getMousePosition: function(t, e) {
                            if (!e) return new l.Point(t.clientX, t.clientY);
                            var i = e.getBoundingClientRect();
                            return new l.Point(t.clientX - i.left - e.clientLeft, t.clientY - i.top - e.clientTop)
                        },
                        getWheelDelta: function(t) {
                            var e = 0;
                            return t.wheelDelta && (e = t.wheelDelta / 120), t.detail && (e = -t.detail / 3), e
                        },
                        _skipEvents: {},
                        _fakeStop: function(t) {
                            l.DomEvent._skipEvents[t.type] = !0
                        },
                        _skipped: function(t) {
                            var e = this._skipEvents[t.type];
                            return this._skipEvents[t.type] = !1, e
                        },
                        _checkMouse: function(t, e) {
                            var i = e.relatedTarget;
                            if (!i) return !0;
                            try {
                                while (i && i !== t) i = i.parentNode
                            } catch (n) {
                                return !1
                            }
                            return i !== t
                        },
                        _getEvent: function() {
                            var t = s.event;
                            if (!t) {
                                var e = arguments.callee.caller;
                                while (e) {
                                    if (t = e["arguments"][0], t && s.Event === t.constructor) break;
                                    e = e.caller
                                }
                            }
                            return t
                        },
                        _filterClick: function(t, e) {
                            var i = t.timeStamp || t.originalEvent.timeStamp,
                                n = l.DomEvent._lastClick && i - l.DomEvent._lastClick;
                            if (!(n && n > 100 && n < 500 || t.target._simulatedClick && !t._simulated)) return l.DomEvent._lastClick = i, e(t);
                            l.DomEvent.stop(t)
                        }
                    }, l.DomEvent.on = l.DomEvent.addListener, l.DomEvent.off = l.DomEvent.removeListener, l.Draggable = l.Class.extend({
                        includes: l.Mixin.Events,
                        statics: {
                            START: l.Browser.touch ? ["touchstart", "mousedown"] : ["mousedown"],
                            END: {
                                mousedown: "mouseup",
                                touchstart: "touchend",
                                pointerdown: "touchend",
                                MSPointerDown: "touchend"
                            },
                            MOVE: {
                                mousedown: "mousemove",
                                touchstart: "touchmove",
                                pointerdown: "touchmove",
                                MSPointerDown: "touchmove"
                            }
                        },
                        initialize: function(t, e) {
                            this._element = t, this._dragStartTarget = e || t
                        },
                        enable: function() {
                            if (!this._enabled) {
                                for (var t = l.Draggable.START.length - 1; t >= 0; t--) l.DomEvent.on(this._dragStartTarget, l.Draggable.START[t], this._onDown, this);
                                this._enabled = !0
                            }
                        },
                        disable: function() {
                            if (this._enabled) {
                                for (var t = l.Draggable.START.length - 1; t >= 0; t--) l.DomEvent.off(this._dragStartTarget, l.Draggable.START[t], this._onDown, this);
                                this._enabled = !1, this._moved = !1
                            }
                        },
                        _onDown: function(t) {
                            if (this._moved = !1, !t.shiftKey && (1 === t.which || 1 === t.button || t.touches) && (l.DomEvent.stopPropagation(t), !l.Draggable._disabled && (l.DomUtil.disableImageDrag(), l.DomUtil.disableTextSelection(), !this._moving))) {
                                var e = t.touches ? t.touches[0] : t;
                                this._startPoint = new l.Point(e.clientX, e.clientY), this._startPos = this._newPos = l.DomUtil.getPosition(this._element), l.DomEvent.on(a, l.Draggable.MOVE[t.type], this._onMove, this).on(a, l.Draggable.END[t.type], this._onUp, this)
                            }
                        },
                        _onMove: function(t) {
                            if (t.touches && t.touches.length > 1) this._moved = !0;
                            else {
                                var e = t.touches && 1 === t.touches.length ? t.touches[0] : t,
                                    i = new l.Point(e.clientX, e.clientY),
                                    n = i.subtract(this._startPoint);
                                (n.x || n.y) && (l.Browser.touch && Math.abs(n.x) + Math.abs(n.y) < 3 || (l.DomEvent.preventDefault(t), this._moved || (this.fire("dragstart"), this._moved = !0, this._startPos = l.DomUtil.getPosition(this._element).subtract(n), l.DomUtil.addClass(a.body, "leaflet-dragging"), this._lastTarget = t.target || t.srcElement, l.DomUtil.addClass(this._lastTarget, "leaflet-drag-target")), this._newPos = this._startPos.add(n), this._moving = !0, l.Util.cancelAnimFrame(this._animRequest), this._animRequest = l.Util.requestAnimFrame(this._updatePosition, this, !0, this._dragStartTarget)))
                            }
                        },
                        _updatePosition: function() {
                            this.fire("predrag"), l.DomUtil.setPosition(this._element, this._newPos), this.fire("drag")
                        },
                        _onUp: function() {
                            for (var t in l.DomUtil.removeClass(a.body, "leaflet-dragging"), this._lastTarget && (l.DomUtil.removeClass(this._lastTarget, "leaflet-drag-target"), this._lastTarget = null), l.Draggable.MOVE) l.DomEvent.off(a, l.Draggable.MOVE[t], this._onMove).off(a, l.Draggable.END[t], this._onUp);
                            l.DomUtil.enableImageDrag(), l.DomUtil.enableTextSelection(), this._moved && this._moving && (l.Util.cancelAnimFrame(this._animRequest), this.fire("dragend", {
                                distance: this._newPos.distanceTo(this._startPos)
                            })), this._moving = !1
                        }
                    }), l.Handler = l.Class.extend({
                        initialize: function(t) {
                            this._map = t
                        },
                        enable: function() {
                            this._enabled || (this._enabled = !0, this.addHooks())
                        },
                        disable: function() {
                            this._enabled && (this._enabled = !1, this.removeHooks())
                        },
                        enabled: function() {
                            return !!this._enabled
                        }
                    }), l.Map.mergeOptions({
                        dragging: !0,
                        inertia: !l.Browser.android23,
                        inertiaDeceleration: 3400,
                        inertiaMaxSpeed: 1 / 0,
                        inertiaThreshold: l.Browser.touch ? 32 : 18,
                        easeLinearity: .25,
                        worldCopyJump: !1
                    }), l.Map.Drag = l.Handler.extend({
                        addHooks: function() {
                            if (!this._draggable) {
                                var t = this._map;
                                this._draggable = new l.Draggable(t._mapPane, t._container), this._draggable.on({
                                    dragstart: this._onDragStart,
                                    drag: this._onDrag,
                                    dragend: this._onDragEnd
                                }, this), t.options.worldCopyJump && (this._draggable.on("predrag", this._onPreDrag, this), t.on("viewreset", this._onViewReset, this), t.whenReady(this._onViewReset, this))
                            }
                            this._draggable.enable()
                        },
                        removeHooks: function() {
                            this._draggable.disable()
                        },
                        moved: function() {
                            return this._draggable && this._draggable._moved
                        },
                        _onDragStart: function() {
                            var t = this._map;
                            t._panAnim && t._panAnim.stop(), t.fire("movestart").fire("dragstart"), t.options.inertia && (this._positions = [], this._times = [])
                        },
                        _onDrag: function() {
                            if (this._map.options.inertia) {
                                var t = this._lastTime = +new Date,
                                    e = this._lastPos = this._draggable._newPos;
                                this._positions.push(e), this._times.push(t), t - this._times[0] > 200 && (this._positions.shift(), this._times.shift())
                            }
                            this._map.fire("move").fire("drag")
                        },
                        _onViewReset: function() {
                            var t = this._map.getSize()._divideBy(2),
                                e = this._map.latLngToLayerPoint([0, 0]);
                            this._initialWorldOffset = e.subtract(t).x, this._worldWidth = this._map.project([0, 180]).x
                        },
                        _onPreDrag: function() {
                            var t = this._worldWidth,
                                e = Math.round(t / 2),
                                i = this._initialWorldOffset,
                                n = this._draggable._newPos.x,
                                o = (n - e + i) % t + e - i,
                                s = (n + e + i) % t - e - i,
                                a = Math.abs(o + i) < Math.abs(s + i) ? o : s;
                            this._draggable._newPos.x = a
                        },
                        _onDragEnd: function(t) {
                            var e = this._map,
                                i = e.options,
                                n = +new Date - this._lastTime,
                                o = !i.inertia || n > i.inertiaThreshold || !this._positions[0];
                            if (e.fire("dragend", t), o) e.fire("moveend");
                            else {
                                var s = this._lastPos.subtract(this._positions[0]),
                                    a = (this._lastTime + n - this._times[0]) / 1e3,
                                    r = i.easeLinearity,
                                    h = s.multiplyBy(r / a),
                                    u = h.distanceTo([0, 0]),
                                    c = Math.min(i.inertiaMaxSpeed, u),
                                    p = h.multiplyBy(c / u),
                                    d = c / (i.inertiaDeceleration * r),
                                    _ = p.multiplyBy(-d / 2).round();
                                _.x && _.y ? (_ = e._limitOffset(_, e.options.maxBounds), l.Util.requestAnimFrame((function() {
                                    e.panBy(_, {
                                        duration: d,
                                        easeLinearity: r,
                                        noMoveStart: !0
                                    })
                                }))) : e.fire("moveend")
                            }
                        }
                    }), l.Map.addInitHook("addHandler", "dragging", l.Map.Drag), l.Map.mergeOptions({
                        doubleClickZoom: !0
                    }), l.Map.DoubleClickZoom = l.Handler.extend({
                        addHooks: function() {
                            this._map.on("dblclick", this._onDoubleClick, this)
                        },
                        removeHooks: function() {
                            this._map.off("dblclick", this._onDoubleClick, this)
                        },
                        _onDoubleClick: function(t) {
                            var e = this._map,
                                i = e.getZoom() + (t.originalEvent.shiftKey ? -1 : 1);
                            "center" === e.options.doubleClickZoom ? e.setZoom(i) : e.setZoomAround(t.containerPoint, i)
                        }
                    }), l.Map.addInitHook("addHandler", "doubleClickZoom", l.Map.DoubleClickZoom), l.Map.mergeOptions({
                        scrollWheelZoom: !0
                    }), l.Map.ScrollWheelZoom = l.Handler.extend({
                        addHooks: function() {
                            l.DomEvent.on(this._map._container, "mousewheel", this._onWheelScroll, this), l.DomEvent.on(this._map._container, "MozMousePixelScroll", l.DomEvent.preventDefault), this._delta = 0
                        },
                        removeHooks: function() {
                            l.DomEvent.off(this._map._container, "mousewheel", this._onWheelScroll), l.DomEvent.off(this._map._container, "MozMousePixelScroll", l.DomEvent.preventDefault)
                        },
                        _onWheelScroll: function(t) {
                            var e = l.DomEvent.getWheelDelta(t);
                            this._delta += e, this._lastMousePos = this._map.mouseEventToContainerPoint(t), this._startTime || (this._startTime = +new Date);
                            var i = Math.max(40 - (+new Date - this._startTime), 0);
                            clearTimeout(this._timer), this._timer = setTimeout(l.bind(this._performZoom, this), i), l.DomEvent.preventDefault(t), l.DomEvent.stopPropagation(t)
                        },
                        _performZoom: function() {
                            var t = this._map,
                                e = this._delta,
                                i = t.getZoom();
                            e = e > 0 ? Math.ceil(e) : Math.floor(e), e = Math.max(Math.min(e, 4), -4), e = t._limitZoom(i + e) - i, this._delta = 0, this._startTime = null, e && ("center" === t.options.scrollWheelZoom ? t.setZoom(i + e) : t.setZoomAround(this._lastMousePos, i + e))
                        }
                    }), l.Map.addInitHook("addHandler", "scrollWheelZoom", l.Map.ScrollWheelZoom), l.extend(l.DomEvent, {
                        _touchstart: l.Browser.msPointer ? "MSPointerDown" : l.Browser.pointer ? "pointerdown" : "touchstart",
                        _touchend: l.Browser.msPointer ? "MSPointerUp" : l.Browser.pointer ? "pointerup" : "touchend",
                        addDoubleTapListener: function(t, e, i) {
                            var n, o, s = !1,
                                r = 250,
                                h = "_leaflet_",
                                u = this._touchstart,
                                c = this._touchend,
                                p = [];

                            function d(t) {
                                var e;
                                if (l.Browser.pointer ? (p.push(t.pointerId), e = p.length) : e = t.touches.length, !(e > 1)) {
                                    var i = Date.now(),
                                        a = i - (n || i);
                                    o = t.touches ? t.touches[0] : t, s = a > 0 && a <= r, n = i
                                }
                            }

                            function _(t) {
                                if (l.Browser.pointer) {
                                    var i = p.indexOf(t.pointerId);
                                    if (-1 === i) return;
                                    p.splice(i, 1)
                                }
                                if (s) {
                                    if (l.Browser.pointer) {
                                        var a, r = {};
                                        for (var h in o) a = o[h], r[h] = "function" === typeof a ? a.bind(o) : a;
                                        o = r
                                    }
                                    o.type = "dblclick", e(o), n = null
                                }
                            }
                            t[h + u + i] = d, t[h + c + i] = _;
                            var m = l.Browser.pointer ? a.documentElement : t;
                            return t.addEventListener(u, d, !1), m.addEventListener(c, _, !1), l.Browser.pointer && m.addEventListener(l.DomEvent.POINTER_CANCEL, _, !1), this
                        },
                        removeDoubleTapListener: function(t, e) {
                            var i = "_leaflet_";
                            return t.removeEventListener(this._touchstart, t[i + this._touchstart + e], !1), (l.Browser.pointer ? a.documentElement : t).removeEventListener(this._touchend, t[i + this._touchend + e], !1), l.Browser.pointer && a.documentElement.removeEventListener(l.DomEvent.POINTER_CANCEL, t[i + this._touchend + e], !1), this
                        }
                    }), l.extend(l.DomEvent, {
                        POINTER_DOWN: l.Browser.msPointer ? "MSPointerDown" : "pointerdown",
                        POINTER_MOVE: l.Browser.msPointer ? "MSPointerMove" : "pointermove",
                        POINTER_UP: l.Browser.msPointer ? "MSPointerUp" : "pointerup",
                        POINTER_CANCEL: l.Browser.msPointer ? "MSPointerCancel" : "pointercancel",
                        _pointers: [],
                        _pointerDocumentListener: !1,
                        addPointerListener: function(t, e, i, n) {
                            switch (e) {
                                case "touchstart":
                                    return this.addPointerListenerStart(t, e, i, n);
                                case "touchend":
                                    return this.addPointerListenerEnd(t, e, i, n);
                                case "touchmove":
                                    return this.addPointerListenerMove(t, e, i, n);
                                default:
                                    throw "Unknown touch event type"
                            }
                        },
                        addPointerListenerStart: function(t, e, i, n) {
                            var o = "_leaflet_",
                                s = this._pointers,
                                r = function(t) {
                                    "mouse" !== t.pointerType && t.pointerType !== t.MSPOINTER_TYPE_MOUSE && l.DomEvent.preventDefault(t);
                                    for (var e = !1, n = 0; n < s.length; n++)
                                        if (s[n].pointerId === t.pointerId) {
                                            e = !0;
                                            break
                                        } e || s.push(t), t.touches = s.slice(), t.changedTouches = [t], i(t)
                                };
                            if (t[o + "touchstart" + n] = r, t.addEventListener(this.POINTER_DOWN, r, !1), !this._pointerDocumentListener) {
                                var h = function(t) {
                                    for (var e = 0; e < s.length; e++)
                                        if (s[e].pointerId === t.pointerId) {
                                            s.splice(e, 1);
                                            break
                                        }
                                };
                                a.documentElement.addEventListener(this.POINTER_UP, h, !1), a.documentElement.addEventListener(this.POINTER_CANCEL, h, !1), this._pointerDocumentListener = !0
                            }
                            return this
                        },
                        addPointerListenerMove: function(t, e, i, n) {
                            var o = "_leaflet_",
                                s = this._pointers;

                            function a(t) {
                                if (t.pointerType !== t.MSPOINTER_TYPE_MOUSE && "mouse" !== t.pointerType || 0 !== t.buttons) {
                                    for (var e = 0; e < s.length; e++)
                                        if (s[e].pointerId === t.pointerId) {
                                            s[e] = t;
                                            break
                                        } t.touches = s.slice(), t.changedTouches = [t], i(t)
                                }
                            }
                            return t[o + "touchmove" + n] = a, t.addEventListener(this.POINTER_MOVE, a, !1), this
                        },
                        addPointerListenerEnd: function(t, e, i, n) {
                            var o = "_leaflet_",
                                s = this._pointers,
                                a = function(t) {
                                    for (var e = 0; e < s.length; e++)
                                        if (s[e].pointerId === t.pointerId) {
                                            s.splice(e, 1);
                                            break
                                        } t.touches = s.slice(), t.changedTouches = [t], i(t)
                                };
                            return t[o + "touchend" + n] = a, t.addEventListener(this.POINTER_UP, a, !1), t.addEventListener(this.POINTER_CANCEL, a, !1), this
                        },
                        removePointerListener: function(t, e, i) {
                            var n = "_leaflet_",
                                o = t[n + e + i];
                            switch (e) {
                                case "touchstart":
                                    t.removeEventListener(this.POINTER_DOWN, o, !1);
                                    break;
                                case "touchmove":
                                    t.removeEventListener(this.POINTER_MOVE, o, !1);
                                    break;
                                case "touchend":
                                    t.removeEventListener(this.POINTER_UP, o, !1), t.removeEventListener(this.POINTER_CANCEL, o, !1);
                                    break
                            }
                            return this
                        }
                    }), l.Map.mergeOptions({
                        touchZoom: l.Browser.touch && !l.Browser.android23,
                        bounceAtZoomLimits: !0
                    }), l.Map.TouchZoom = l.Handler.extend({
                        addHooks: function() {
                            l.DomEvent.on(this._map._container, "touchstart", this._onTouchStart, this)
                        },
                        removeHooks: function() {
                            l.DomEvent.off(this._map._container, "touchstart", this._onTouchStart, this)
                        },
                        _onTouchStart: function(t) {
                            var e = this._map;
                            if (t.touches && 2 === t.touches.length && !e._animatingZoom && !this._zooming) {
                                var i = e.mouseEventToLayerPoint(t.touches[0]),
                                    n = e.mouseEventToLayerPoint(t.touches[1]),
                                    o = e._getCenterLayerPoint();
                                this._startCenter = i.add(n)._divideBy(2), this._startDist = i.distanceTo(n), this._moved = !1, this._zooming = !0, this._centerOffset = o.subtract(this._startCenter), e._panAnim && e._panAnim.stop(), l.DomEvent.on(a, "touchmove", this._onTouchMove, this).on(a, "touchend", this._onTouchEnd, this), l.DomEvent.preventDefault(t)
                            }
                        },
                        _onTouchMove: function(t) {
                            var e = this._map;
                            if (t.touches && 2 === t.touches.length && this._zooming) {
                                var i = e.mouseEventToLayerPoint(t.touches[0]),
                                    n = e.mouseEventToLayerPoint(t.touches[1]);
                                this._scale = i.distanceTo(n) / this._startDist, this._delta = i._add(n)._divideBy(2)._subtract(this._startCenter), 1 !== this._scale && (!e.options.bounceAtZoomLimits && (e.getZoom() === e.getMinZoom() && this._scale < 1 || e.getZoom() === e.getMaxZoom() && this._scale > 1) || (this._moved || (l.DomUtil.addClass(e._mapPane, "leaflet-touching"), e.fire("movestart").fire("zoomstart"), this._moved = !0), l.Util.cancelAnimFrame(this._animRequest), this._animRequest = l.Util.requestAnimFrame(this._updateOnMove, this, !0, this._map._container), l.DomEvent.preventDefault(t)))
                            }
                        },
                        _updateOnMove: function() {
                            var t = this._map,
                                e = this._getScaleOrigin(),
                                i = t.layerPointToLatLng(e),
                                n = t.getScaleZoom(this._scale);
                            t._animateZoom(i, n, this._startCenter, this._scale, this._delta, !1, !0)
                        },
                        _onTouchEnd: function() {
                            if (this._moved && this._zooming) {
                                var t = this._map;
                                this._zooming = !1, l.DomUtil.removeClass(t._mapPane, "leaflet-touching"), l.Util.cancelAnimFrame(this._animRequest), l.DomEvent.off(a, "touchmove", this._onTouchMove).off(a, "touchend", this._onTouchEnd);
                                var e = this._getScaleOrigin(),
                                    i = t.layerPointToLatLng(e),
                                    n = t.getZoom(),
                                    o = t.getScaleZoom(this._scale) - n,
                                    s = o > 0 ? Math.ceil(o) : Math.floor(o),
                                    r = t._limitZoom(n + s),
                                    h = t.getZoomScale(r) / this._scale;
                                t._animateZoom(i, r, e, h)
                            } else this._zooming = !1
                        },
                        _getScaleOrigin: function() {
                            var t = this._centerOffset.subtract(this._delta).divideBy(this._scale);
                            return this._startCenter.add(t)
                        }
                    }), l.Map.addInitHook("addHandler", "touchZoom", l.Map.TouchZoom), l.Map.mergeOptions({
                        tap: !0,
                        tapTolerance: 15
                    }), l.Map.Tap = l.Handler.extend({
                        addHooks: function() {
                            l.DomEvent.on(this._map._container, "touchstart", this._onDown, this)
                        },
                        removeHooks: function() {
                            l.DomEvent.off(this._map._container, "touchstart", this._onDown, this)
                        },
                        _onDown: function(t) {
                            if (t.touches) {
                                if (l.DomEvent.preventDefault(t), this._fireClick = !0, t.touches.length > 1) return this._fireClick = !1, void clearTimeout(this._holdTimeout);
                                var e = t.touches[0],
                                    i = e.target;
                                this._startPos = this._newPos = new l.Point(e.clientX, e.clientY), i.tagName && "a" === i.tagName.toLowerCase() && l.DomUtil.addClass(i, "leaflet-active"), this._holdTimeout = setTimeout(l.bind((function() {
                                    this._isTapValid() && (this._fireClick = !1, this._onUp(), this._simulateEvent("contextmenu", e))
                                }), this), 1e3), l.DomEvent.on(a, "touchmove", this._onMove, this).on(a, "touchend", this._onUp, this)
                            }
                        },
                        _onUp: function(t) {
                            if (clearTimeout(this._holdTimeout), l.DomEvent.off(a, "touchmove", this._onMove, this).off(a, "touchend", this._onUp, this), this._fireClick && t && t.changedTouches) {
                                var e = t.changedTouches[0],
                                    i = e.target;
                                i && i.tagName && "a" === i.tagName.toLowerCase() && l.DomUtil.removeClass(i, "leaflet-active"), this._isTapValid() && this._simulateEvent("click", e)
                            }
                        },
                        _isTapValid: function() {
                            return this._newPos.distanceTo(this._startPos) <= this._map.options.tapTolerance
                        },
                        _onMove: function(t) {
                            var e = t.touches[0];
                            this._newPos = new l.Point(e.clientX, e.clientY)
                        },
                        _simulateEvent: function(t, e) {
                            var i = a.createEvent("MouseEvents");
                            i._simulated = !0, e.target._simulatedClick = !0, i.initMouseEvent(t, !0, !0, s, 1, e.screenX, e.screenY, e.clientX, e.clientY, !1, !1, !1, !1, 0, null), e.target.dispatchEvent(i)
                        }
                    }), l.Browser.touch && !l.Browser.pointer && l.Map.addInitHook("addHandler", "tap", l.Map.Tap), l.Map.mergeOptions({
                        boxZoom: !0
                    }), l.Map.BoxZoom = l.Handler.extend({
                        initialize: function(t) {
                            this._map = t, this._container = t._container, this._pane = t._panes.overlayPane, this._moved = !1
                        },
                        addHooks: function() {
                            l.DomEvent.on(this._container, "mousedown", this._onMouseDown, this)
                        },
                        removeHooks: function() {
                            l.DomEvent.off(this._container, "mousedown", this._onMouseDown), this._moved = !1
                        },
                        moved: function() {
                            return this._moved
                        },
                        _onMouseDown: function(t) {
                            if (this._moved = !1, !t.shiftKey || 1 !== t.which && 1 !== t.button) return !1;
                            l.DomUtil.disableTextSelection(), l.DomUtil.disableImageDrag(), this._startLayerPoint = this._map.mouseEventToLayerPoint(t), l.DomEvent.on(a, "mousemove", this._onMouseMove, this).on(a, "mouseup", this._onMouseUp, this).on(a, "keydown", this._onKeyDown, this)
                        },
                        _onMouseMove: function(t) {
                            this._moved || (this._box = l.DomUtil.create("div", "leaflet-zoom-box", this._pane), l.DomUtil.setPosition(this._box, this._startLayerPoint), this._container.style.cursor = "crosshair", this._map.fire("boxzoomstart"));
                            var e = this._startLayerPoint,
                                i = this._box,
                                n = this._map.mouseEventToLayerPoint(t),
                                o = n.subtract(e),
                                s = new l.Point(Math.min(n.x, e.x), Math.min(n.y, e.y));
                            l.DomUtil.setPosition(i, s), this._moved = !0, i.style.width = Math.max(0, Math.abs(o.x) - 4) + "px", i.style.height = Math.max(0, Math.abs(o.y) - 4) + "px"
                        },
                        _finish: function() {
                            this._moved && (this._pane.removeChild(this._box), this._container.style.cursor = ""), l.DomUtil.enableTextSelection(), l.DomUtil.enableImageDrag(), l.DomEvent.off(a, "mousemove", this._onMouseMove).off(a, "mouseup", this._onMouseUp).off(a, "keydown", this._onKeyDown)
                        },
                        _onMouseUp: function(t) {
                            this._finish();
                            var e = this._map,
                                i = e.mouseEventToLayerPoint(t);
                            if (!this._startLayerPoint.equals(i)) {
                                var n = new l.LatLngBounds(e.layerPointToLatLng(this._startLayerPoint), e.layerPointToLatLng(i));
                                e.fitBounds(n), e.fire("boxzoomend", {
                                    boxZoomBounds: n
                                })
                            }
                        },
                        _onKeyDown: function(t) {
                            27 === t.keyCode && this._finish()
                        }
                    }), l.Map.addInitHook("addHandler", "boxZoom", l.Map.BoxZoom), l.Map.mergeOptions({
                        keyboard: !0,
                        keyboardPanOffset: 80,
                        keyboardZoomOffset: 1
                    }), l.Map.Keyboard = l.Handler.extend({
                        keyCodes: {
                            left: [37],
                            right: [39],
                            down: [40],
                            up: [38],
                            zoomIn: [187, 107, 61, 171],
                            zoomOut: [189, 109, 173]
                        },
                        initialize: function(t) {
                            this._map = t, this._setPanOffset(t.options.keyboardPanOffset), this._setZoomOffset(t.options.keyboardZoomOffset)
                        },
                        addHooks: function() {
                            var t = this._map._container; - 1 === t.tabIndex && (t.tabIndex = "0"), l.DomEvent.on(t, "focus", this._onFocus, this).on(t, "blur", this._onBlur, this).on(t, "mousedown", this._onMouseDown, this), this._map.on("focus", this._addHooks, this).on("blur", this._removeHooks, this)
                        },
                        removeHooks: function() {
                            this._removeHooks();
                            var t = this._map._container;
                            l.DomEvent.off(t, "focus", this._onFocus, this).off(t, "blur", this._onBlur, this).off(t, "mousedown", this._onMouseDown, this), this._map.off("focus", this._addHooks, this).off("blur", this._removeHooks, this)
                        },
                        _onMouseDown: function() {
                            if (!this._focused) {
                                var t = a.body,
                                    e = a.documentElement,
                                    i = t.scrollTop || e.scrollTop,
                                    n = t.scrollLeft || e.scrollLeft;
                                this._map._container.focus(), s.scrollTo(n, i)
                            }
                        },
                        _onFocus: function() {
                            this._focused = !0, this._map.fire("focus")
                        },
                        _onBlur: function() {
                            this._focused = !1, this._map.fire("blur")
                        },
                        _setPanOffset: function(t) {
                            var e, i, n = this._panKeys = {},
                                o = this.keyCodes;
                            for (e = 0, i = o.left.length; e < i; e++) n[o.left[e]] = [-1 * t, 0];
                            for (e = 0, i = o.right.length; e < i; e++) n[o.right[e]] = [t, 0];
                            for (e = 0, i = o.down.length; e < i; e++) n[o.down[e]] = [0, t];
                            for (e = 0, i = o.up.length; e < i; e++) n[o.up[e]] = [0, -1 * t]
                        },
                        _setZoomOffset: function(t) {
                            var e, i, n = this._zoomKeys = {},
                                o = this.keyCodes;
                            for (e = 0, i = o.zoomIn.length; e < i; e++) n[o.zoomIn[e]] = t;
                            for (e = 0, i = o.zoomOut.length; e < i; e++) n[o.zoomOut[e]] = -t
                        },
                        _addHooks: function() {
                            l.DomEvent.on(a, "keydown", this._onKeyDown, this)
                        },
                        _removeHooks: function() {
                            l.DomEvent.off(a, "keydown", this._onKeyDown, this)
                        },
                        _onKeyDown: function(t) {
                            var e = t.keyCode,
                                i = this._map;
                            if (e in this._panKeys) {
                                if (i._panAnim && i._panAnim._inProgress) return;
                                i.panBy(this._panKeys[e]), i.options.maxBounds && i.panInsideBounds(i.options.maxBounds)
                            } else {
                                if (!(e in this._zoomKeys)) return;
                                i.setZoom(i.getZoom() + this._zoomKeys[e])
                            }
                            l.DomEvent.stop(t)
                        }
                    }), l.Map.addInitHook("addHandler", "keyboard", l.Map.Keyboard), l.Handler.MarkerDrag = l.Handler.extend({
                        initialize: function(t) {
                            this._marker = t
                        },
                        addHooks: function() {
                            var t = this._marker._icon;
                            this._draggable || (this._draggable = new l.Draggable(t, t)), this._draggable.on("dragstart", this._onDragStart, this).on("drag", this._onDrag, this).on("dragend", this._onDragEnd, this), this._draggable.enable(), l.DomUtil.addClass(this._marker._icon, "leaflet-marker-draggable")
                        },
                        removeHooks: function() {
                            this._draggable.off("dragstart", this._onDragStart, this).off("drag", this._onDrag, this).off("dragend", this._onDragEnd, this), this._draggable.disable(), l.DomUtil.removeClass(this._marker._icon, "leaflet-marker-draggable")
                        },
                        moved: function() {
                            return this._draggable && this._draggable._moved
                        },
                        _onDragStart: function() {
                            this._marker.closePopup().fire("movestart").fire("dragstart")
                        },
                        _onDrag: function() {
                            var t = this._marker,
                                e = t._shadow,
                                i = l.DomUtil.getPosition(t._icon),
                                n = t._map.layerPointToLatLng(i);
                            e && l.DomUtil.setPosition(e, i), t._latlng = n, t.fire("move", {
                                latlng: n
                            }).fire("drag")
                        },
                        _onDragEnd: function(t) {
                            this._marker.fire("moveend").fire("dragend", t)
                        }
                    }), l.Control = l.Class.extend({
                        options: {
                            position: "topright"
                        },
                        initialize: function(t) {
                            l.setOptions(this, t)
                        },
                        getPosition: function() {
                            return this.options.position
                        },
                        setPosition: function(t) {
                            var e = this._map;
                            return e && e.removeControl(this), this.options.position = t, e && e.addControl(this), this
                        },
                        getContainer: function() {
                            return this._container
                        },
                        addTo: function(t) {
                            this._map = t;
                            var e = this._container = this.onAdd(t),
                                i = this.getPosition(),
                                n = t._controlCorners[i];
                            return l.DomUtil.addClass(e, "leaflet-control"), -1 !== i.indexOf("bottom") ? n.insertBefore(e, n.firstChild) : n.appendChild(e), this
                        },
                        removeFrom: function(t) {
                            var e = this.getPosition(),
                                i = t._controlCorners[e];
                            return i.removeChild(this._container), this._map = null, this.onRemove && this.onRemove(t), this
                        },
                        _refocusOnMap: function() {
                            this._map && this._map.getContainer().focus()
                        }
                    }), l.control = function(t) {
                        return new l.Control(t)
                    }, l.Map.include({
                        addControl: function(t) {
                            return t.addTo(this), this
                        },
                        removeControl: function(t) {
                            return t.removeFrom(this), this
                        },
                        _initControlPos: function() {
                            var t = this._controlCorners = {},
                                e = "leaflet-",
                                i = this._controlContainer = l.DomUtil.create("div", e + "control-container", this._container);

                            function n(n, o) {
                                var s = e + n + " " + e + o;
                                t[n + o] = l.DomUtil.create("div", s, i)
                            }
                            n("top", "left"), n("top", "right"), n("bottom", "left"), n("bottom", "right")
                        },
                        _clearControlPos: function() {
                            this._container.removeChild(this._controlContainer)
                        }
                    }), l.Control.Zoom = l.Control.extend({
                        options: {
                            position: "topleft",
                            zoomInText: "+",
                            zoomInTitle: "Zoom in",
                            zoomOutText: "-",
                            zoomOutTitle: "Zoom out"
                        },
                        onAdd: function(t) {
                            var e = "leaflet-control-zoom",
                                i = l.DomUtil.create("div", e + " leaflet-bar");
                            return this._map = t, this._zoomInButton = this._createButton(this.options.zoomInText, this.options.zoomInTitle, e + "-in", i, this._zoomIn, this), this._zoomOutButton = this._createButton(this.options.zoomOutText, this.options.zoomOutTitle, e + "-out", i, this._zoomOut, this), this._updateDisabled(), t.on("zoomend zoomlevelschange", this._updateDisabled, this), i
                        },
                        onRemove: function(t) {
                            t.off("zoomend zoomlevelschange", this._updateDisabled, this)
                        },
                        _zoomIn: function(t) {
                            this._map.zoomIn(t.shiftKey ? 3 : 1)
                        },
                        _zoomOut: function(t) {
                            this._map.zoomOut(t.shiftKey ? 3 : 1)
                        },
                        _createButton: function(t, e, i, n, o, s) {
                            var a = l.DomUtil.create("a", i, n);
                            a.innerHTML = t, a.href = "#", a.title = e;
                            var r = l.DomEvent.stopPropagation;
                            return l.DomEvent.on(a, "click", r).on(a, "mousedown", r).on(a, "dblclick", r).on(a, "click", l.DomEvent.preventDefault).on(a, "click", o, s).on(a, "click", this._refocusOnMap, s), a
                        },
                        _updateDisabled: function() {
                            var t = this._map,
                                e = "leaflet-disabled";
                            l.DomUtil.removeClass(this._zoomInButton, e), l.DomUtil.removeClass(this._zoomOutButton, e), t._zoom === t.getMinZoom() && l.DomUtil.addClass(this._zoomOutButton, e), t._zoom === t.getMaxZoom() && l.DomUtil.addClass(this._zoomInButton, e)
                        }
                    }), l.Map.mergeOptions({
                        zoomControl: !0
                    }), l.Map.addInitHook((function() {
                        this.options.zoomControl && (this.zoomControl = new l.Control.Zoom, this.addControl(this.zoomControl))
                    })), l.control.zoom = function(t) {
                        return new l.Control.Zoom(t)
                    }, l.Control.Attribution = l.Control.extend({
                        options: {
                            position: "bottomright",
                            prefix: '<a href="http://leafletjs.com" title="A JS library for interactive maps">Leaflet</a>'
                        },
                        initialize: function(t) {
                            l.setOptions(this, t), this._attributions = {}
                        },
                        onAdd: function(t) {
                            for (var e in this._container = l.DomUtil.create("div", "leaflet-control-attribution"), l.DomEvent.disableClickPropagation(this._container), t._layers) t._layers[e].getAttribution && this.addAttribution(t._layers[e].getAttribution());
                            return t.on("layeradd", this._onLayerAdd, this).on("layerremove", this._onLayerRemove, this), this._update(), this._container
                        },
                        onRemove: function(t) {
                            t.off("layeradd", this._onLayerAdd).off("layerremove", this._onLayerRemove)
                        },
                        setPrefix: function(t) {
                            return this.options.prefix = t, this._update(), this
                        },
                        addAttribution: function(t) {
                            if (t) return this._attributions[t] || (this._attributions[t] = 0), this._attributions[t]++, this._update(), this
                        },
                        removeAttribution: function(t) {
                            if (t) return this._attributions[t] && (this._attributions[t]--, this._update()), this
                        },
                        _update: function() {
                            if (this._map) {
                                var t = [];
                                for (var e in this._attributions) this._attributions[e] && t.push(e);
                                var i = [];
                                this.options.prefix && i.push(this.options.prefix), t.length && i.push(t.join(", ")), this._container.innerHTML = i.join(" | ")
                            }
                        },
                        _onLayerAdd: function(t) {
                            t.layer.getAttribution && this.addAttribution(t.layer.getAttribution())
                        },
                        _onLayerRemove: function(t) {
                            t.layer.getAttribution && this.removeAttribution(t.layer.getAttribution())
                        }
                    }), l.Map.mergeOptions({
                        attributionControl: !0
                    }), l.Map.addInitHook((function() {
                        this.options.attributionControl && (this.attributionControl = (new l.Control.Attribution).addTo(this))
                    })), l.control.attribution = function(t) {
                        return new l.Control.Attribution(t)
                    }, l.Control.Scale = l.Control.extend({
                        options: {
                            position: "bottomleft",
                            maxWidth: 100,
                            metric: !0,
                            imperial: !0,
                            updateWhenIdle: !1
                        },
                        onAdd: function(t) {
                            this._map = t;
                            var e = "leaflet-control-scale",
                                i = l.DomUtil.create("div", e),
                                n = this.options;
                            return this._addScales(n, e, i), t.on(n.updateWhenIdle ? "moveend" : "move", this._update, this), t.whenReady(this._update, this), i
                        },
                        onRemove: function(t) {
                            t.off(this.options.updateWhenIdle ? "moveend" : "move", this._update, this)
                        },
                        _addScales: function(t, e, i) {
                            t.metric && (this._mScale = l.DomUtil.create("div", e + "-line", i)), t.imperial && (this._iScale = l.DomUtil.create("div", e + "-line", i))
                        },
                        _update: function() {
                            var t = this._map.getBounds(),
                                e = t.getCenter().lat,
                                i = 6378137 * Math.PI * Math.cos(e * Math.PI / 180),
                                n = i * (t.getNorthEast().lng - t.getSouthWest().lng) / 180,
                                o = this._map.getSize(),
                                s = this.options,
                                a = 0;
                            o.x > 0 && (a = n * (s.maxWidth / o.x)), this._updateScales(s, a)
                        },
                        _updateScales: function(t, e) {
                            t.metric && e && this._updateMetric(e), t.imperial && e && this._updateImperial(e)
                        },
                        _updateMetric: function(t) {
                            var e = this._getRoundNum(t);
                            this._mScale.style.width = this._getScaleWidth(e / t) + "px", this._mScale.innerHTML = e < 1e3 ? e + " m" : e / 1e3 + " km"
                        },
                        _updateImperial: function(t) {
                            var e, i, n, o = 3.2808399 * t,
                                s = this._iScale;
                            o > 5280 ? (e = o / 5280, i = this._getRoundNum(e), s.style.width = this._getScaleWidth(i / e) + "px", s.innerHTML = i + " mi") : (n = this._getRoundNum(o), s.style.width = this._getScaleWidth(n / o) + "px", s.innerHTML = n + " ft")
                        },
                        _getScaleWidth: function(t) {
                            return Math.round(this.options.maxWidth * t) - 10
                        },
                        _getRoundNum: function(t) {
                            var e = Math.pow(10, (Math.floor(t) + "").length - 1),
                                i = t / e;
                            return i = i >= 10 ? 10 : i >= 5 ? 5 : i >= 3 ? 3 : i >= 2 ? 2 : 1, e * i
                        }
                    }), l.control.scale = function(t) {
                        return new l.Control.Scale(t)
                    }, l.Control.Layers = l.Control.extend({
                        options: {
                            collapsed: !0,
                            position: "topright",
                            autoZIndex: !0
                        },
                        initialize: function(t, e, i) {
                            for (var n in l.setOptions(this, i), this._layers = {}, this._lastZIndex = 0, this._handlingClick = !1, t) this._addLayer(t[n], n);
                            for (n in e) this._addLayer(e[n], n, !0)
                        },
                        onAdd: function(t) {
                            return this._initLayout(), this._update(), t.on("layeradd", this._onLayerChange, this).on("layerremove", this._onLayerChange, this), this._container
                        },
                        onRemove: function(t) {
                            t.off("layeradd", this._onLayerChange, this).off("layerremove", this._onLayerChange, this)
                        },
                        addBaseLayer: function(t, e) {
                            return this._addLayer(t, e), this._update(), this
                        },
                        addOverlay: function(t, e) {
                            return this._addLayer(t, e, !0), this._update(), this
                        },
                        removeLayer: function(t) {
                            var e = l.stamp(t);
                            return delete this._layers[e], this._update(), this
                        },
                        _initLayout: function() {
                            var t = "leaflet-control-layers",
                                e = this._container = l.DomUtil.create("div", t);
                            e.setAttribute("aria-haspopup", !0), l.Browser.touch ? l.DomEvent.on(e, "click", l.DomEvent.stopPropagation) : l.DomEvent.disableClickPropagation(e).disableScrollPropagation(e);
                            var i = this._form = l.DomUtil.create("form", t + "-list");
                            if (this.options.collapsed) {
                                l.Browser.android || l.DomEvent.on(e, "mouseover", this._expand, this).on(e, "mouseout", this._collapse, this);
                                var n = this._layersLink = l.DomUtil.create("a", t + "-toggle", e);
                                n.href = "#", n.title = "Layers", l.Browser.touch ? l.DomEvent.on(n, "click", l.DomEvent.stop).on(n, "click", this._expand, this) : l.DomEvent.on(n, "focus", this._expand, this), l.DomEvent.on(i, "click", (function() {
                                    setTimeout(l.bind(this._onInputClick, this), 0)
                                }), this), this._map.on("click", this._collapse, this)
                            } else this._expand();
                            this._baseLayersList = l.DomUtil.create("div", t + "-base", i), this._separator = l.DomUtil.create("div", t + "-separator", i), this._overlaysList = l.DomUtil.create("div", t + "-overlays", i), e.appendChild(i)
                        },
                        _addLayer: function(t, e, i) {
                            var n = l.stamp(t);
                            this._layers[n] = {
                                layer: t,
                                name: e,
                                overlay: i
                            }, this.options.autoZIndex && t.setZIndex && (this._lastZIndex++, t.setZIndex(this._lastZIndex))
                        },
                        _update: function() {
                            if (this._container) {
                                this._baseLayersList.innerHTML = "", this._overlaysList.innerHTML = "";
                                var t, e, i = !1,
                                    n = !1;
                                for (t in this._layers) e = this._layers[t], this._addItem(e), n = n || e.overlay, i = i || !e.overlay;
                                this._separator.style.display = n && i ? "" : "none"
                            }
                        },
                        _onLayerChange: function(t) {
                            var e = this._layers[l.stamp(t.layer)];
                            if (e) {
                                this._handlingClick || this._update();
                                var i = e.overlay ? "layeradd" === t.type ? "overlayadd" : "overlayremove" : "layeradd" === t.type ? "baselayerchange" : null;
                                i && this._map.fire(i, e)
                            }
                        },
                        _createRadioElement: function(t, e) {
                            var i = '<input type="radio" class="leaflet-control-layers-selector" name="' + t + '"';
                            e && (i += ' checked="checked"'), i += "/>";
                            var n = a.createElement("div");
                            return n.innerHTML = i, n.firstChild
                        },
                        _addItem: function(t) {
                            var e, i = a.createElement("label"),
                                n = this._map.hasLayer(t.layer);
                            t.overlay ? (e = a.createElement("input"), e.type = "checkbox", e.className = "leaflet-control-layers-selector", e.defaultChecked = n) : e = this._createRadioElement("leaflet-base-layers", n), e.layerId = l.stamp(t.layer), l.DomEvent.on(e, "click", this._onInputClick, this);
                            var o = a.createElement("span");
                            o.innerHTML = " " + t.name, i.appendChild(e), i.appendChild(o);
                            var s = t.overlay ? this._overlaysList : this._baseLayersList;
                            return s.appendChild(i), i
                        },
                        _onInputClick: function() {
                            var t, e, i, n = this._form.getElementsByTagName("input"),
                                o = n.length;
                            for (this._handlingClick = !0, t = 0; t < o; t++) e = n[t], i = this._layers[e.layerId], e.checked && !this._map.hasLayer(i.layer) ? this._map.addLayer(i.layer) : !e.checked && this._map.hasLayer(i.layer) && this._map.removeLayer(i.layer);
                            this._handlingClick = !1, this._refocusOnMap()
                        },
                        _expand: function() {
                            l.DomUtil.addClass(this._container, "leaflet-control-layers-expanded")
                        },
                        _collapse: function() {
                            this._container.className = this._container.className.replace(" leaflet-control-layers-expanded", "")
                        }
                    }), l.control.layers = function(t, e, i) {
                        return new l.Control.Layers(t, e, i)
                    }, l.PosAnimation = l.Class.extend({
                        includes: l.Mixin.Events,
                        run: function(t, e, i, n) {
                            this.stop(), this._el = t, this._inProgress = !0, this._newPos = e, this.fire("start"), t.style[l.DomUtil.TRANSITION] = "all " + (i || .25) + "s cubic-bezier(0,0," + (n || .5) + ",1)", l.DomEvent.on(t, l.DomUtil.TRANSITION_END, this._onTransitionEnd, this), l.DomUtil.setPosition(t, e), l.Util.falseFn(t.offsetWidth), this._stepTimer = setInterval(l.bind(this._onStep, this), 50)
                        },
                        stop: function() {
                            this._inProgress && (l.DomUtil.setPosition(this._el, this._getPos()), this._onTransitionEnd(), l.Util.falseFn(this._el.offsetWidth))
                        },
                        _onStep: function() {
                            var t = this._getPos();
                            t ? (this._el._leaflet_pos = t, this.fire("step")) : this._onTransitionEnd()
                        },
                        _transformRe: /([-+]?(?:\d*\.)?\d+)\D*, ([-+]?(?:\d*\.)?\d+)\D*\)/,
                        _getPos: function() {
                            var t, e, i, n = this._el,
                                o = s.getComputedStyle(n);
                            if (l.Browser.any3d) {
                                if (i = o[l.DomUtil.TRANSFORM].match(this._transformRe), !i) return;
                                t = parseFloat(i[1]), e = parseFloat(i[2])
                            } else t = parseFloat(o.left), e = parseFloat(o.top);
                            return new l.Point(t, e, !0)
                        },
                        _onTransitionEnd: function() {
                            l.DomEvent.off(this._el, l.DomUtil.TRANSITION_END, this._onTransitionEnd, this), this._inProgress && (this._inProgress = !1, this._el.style[l.DomUtil.TRANSITION] = "", this._el._leaflet_pos = this._newPos, clearInterval(this._stepTimer), this.fire("step").fire("end"))
                        }
                    }), l.Map.include({
                        setView: function(t, e, i) {
                            if (e = e === r ? this._zoom : this._limitZoom(e), t = this._limitCenter(l.latLng(t), e, this.options.maxBounds), i = i || {}, this._panAnim && this._panAnim.stop(), this._loaded && !i.reset && !0 !== i) {
                                i.animate !== r && (i.zoom = l.extend({
                                    animate: i.animate
                                }, i.zoom), i.pan = l.extend({
                                    animate: i.animate
                                }, i.pan));
                                var n = this._zoom !== e ? this._tryAnimatedZoom && this._tryAnimatedZoom(t, e, i.zoom) : this._tryAnimatedPan(t, i.pan);
                                if (n) return clearTimeout(this._sizeTimer), this
                            }
                            return this._resetView(t, e), this
                        },
                        panBy: function(t, e) {
                            if (t = l.point(t).round(), e = e || {}, !t.x && !t.y) return this;
                            if (this._panAnim || (this._panAnim = new l.PosAnimation, this._panAnim.on({
                                    step: this._onPanTransitionStep,
                                    end: this._onPanTransitionEnd
                                }, this)), e.noMoveStart || this.fire("movestart"), !1 !== e.animate) {
                                l.DomUtil.addClass(this._mapPane, "leaflet-pan-anim");
                                var i = this._getMapPanePos().subtract(t);
                                this._panAnim.run(this._mapPane, i, e.duration || .25, e.easeLinearity)
                            } else this._rawPanBy(t), this.fire("move").fire("moveend");
                            return this
                        },
                        _onPanTransitionStep: function() {
                            this.fire("move")
                        },
                        _onPanTransitionEnd: function() {
                            l.DomUtil.removeClass(this._mapPane, "leaflet-pan-anim"), this.fire("moveend")
                        },
                        _tryAnimatedPan: function(t, e) {
                            var i = this._getCenterOffset(t)._floor();
                            return !(!0 !== (e && e.animate) && !this.getSize().contains(i)) && (this.panBy(i, e), !0)
                        }
                    }), l.PosAnimation = l.DomUtil.TRANSITION ? l.PosAnimation : l.PosAnimation.extend({
                        run: function(t, e, i, n) {
                            this.stop(), this._el = t, this._inProgress = !0, this._duration = i || .25, this._easeOutPower = 1 / Math.max(n || .5, .2), this._startPos = l.DomUtil.getPosition(t), this._offset = e.subtract(this._startPos), this._startTime = +new Date, this.fire("start"), this._animate()
                        },
                        stop: function() {
                            this._inProgress && (this._step(), this._complete())
                        },
                        _animate: function() {
                            this._animId = l.Util.requestAnimFrame(this._animate, this), this._step()
                        },
                        _step: function() {
                            var t = +new Date - this._startTime,
                                e = 1e3 * this._duration;
                            t < e ? this._runFrame(this._easeOut(t / e)) : (this._runFrame(1), this._complete())
                        },
                        _runFrame: function(t) {
                            var e = this._startPos.add(this._offset.multiplyBy(t));
                            l.DomUtil.setPosition(this._el, e), this.fire("step")
                        },
                        _complete: function() {
                            l.Util.cancelAnimFrame(this._animId), this._inProgress = !1, this.fire("end")
                        },
                        _easeOut: function(t) {
                            return 1 - Math.pow(1 - t, this._easeOutPower)
                        }
                    }), l.Map.mergeOptions({
                        zoomAnimation: !0,
                        zoomAnimationThreshold: 4
                    }), l.DomUtil.TRANSITION && l.Map.addInitHook((function() {
                        this._zoomAnimated = this.options.zoomAnimation && l.DomUtil.TRANSITION && l.Browser.any3d && !l.Browser.android23 && !l.Browser.mobileOpera, this._zoomAnimated && l.DomEvent.on(this._mapPane, l.DomUtil.TRANSITION_END, this._catchTransitionEnd, this)
                    })), l.Map.include(l.DomUtil.TRANSITION ? {
                        _catchTransitionEnd: function(t) {
                            this._animatingZoom && t.propertyName.indexOf("transform") >= 0 && this._onZoomTransitionEnd()
                        },
                        _nothingToAnimate: function() {
                            return !this._container.getElementsByClassName("leaflet-zoom-animated").length
                        },
                        _tryAnimatedZoom: function(t, e, i) {
                            if (this._animatingZoom) return !0;
                            if (i = i || {}, !this._zoomAnimated || !1 === i.animate || this._nothingToAnimate() || Math.abs(e - this._zoom) > this.options.zoomAnimationThreshold) return !1;
                            var n = this.getZoomScale(e),
                                o = this._getCenterOffset(t)._divideBy(1 - 1 / n),
                                s = this._getCenterLayerPoint()._add(o);
                            return !(!0 !== i.animate && !this.getSize().contains(o)) && (this.fire("movestart").fire("zoomstart"), this._animateZoom(t, e, s, n, null, !0), !0)
                        },
                        _animateZoom: function(t, e, i, n, o, s, a) {
                            a || (this._animatingZoom = !0), l.DomUtil.addClass(this._mapPane, "leaflet-zoom-anim"), this._animateToCenter = t, this._animateToZoom = e, l.Draggable && (l.Draggable._disabled = !0), l.Util.requestAnimFrame((function() {
                                this.fire("zoomanim", {
                                    center: t,
                                    zoom: e,
                                    origin: i,
                                    scale: n,
                                    delta: o,
                                    backwards: s
                                }), setTimeout(l.bind(this._onZoomTransitionEnd, this), 250)
                            }), this)
                        },
                        _onZoomTransitionEnd: function() {
                            this._animatingZoom && (this._animatingZoom = !1, l.DomUtil.removeClass(this._mapPane, "leaflet-zoom-anim"), l.Util.requestAnimFrame((function() {
                                this._resetView(this._animateToCenter, this._animateToZoom, !0, !0), l.Draggable && (l.Draggable._disabled = !1)
                            }), this))
                        }
                    } : {}), l.TileLayer.include({
                        _animateZoom: function(t) {
                            this._animating || (this._animating = !0, this._prepareBgBuffer());
                            var e = this._bgBuffer,
                                i = l.DomUtil.TRANSFORM,
                                n = t.delta ? l.DomUtil.getTranslateString(t.delta) : e.style[i],
                                o = l.DomUtil.getScaleString(t.scale, t.origin);
                            e.style[i] = t.backwards ? o + " " + n : n + " " + o
                        },
                        _endZoomAnim: function() {
                            var t = this._tileContainer,
                                e = this._bgBuffer;
                            t.style.visibility = "", t.parentNode.appendChild(t), l.Util.falseFn(e.offsetWidth);
                            var i = this._map.getZoom();
                            (i > this.options.maxZoom || i < this.options.minZoom) && this._clearBgBuffer(), this._animating = !1
                        },
                        _clearBgBuffer: function() {
                            var t = this._map;
                            !t || t._animatingZoom || t.touchZoom._zooming || (this._bgBuffer.innerHTML = "", this._bgBuffer.style[l.DomUtil.TRANSFORM] = "")
                        },
                        _prepareBgBuffer: function() {
                            var t = this._tileContainer,
                                e = this._bgBuffer,
                                i = this._getLoadedTilesPercentage(e),
                                n = this._getLoadedTilesPercentage(t);
                            if (e && i > .5 && n < .5) return t.style.visibility = "hidden", void this._stopLoadingImages(t);
                            e.style.visibility = "hidden", e.style[l.DomUtil.TRANSFORM] = "", this._tileContainer = e, e = this._bgBuffer = t, this._stopLoadingImages(e), clearTimeout(this._clearBgBufferTimer)
                        },
                        _getLoadedTilesPercentage: function(t) {
                            var e, i, n = t.getElementsByTagName("img"),
                                o = 0;
                            for (e = 0, i = n.length; e < i; e++) n[e].complete && o++;
                            return o / i
                        },
                        _stopLoadingImages: function(t) {
                            var e, i, n, o = Array.prototype.slice.call(t.getElementsByTagName("img"));
                            for (e = 0, i = o.length; e < i; e++) n = o[e], n.complete || (n.onload = l.Util.falseFn, n.onerror = l.Util.falseFn, n.src = l.Util.emptyImageUrl, n.parentNode.removeChild(n))
                        }
                    }), l.Map.include({
                        _defaultLocateOptions: {
                            watch: !1,
                            setView: !1,
                            maxZoom: 1 / 0,
                            timeout: 1e4,
                            maximumAge: 0,
                            enableHighAccuracy: !1
                        },
                        locate: function(t) {
                            if (t = this._locateOptions = l.extend(this._defaultLocateOptions, t), !navigator.geolocation) return this._handleGeolocationError({
                                code: 0,
                                message: "Geolocation not supported."
                            }), this;
                            var e = l.bind(this._handleGeolocationResponse, this),
                                i = l.bind(this._handleGeolocationError, this);
                            return t.watch ? this._locationWatchId = navigator.geolocation.watchPosition(e, i, t) : navigator.geolocation.getCurrentPosition(e, i, t), this
                        },
                        stopLocate: function() {
                            return navigator.geolocation && navigator.geolocation.clearWatch(this._locationWatchId), this._locateOptions && (this._locateOptions.setView = !1), this
                        },
                        _handleGeolocationError: function(t) {
                            var e = t.code,
                                i = t.message || (1 === e ? "permission denied" : 2 === e ? "position unavailable" : "timeout");
                            this._locateOptions.setView && !this._loaded && this.fitWorld(), this.fire("locationerror", {
                                code: e,
                                message: "Geolocation error: " + i + "."
                            })
                        },
                        _handleGeolocationResponse: function(t) {
                            var e = t.coords.latitude,
                                i = t.coords.longitude,
                                n = new l.LatLng(e, i),
                                o = 180 * t.coords.accuracy / 40075017,
                                s = o / Math.cos(l.LatLng.DEG_TO_RAD * e),
                                a = l.latLngBounds([e - o, i - s], [e + o, i + s]),
                                r = this._locateOptions;
                            if (r.setView) {
                                var h = Math.min(this.getBoundsZoom(a), r.maxZoom);
                                this.setView(n, h)
                            }
                            var u = {
                                latlng: n,
                                bounds: a,
                                timestamp: t.timestamp
                            };
                            for (var c in t.coords) "number" === typeof t.coords[c] && (u[c] = t.coords[c]);
                            this.fire("locationfound", u)
                        }
                    })
            })(window, document)
        }
    }
]);
