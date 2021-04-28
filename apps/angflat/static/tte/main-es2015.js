(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["main"], {

        /***/
        "./$$_lazy_route_resource lazy recursive":
            /*!******************************************************!*\
              !*** ./$$_lazy_route_resource lazy namespace object ***!
              \******************************************************/
            /*! no static exports found */
            /***/
            (function(module, exports) {

                function webpackEmptyAsyncContext(req) {
                    // Here Promise.resolve().then() is used instead of new Promise() to prevent
                    // uncaught exception popping up in devtools
                    return Promise.resolve().then(function() {
                        var e = new Error("Cannot find module '" + req + "'");
                        e.code = 'MODULE_NOT_FOUND';
                        throw e;
                    });
                }
                webpackEmptyAsyncContext.keys = function() {
                    return [];
                };
                webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
                module.exports = webpackEmptyAsyncContext;
                webpackEmptyAsyncContext.id = "./$$_lazy_route_resource lazy recursive";

                /***/
            }),

        /***/
        "./src/app/app-routing.module.ts":
            /*!***************************************!*\
              !*** ./src/app/app-routing.module.ts ***!
              \***************************************/
            /*! exports provided: AppRoutingModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() {
                    return AppRoutingModule;
                });
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _pages_dashboard_containers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./pages/dashboard/containers */ "./src/app/pages/dashboard/containers/index.ts");
                /* harmony import */
                var _pages_not_found_not_found_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ./pages/not-found/not-found.component */ "./src/app/pages/not-found/not-found.component.ts");
                /* harmony import */
                var _pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ./pages/auth/guards */ "./src/app/pages/auth/guards/index.ts");







                const routes = [{
                    path: 'dashboard',
                    pathMatch: 'full',
                    canActivate: [_pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__["AuthGuard"]],
                    component: _pages_dashboard_containers__WEBPACK_IMPORTED_MODULE_2__["DashboardPageComponent"]
                }, {
                    path: 'typography',
                    pathMatch: 'full',
                    canActivate: [_pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__["AuthGuard"]],
                    loadChildren: () => __webpack_require__.e( /*! import() | pages-typography-typography-module */ "pages-typography-typography-module").then(__webpack_require__.bind(null, /*! ./pages/typography/typography.module */ "./src/app/pages/typography/typography.module.ts")).then(m => m.TypographyModule)
                }, {
                    path: 'tables',
                    pathMatch: 'full',
                    canActivate: [_pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__["AuthGuard"]],
                    loadChildren: () => __webpack_require__.e( /*! import() | pages-tables-tables-module */ "pages-tables-tables-module").then(__webpack_require__.bind(null, /*! ./pages/tables/tables.module */ "./src/app/pages/tables/tables.module.ts")).then(m => m.TablesModule)
                }, {
                    path: 'notification',
                    pathMatch: 'full',
                    canActivate: [_pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__["AuthGuard"]],
                    loadChildren: () => __webpack_require__.e( /*! import() | pages-notification-notification-module */ "pages-notification-notification-module").then(__webpack_require__.bind(null, /*! ./pages/notification/notification.module */ "./src/app/pages/notification/notification.module.ts")).then(m => m.NotificationModule)
                }, {
                    path: 'ui',
                    canActivate: [_pages_auth_guards__WEBPACK_IMPORTED_MODULE_4__["AuthGuard"]],
                    loadChildren: () => __webpack_require__.e( /*! import() | pages-ui-elements-ui-elements-module */ "pages-ui-elements-ui-elements-module").then(__webpack_require__.bind(null, /*! ./pages/ui-elements/ui-elements.module */ "./src/app/pages/ui-elements/ui-elements.module.ts")).then(m => m.UiElementsModule)
                }, {
                    path: '404',
                    component: _pages_not_found_not_found_component__WEBPACK_IMPORTED_MODULE_3__["NotFoundComponent"]
                }, {
                    path: 'login',
                    loadChildren: () => Promise.resolve( /*! import() */ ).then(__webpack_require__.bind(null, /*! ./pages/auth/auth.module */ "./src/app/pages/auth/auth.module.ts")).then(m => m.AuthModule)
                }, {
                    path: '**',
                    redirectTo: '404'
                }];
                class AppRoutingModule {}
                AppRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: AppRoutingModule
                });
                AppRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function AppRoutingModule_Factory(t) {
                        return new(t || AppRoutingModule)();
                    },
                    imports: [
                        [
                            _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forRoot(routes, {
                                useHash: true,
                                preloadingStrategy: _angular_router__WEBPACK_IMPORTED_MODULE_0__["PreloadAllModules"]
                            })
                        ],
                        _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](AppRoutingModule, {
                        imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]],
                        exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](AppRoutingModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            imports: [
                                _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forRoot(routes, {
                                    useHash: true,
                                    preloadingStrategy: _angular_router__WEBPACK_IMPORTED_MODULE_0__["PreloadAllModules"]
                                })
                            ],
                            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/app.component.ts":
            /*!**********************************!*\
              !*** ./src/app/app.component.ts ***!
              \**********************************/
            /*! exports provided: AppComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AppComponent", function() {
                    return AppComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");



                class AppComponent {}
                AppComponent.ɵfac = function AppComponent_Factory(t) {
                    return new(t || AppComponent)();
                };
                AppComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: AppComponent,
                    selectors: [
                        ["app-root"]
                    ],
                    decls: 1,
                    vars: 0,
                    template: function AppComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "router-outlet");
                        }
                    },
                    directives: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterOutlet"]],
                    styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC5jb21wb25lbnQuc2NzcyJ9 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AppComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-root',
                            templateUrl: './app.component.html',
                            styleUrls: ['./app.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/app.module.ts":
            /*!*******************************!*\
              !*** ./src/app/app.module.ts ***!
              \*******************************/
            /*! exports provided: AppModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AppModule", function() {
                    return AppModule;
                });
                /* harmony import */
                var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/__ivy_ngcc__/fesm2015/platform-browser.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/platform-browser/animations */ "./node_modules/@angular/platform-browser/__ivy_ngcc__/fesm2015/animations.js");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var ngx_toastr__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ngx-toastr */ "./node_modules/ngx-toastr/__ivy_ngcc__/fesm2015/ngx-toastr.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _app_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! ./app.component */ "./src/app/app.component.ts");
                /* harmony import */
                var _shared_shared_module__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! ./shared/shared.module */ "./src/app/shared/shared.module.ts");
                /* harmony import */
                var _app_routing_module__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! ./app-routing.module */ "./src/app/app-routing.module.ts");
                /* harmony import */
                var _pages_dashboard_dashboard_module__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ./pages/dashboard/dashboard.module */ "./src/app/pages/dashboard/dashboard.module.ts");
                /* harmony import */
                var _pages_not_found_not_found_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ./pages/not-found/not-found.component */ "./src/app/pages/not-found/not-found.component.ts");
                /* harmony import */
                var _pages_auth_auth_module__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! ./pages/auth/auth.module */ "./src/app/pages/auth/auth.module.ts");















                class AppModule {}
                AppModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: AppModule,
                    bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"]]
                });
                AppModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function AppModule_Factory(t) {
                        return new(t || AppModule)();
                    },
                    providers: [],
                    imports: [
                        [
                            _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_8__["SharedModule"],
                            _pages_auth_auth_module__WEBPACK_IMPORTED_MODULE_12__["AuthModule"],
                            _pages_dashboard_dashboard_module__WEBPACK_IMPORTED_MODULE_10__["DashboardModule"],
                            _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_2__["BrowserAnimationsModule"],
                            _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                            _app_routing_module__WEBPACK_IMPORTED_MODULE_9__["AppRoutingModule"],
                            ngx_toastr__WEBPACK_IMPORTED_MODULE_4__["ToastrModule"].forRoot(),
                            _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](AppModule, {
                        declarations: [_app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"],
                            _pages_not_found_not_found_component__WEBPACK_IMPORTED_MODULE_11__["NotFoundComponent"]
                        ],
                        imports: [_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_8__["SharedModule"],
                            _pages_auth_auth_module__WEBPACK_IMPORTED_MODULE_12__["AuthModule"],
                            _pages_dashboard_dashboard_module__WEBPACK_IMPORTED_MODULE_10__["DashboardModule"],
                            _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_2__["BrowserAnimationsModule"],
                            _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                            _app_routing_module__WEBPACK_IMPORTED_MODULE_9__["AppRoutingModule"], ngx_toastr__WEBPACK_IMPORTED_MODULE_4__["ToastrModule"], _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"]
                        ]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](AppModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            declarations: [
                                _app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"],
                                _pages_not_found_not_found_component__WEBPACK_IMPORTED_MODULE_11__["NotFoundComponent"]
                            ],
                            imports: [
                                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
                                _shared_shared_module__WEBPACK_IMPORTED_MODULE_8__["SharedModule"],
                                _pages_auth_auth_module__WEBPACK_IMPORTED_MODULE_12__["AuthModule"],
                                _pages_dashboard_dashboard_module__WEBPACK_IMPORTED_MODULE_10__["DashboardModule"],
                                _angular_platform_browser_animations__WEBPACK_IMPORTED_MODULE_2__["BrowserAnimationsModule"],
                                _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                                _app_routing_module__WEBPACK_IMPORTED_MODULE_9__["AppRoutingModule"],
                                ngx_toastr__WEBPACK_IMPORTED_MODULE_4__["ToastrModule"].forRoot(),
                                _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                            ],
                            providers: [],
                            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_7__["AppComponent"]]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/consts/colors.ts":
            /*!**********************************!*\
              !*** ./src/app/consts/colors.ts ***!
              \**********************************/
            /*! exports provided: colors */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "colors", function() {
                    return colors;
                });
                var colors;
                (function(colors) {
                    colors["YELLOW"] = "#ffc260";
                    colors["BLUE"] = "#536DFE";
                    colors["LIGHT_BLUE"] = "#F8F9FF";
                    colors["PINK"] = "#ff4081";
                    colors["GREEN"] = "#3CD4A0";
                    colors["VIOLET"] = "#9013FE";
                })(colors || (colors = {}));


                /***/
            }),

        /***/
        "./src/app/consts/index.ts":
            /*!*********************************!*\
              !*** ./src/app/consts/index.ts ***!
              \*********************************/
            /*! exports provided: routes, colors */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _routes__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./routes */ "./src/app/consts/routes.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "routes", function() {
                    return _routes__WEBPACK_IMPORTED_MODULE_0__["routes"];
                });

                /* harmony import */
                var _colors__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./colors */ "./src/app/consts/colors.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "colors", function() {
                    return _colors__WEBPACK_IMPORTED_MODULE_1__["colors"];
                });





                /***/
            }),

        /***/
        "./src/app/consts/routes.ts":
            /*!**********************************!*\
              !*** ./src/app/consts/routes.ts ***!
              \**********************************/
            /*! exports provided: routes */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "routes", function() {
                    return routes;
                });
                var routes;
                (function(routes) {
                    routes["DASHBOARD"] = "/dashboard";
                    routes["TYPOGRAPHY"] = "/typography";
                    routes["TABLES"] = "/tables";
                    routes["NOTIFICATION"] = "/notification";
                    routes["UI_ELEMENTS_ICONS"] = "/ui/icons";
                    routes["UI_ELEMENTS_CHARTS"] = "/ui/charts";
                    routes["UI_ELEMENTS_MAP"] = "/ui/map";
                    routes["LOGIN"] = "/login";
                })(routes || (routes = {}));


                /***/
            }),

        /***/
        "./src/app/pages/auth/auth-routing.module.ts":
            /*!***************************************************!*\
              !*** ./src/app/pages/auth/auth-routing.module.ts ***!
              \***************************************************/
            /*! exports provided: AuthRoutingModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AuthRoutingModule", function() {
                    return AuthRoutingModule;
                });
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./containers */ "./src/app/pages/auth/containers/index.ts");





                const routes = [{
                    path: '',
                    component: _containers__WEBPACK_IMPORTED_MODULE_2__["AuthPageComponent"]
                }];
                class AuthRoutingModule {}
                AuthRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: AuthRoutingModule
                });
                AuthRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function AuthRoutingModule_Factory(t) {
                        return new(t || AuthRoutingModule)();
                    },
                    imports: [
                        [
                            _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)
                        ],
                        _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](AuthRoutingModule, {
                        imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]],
                        exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](AuthRoutingModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            imports: [
                                _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)
                            ],
                            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/auth.module.ts":
            /*!*******************************************!*\
              !*** ./src/app/pages/auth/auth.module.ts ***!
              \*******************************************/
            /*! exports provided: AuthModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AuthModule", function() {
                    return AuthModule;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_tabs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/tabs */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/tabs.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_input__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/input */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/input.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ./containers */ "./src/app/pages/auth/containers/index.ts");
                /* harmony import */
                var _auth_routing_module__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! ./auth-routing.module */ "./src/app/pages/auth/auth-routing.module.ts");
                /* harmony import */
                var _pipes__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! ./pipes */ "./src/app/pages/auth/pipes/index.ts");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! ./services */ "./src/app/pages/auth/services/index.ts");
                /* harmony import */
                var _components__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ./components */ "./src/app/pages/auth/components/index.ts");
                /* harmony import */
                var _guards__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ./guards */ "./src/app/pages/auth/guards/index.ts");













                class AuthModule {}
                AuthModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: AuthModule
                });
                AuthModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function AuthModule_Factory(t) {
                        return new(t || AuthModule)();
                    },
                    providers: [
                        _services__WEBPACK_IMPORTED_MODULE_9__["AuthService"],
                        _services__WEBPACK_IMPORTED_MODULE_9__["EmailService"],
                        _guards__WEBPACK_IMPORTED_MODULE_11__["AuthGuard"]
                    ],
                    imports: [
                        [
                            _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _auth_routing_module__WEBPACK_IMPORTED_MODULE_7__["AuthRoutingModule"],
                            _angular_material_tabs__WEBPACK_IMPORTED_MODULE_2__["MatTabsModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_3__["MatButtonModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_4__["MatInputModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_5__["ReactiveFormsModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_5__["FormsModule"]
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](AuthModule, {
                        declarations: [_containers__WEBPACK_IMPORTED_MODULE_6__["AuthPageComponent"],
                            _pipes__WEBPACK_IMPORTED_MODULE_8__["YearPipe"],
                            _components__WEBPACK_IMPORTED_MODULE_10__["LoginFormComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_10__["SignFormComponent"]
                        ],
                        imports: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _auth_routing_module__WEBPACK_IMPORTED_MODULE_7__["AuthRoutingModule"],
                            _angular_material_tabs__WEBPACK_IMPORTED_MODULE_2__["MatTabsModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_3__["MatButtonModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_4__["MatInputModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_5__["ReactiveFormsModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_5__["FormsModule"]
                        ]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AuthModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [
                                _containers__WEBPACK_IMPORTED_MODULE_6__["AuthPageComponent"],
                                _pipes__WEBPACK_IMPORTED_MODULE_8__["YearPipe"],
                                _components__WEBPACK_IMPORTED_MODULE_10__["LoginFormComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_10__["SignFormComponent"]
                            ],
                            imports: [
                                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                                _auth_routing_module__WEBPACK_IMPORTED_MODULE_7__["AuthRoutingModule"],
                                _angular_material_tabs__WEBPACK_IMPORTED_MODULE_2__["MatTabsModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_3__["MatButtonModule"],
                                _angular_material_input__WEBPACK_IMPORTED_MODULE_4__["MatInputModule"],
                                _angular_forms__WEBPACK_IMPORTED_MODULE_5__["ReactiveFormsModule"],
                                _angular_forms__WEBPACK_IMPORTED_MODULE_5__["FormsModule"]
                            ],
                            providers: [
                                _services__WEBPACK_IMPORTED_MODULE_9__["AuthService"],
                                _services__WEBPACK_IMPORTED_MODULE_9__["EmailService"],
                                _guards__WEBPACK_IMPORTED_MODULE_11__["AuthGuard"]
                            ]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/components/index.ts":
            /*!************************************************!*\
              !*** ./src/app/pages/auth/components/index.ts ***!
              \************************************************/
            /*! exports provided: LoginFormComponent, SignFormComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _login_form_login_form_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./login-form/login-form.component */ "./src/app/pages/auth/components/login-form/login-form.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "LoginFormComponent", function() {
                    return _login_form_login_form_component__WEBPACK_IMPORTED_MODULE_0__["LoginFormComponent"];
                });

                /* harmony import */
                var _sign_form_sign_form_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./sign-form/sign-form.component */ "./src/app/pages/auth/components/sign-form/sign-form.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "SignFormComponent", function() {
                    return _sign_form_sign_form_component__WEBPACK_IMPORTED_MODULE_1__["SignFormComponent"];
                });





                /***/
            }),

        /***/
        "./src/app/pages/auth/components/login-form/login-form.component.ts":
            /*!**************************************************************************!*\
              !*** ./src/app/pages/auth/components/login-form/login-form.component.ts ***!
              \**************************************************************************/
            /*! exports provided: LoginFormComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "LoginFormComponent", function() {
                    return LoginFormComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/form-field */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/form-field.js");
                /* harmony import */
                var _angular_material_input__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/input */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/input.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");







                class LoginFormComponent {
                    constructor() {
                        this.sendLoginForm = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
                        this.flatlogicEmail = 'admin@flatlogic.com';
                        this.flatlogicPassword = 'admin';
                    }
                    ngOnInit() {
                        this.form = new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormGroup"]({
                            email: new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControl"](this.flatlogicEmail, [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].required, _angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].email]),
                            password: new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControl"](this.flatlogicPassword, [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].required])
                        });
                    }
                    login() {
                        if (this.form.valid) {
                            this.sendLoginForm.emit();
                        }
                    }
                }
                LoginFormComponent.ɵfac = function LoginFormComponent_Factory(t) {
                    return new(t || LoginFormComponent)();
                };
                LoginFormComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: LoginFormComponent,
                    selectors: [
                        ["app-login-form"]
                    ],
                    outputs: {
                        sendLoginForm: "sendLoginForm"
                    },
                    decls: 10,
                    vars: 1,
                    consts: [
                        [1, "form", 3, "formGroup", "ngSubmit"],
                        [1, "form__input"],
                        ["matInput", "", "placeholder", "Email Address", "type", "email", "formControlName", "email"],
                        ["matInput", "", "placeholder", "Password", "type", "password", "formControlName", "password"],
                        [1, "form-actions"],
                        ["mat-raised-button", "", "color", "primary", "type", "submit", 1, "form-actions__login"],
                        ["mat-button", "", 1, "form-actions__forget"]
                    ],
                    template: function LoginFormComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "form", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("ngSubmit", function LoginFormComponent_Template_form_ngSubmit_0_listener() {
                                return ctx.login();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-form-field", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "input", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-form-field", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "input", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Login");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "button", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Forget password");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("formGroup", ctx.form);
                        }
                    },
                    directives: [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["ɵangular_packages_forms_forms_y"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatusGroup"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormGroupDirective"], _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__["MatFormField"], _angular_material_input__WEBPACK_IMPORTED_MODULE_3__["MatInput"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["DefaultValueAccessor"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControlName"], _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButton"]],
                    styles: [".form[_ngcontent-%COMP%] {\n  width: 100%;\n}\n.form__input[_ngcontent-%COMP%] {\n  width: 100%;\n  margin-top: 6px;\n}\n.form-actions[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n.form-actions__login[_ngcontent-%COMP%] {\n  margin-right: 10px;\n}\n.form-actions__forget[_ngcontent-%COMP%] {\n  font-size: 12px;\n  font-weight: 400;\n  color: #536DFE;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvYXV0aC9jb21wb25lbnRzL2xvZ2luLWZvcm0vbG9naW4tZm9ybS5jb21wb25lbnQuc2NzcyIsInNyYy9hcHAvcGFnZXMvYXV0aC9jb21wb25lbnRzL2xvZ2luLWZvcm0vbG9naW4tZm9ybS5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UsV0FBQTtBQ0ZGO0FESUU7RUFDRSxXQUFBO0VBQ0EsZUFBQTtBQ0ZKO0FETUE7RUFDRSxhQUFBO0VBQ0EsOEJBQUE7RUFDQSxtQkFBQTtBQ0hGO0FES0U7RUFDRSxrQkFBQTtBQ0hKO0FETUU7RUFDRSxlQUFBO0VBQ0EsZ0JFdkJTO0VGd0JULGNHdkJHO0FGbUJQIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvYXV0aC9jb21wb25lbnRzL2xvZ2luLWZvcm0vbG9naW4tZm9ybS5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9jb2xvcnNcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9mb250XCI7XG5cbi5mb3JtIHtcbiAgd2lkdGg6IDEwMCU7XG5cbiAgJl9faW5wdXQge1xuICAgIHdpZHRoOiAxMDAlO1xuICAgIG1hcmdpbi10b3A6IDZweDtcbiAgfVxufVxuXG4uZm9ybS1hY3Rpb25zIHtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuXG4gICZfX2xvZ2luIHtcbiAgICBtYXJnaW4tcmlnaHQ6IDEwcHg7XG4gIH1cblxuICAmX19mb3JnZXQge1xuICAgIGZvbnQtc2l6ZTogMTJweDtcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgY29sb3I6ICRibHVlO1xuICB9XG59XG4iLCIuZm9ybSB7XG4gIHdpZHRoOiAxMDAlO1xufVxuLmZvcm1fX2lucHV0IHtcbiAgd2lkdGg6IDEwMCU7XG4gIG1hcmdpbi10b3A6IDZweDtcbn1cblxuLmZvcm0tYWN0aW9ucyB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cbi5mb3JtLWFjdGlvbnNfX2xvZ2luIHtcbiAgbWFyZ2luLXJpZ2h0OiAxMHB4O1xufVxuLmZvcm0tYWN0aW9uc19fZm9yZ2V0IHtcbiAgZm9udC1zaXplOiAxMnB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBjb2xvcjogIzUzNkRGRTtcbn0iLCIkZnctbGlnaHRlcjogNDAwO1xuJGZ3LW5vcm1hbDogNTAwO1xuJGZ3LWJvbGQ6IDYwMDtcblxuXG4kZnMteHM6IDExLjJweDtcbiRmcy1zbWFsbDogMTRweDtcbiRmcy1ub3JtYWw6IDE2cHg7XG4kZnMtcmVndWxhcjogMThweDtcbiRmcy1tZWRpdW06IDIxcHg7XG4kZnMtbGFyZ2U6IDI0cHg7XG4kZnMteGw6IDI4cHg7XG4kZnMteHhsOiAzOHB4O1xuJGZzLXh4eGw6IDQycHg7XG4iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](LoginFormComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-login-form',
                            templateUrl: './login-form.component.html',
                            styleUrls: ['./login-form.component.scss']
                        }]
                    }], null, {
                        sendLoginForm: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/components/sign-form/sign-form.component.ts":
            /*!************************************************************************!*\
              !*** ./src/app/pages/auth/components/sign-form/sign-form.component.ts ***!
              \************************************************************************/
            /*! exports provided: SignFormComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SignFormComponent", function() {
                    return SignFormComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/form-field */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/form-field.js");
                /* harmony import */
                var _angular_material_input__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/input */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/input.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");







                class SignFormComponent {
                    constructor() {
                        this.sendSignForm = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
                    }
                    ngOnInit() {
                        this.form = new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormGroup"]({
                            name: new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControl"]('', [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].required]),
                            email: new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControl"]('', [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].required, _angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].email]),
                            password: new _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControl"]('', [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].required])
                        });
                    }
                    sign() {
                        if (this.form.valid) {
                            this.sendSignForm.emit();
                        }
                    }
                }
                SignFormComponent.ɵfac = function SignFormComponent_Factory(t) {
                    return new(t || SignFormComponent)();
                };
                SignFormComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: SignFormComponent,
                    selectors: [
                        ["app-sign-form"]
                    ],
                    outputs: {
                        sendSignForm: "sendSignForm"
                    },
                    decls: 10,
                    vars: 1,
                    consts: [
                        [1, "form", 3, "formGroup", "ngSubmit"],
                        [1, "form__input"],
                        ["matInput", "", "placeholder", "Full name", "formControlName", "name"],
                        ["matInput", "", "placeholder", "Email Address", "type", "email", "formControlName", "email"],
                        ["matInput", "", "placeholder", "Password", "type", "password", "formControlName", "password"],
                        [1, "form-actions"],
                        ["mat-raised-button", "", "color", "primary", "type", "submit", 1, "form-actions__create"]
                    ],
                    template: function SignFormComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "form", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("ngSubmit", function SignFormComponent_Template_form_ngSubmit_0_listener() {
                                return ctx.sign();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-form-field", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "input", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-form-field", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "input", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-form-field", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](6, "input", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "button", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Create your account");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("formGroup", ctx.form);
                        }
                    },
                    directives: [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["ɵangular_packages_forms_forms_y"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatusGroup"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormGroupDirective"], _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__["MatFormField"], _angular_material_input__WEBPACK_IMPORTED_MODULE_3__["MatInput"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["DefaultValueAccessor"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControlName"], _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButton"]],
                    styles: [".form[_ngcontent-%COMP%] {\n  width: 100%;\n}\n.form__input[_ngcontent-%COMP%] {\n  width: 100%;\n  margin-top: -15px;\n}\n.form-actions[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  margin-top: 5px;\n}\n.form-actions__create[_ngcontent-%COMP%] {\n  margin: 0;\n  width: 95%;\n  box-shadow: 0 0 11px 0 #E8EAFC, 0 0 0 -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvYXV0aC9jb21wb25lbnRzL3NpZ24tZm9ybS9zaWduLWZvcm0uY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL2F1dGgvY29tcG9uZW50cy9zaWduLWZvcm0vc2lnbi1mb3JtLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUVBO0VBQ0UsV0FBQTtBQ0RGO0FER0U7RUFDRSxXQUFBO0VBQ0EsaUJBQUE7QUNESjtBREtBO0VBQ0UsYUFBQTtFQUNBLHVCQUFBO0VBQ0EsbUJBQUE7RUFDQSxlQUFBO0FDRkY7QURJRTtFQUNFLFNBQUE7RUFDQSxVQUFBO0VBQ0EsMkVBQUE7QUNGSiIsImZpbGUiOiJzcmMvYXBwL3BhZ2VzL2F1dGgvY29tcG9uZW50cy9zaWduLWZvcm0vc2lnbi1mb3JtLmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2NvbG9yc1wiO1xuXG4uZm9ybSB7XG4gIHdpZHRoOiAxMDAlO1xuXG4gICZfX2lucHV0IHtcbiAgICB3aWR0aDogMTAwJTtcbiAgICBtYXJnaW4tdG9wOiAtMTVweDtcbiAgfVxufVxuXG4uZm9ybS1hY3Rpb25zIHtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIG1hcmdpbi10b3A6IDVweDtcblxuICAmX19jcmVhdGUge1xuICAgIG1hcmdpbjogMDtcbiAgICB3aWR0aDogOTUlO1xuICAgIGJveC1zaGFkb3c6IDAgMCAxMXB4IDAgJHNoYWRvdy13aGl0ZSwgMCAwIDAgLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuICB9XG59XG4iLCIuZm9ybSB7XG4gIHdpZHRoOiAxMDAlO1xufVxuLmZvcm1fX2lucHV0IHtcbiAgd2lkdGg6IDEwMCU7XG4gIG1hcmdpbi10b3A6IC0xNXB4O1xufVxuXG4uZm9ybS1hY3Rpb25zIHtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIG1hcmdpbi10b3A6IDVweDtcbn1cbi5mb3JtLWFjdGlvbnNfX2NyZWF0ZSB7XG4gIG1hcmdpbjogMDtcbiAgd2lkdGg6IDk1JTtcbiAgYm94LXNoYWRvdzogMCAwIDExcHggMCAjRThFQUZDLCAwIDAgMCAtMnB4ICNCMkIyQjIxQSwgMCAxcHggOHB4IDAgIzlBOUE5QTFBO1xufSJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SignFormComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-sign-form',
                            templateUrl: './sign-form.component.html',
                            styleUrls: ['./sign-form.component.scss']
                        }]
                    }], null, {
                        sendSignForm: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/containers/auth-page/auth-page.component.ts":
            /*!************************************************************************!*\
              !*** ./src/app/pages/auth/containers/auth-page/auth-page.component.ts ***!
              \************************************************************************/
            /*! exports provided: AuthPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AuthPageComponent", function() {
                    return AuthPageComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../services */ "./src/app/pages/auth/services/index.ts");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_material_tabs__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/tabs */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/tabs.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _components_login_form_login_form_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ../../components/login-form/login-form.component */ "./src/app/pages/auth/components/login-form/login-form.component.ts");
                /* harmony import */
                var _components_sign_form_sign_form_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! ../../components/sign-form/sign-form.component */ "./src/app/pages/auth/components/sign-form/sign-form.component.ts");
                /* harmony import */
                var _pipes_year_pipe__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! ../../pipes/year.pipe */ "./src/app/pages/auth/pipes/year.pipe.ts");










                class AuthPageComponent {
                    constructor(service, router) {
                        this.service = service;
                        this.router = router;
                        this.todayDate = new Date();
                        this.routers = _consts__WEBPACK_IMPORTED_MODULE_1__["routes"];
                    }
                    sendLoginForm() {
                        this.service.login();
                        this.router.navigate([this.routers.DASHBOARD]).then();
                    }
                    sendSignForm() {
                        this.service.sign();
                        this.router.navigate([this.routers.DASHBOARD]).then();
                    }
                }
                AuthPageComponent.ɵfac = function AuthPageComponent_Factory(t) {
                    return new(t || AuthPageComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services__WEBPACK_IMPORTED_MODULE_2__["AuthService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]));
                };
                AuthPageComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: AuthPageComponent,
                    selectors: [
                        ["app-auth-page"]
                    ],
                    decls: 43,
                    vars: 3,
                    consts: [
                        [1, "auth-page"],
                        [1, "auth-page__content-block"],
                        [1, "auth-page__content-wrapper"],
                        [1, "auth-page__group"],
                        ["label", "Login"],
                        [1, "auth-page__group-title"],
                        [1, "auth-page__google-button-wrapper"],
                        ["mat-raised-button", "", 1, "auth-page__google-button"],
                        ["src", "/angflat/static/tte/assets/auth/google.svg", "alt", "google", 1, "auth-page__google-button-icon"],
                        [1, "auth-page__border-wrapper"],
                        [1, "auth-page__border-line"],
                        [1, "auth-page__border-title"],
                        [3, "sendLoginForm"],
                        ["label", "New User"],
                        [1, "auth-page__group-sub-title"],
                        [3, "sendSignForm"],
                        [1, "auth-page__footer-title"],
                        ["href", "https://flatlogic.com/"],
                        [1, "auth-page__logo"],
                        [1, "auth-page__logo-wrapper"],
                        ["src", "/angflat/static/tte/assets/auth/logo.svg", "alt", "logo", 1, "auth-page__logo-img"],
                        [1, "auth-page__logo-title"]
                    ],
                    template: function AuthPageComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-tab-group", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "mat-tab", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "h4", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, "Good Morning, User");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "button", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](9, "img", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10, "Sign in with Google ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "div", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "div", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "p", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "or");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](15, "div", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "app-login-form", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("sendLoginForm", function AuthPageComponent_Template_app_login_form_sendLoginForm_16_listener() {
                                return ctx.sendLoginForm();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "mat-tab", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "h4", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](19, "Welcome!");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](20, "p", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](21, "Create you account");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "app-sign-form", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("sendSignForm", function AuthPageComponent_Template_app_sign_form_sendSignForm_22_listener() {
                                return ctx.sendSignForm();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](23, "div", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](24, "div", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](25, "p", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](26, "or");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](27, "div", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](28, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](29, "button", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](30, "img", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](31, "Sign in with Google ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](32, "p", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](33);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](34, "year");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](35, "a", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](36, "Flatlogic");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](37, ", LLC. All rights reserved.");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](38, "div", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](39, "div", 19);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](40, "img", 20);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](41, "h6", 21);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](42, "Material Admin");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](33);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("\u00A9 2014-", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](34, 1, ctx.todayDate), " ");
                        }
                    },
                    directives: [_angular_material_tabs__WEBPACK_IMPORTED_MODULE_4__["MatTabGroup"], _angular_material_tabs__WEBPACK_IMPORTED_MODULE_4__["MatTab"], _angular_material_button__WEBPACK_IMPORTED_MODULE_5__["MatButton"], _components_login_form_login_form_component__WEBPACK_IMPORTED_MODULE_6__["LoginFormComponent"], _components_sign_form_sign_form_component__WEBPACK_IMPORTED_MODULE_7__["SignFormComponent"]],
                    pipes: [_pipes_year_pipe__WEBPACK_IMPORTED_MODULE_8__["YearPipe"]],
                    styles: [".auth-page[_ngcontent-%COMP%] {\n  width: 100%;\n  height: 100%;\n  display: flex;\n}\n@media (max-width: 768px) {\n  .auth-page[_ngcontent-%COMP%] {\n    flex-direction: column;\n  }\n}\n.auth-page__content-block[_ngcontent-%COMP%] {\n  width: 37%;\n  height: 100%;\n  background-color: white;\n  display: flex;\n  align-items: center;\n  flex-direction: column;\n}\n@media (max-width: 768px) {\n  .auth-page__content-block[_ngcontent-%COMP%] {\n    width: 100%;\n  }\n}\n.auth-page__content-wrapper[_ngcontent-%COMP%] {\n  width: 45%;\n  height: 100%;\n  padding: 16px;\n  display: flex;\n  justify-content: space-between;\n  flex-direction: column;\n}\n@media (max-width: 576px) {\n  .auth-page__content-wrapper[_ngcontent-%COMP%] {\n    width: 70%;\n  }\n}\n@media (min-width: 768px) and (max-width: 992px) {\n  .auth-page__content-wrapper[_ngcontent-%COMP%] {\n    width: 45%;\n  }\n}\n.auth-page__group[_ngcontent-%COMP%] {\n  margin-top: 28px;\n}\n.auth-page__group-title[_ngcontent-%COMP%] {\n  font-size: 32px;\n  font-weight: 500;\n  margin-top: 37px;\n  letter-spacing: -0.7px;\n  text-align: center;\n  line-height: 37px;\n  color: #4A4A4A;\n}\n.auth-page__group-sub-title[_ngcontent-%COMP%] {\n  font-size: 24px;\n  font-weight: 500;\n  margin-bottom: 60px;\n  letter-spacing: -0.5px;\n  text-align: center;\n  line-height: 24px;\n  color: #4A4A4A;\n}\n.auth-page__google-button-wrapper[_ngcontent-%COMP%] {\n  margin-top: 32px;\n  margin-bottom: 10px;\n  width: 100%;\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n}\n.auth-page__google-button[_ngcontent-%COMP%] {\n  width: 95%;\n  padding: 0;\n  box-shadow: 0 0 11px 0 #E8EAFC, 0 0 0 -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n.auth-page__google-button-icon[_ngcontent-%COMP%] {\n  width: 20px;\n  margin-right: 16px;\n}\n.auth-page__border-wrapper[_ngcontent-%COMP%] {\n  align-items: center;\n  display: flex;\n  justify-content: center;\n  margin: 32px 0;\n}\n.auth-page__border-line[_ngcontent-%COMP%] {\n  height: 1px;\n  width: 100%;\n  background-color: #B9B9B9;\n  opacity: 0.3;\n}\n.auth-page__border-title[_ngcontent-%COMP%] {\n  font-size: 11.2px;\n  padding: 0 16px;\n  margin: 0;\n  color: #4A4A4A;\n}\n.auth-page__logo[_ngcontent-%COMP%] {\n  width: 63%;\n  height: 100%;\n  background-color: #536DFE;\n  display: flex;\n  align-items: center;\n}\n@media (max-width: 768px) {\n  .auth-page__logo[_ngcontent-%COMP%] {\n    display: none;\n  }\n}\n.auth-page__logo-wrapper[_ngcontent-%COMP%] {\n  width: 100%;\n  display: flex;\n  justify-content: center;\n  flex-direction: column;\n  align-items: center;\n}\n.auth-page__logo-img[_ngcontent-%COMP%] {\n  margin-bottom: 50px;\n}\n.auth-page__logo-title[_ngcontent-%COMP%] {\n  font-size: 62px;\n  color: white;\n  font-weight: 500;\n  letter-spacing: -1.5px;\n  line-height: 62px;\n}\n.auth-page__footer-title[_ngcontent-%COMP%] {\n  color: #536DFE;\n  font-size: 10px;\n  opacity: 0.7;\n}\n.auth-page__footer-title[_ngcontent-%COMP%]   a[_ngcontent-%COMP%] {\n  text-decoration: none;\n  color: #536DFE;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvYXV0aC9jb250YWluZXJzL2F1dGgtcGFnZS9hdXRoLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL2F1dGgvY29udGFpbmVycy9hdXRoLXBhZ2UvYXV0aC1wYWdlLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxXQUFBO0VBQ0EsWUFBQTtFQUNBLGFBQUE7QUNIRjtBREtFO0VBTEY7SUFNSSxzQkFBQTtFQ0ZGO0FBQ0Y7QURJRTtFQUNFLFVBQUE7RUFDQSxZQUFBO0VBQ0EsdUJFUEk7RUZRSixhQUFBO0VBQ0EsbUJBQUE7RUFDQSxzQkFBQTtBQ0ZKO0FESUk7RUFSRjtJQVNJLFdBQUE7RUNESjtBQUNGO0FESUU7RUFDRSxVQUFBO0VBQ0EsWUFBQTtFQUNBLGFBQUE7RUFDQSxhQUFBO0VBQ0EsOEJBQUE7RUFDQSxzQkFBQTtBQ0ZKO0FESUk7RUFSRjtJQVNJLFVBQUE7RUNESjtBQUNGO0FER0k7RUFaRjtJQWFJLFVBQUE7RUNBSjtBQUNGO0FER0U7RUFDRSxnQkFBQTtBQ0RKO0FESUU7RUFDRSxlQUFBO0VBQ0EsZ0JHaERRO0VIaURSLGdCQUFBO0VBQ0Esc0JBQUE7RUFDQSxrQkFBQTtFQUNBLGlCQUFBO0VBQ0EsY0U1Q1E7QUQwQ1o7QURLRTtFQUNFLGVHaERPO0VIaURQLGdCRzFEUTtFSDJEUixtQkFBQTtFQUNBLHNCQUFBO0VBQ0Esa0JBQUE7RUFDQSxpQkFBQTtFQUNBLGNFdERRO0FEbURaO0FETUU7RUFDRSxnQkFBQTtFQUNBLG1CQUFBO0VBQ0EsV0FBQTtFQUNBLGFBQUE7RUFDQSxzQkFBQTtFQUNBLG1CQUFBO0FDSko7QURPRTtFQUNFLFVBQUE7RUFDQSxVQUFBO0VBQ0EsMkVBQUE7QUNMSjtBRFFFO0VBQ0UsV0FBQTtFQUNBLGtCQUFBO0FDTko7QURTRTtFQUNFLG1CQUFBO0VBQ0EsYUFBQTtFQUNBLHVCQUFBO0VBQ0EsY0FBQTtBQ1BKO0FEVUU7RUFDRSxXQUFBO0VBQ0EsV0FBQTtFQUNBLHlCRXRGUztFRnVGVCxZQUFBO0FDUko7QURXRTtFQUNFLGlCR2pHSTtFSGtHSixlQUFBO0VBQ0EsU0FBQTtFQUNBLGNFL0ZRO0FEc0ZaO0FEWUU7RUFDRSxVQUFBO0VBQ0EsWUFBQTtFQUNBLHlCRTlHRztFRitHSCxhQUFBO0VBQ0EsbUJBQUE7QUNWSjtBRFlJO0VBUEY7SUFRSSxhQUFBO0VDVEo7QUFDRjtBRFlFO0VBQ0UsV0FBQTtFQUNBLGFBQUE7RUFDQSx1QkFBQTtFQUNBLHNCQUFBO0VBQ0EsbUJBQUE7QUNWSjtBRGFFO0VBQ0UsbUJBQUE7QUNYSjtBRGNFO0VBQ0UsZUFBQTtFQUNBLFlFN0hJO0VGOEhKLGdCQUFBO0VBQ0Esc0JBQUE7RUFDQSxpQkFBQTtBQ1pKO0FEZUU7RUFDRSxjRTVJRztFRjZJSCxlQUFBO0VBQ0EsWUFBQTtBQ2JKO0FEY0k7RUFDRSxxQkFBQTtFQUNBLGNFakpDO0FEcUlQIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvYXV0aC9jb250YWluZXJzL2F1dGgtcGFnZS9hdXRoLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvY29sb3JzXCI7XG5AaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvdmFyaWFibGVzXCI7XG5AaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvZm9udFwiO1xuXG4uYXV0aC1wYWdlIHtcbiAgd2lkdGg6IDEwMCU7XG4gIGhlaWdodDogMTAwJTtcbiAgZGlzcGxheTogZmxleDtcblxuICBAbWVkaWEgKG1heC13aWR0aDogJG1lZGl1bSkge1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIH1cblxuICAmX19jb250ZW50LWJsb2NrIHtcbiAgICB3aWR0aDogMzclO1xuICAgIGhlaWdodDogMTAwJTtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkd2hpdGU7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG5cbiAgICBAbWVkaWEgKG1heC13aWR0aDogJG1lZGl1bSkge1xuICAgICAgd2lkdGg6IDEwMCU7XG4gICAgfVxuICB9XG5cbiAgJl9fY29udGVudC13cmFwcGVyIHtcbiAgICB3aWR0aDogNDUlO1xuICAgIGhlaWdodDogMTAwJTtcbiAgICBwYWRkaW5nOiAxNnB4O1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG5cbiAgICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgICB3aWR0aDogNzAlO1xuICAgIH1cblxuICAgIEBtZWRpYSAobWluLXdpZHRoOiAkbWVkaXVtKSBhbmQgKG1heC13aWR0aDogJGxhcmdlKXtcbiAgICAgIHdpZHRoOiA0NSU7XG4gICAgfVxuICB9XG5cbiAgJl9fZ3JvdXAge1xuICAgIG1hcmdpbi10b3A6IDI4cHg7XG4gIH1cblxuICAmX19ncm91cC10aXRsZSB7XG4gICAgZm9udC1zaXplOiAzMnB4O1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbm9ybWFsO1xuICAgIG1hcmdpbi10b3A6IDM3cHg7XG4gICAgbGV0dGVyLXNwYWNpbmc6IC0wLjdweDtcbiAgICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gICAgbGluZS1oZWlnaHQ6IDM3cHg7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gIH1cblxuICAmX19ncm91cC1zdWItdGl0bGUge1xuICAgIGZvbnQtc2l6ZTogJGZzLWxhcmdlO1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbm9ybWFsO1xuICAgIG1hcmdpbi1ib3R0b206IDYwcHg7XG4gICAgbGV0dGVyLXNwYWNpbmc6IC0wLjVweDtcbiAgICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gICAgbGluZS1oZWlnaHQ6IDI0cHg7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gIH1cblxuICAmX19nb29nbGUtYnV0dG9uLXdyYXBwZXIge1xuICAgIG1hcmdpbi10b3A6IDMycHg7XG4gICAgbWFyZ2luLWJvdHRvbTogMTBweDtcbiAgICB3aWR0aDogMTAwJTtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgfVxuXG4gICZfX2dvb2dsZS1idXR0b24ge1xuICAgIHdpZHRoOiA5NSU7XG4gICAgcGFkZGluZzogMDtcbiAgICBib3gtc2hhZG93OiAwIDAgMTFweCAwICRzaGFkb3ctd2hpdGUsIDAgMCAwIC0ycHggJHNoYWRvdy1ncmV5LCAwIDFweCA4cHggMCAkc2hhZG93LWRhcmstZ3JleTtcbiAgfVxuXG4gICZfX2dvb2dsZS1idXR0b24taWNvbiB7XG4gICAgd2lkdGg6IDIwcHg7XG4gICAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICB9XG5cbiAgJl9fYm9yZGVyLXdyYXBwZXIge1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbiAgICBtYXJnaW46IDMycHggMDtcbiAgfVxuXG4gICZfX2JvcmRlci1saW5lIHtcbiAgICBoZWlnaHQ6IDFweDtcbiAgICB3aWR0aDogMTAwJTtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiAgICBvcGFjaXR5OiAwLjM7XG4gIH1cblxuICAmX19ib3JkZXItdGl0bGUge1xuICAgIGZvbnQtc2l6ZTogJGZzLXhzO1xuICAgIHBhZGRpbmc6IDAgMTZweDtcbiAgICBtYXJnaW46IDA7XG4gICAgY29sb3I6ICRkYXJrLWdyZXlcbiAgfVxuXG4gICZfX2xvZ28ge1xuICAgIHdpZHRoOiA2MyU7XG4gICAgaGVpZ2h0OiAxMDAlO1xuICAgIGJhY2tncm91bmQtY29sb3I6ICRibHVlO1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcblxuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkbWVkaXVtKSB7XG4gICAgICBkaXNwbGF5OiBub25lO1xuICAgIH1cbiAgfVxuXG4gICZfX2xvZ28td3JhcHBlciB7XG4gICAgd2lkdGg6IDEwMCU7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbiAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIH1cblxuICAmX19sb2dvLWltZyB7XG4gICAgbWFyZ2luLWJvdHRvbTogNTBweDtcbiAgfVxuXG4gICZfX2xvZ28tdGl0bGUge1xuICAgIGZvbnQtc2l6ZTogNjJweDtcbiAgICBjb2xvcjogJHdoaXRlO1xuICAgIGZvbnQtd2VpZ2h0OiA1MDA7XG4gICAgbGV0dGVyLXNwYWNpbmc6IC0xLjVweDtcbiAgICBsaW5lLWhlaWdodDogNjJweDtcbiAgfVxuXG4gICZfX2Zvb3Rlci10aXRsZSB7XG4gICAgY29sb3I6ICRibHVlO1xuICAgIGZvbnQtc2l6ZTogMTBweDtcbiAgICBvcGFjaXR5OiAwLjc7XG4gICAgYSB7XG4gICAgICB0ZXh0LWRlY29yYXRpb246IG5vbmU7XG4gICAgICBjb2xvcjogJGJsdWU7XG4gICAgfVxuICB9XG59XG4iLCIuYXV0aC1wYWdlIHtcbiAgd2lkdGg6IDEwMCU7XG4gIGhlaWdodDogMTAwJTtcbiAgZGlzcGxheTogZmxleDtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA3NjhweCkge1xuICAuYXV0aC1wYWdlIHtcbiAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICB9XG59XG4uYXV0aC1wYWdlX19jb250ZW50LWJsb2NrIHtcbiAgd2lkdGg6IDM3JTtcbiAgaGVpZ2h0OiAxMDAlO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiB3aGl0ZTtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA3NjhweCkge1xuICAuYXV0aC1wYWdlX19jb250ZW50LWJsb2NrIHtcbiAgICB3aWR0aDogMTAwJTtcbiAgfVxufVxuLmF1dGgtcGFnZV9fY29udGVudC13cmFwcGVyIHtcbiAgd2lkdGg6IDQ1JTtcbiAgaGVpZ2h0OiAxMDAlO1xuICBwYWRkaW5nOiAxNnB4O1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmF1dGgtcGFnZV9fY29udGVudC13cmFwcGVyIHtcbiAgICB3aWR0aDogNzAlO1xuICB9XG59XG5AbWVkaWEgKG1pbi13aWR0aDogNzY4cHgpIGFuZCAobWF4LXdpZHRoOiA5OTJweCkge1xuICAuYXV0aC1wYWdlX19jb250ZW50LXdyYXBwZXIge1xuICAgIHdpZHRoOiA0NSU7XG4gIH1cbn1cbi5hdXRoLXBhZ2VfX2dyb3VwIHtcbiAgbWFyZ2luLXRvcDogMjhweDtcbn1cbi5hdXRoLXBhZ2VfX2dyb3VwLXRpdGxlIHtcbiAgZm9udC1zaXplOiAzMnB4O1xuICBmb250LXdlaWdodDogNTAwO1xuICBtYXJnaW4tdG9wOiAzN3B4O1xuICBsZXR0ZXItc3BhY2luZzogLTAuN3B4O1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gIGxpbmUtaGVpZ2h0OiAzN3B4O1xuICBjb2xvcjogIzRBNEE0QTtcbn1cbi5hdXRoLXBhZ2VfX2dyb3VwLXN1Yi10aXRsZSB7XG4gIGZvbnQtc2l6ZTogMjRweDtcbiAgZm9udC13ZWlnaHQ6IDUwMDtcbiAgbWFyZ2luLWJvdHRvbTogNjBweDtcbiAgbGV0dGVyLXNwYWNpbmc6IC0wLjVweDtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICBsaW5lLWhlaWdodDogMjRweDtcbiAgY29sb3I6ICM0QTRBNEE7XG59XG4uYXV0aC1wYWdlX19nb29nbGUtYnV0dG9uLXdyYXBwZXIge1xuICBtYXJnaW4tdG9wOiAzMnB4O1xuICBtYXJnaW4tYm90dG9tOiAxMHB4O1xuICB3aWR0aDogMTAwJTtcbiAgZGlzcGxheTogZmxleDtcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cbi5hdXRoLXBhZ2VfX2dvb2dsZS1idXR0b24ge1xuICB3aWR0aDogOTUlO1xuICBwYWRkaW5nOiAwO1xuICBib3gtc2hhZG93OiAwIDAgMTFweCAwICNFOEVBRkMsIDAgMCAwIC0ycHggI0IyQjJCMjFBLCAwIDFweCA4cHggMCAjOUE5QTlBMUE7XG59XG4uYXV0aC1wYWdlX19nb29nbGUtYnV0dG9uLWljb24ge1xuICB3aWR0aDogMjBweDtcbiAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xufVxuLmF1dGgtcGFnZV9fYm9yZGVyLXdyYXBwZXIge1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbiAgbWFyZ2luOiAzMnB4IDA7XG59XG4uYXV0aC1wYWdlX19ib3JkZXItbGluZSB7XG4gIGhlaWdodDogMXB4O1xuICB3aWR0aDogMTAwJTtcbiAgYmFja2dyb3VuZC1jb2xvcjogI0I5QjlCOTtcbiAgb3BhY2l0eTogMC4zO1xufVxuLmF1dGgtcGFnZV9fYm9yZGVyLXRpdGxlIHtcbiAgZm9udC1zaXplOiAxMS4ycHg7XG4gIHBhZGRpbmc6IDAgMTZweDtcbiAgbWFyZ2luOiAwO1xuICBjb2xvcjogIzRBNEE0QTtcbn1cbi5hdXRoLXBhZ2VfX2xvZ28ge1xuICB3aWR0aDogNjMlO1xuICBoZWlnaHQ6IDEwMCU7XG4gIGJhY2tncm91bmQtY29sb3I6ICM1MzZERkU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNzY4cHgpIHtcbiAgLmF1dGgtcGFnZV9fbG9nbyB7XG4gICAgZGlzcGxheTogbm9uZTtcbiAgfVxufVxuLmF1dGgtcGFnZV9fbG9nby13cmFwcGVyIHtcbiAgd2lkdGg6IDEwMCU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xuICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xufVxuLmF1dGgtcGFnZV9fbG9nby1pbWcge1xuICBtYXJnaW4tYm90dG9tOiA1MHB4O1xufVxuLmF1dGgtcGFnZV9fbG9nby10aXRsZSB7XG4gIGZvbnQtc2l6ZTogNjJweDtcbiAgY29sb3I6IHdoaXRlO1xuICBmb250LXdlaWdodDogNTAwO1xuICBsZXR0ZXItc3BhY2luZzogLTEuNXB4O1xuICBsaW5lLWhlaWdodDogNjJweDtcbn1cbi5hdXRoLXBhZ2VfX2Zvb3Rlci10aXRsZSB7XG4gIGNvbG9yOiAjNTM2REZFO1xuICBmb250LXNpemU6IDEwcHg7XG4gIG9wYWNpdHk6IDAuNztcbn1cbi5hdXRoLXBhZ2VfX2Zvb3Rlci10aXRsZSBhIHtcbiAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xuICBjb2xvcjogIzUzNkRGRTtcbn0iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iLCIkZnctbGlnaHRlcjogNDAwO1xuJGZ3LW5vcm1hbDogNTAwO1xuJGZ3LWJvbGQ6IDYwMDtcblxuXG4kZnMteHM6IDExLjJweDtcbiRmcy1zbWFsbDogMTRweDtcbiRmcy1ub3JtYWw6IDE2cHg7XG4kZnMtcmVndWxhcjogMThweDtcbiRmcy1tZWRpdW06IDIxcHg7XG4kZnMtbGFyZ2U6IDI0cHg7XG4kZnMteGw6IDI4cHg7XG4kZnMteHhsOiAzOHB4O1xuJGZzLXh4eGw6IDQycHg7XG4iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AuthPageComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-auth-page',
                            templateUrl: './auth-page.component.html',
                            styleUrls: ['./auth-page.component.scss']
                        }]
                    }], function() {
                        return [{
                            type: _services__WEBPACK_IMPORTED_MODULE_2__["AuthService"]
                        }, {
                            type: _angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]
                        }];
                    }, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/containers/index.ts":
            /*!************************************************!*\
              !*** ./src/app/pages/auth/containers/index.ts ***!
              \************************************************/
            /*! exports provided: AuthPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _auth_page_auth_page_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./auth-page/auth-page.component */ "./src/app/pages/auth/containers/auth-page/auth-page.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "AuthPageComponent", function() {
                    return _auth_page_auth_page_component__WEBPACK_IMPORTED_MODULE_0__["AuthPageComponent"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/auth/guards/auth.guard.ts":
            /*!*************************************************!*\
              !*** ./src/app/pages/auth/guards/auth.guard.ts ***!
              \*************************************************/
            /*! exports provided: AuthGuard */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AuthGuard", function() {
                    return AuthGuard;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");




                class AuthGuard {
                    constructor(router) {
                        this.router = router;
                        this.routers = _consts__WEBPACK_IMPORTED_MODULE_1__["routes"];
                    }
                    canActivate(route, state) {
                        const token = localStorage.getItem('token');
                        if (token) {
                            return true;
                        } else {
                            this.router.navigate([this.routers.LOGIN]);
                        }
                    }
                }
                AuthGuard.ɵfac = function AuthGuard_Factory(t) {
                    return new(t || AuthGuard)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"]));
                };
                AuthGuard.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({
                    token: AuthGuard,
                    factory: AuthGuard.ɵfac
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AuthGuard, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"]
                    }], function() {
                        return [{
                            type: _angular_router__WEBPACK_IMPORTED_MODULE_2__["Router"]
                        }];
                    }, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/guards/index.ts":
            /*!********************************************!*\
              !*** ./src/app/pages/auth/guards/index.ts ***!
              \********************************************/
            /*! exports provided: AuthGuard */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _auth_guard__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./auth.guard */ "./src/app/pages/auth/guards/auth.guard.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "AuthGuard", function() {
                    return _auth_guard__WEBPACK_IMPORTED_MODULE_0__["AuthGuard"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/auth/pipes/index.ts":
            /*!*******************************************!*\
              !*** ./src/app/pages/auth/pipes/index.ts ***!
              \*******************************************/
            /*! exports provided: YearPipe */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _year_pipe__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./year.pipe */ "./src/app/pages/auth/pipes/year.pipe.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "YearPipe", function() {
                    return _year_pipe__WEBPACK_IMPORTED_MODULE_0__["YearPipe"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/auth/pipes/year.pipe.ts":
            /*!***********************************************!*\
              !*** ./src/app/pages/auth/pipes/year.pipe.ts ***!
              \***********************************************/
            /*! exports provided: YearPipe */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "YearPipe", function() {
                    return YearPipe;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");



                class YearPipe extends _angular_common__WEBPACK_IMPORTED_MODULE_1__["DatePipe"] {
                    transform(date) {
                        return super.transform(date, 'y');
                    }
                }
                YearPipe.ɵfac = function YearPipe_Factory(t) {
                    return ɵYearPipe_BaseFactory(t || YearPipe);
                };
                YearPipe.ɵpipe = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefinePipe"]({
                    name: "year",
                    type: YearPipe,
                    pure: true
                });
                const ɵYearPipe_BaseFactory = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetInheritedFactory"](YearPipe);
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](YearPipe, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Pipe"],
                        args: [{
                            name: 'year'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/services/auth.service.ts":
            /*!*****************************************************!*\
              !*** ./src/app/pages/auth/services/auth.service.ts ***!
              \*****************************************************/
            /*! exports provided: AuthService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "AuthService", function() {
                    return AuthService;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");



                class AuthService {
                    login() {
                        localStorage.setItem('token', 'token');
                    }
                    sign() {
                        localStorage.setItem('token', 'token');
                    }
                    signOut() {
                        localStorage.removeItem('token');
                    }
                    getUser() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            name: 'John',
                            lastName: 'Smith'
                        });
                    }
                }
                AuthService.ɵfac = function AuthService_Factory(t) {
                    return new(t || AuthService)();
                };
                AuthService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({
                    token: AuthService,
                    factory: AuthService.ɵfac,
                    providedIn: 'root'
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AuthService, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
                        args: [{
                            providedIn: 'root'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/services/email.service.ts":
            /*!******************************************************!*\
              !*** ./src/app/pages/auth/services/email.service.ts ***!
              \******************************************************/
            /*! exports provided: EmailService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "EmailService", function() {
                    return EmailService;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");



                class EmailService {
                    loadEmails() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])([{
                            name: 'Jane Hew',
                            time: '9:32',
                            message: 'Hey! How is it going?'
                        }, {
                            name: 'Lloyd Brown',
                            time: '9:18',
                            message: 'Check out my new Dashboard'
                        }, {
                            name: 'Mark Winstein',
                            time: '9:15',
                            message: 'I want rearrange the appointment'
                        }, {
                            name: 'Liana Dutti',
                            time: '9:09',
                            message: 'Good news from sale department'
                        }]);
                    }
                }
                EmailService.ɵfac = function EmailService_Factory(t) {
                    return new(t || EmailService)();
                };
                EmailService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({
                    token: EmailService,
                    factory: EmailService.ɵfac,
                    providedIn: 'root'
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](EmailService, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
                        args: [{
                            providedIn: 'root'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/auth/services/index.ts":
            /*!**********************************************!*\
              !*** ./src/app/pages/auth/services/index.ts ***!
              \**********************************************/
            /*! exports provided: AuthService, EmailService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _auth_service__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./auth.service */ "./src/app/pages/auth/services/auth.service.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "AuthService", function() {
                    return _auth_service__WEBPACK_IMPORTED_MODULE_0__["AuthService"];
                });

                /* harmony import */
                var _email_service__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./email.service */ "./src/app/pages/auth/services/email.service.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "EmailService", function() {
                    return _email_service__WEBPACK_IMPORTED_MODULE_1__["EmailService"];
                });





                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/daily-line-chart/daily-line-chart.component.ts":
            /*!*******************************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/daily-line-chart/daily-line-chart.component.ts ***!
              \*******************************************************************************************/
            /*! exports provided: DailyLineChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "DailyLineChartComponent", function() {
                    return DailyLineChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../consts */ "./src/app/pages/dashboard/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_material_select__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/select */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/select.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_core__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/core */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/core.js");








                const _c0 = ["chart"];
                var matSelectedFields;
                (function(matSelectedFields) {
                    matSelectedFields["daily"] = "Daily";
                    matSelectedFields["weekly"] = "Weekly";
                    matSelectedFields["monthly"] = "Monthly";
                })(matSelectedFields || (matSelectedFields = {}));
                class DailyLineChartComponent {
                    constructor() {
                        this.matSelectFields = matSelectedFields;
                        this.selectedMatSelectValue = matSelectedFields.monthly;
                        this.colors = _consts__WEBPACK_IMPORTED_MODULE_1__["colors"];
                    }
                    ngOnInit() {
                        this.initChart(this.dailyLineChartData.monthlyData, this.dailyLineChartData.labels);
                    }
                    ngAfterViewInit() {
                        this.chartObj = new ApexCharts(this.chart.nativeElement, this.chartOptions);
                        this.chartObj.render();
                    }
                    initChart(data, labels) {
                        this.chartOptions = {
                            legend: {
                                show: false
                            },
                            markers: {
                                size: [0, 0, 5]
                            },
                            series: [{
                                name: 'Mobile',
                                type: 'line',
                                data: data.mobile,
                            }, {
                                name: 'Desktop',
                                type: 'area',
                                data: data.desktop
                            }, {
                                name: 'Tablet',
                                type: 'line',
                                data: data.tablet
                            }],
                            colors: [_consts__WEBPACK_IMPORTED_MODULE_1__["colors"].BLUE, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].LIGHT_BLUE, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].YELLOW],
                            chart: {
                                toolbar: {
                                    show: false
                                },
                                height: 350,
                                width: '100%',
                                type: 'line',
                                stacked: true
                            },
                            stroke: {
                                width: [2, 0, 2],
                                curve: ['smooth', 'smooth', 'straight']
                            },
                            plotOptions: {
                                bar: {
                                    columnWidth: '50%'
                                },
                            },
                            grid: {
                                yaxis: {
                                    lines: {
                                        show: false,
                                    }
                                },
                            },
                            fill: {
                                opacity: 1,
                                gradient: {
                                    inverseColors: false,
                                    shade: 'light',
                                    type: 'vertical',
                                    opacityFrom: 0.85,
                                    opacityTo: 0.55,
                                    stops: [0, 100, 100, 100]
                                }
                            },
                            labels: labels,
                            xaxis: {
                                type: 'datetime',
                                labels: {
                                    style: {
                                        colors: '#4A4A4A',
                                        fontSize: '0.875rem',
                                        fontFamily: 'Roboto, Helvetica, Arial, sans-serif',
                                        fontWeight: 400,
                                    },
                                },
                            },
                            yaxis: {
                                show: true,
                                labels: {
                                    style: {
                                        colors: '#4A4A4A',
                                        fontSize: '0.875rem',
                                        fontFamily: 'Roboto, Helvetica, Arial, sans-serif',
                                        fontWeight: 400,
                                    },
                                },
                            },
                            tooltip: {
                                custom: ({
                                    series,
                                    seriesIndex,
                                    dataPointIndex,
                                    w
                                }) => {
                                    return _consts__WEBPACK_IMPORTED_MODULE_2__["customTooltip"];
                                }
                            }
                        };
                    };
                    changedMatSelectionValue() {
                        switch (this.selectedMatSelectValue) {
                            case matSelectedFields.daily:
                                this.chartOptions = Object.assign(Object.assign({}, this.chartOptions), {
                                    series: [{
                                        name: 'Mobile',
                                        type: 'line',
                                        data: this.dailyLineChartData.dailyData.mobile,
                                    }, {
                                        name: 'Desktop',
                                        type: 'area',
                                        data: this.dailyLineChartData.dailyData.desktop,
                                    }, {
                                        name: 'Tablet',
                                        type: 'line',
                                        data: this.dailyLineChartData.dailyData.tablet,
                                    }]
                                });
                                break;
                            case matSelectedFields.weekly:
                                this.chartOptions = Object.assign(Object.assign({}, this.chartOptions), {
                                    series: [{
                                        name: 'Mobile',
                                        type: 'line',
                                        data: this.dailyLineChartData.weeklyData.mobile,
                                    }, {
                                        name: 'Desktop',
                                        type: 'area',
                                        data: this.dailyLineChartData.weeklyData.desktop,
                                    }, {
                                        name: 'Tablet',
                                        type: 'line',
                                        data: this.dailyLineChartData.weeklyData.tablet,
                                    }]
                                });
                                break;
                            default:
                                this.chartOptions = Object.assign(Object.assign({}, this.chartOptions), {
                                    series: [{
                                        name: 'Mobile',
                                        type: 'line',
                                        data: this.dailyLineChartData.monthlyData.mobile,
                                    }, {
                                        name: 'Desktop',
                                        type: 'area',
                                        data: this.dailyLineChartData.monthlyData.desktop,
                                    }, {
                                        name: 'Tablet',
                                        type: 'line',
                                        data: this.dailyLineChartData.monthlyData.tablet,
                                    }]
                                });
                        }
                        this.chartObj.updateSeries(this.chartOptions.series);
                    }
                }
                DailyLineChartComponent.ɵfac = function DailyLineChartComponent_Factory(t) {
                    return new(t || DailyLineChartComponent)();
                };
                DailyLineChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: DailyLineChartComponent,
                    selectors: [
                        ["app-daily-line-chart"]
                    ],
                    viewQuery: function DailyLineChartComponent_Query(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵviewQuery"](_c0, true);
                        }
                        if (rf & 2) {
                            var _t;
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.chart = _t.first);
                        }
                    },
                    inputs: {
                        dailyLineChartData: "dailyLineChartData"
                    },
                    decls: 27,
                    vars: 4,
                    consts: [
                        [1, "chart"],
                        [1, "chart__header"],
                        [1, "chart__title"],
                        [1, "chart-legend"],
                        [1, "chart-legend__item"],
                        [1, "chart-legend__icon", "yellow"],
                        [1, "chart-legend__title"],
                        [1, "chart-legend__icon", "blue"],
                        [1, "chart-legend__icon", "light-blue"],
                        [1, "chart-select", 3, "ngModel", "ngModelChange", "selectionChange"],
                        [3, "value"],
                        [1, "chart__content"],
                        [1, "chart__content-item"],
                        ["chart", ""]
                    ],
                    template: function DailyLineChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "p", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Daily Line Chart");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](6, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "span", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](8, "Tablet");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](10, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "span", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, "Mobile");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](14, "div", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "span", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, "Desktop");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "mat-select", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("ngModelChange", function DailyLineChartComponent_Template_mat_select_ngModelChange_17_listener($event) {
                                return ctx.selectedMatSelectValue = $event;
                            })("selectionChange", function DailyLineChartComponent_Template_mat_select_selectionChange_17_listener() {
                                return ctx.changedMatSelectionValue();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "mat-option", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](19, "Daily");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](20, "mat-option", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](21, "Weekly");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "mat-option", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](23, "Monthly");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](24, "mat-card-content", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](25, "div", 12, 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngModel", ctx.selectedMatSelectValue);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.daily);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.weekly);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.monthly);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCardTitle"], _angular_material_select__WEBPACK_IMPORTED_MODULE_4__["MatSelect"], _angular_forms__WEBPACK_IMPORTED_MODULE_5__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_5__["NgModel"], _angular_material_core__WEBPACK_IMPORTED_MODULE_6__["MatOption"], _angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCardContent"]],
                    styles: [".chart[_ngcontent-%COMP%] {\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n  margin: 16px 24px;\n}\n.chart__header[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n  padding: 8px;\n}\n@media (max-width: 576px) {\n  .chart__header[_ngcontent-%COMP%] {\n    flex-wrap: wrap;\n  }\n}\n.chart__title[_ngcontent-%COMP%] {\n  margin: 0;\n  display: flex;\n  align-items: center;\n  color: #6E6E6E;\n  font-weight: 500;\n  font-size: 18px;\n  text-transform: none;\n  line-height: 1.6;\n  letter-spacing: 0.12px;\n  order: 1;\n}\n.chart__content[_ngcontent-%COMP%] {\n  height: 380px;\n  width: 100%;\n}\n@media (max-width: 576px) {\n  .chart__content[_ngcontent-%COMP%] {\n    overflow-x: scroll;\n  }\n}\n@media (max-width: 576px) {\n  .chart__content-item[_ngcontent-%COMP%] {\n    width: 600px;\n  }\n}\n.chart-legend[_ngcontent-%COMP%] {\n  display: flex;\n  order: 2;\n}\n.chart-legend__item[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n  margin-top: 2.24px;\n  margin-right: 24px;\n}\n.chart-legend__icon[_ngcontent-%COMP%] {\n  width: 5px;\n  height: 5px;\n  border-radius: 50%;\n}\n.chart-legend__title[_ngcontent-%COMP%] {\n  font-weight: 400;\n  text-transform: none;\n  font-size: 18px;\n  margin-left: 8px;\n}\n@media (max-width: 576px) {\n  .chart-legend[_ngcontent-%COMP%] {\n    margin-top: 20px;\n    order: 3;\n  }\n}\n.chart-select[_ngcontent-%COMP%] {\n  order: 3;\n}\n@media (max-width: 576px) {\n  .chart-select[_ngcontent-%COMP%] {\n    order: 2;\n  }\n}\n.yellow[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n}\n.blue[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n}\n.light-blue[_ngcontent-%COMP%] {\n  background-color: #B1BCFF;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvZGFpbHktbGluZS1jaGFydC9kYWlseS1saW5lLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy9kYWlseS1saW5lLWNoYXJ0L2RhaWx5LWxpbmUtY2hhcnQuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9jb2xvcnMuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFJQTtFQUNFLGlGQUFBO0VBQ0EsaUJBQUE7QUNIRjtBREtHO0VBQ0UsYUFBQTtFQUNBLDhCQUFBO0VBQ0EsWUFBQTtBQ0hMO0FES0s7RUFMRjtJQU1JLGVBQUE7RUNGTDtBQUNGO0FES0c7RUFDRSxTQUFBO0VBQ0EsYUFBQTtFQUNBLG1CQUFBO0VBQ0EsY0VWRTtFRldGLGdCR3RCTztFSHVCUCxlR2hCUTtFSGlCUixvQkFBQTtFQUNBLGdCQUFBO0VBQ0Esc0JBQUE7RUFDQSxRQUFBO0FDSEw7QURNRTtFQUNFLGFBQUE7RUFDQSxXQUFBO0FDSko7QURLSTtFQUhGO0lBSUksa0JBQUE7RUNGSjtBQUNGO0FETUk7RUFERjtJQUVJLFlBQUE7RUNISjtBQUNGO0FET0E7RUFDRSxhQUFBO0VBQ0EsUUFBQTtBQ0pGO0FETUU7RUFDRSxhQUFBO0VBQ0EsbUJBQUE7RUFDQSxrQkFBQTtFQUNBLGtCQUFBO0FDSko7QURPRTtFQUNFLFVBQUE7RUFDQSxXQUFBO0VBQ0Esa0JBQUE7QUNMSjtBRFFFO0VBQ0UsZ0JHaEVTO0VIaUVULG9CQUFBO0VBQ0EsZUcxRFM7RUgyRFQsZ0JBQUE7QUNOSjtBRFNFO0VBeEJGO0lBeUJJLGdCQUFBO0lBQ0EsUUFBQTtFQ05GO0FBQ0Y7QURTQTtFQUNFLFFBQUE7QUNORjtBRFFFO0VBSEY7SUFJSSxRQUFBO0VDTEY7QUFDRjtBRFFBO0VBQ0UseUJFckZPO0FEZ0ZUO0FEUUE7RUFDRSx5QkV4Rks7QURtRlA7QURRQTtFQUNFLHlCRTFGVztBRHFGYiIsImZpbGUiOiJzcmMvYXBwL3BhZ2VzL2Rhc2hib2FyZC9jb21wb25lbnRzL2RhaWx5LWxpbmUtY2hhcnQvZGFpbHktbGluZS1jaGFydC5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9jb2xvcnNcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9mb250XCI7XG5AaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvdmFyaWFibGVzXCI7XG5cbi5jaGFydCB7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAkc2hhZG93LXdoaXRlLCAwIDNweCAzcHggLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuICBtYXJnaW46IDE2cHggMjRweDtcblxuICAgJl9faGVhZGVyIHtcbiAgICAgZGlzcGxheTogZmxleDtcbiAgICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgICBwYWRkaW5nOiA4cHg7XG5cbiAgICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgIGZsZXgtd3JhcDogd3JhcDtcbiAgICAgfVxuICAgfVxuXG4gICAmX190aXRsZSB7XG4gICAgIG1hcmdpbjogMDtcbiAgICAgZGlzcGxheTogZmxleDtcbiAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgY29sb3I6ICRncmV5O1xuICAgICBmb250LXdlaWdodDogJGZ3LW5vcm1hbDtcbiAgICAgZm9udC1zaXplOiAkZnMtcmVndWxhcjtcbiAgICAgdGV4dC10cmFuc2Zvcm06IG5vbmU7XG4gICAgIGxpbmUtaGVpZ2h0OiAxLjY7XG4gICAgIGxldHRlci1zcGFjaW5nOiAwLjEycHg7XG4gICAgIG9yZGVyOiAxO1xuICAgfVxuXG4gICZfX2NvbnRlbnQge1xuICAgIGhlaWdodDogMzgwcHg7XG4gICAgd2lkdGg6IDEwMCU7XG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgb3ZlcmZsb3cteDogc2Nyb2xsO1xuICAgIH1cbiAgfVxuXG4gICZfX2NvbnRlbnQtaXRlbSB7XG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgd2lkdGg6IDYwMHB4O1xuICAgIH1cbiAgfVxufVxuXG4uY2hhcnQtbGVnZW5kIHtcbiAgZGlzcGxheTogZmxleDtcbiAgb3JkZXI6IDI7XG5cbiAgJl9faXRlbSB7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIG1hcmdpbi10b3A6IDIuMjRweDtcbiAgICBtYXJnaW4tcmlnaHQ6IDI0cHg7XG4gIH1cblxuICAmX19pY29uIHtcbiAgICB3aWR0aDogNXB4O1xuICAgIGhlaWdodDogNXB4O1xuICAgIGJvcmRlci1yYWRpdXM6IDUwJTtcbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgdGV4dC10cmFuc2Zvcm06IG5vbmU7XG4gICAgZm9udC1zaXplOiAkZnMtcmVndWxhcjtcbiAgICBtYXJnaW4tbGVmdDogOHB4O1xuICB9XG5cbiAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgIG1hcmdpbi10b3A6IDIwcHg7XG4gICAgb3JkZXI6IDM7XG4gIH1cbn1cblxuLmNoYXJ0LXNlbGVjdCB7XG4gIG9yZGVyOiAzO1xuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICBvcmRlcjogMjtcbiAgfVxufVxuXG4ueWVsbG93IHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJHllbGxvdztcbn1cblxuLmJsdWUge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbn1cblxuLmxpZ2h0LWJsdWUge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkd2hpdGUtYmx1ZTtcbn1cblxuIiwiLmNoYXJ0IHtcbiAgYm94LXNoYWRvdzogMCAzcHggMTFweCAwICNFOEVBRkMsIDAgM3B4IDNweCAtMnB4ICNCMkIyQjIxQSwgMCAxcHggOHB4IDAgIzlBOUE5QTFBO1xuICBtYXJnaW46IDE2cHggMjRweDtcbn1cbi5jaGFydF9faGVhZGVyIHtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICBwYWRkaW5nOiA4cHg7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmNoYXJ0X19oZWFkZXIge1xuICAgIGZsZXgtd3JhcDogd3JhcDtcbiAgfVxufVxuLmNoYXJ0X190aXRsZSB7XG4gIG1hcmdpbjogMDtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIGZvbnQtd2VpZ2h0OiA1MDA7XG4gIGZvbnQtc2l6ZTogMThweDtcbiAgdGV4dC10cmFuc2Zvcm06IG5vbmU7XG4gIGxpbmUtaGVpZ2h0OiAxLjY7XG4gIGxldHRlci1zcGFjaW5nOiAwLjEycHg7XG4gIG9yZGVyOiAxO1xufVxuLmNoYXJ0X19jb250ZW50IHtcbiAgaGVpZ2h0OiAzODBweDtcbiAgd2lkdGg6IDEwMCU7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmNoYXJ0X19jb250ZW50IHtcbiAgICBvdmVyZmxvdy14OiBzY3JvbGw7XG4gIH1cbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuY2hhcnRfX2NvbnRlbnQtaXRlbSB7XG4gICAgd2lkdGg6IDYwMHB4O1xuICB9XG59XG5cbi5jaGFydC1sZWdlbmQge1xuICBkaXNwbGF5OiBmbGV4O1xuICBvcmRlcjogMjtcbn1cbi5jaGFydC1sZWdlbmRfX2l0ZW0ge1xuICBkaXNwbGF5OiBmbGV4O1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICBtYXJnaW4tdG9wOiAyLjI0cHg7XG4gIG1hcmdpbi1yaWdodDogMjRweDtcbn1cbi5jaGFydC1sZWdlbmRfX2ljb24ge1xuICB3aWR0aDogNXB4O1xuICBoZWlnaHQ6IDVweDtcbiAgYm9yZGVyLXJhZGl1czogNTAlO1xufVxuLmNoYXJ0LWxlZ2VuZF9fdGl0bGUge1xuICBmb250LXdlaWdodDogNDAwO1xuICB0ZXh0LXRyYW5zZm9ybTogbm9uZTtcbiAgZm9udC1zaXplOiAxOHB4O1xuICBtYXJnaW4tbGVmdDogOHB4O1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5jaGFydC1sZWdlbmQge1xuICAgIG1hcmdpbi10b3A6IDIwcHg7XG4gICAgb3JkZXI6IDM7XG4gIH1cbn1cblxuLmNoYXJ0LXNlbGVjdCB7XG4gIG9yZGVyOiAzO1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5jaGFydC1zZWxlY3Qge1xuICAgIG9yZGVyOiAyO1xuICB9XG59XG5cbi55ZWxsb3cge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjZmZjMjYwO1xufVxuXG4uYmx1ZSB7XG4gIGJhY2tncm91bmQtY29sb3I6ICM1MzZERkU7XG59XG5cbi5saWdodC1ibHVlIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI0IxQkNGRjtcbn0iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iLCIkZnctbGlnaHRlcjogNDAwO1xuJGZ3LW5vcm1hbDogNTAwO1xuJGZ3LWJvbGQ6IDYwMDtcblxuXG4kZnMteHM6IDExLjJweDtcbiRmcy1zbWFsbDogMTRweDtcbiRmcy1ub3JtYWw6IDE2cHg7XG4kZnMtcmVndWxhcjogMThweDtcbiRmcy1tZWRpdW06IDIxcHg7XG4kZnMtbGFyZ2U6IDI0cHg7XG4kZnMteGw6IDI4cHg7XG4kZnMteHhsOiAzOHB4O1xuJGZzLXh4eGw6IDQycHg7XG4iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DailyLineChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-daily-line-chart',
                            templateUrl: './daily-line-chart.component.html',
                            styleUrls: ['./daily-line-chart.component.scss']
                        }]
                    }], null, {
                        dailyLineChartData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }],
                        chart: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"],
                            args: ['chart']
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/index.ts":
            /*!*****************************************************!*\
              !*** ./src/app/pages/dashboard/components/index.ts ***!
              \*****************************************************/
            /*! exports provided: VisitsChartComponent, PerformanceChartComponent, RevenueChartComponent, ServerChartComponent, DailyLineChartComponent, SupportRequestsComponent, ProjectStatChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _visits_chart_visits_chart_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./visits-chart/visits-chart.component */ "./src/app/pages/dashboard/components/visits-chart/visits-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "VisitsChartComponent", function() {
                    return _visits_chart_visits_chart_component__WEBPACK_IMPORTED_MODULE_0__["VisitsChartComponent"];
                });

                /* harmony import */
                var _performance_chart_performance_chart_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./performance-chart/performance-chart.component */ "./src/app/pages/dashboard/components/performance-chart/performance-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "PerformanceChartComponent", function() {
                    return _performance_chart_performance_chart_component__WEBPACK_IMPORTED_MODULE_1__["PerformanceChartComponent"];
                });

                /* harmony import */
                var _revenue_chart_revenue_chart_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./revenue-chart/revenue-chart.component */ "./src/app/pages/dashboard/components/revenue-chart/revenue-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "RevenueChartComponent", function() {
                    return _revenue_chart_revenue_chart_component__WEBPACK_IMPORTED_MODULE_2__["RevenueChartComponent"];
                });

                /* harmony import */
                var _server_chart_server_chart_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ./server-chart/server-chart.component */ "./src/app/pages/dashboard/components/server-chart/server-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "ServerChartComponent", function() {
                    return _server_chart_server_chart_component__WEBPACK_IMPORTED_MODULE_3__["ServerChartComponent"];
                });

                /* harmony import */
                var _daily_line_chart_daily_line_chart_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ./daily-line-chart/daily-line-chart.component */ "./src/app/pages/dashboard/components/daily-line-chart/daily-line-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "DailyLineChartComponent", function() {
                    return _daily_line_chart_daily_line_chart_component__WEBPACK_IMPORTED_MODULE_4__["DailyLineChartComponent"];
                });

                /* harmony import */
                var _support_requests_support_requests_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! ./support-requests/support-requests.component */ "./src/app/pages/dashboard/components/support-requests/support-requests.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "SupportRequestsComponent", function() {
                    return _support_requests_support_requests_component__WEBPACK_IMPORTED_MODULE_5__["SupportRequestsComponent"];
                });

                /* harmony import */
                var _project_stat_chart_project_stat_chart_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ./project-stat-chart/project-stat-chart.component */ "./src/app/pages/dashboard/components/project-stat-chart/project-stat-chart.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "ProjectStatChartComponent", function() {
                    return _project_stat_chart_project_stat_chart_component__WEBPACK_IMPORTED_MODULE_6__["ProjectStatChartComponent"];
                });










                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/performance-chart/performance-chart.component.ts":
            /*!*********************************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/performance-chart/performance-chart.component.ts ***!
              \*********************************************************************************************/
            /*! exports provided: PerformanceChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "PerformanceChartComponent", function() {
                    return PerformanceChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/progress-bar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/progress-bar.js");





                class PerformanceChartComponent {}
                PerformanceChartComponent.ɵfac = function PerformanceChartComponent_Factory(t) {
                    return new(t || PerformanceChartComponent)();
                };
                PerformanceChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: PerformanceChartComponent,
                    selectors: [
                        ["app-performance-chart"]
                    ],
                    inputs: {
                        performanceChartData: "performanceChartData"
                    },
                    decls: 22,
                    vars: 2,
                    consts: [
                        [1, "performance-chart"],
                        [1, "performance-chart__header"],
                        [1, "performance-chart__header-title"],
                        [1, "performance-chart__content"],
                        [1, "performance-chart__content-header"],
                        [1, "performance-chart__content-header-item"],
                        [1, "performance-chart__content-header-item-icon_blue"],
                        [1, "performance-chart__content-header-item-text"],
                        [1, "performance-chart__content-header-item-icon_yellow"],
                        [1, "performance-chart__progress-wrapper"],
                        [1, "performance-chart__progress-title"],
                        ["mode", "determinate", 1, "performance-chart__progress-bar", 3, "value"],
                        ["mode", "determinate", "color", "accent", 1, "performance-chart__progress-bar", 3, "value"]
                    ],
                    template: function PerformanceChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "App Performance");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](8, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "span", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10, "Integration");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "div", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "span", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "SDK");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "div", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "h6", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "Integration");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](18, "mat-progress-bar", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "h6", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "SDK");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](21, "mat-progress-bar", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.performanceChartData.integration);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.performanceChartData.sdk);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardContent"], _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_3__["MatProgressBar"]],
                    styles: [".performance-chart[_ngcontent-%COMP%] {\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n  display: flex;\n  flex-direction: column;\n  height: 192px;\n  justify-content: space-between;\n}\n.performance-chart__header[_ngcontent-%COMP%] {\n  align-items: center;\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n}\n.performance-chart__header-title[_ngcontent-%COMP%] {\n  font-size: 20px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.performance-chart__content[_ngcontent-%COMP%] {\n  display: flex;\n  height: 70%;\n  flex-direction: column;\n  justify-content: space-between;\n}\n.performance-chart__content-header[_ngcontent-%COMP%] {\n  display: flex;\n}\n.performance-chart__content-header-item[_ngcontent-%COMP%] {\n  align-items: center;\n  display: flex;\n  margin-right: 16px;\n}\n.performance-chart__content-header-item-icon_blue[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  border-radius: 50%;\n  width: 5px;\n  height: 5px;\n}\n.performance-chart__content-header-item-icon_yellow[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n  border-radius: 50%;\n  width: 5px;\n  height: 5px;\n}\n.performance-chart__content-header-item-text[_ngcontent-%COMP%] {\n  margin-left: 8px;\n  color: #6E6E6E;\n}\n.performance-chart__progress-title[_ngcontent-%COMP%] {\n  margin: 20px 0 5px 0;\n  font-weight: 400;\n  font-size: 21px;\n  color: #6E6E6E;\n}\n.performance-chart__progress-bar[_ngcontent-%COMP%] {\n  margin-bottom: 8px;\n}\n@media (576px) {\n  .performance-chart__progress-bar[_ngcontent-%COMP%] {\n    margin-bottom: 10px;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcGVyZm9ybWFuY2UtY2hhcnQvcGVyZm9ybWFuY2UtY2hhcnQuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL2Rhc2hib2FyZC9jb21wb25lbnRzL3BlcmZvcm1hbmNlLWNoYXJ0L3BlcmZvcm1hbmNlLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxpRkFBQTtFQUNBLGFBQUE7RUFDQSxzQkFBQTtFQUNBLGFBQUE7RUFDQSw4QkFBQTtBQ0hGO0FES0U7RUFDRSxtQkFBQTtFQUNBLGNFREc7RUZFSCxhQUFBO0VBQ0EsOEJBQUE7QUNISjtBREtJO0VBQ0UsZUFBQTtFQUNBLGdCQUFBO0VBQ0EsU0FBQTtFQUNBLGlCQUFBO0FDSE47QURPRTtFQUNFLGFBQUE7RUFDQSxXQUFBO0VBQ0Esc0JBQUE7RUFDQSw4QkFBQTtBQ0xKO0FET0k7RUFDRSxhQUFBO0FDTE47QURPTTtFQUNFLG1CQUFBO0VBQ0EsYUFBQTtFQUNBLGtCQUFBO0FDTFI7QURPUTtFQUNFLHlCRXZDSDtFRndDRyxrQkFBQTtFQUNBLFVBQUE7RUFDQSxXQUFBO0FDTFY7QURRUTtFQUNFLHlCRS9DRDtFRmdEQyxrQkFBQTtFQUNBLFVBQUE7RUFDQSxXQUFBO0FDTlY7QURTUTtFQUNFLGdCQUFBO0VBQ0EsY0UzQ0g7QURvQ1A7QURhRTtFQUNFLG9CQUFBO0VBQ0EsZ0JBQUE7RUFDQSxlR3ZEUTtFSHdEUixjRXJERztBRDBDUDtBRGNFO0VBQ0Usa0JBQUE7QUNaSjtBRGNJO0VBSEY7SUFJSSxtQkFBQTtFQ1hKO0FBQ0YiLCJmaWxlIjoic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy9wZXJmb3JtYW5jZS1jaGFydC9wZXJmb3JtYW5jZS1jaGFydC5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2NvbG9ycyc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvZm9udCc7XG5cbi5wZXJmb3JtYW5jZS1jaGFydCB7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAjRThFQUZDLCAwIDNweCAzcHggLTJweCAjQjJCMkIyMUEsIDAgMXB4IDhweCAwICM5QTlBOUExQTtcbiAgZGlzcGxheTogZmxleDtcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAgaGVpZ2h0OiAxOTJweDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuXG4gICZfX2hlYWRlciB7XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICBjb2xvcjogJGdyZXk7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgICAmLXRpdGxlIHtcbiAgICAgIGZvbnQtc2l6ZTogMjBweDtcbiAgICAgIGZvbnQtd2VpZ2h0OiA0MDA7XG4gICAgICBtYXJnaW46IDA7XG4gICAgICBsaW5lLWhlaWdodDogNDBweDtcbiAgICB9XG4gIH1cblxuICAmX19jb250ZW50IHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGhlaWdodDogNzAlO1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuXG4gICAgJi1oZWFkZXIge1xuICAgICAgZGlzcGxheTogZmxleDtcblxuICAgICAgJi1pdGVtIHtcbiAgICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgICAgZGlzcGxheTogZmxleDtcbiAgICAgICAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuXG4gICAgICAgICYtaWNvbl9ibHVlIHtcbiAgICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiAgICAgICAgICBib3JkZXItcmFkaXVzOiA1MCU7XG4gICAgICAgICAgd2lkdGg6IDVweDtcbiAgICAgICAgICBoZWlnaHQ6IDVweDtcbiAgICAgICAgfVxuXG4gICAgICAgICYtaWNvbl95ZWxsb3cge1xuICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6ICR5ZWxsb3c7XG4gICAgICAgICAgYm9yZGVyLXJhZGl1czogNTAlO1xuICAgICAgICAgIHdpZHRoOiA1cHg7XG4gICAgICAgICAgaGVpZ2h0OiA1cHg7XG4gICAgICAgIH1cblxuICAgICAgICAmLXRleHQge1xuICAgICAgICAgIG1hcmdpbi1sZWZ0OiA4cHg7XG4gICAgICAgICAgY29sb3I6ICRncmV5O1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgJl9fcHJvZ3Jlc3MtdGl0bGUge1xuICAgIG1hcmdpbjogMjBweCAwIDVweCAwO1xuICAgIGZvbnQtd2VpZ2h0OiA0MDA7XG4gICAgZm9udC1zaXplOiAkZnMtbWVkaXVtO1xuICAgIGNvbG9yOiAkZ3JleTtcbiAgfVxuXG4gICZfX3Byb2dyZXNzLWJhciB7XG4gICAgbWFyZ2luLWJvdHRvbTogOHB4O1xuXG4gICAgQG1lZGlhICgkc21hbGwpIHtcbiAgICAgIG1hcmdpbi1ib3R0b206IDEwcHg7XG4gICAgfVxuICB9XG59XG4iLCIucGVyZm9ybWFuY2UtY2hhcnQge1xuICBib3gtc2hhZG93OiAwIDNweCAxMXB4IDAgI0U4RUFGQywgMCAzcHggM3B4IC0ycHggI0IyQjJCMjFBLCAwIDFweCA4cHggMCAjOUE5QTlBMUE7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGhlaWdodDogMTkycHg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi5wZXJmb3JtYW5jZS1jaGFydF9faGVhZGVyIHtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi5wZXJmb3JtYW5jZS1jaGFydF9faGVhZGVyLXRpdGxlIHtcbiAgZm9udC1zaXplOiAyMHB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBtYXJnaW46IDA7XG4gIGxpbmUtaGVpZ2h0OiA0MHB4O1xufVxuLnBlcmZvcm1hbmNlLWNoYXJ0X19jb250ZW50IHtcbiAgZGlzcGxheTogZmxleDtcbiAgaGVpZ2h0OiA3MCU7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi5wZXJmb3JtYW5jZS1jaGFydF9fY29udGVudC1oZWFkZXIge1xuICBkaXNwbGF5OiBmbGV4O1xufVxuLnBlcmZvcm1hbmNlLWNoYXJ0X19jb250ZW50LWhlYWRlci1pdGVtIHtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgZGlzcGxheTogZmxleDtcbiAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xufVxuLnBlcmZvcm1hbmNlLWNoYXJ0X19jb250ZW50LWhlYWRlci1pdGVtLWljb25fYmx1ZSB7XG4gIGJhY2tncm91bmQtY29sb3I6ICM1MzZERkU7XG4gIGJvcmRlci1yYWRpdXM6IDUwJTtcbiAgd2lkdGg6IDVweDtcbiAgaGVpZ2h0OiA1cHg7XG59XG4ucGVyZm9ybWFuY2UtY2hhcnRfX2NvbnRlbnQtaGVhZGVyLWl0ZW0taWNvbl95ZWxsb3cge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjZmZjMjYwO1xuICBib3JkZXItcmFkaXVzOiA1MCU7XG4gIHdpZHRoOiA1cHg7XG4gIGhlaWdodDogNXB4O1xufVxuLnBlcmZvcm1hbmNlLWNoYXJ0X19jb250ZW50LWhlYWRlci1pdGVtLXRleHQge1xuICBtYXJnaW4tbGVmdDogOHB4O1xuICBjb2xvcjogIzZFNkU2RTtcbn1cbi5wZXJmb3JtYW5jZS1jaGFydF9fcHJvZ3Jlc3MtdGl0bGUge1xuICBtYXJnaW46IDIwcHggMCA1cHggMDtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgZm9udC1zaXplOiAyMXB4O1xuICBjb2xvcjogIzZFNkU2RTtcbn1cbi5wZXJmb3JtYW5jZS1jaGFydF9fcHJvZ3Jlc3MtYmFyIHtcbiAgbWFyZ2luLWJvdHRvbTogOHB4O1xufVxuQG1lZGlhICg1NzZweCkge1xuICAucGVyZm9ybWFuY2UtY2hhcnRfX3Byb2dyZXNzLWJhciB7XG4gICAgbWFyZ2luLWJvdHRvbTogMTBweDtcbiAgfVxufSIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIiRmdy1saWdodGVyOiA0MDA7XG4kZnctbm9ybWFsOiA1MDA7XG4kZnctYm9sZDogNjAwO1xuXG5cbiRmcy14czogMTEuMnB4O1xuJGZzLXNtYWxsOiAxNHB4O1xuJGZzLW5vcm1hbDogMTZweDtcbiRmcy1yZWd1bGFyOiAxOHB4O1xuJGZzLW1lZGl1bTogMjFweDtcbiRmcy1sYXJnZTogMjRweDtcbiRmcy14bDogMjhweDtcbiRmcy14eGw6IDM4cHg7XG4kZnMteHh4bDogNDJweDtcbiJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](PerformanceChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-performance-chart',
                            templateUrl: './performance-chart.component.html',
                            styleUrls: ['./performance-chart.component.scss']
                        }]
                    }], null, {
                        performanceChartData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/project-stat-chart/project-stat-chart.component.ts":
            /*!***********************************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/project-stat-chart/project-stat-chart.component.ts ***!
              \***********************************************************************************************/
            /*! exports provided: ProjectStatChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "ProjectStatChartComponent", function() {
                    return ProjectStatChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ../../../../shared/ui-elements/date-menu/date-menu.component */ "./src/app/shared/ui-elements/date-menu/date-menu.component.ts");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var ng_apexcharts__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! ng-apexcharts */ "./node_modules/ng-apexcharts/__ivy_ngcc__/fesm2015/ng-apexcharts.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");








                function ProjectStatChartComponent_p_11_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 20);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("+", ctx_r0.selectedStatsLightBlueData.percent, "%");
                    }
                }

                function ProjectStatChartComponent_p_12_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 21);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", ctx_r1.selectedStatsLightBlueData.percent, "%");
                    }
                }

                function ProjectStatChartComponent_p_50_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 20);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r2 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("+", ctx_r2.selectedStatsSingAppData.percent, "%");
                    }
                }

                function ProjectStatChartComponent_p_51_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 21);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", ctx_r3.selectedStatsSingAppData.percent, "%");
                    }
                }

                function ProjectStatChartComponent_p_89_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 20);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r4 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("+", ctx_r4.selectedStatsRNSData.percent, "%");
                    }
                }

                function ProjectStatChartComponent_p_90_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "p", 21);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const ctx_r5 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", ctx_r5.selectedStatsRNSData.percent, "%");
                    }
                }
                var ProjectsType;
                (function(ProjectsType) {
                    ProjectsType["lightBlue"] = "lightBlue";
                    ProjectsType["SingApp"] = "SingApp";
                    ProjectsType["RNS"] = "RNS";
                })(ProjectsType || (ProjectsType = {}));
                class ProjectStatChartComponent {
                    constructor() {
                        this.projectsType = ProjectsType;
                        this.colors = _consts__WEBPACK_IMPORTED_MODULE_1__["colors"];
                    }
                    ngOnInit() {
                        this.selectedStatsLightBlueData = this.projectsStatsData.lightBlue.daily;
                        this.selectedStatsSingAppData = this.projectsStatsData.singApp.daily;
                        this.selectedStatsRNSData = this.projectsStatsData.rns.daily;
                        this.initChart();
                    }
                    initChart() {
                        this.chartOptions = {
                            chart: {
                                type: 'bar',
                                height: 100,
                                width: 130,
                                toolbar: {
                                    show: false
                                }
                            },
                            legend: {
                                show: false
                            },
                            grid: {
                                show: false
                            },
                            plotOptions: {
                                bar: {
                                    horizontal: false,
                                    columnWidth: '70%',
                                    endingShape: 'rounded',
                                    startingShape: 'rounded'
                                }
                            },
                            dataLabels: {
                                enabled: false
                            },
                            stroke: {
                                show: true,
                                width: 2,
                                colors: ['transparent']
                            },
                            xaxis: {
                                categories: [
                                    'Feb',
                                    'Mar',
                                    'Apr',
                                    'May',
                                    'Jun',
                                    'Jul',
                                    'Aug'
                                ],
                                labels: {
                                    show: false
                                },
                                axisTicks: {
                                    show: false
                                },
                                axisBorder: {
                                    show: false
                                }
                            },
                            yaxis: {
                                show: false
                            },
                            tooltip: {
                                y: {
                                    formatter(val) {
                                        return '$ ' + val + ' thousands';
                                    }
                                }
                            }
                        };
                    }
                    changeDateType(dateType, projectType) {
                        switch (projectType) {
                            case this.projectsType.lightBlue:
                                switch (dateType) {
                                    case 'Weekly':
                                        this.selectedStatsLightBlueData = this.projectsStatsData.lightBlue.week;
                                        break;
                                    case 'Monthly':
                                        this.selectedStatsLightBlueData = this.projectsStatsData.lightBlue.monthly;
                                        break;
                                    default:
                                        this.selectedStatsLightBlueData = this.projectsStatsData.lightBlue.daily;
                                }
                                break;
                            case this.projectsType.SingApp:
                                switch (dateType) {
                                    case 'Weekly':
                                        this.selectedStatsSingAppData = this.projectsStatsData.singApp.week;
                                        break;
                                    case 'Monthly':
                                        this.selectedStatsSingAppData = this.projectsStatsData.singApp.monthly;
                                        break;
                                    default:
                                        this.selectedStatsSingAppData = this.projectsStatsData.singApp.daily;
                                }
                                break;
                            case this.projectsType.RNS:
                                switch (dateType) {
                                    case 'Weekly':
                                        this.selectedStatsRNSData = this.projectsStatsData.rns.week;
                                        break;
                                    case 'Monthly':
                                        this.selectedStatsRNSData = this.projectsStatsData.rns.monthly;
                                        break;
                                    default:
                                        this.selectedStatsRNSData = this.projectsStatsData.rns.daily;
                                }
                                break;
                        }
                    }
                }
                ProjectStatChartComponent.ɵfac = function ProjectStatChartComponent_Factory(t) {
                    return new(t || ProjectStatChartComponent)();
                };
                ProjectStatChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: ProjectStatChartComponent,
                    selectors: [
                        ["app-project-stat-chart"]
                    ],
                    inputs: {
                        projectsStatsData: "projectsStatsData"
                    },
                    decls: 118,
                    vars: 57,
                    consts: [
                        [1, "project-stat"],
                        [1, "project-stat__item"],
                        [1, "project-stat__title"],
                        [1, "project-stat__title-text"],
                        [3, "changeDateType"],
                        [1, "project-stat-content"],
                        [1, "project-stat-content__total-info-wrapper"],
                        [1, "project-stat-content__total-info"],
                        [1, "project-stat-content__total-info-users"],
                        ["class", "project-stat-content__total-info-percent", 4, "ngIf"],
                        ["class", "project-stat-content__total-info-percent-warn", 4, "ngIf"],
                        [1, "project-stat-content__total-info-chart"],
                        [3, "series", "chart", "dataLabels", "plotOptions", "yaxis", "legend", "fill", "stroke", "tooltip", "xaxis", "grid", "colors"],
                        [1, "project-stat-content__stat-wrapper"],
                        [1, "project-stat-content__stat-item"],
                        [1, "project-stat-content__stat-value-wrapper"],
                        [1, "project-stat-content__stat-value"],
                        [1, "project-stat-content__stat-icon"],
                        [1, "project-stat-content__stat-item-title"],
                        [1, "project-stat-content__stat-icon-warn"],
                        [1, "project-stat-content__total-info-percent"],
                        [1, "project-stat-content__total-info-percent-warn"]
                    ],
                    template: function ProjectStatChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "mat-card-title", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "h5", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "app-date-menu", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("changeDateType", function ProjectStatChartComponent_Template_app_date_menu_changeDateType_5_listener($event) {
                                return ctx.changeDateType($event, ctx.projectsType.lightBlue);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-card-content", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](11, ProjectStatChartComponent_p_11_Template, 2, 1, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](12, ProjectStatChartComponent_p_12_Template, 2, 1, "p", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "div", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](14, "apx-chart", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "div", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](19);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](20, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](21, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](23, "Registrations");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](24, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](25, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](26, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](27);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](28, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](29, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](30, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](31, "Bounce Rate");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](32, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](33, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](34, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](35);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](36, "mat-icon", 19);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](37, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](38, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](39, "Views");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](40, "mat-card", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](41, "mat-card-title", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](42, "h5", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](43);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](44, "app-date-menu", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("changeDateType", function ProjectStatChartComponent_Template_app_date_menu_changeDateType_44_listener($event) {
                                return ctx.changeDateType($event, ctx.projectsType.SingApp);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](45, "mat-card-content", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](46, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](47, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](48, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](49);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](50, ProjectStatChartComponent_p_50_Template, 2, 1, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](51, ProjectStatChartComponent_p_51_Template, 2, 1, "p", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](52, "div", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](53, "apx-chart", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](54, "div", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](55, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](56, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](57, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](58);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](59, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](60, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](61, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](62, "Registrations");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](63, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](64, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](65, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](66);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](67, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](68, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](69, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](70, "Bounce Rate");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](71, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](72, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](73, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](74);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](75, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](76, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](77, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](78, "Views");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](79, "mat-card", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](80, "mat-card-title", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](81, "h5", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](82);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](83, "app-date-menu", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("changeDateType", function ProjectStatChartComponent_Template_app_date_menu_changeDateType_83_listener($event) {
                                return ctx.changeDateType($event, ctx.projectsType.RNS);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](84, "mat-card-content", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](85, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](86, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](87, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](88);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](89, ProjectStatChartComponent_p_89_Template, 2, 1, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](90, ProjectStatChartComponent_p_90_Template, 2, 1, "p", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](91, "div", 11);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](92, "apx-chart", 12);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](93, "div", 13);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](94, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](95, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](96, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](97);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](98, "mat-icon", 19);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](99, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](100, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](101, "Registrations");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](102, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](103, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](104, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](105);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](106, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](107, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](108, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](109, "Bounce Rate");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](110, "div", 14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](111, "div", 15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](112, "h6", 16);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](113);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](114, "mat-icon", 17);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](115, "arrow_upward");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](116, "p", 18);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](117, "Views");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsLightBlueData.name);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsLightBlueData.users);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsLightBlueData.percent > 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsLightBlueData.percent < 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("series", ctx.selectedStatsLightBlueData.series)("chart", ctx.chartOptions.chart)("dataLabels", ctx.chartOptions.dataLabels)("plotOptions", ctx.chartOptions.plotOptions)("yaxis", ctx.chartOptions.yaxis)("legend", ctx.chartOptions.legend)("fill", ctx.chartOptions.fill)("stroke", ctx.chartOptions.stroke)("tooltip", ctx.chartOptions.tooltip)("xaxis", ctx.chartOptions.xaxis)("grid", ctx.chartOptions.grid)("colors", ctx.colors.BLUE);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsLightBlueData.registrations);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsLightBlueData.bounce);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsLightBlueData.views);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsSingAppData.name);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsSingAppData.users);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsSingAppData.percent > 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsSingAppData.percent < 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("series", ctx.selectedStatsSingAppData.series)("chart", ctx.chartOptions.chart)("dataLabels", ctx.chartOptions.dataLabels)("plotOptions", ctx.chartOptions.plotOptions)("yaxis", ctx.chartOptions.yaxis)("legend", ctx.chartOptions.legend)("fill", ctx.chartOptions.fill)("stroke", ctx.chartOptions.stroke)("tooltip", ctx.chartOptions.tooltip)("xaxis", ctx.chartOptions.xaxis)("grid", ctx.chartOptions.grid)("colors", ctx.colors.YELLOW);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsSingAppData.registrations);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsSingAppData.bounce);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsSingAppData.views);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsRNSData.name);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsRNSData.users);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsRNSData.percent > 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.selectedStatsRNSData.percent < 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("series", ctx.selectedStatsRNSData.series)("chart", ctx.chartOptions.chart)("dataLabels", ctx.chartOptions.dataLabels)("plotOptions", ctx.chartOptions.plotOptions)("yaxis", ctx.chartOptions.yaxis)("legend", ctx.chartOptions.legend)("fill", ctx.chartOptions.fill)("stroke", ctx.chartOptions.stroke)("tooltip", ctx.chartOptions.tooltip)("xaxis", ctx.chartOptions.xaxis)("grid", ctx.chartOptions.grid)("colors", ctx.colors.PINK);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsRNSData.registrations);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsRNSData.bounce);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.selectedStatsRNSData.views);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardTitle"], _shared_ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_3__["DateMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardContent"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgIf"], ng_apexcharts__WEBPACK_IMPORTED_MODULE_5__["ChartComponent"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__["MatIcon"]],
                    styles: [".project-stat[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-around;\n  width: calc(100% - 16px);\n  margin: 16px 8px;\n}\n.project-stat__item[_ngcontent-%COMP%] {\n  height: 208px;\n  margin: 16px;\n  width: 100%;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n@media (min-width: 576px) and (max-width: 992px) {\n  .project-stat__item[_ngcontent-%COMP%] {\n    width: 41.4%;\n  }\n}\n@media (min-width: 992px) and (max-width: 1024px) {\n  .project-stat__item[_ngcontent-%COMP%] {\n    width: 43.6%;\n  }\n}\n.project-stat__title[_ngcontent-%COMP%] {\n  padding: 8px;\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n.project-stat__title-text[_ngcontent-%COMP%] {\n  font-weight: 400;\n  font-size: 21px;\n  color: #4A4A4A;\n  margin: 0;\n}\n@media (min-width: 576px) and (max-width: 1024px) {\n  .project-stat[_ngcontent-%COMP%] {\n    justify-content: start;\n  }\n}\n@media (max-width: 1024px) {\n  .project-stat[_ngcontent-%COMP%] {\n    flex-wrap: wrap;\n  }\n}\n.project-stat-content[_ngcontent-%COMP%] {\n  padding: 8px;\n}\n.project-stat-content__total-info-wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  height: 70px;\n}\n.project-stat-content__total-info[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n  align-items: flex-end;\n}\n.project-stat-content__total-info-users[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  font-weight: 400;\n  font-size: 42px;\n  margin: 0;\n  height: 45px;\n  letter-spacing: 0.15px;\n}\n.project-stat-content__total-info-percent[_ngcontent-%COMP%] {\n  color: #3CD4A0;\n  font-weight: 400;\n  font-size: 14px;\n  margin: 0 0 0 5px;\n}\n.project-stat-content__total-info-percent-warn[_ngcontent-%COMP%] {\n  color: #ff4081;\n  font-weight: 400;\n  font-size: 14px;\n  margin: 0 0 0 5px;\n}\n.project-stat-content__total-info-chart[_ngcontent-%COMP%] {\n  position: relative;\n  right: -9px;\n  top: -2px;\n}\n.project-stat-content__stat-wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n  margin-top: 24px;\n}\n.project-stat-content__stat-value-wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n}\n.project-stat-content__stat-value[_ngcontent-%COMP%] {\n  font-weight: 400;\n  font-size: 18px;\n  color: #4A4A4A;\n  margin: 0;\n}\n.project-stat-content__stat-icon[_ngcontent-%COMP%] {\n  transform: rotate(45deg);\n  color: #3CD4A0;\n}\n.project-stat-content__stat-icon-warn[_ngcontent-%COMP%] {\n  transform: rotate(135deg);\n  color: #ff4081;\n}\n.project-stat-content__stat-item-title[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  font-weight: 400;\n  font-size: 11.2px;\n  margin: 0;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcHJvamVjdC1zdGF0LWNoYXJ0L3Byb2plY3Qtc3RhdC1jaGFydC5jb21wb25lbnQuc2NzcyIsInNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcHJvamVjdC1zdGF0LWNoYXJ0L3Byb2plY3Qtc3RhdC1jaGFydC5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUlBO0VBQ0UsYUFBQTtFQUNBLDZCQUFBO0VBQ0Esd0JBQUE7RUFDQSxnQkFBQTtBQ0hGO0FES0U7RUFDRSxhQUFBO0VBQ0EsWUFBQTtFQUNBLFdBQUE7RUFDQSxpRkFBQTtBQ0hKO0FES0k7RUFORjtJQU9JLFlBQUE7RUNGSjtBQUNGO0FESUk7RUFWRjtJQVdJLFlBQUE7RUNESjtBQUNGO0FESUU7RUFDRSxZQUFBO0VBQ0EsYUFBQTtFQUNBLDhCQUFBO0VBQ0EsbUJBQUE7QUNGSjtBREtFO0VBQ0UsZ0JFakNTO0VGa0NULGVFekJRO0VGMEJSLGNHekJRO0VIMEJSLFNBQUE7QUNISjtBRE1FO0VBbkNGO0lBb0NJLHNCQUFBO0VDSEY7QUFDRjtBREtFO0VBdkNGO0lBd0NJLGVBQUE7RUNGRjtBQUNGO0FES0E7RUFDRSxZQUFBO0FDRkY7QURJRTtFQUNFLGFBQUE7RUFDQSw4QkFBQTtFQUNBLG1CQUFBO0VBQ0EsWUFBQTtBQ0ZKO0FES0U7RUFDRSxhQUFBO0VBQ0EsOEJBQUE7RUFDQSxxQkFBQTtBQ0hKO0FETUU7RUFDRSxjR3JERztFSHNESCxnQkVsRVM7RUZtRVQsZUV0RE07RUZ1RE4sU0FBQTtFQUNBLFlBQUE7RUFDQSxzQkFBQTtBQ0pKO0FET0U7RUFDRSxjR25FSTtFSG9FSixnQkUzRVM7RUY0RVQsZUV0RU87RUZ1RVAsaUJBQUE7QUNMSjtBRFFFO0VBQ0UsY0c1RUc7RUg2RUgsZ0JFbEZTO0VGbUZULGVFN0VPO0VGOEVQLGlCQUFBO0FDTko7QURTRTtFQUNFLGtCQUFBO0VBQ0EsV0FBQTtFQUNBLFNBQUE7QUNQSjtBRFVFO0VBQ0UsYUFBQTtFQUNBLDhCQUFBO0VBQ0EsZ0JBQUE7QUNSSjtBRFdFO0VBQ0UsYUFBQTtFQUNBLG1CQUFBO0FDVEo7QURZRTtFQUNFLGdCRXpHUztFRjBHVCxlRWxHUztFRm1HVCxjR2pHUTtFSGtHUixTQUFBO0FDVko7QURhRTtFQUNFLHdCQUFBO0VBQ0EsY0cxR0k7QUYrRlI7QURjRTtFQUNFLHlCQUFBO0VBQ0EsY0dqSEc7QUZxR1A7QURlRTtFQUNFLGNHOUdHO0VIK0dILGdCRTNIUztFRjRIVCxpQkV2SEk7RUZ3SEosU0FBQTtBQ2JKIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcHJvamVjdC1zdGF0LWNoYXJ0L3Byb2plY3Qtc3RhdC1jaGFydC5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9jb2xvcnNcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXNcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9mb250XCI7XG5cbi5wcm9qZWN0LXN0YXQge1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWFyb3VuZDtcbiAgd2lkdGg6IGNhbGMoMTAwJSAtIDE2cHgpO1xuICBtYXJnaW46IDE2cHggOHB4O1xuXG4gICZfX2l0ZW0ge1xuICAgIGhlaWdodDogMjA4cHg7XG4gICAgbWFyZ2luOiAxNnB4O1xuICAgIHdpZHRoOiAxMDAlO1xuICAgIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAkc2hhZG93LXdoaXRlLCAwIDNweCAzcHggLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuXG4gICAgQG1lZGlhIChtaW4td2lkdGg6ICRzbWFsbCkgYW5kIChtYXgtd2lkdGg6ICRsYXJnZSkge1xuICAgICAgd2lkdGg6IDQxLjQlO1xuICAgIH1cblxuICAgIEBtZWRpYSAobWluLXdpZHRoOiAkbGFyZ2UpIGFuZCAobWF4LXdpZHRoOiAkbm9ybWFsKSB7XG4gICAgICB3aWR0aDogNDMuNiU7XG4gICAgfVxuICB9XG5cbiAgJl9fdGl0bGUge1xuICAgIHBhZGRpbmc6IDhweDtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICB9XG5cbiAgJl9fdGl0bGUtdGV4dCB7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGZvbnQtc2l6ZTogJGZzLW1lZGl1bTtcbiAgICBjb2xvcjogJGRhcmstZ3JleTtcbiAgICBtYXJnaW46IDA7XG4gIH1cblxuICBAbWVkaWEgKG1pbi13aWR0aDogJHNtYWxsKSBhbmQgKG1heC13aWR0aDogJG5vcm1hbCkge1xuICAgIGp1c3RpZnktY29udGVudDogc3RhcnQ7XG4gIH1cblxuICBAbWVkaWEgKG1heC13aWR0aDogJG5vcm1hbCkge1xuICAgIGZsZXgtd3JhcDogd3JhcDtcbiAgfVxufVxuXG4ucHJvamVjdC1zdGF0LWNvbnRlbnQge1xuICBwYWRkaW5nOiA4cHg7XG5cbiAgJl9fdG90YWwtaW5mby13cmFwcGVyIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIGhlaWdodDogNzBweDtcbiAgfVxuXG4gICZfX3RvdGFsLWluZm8ge1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIGFsaWduLWl0ZW1zOiBmbGV4LWVuZDtcbiAgfVxuXG4gICZfX3RvdGFsLWluZm8tdXNlcnMge1xuICAgIGNvbG9yOiAkZ3JleTtcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgZm9udC1zaXplOiAkZnMteHh4bDtcbiAgICBtYXJnaW46IDA7XG4gICAgaGVpZ2h0OiA0NXB4O1xuICAgIGxldHRlci1zcGFjaW5nOiAwLjE1cHg7XG4gIH1cblxuICAmX190b3RhbC1pbmZvLXBlcmNlbnQge1xuICAgIGNvbG9yOiAkZ3JlZW47XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGZvbnQtc2l6ZTogJGZzLXNtYWxsO1xuICAgIG1hcmdpbjogMCAwIDAgNXB4O1xuICB9XG5cbiAgJl9fdG90YWwtaW5mby1wZXJjZW50LXdhcm4ge1xuICAgIGNvbG9yOiAkcGluaztcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgbWFyZ2luOiAwIDAgMCA1cHg7XG4gIH1cblxuICAmX190b3RhbC1pbmZvLWNoYXJ0IHtcbiAgICBwb3NpdGlvbjogcmVsYXRpdmU7XG4gICAgcmlnaHQ6IC05cHg7XG4gICAgdG9wOiAtMnB4O1xuICB9XG5cbiAgJl9fc3RhdC13cmFwcGVyIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgICBtYXJnaW4tdG9wOiAyNHB4O1xuICB9XG5cbiAgJl9fc3RhdC12YWx1ZS13cmFwcGVyIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIH1cblxuICAmX19zdGF0LXZhbHVlIHtcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgZm9udC1zaXplOiAkZnMtcmVndWxhcjtcbiAgICBjb2xvcjogJGRhcmstZ3JleTtcbiAgICBtYXJnaW46IDA7XG4gIH1cblxuICAmX19zdGF0LWljb24ge1xuICAgIHRyYW5zZm9ybTogcm90YXRlKDQ1ZGVnKTtcbiAgICBjb2xvcjogJGdyZWVuO1xuICB9XG5cbiAgJl9fc3RhdC1pY29uLXdhcm4ge1xuICAgIHRyYW5zZm9ybTogcm90YXRlKDEzNWRlZyk7XG4gICAgY29sb3I6ICRwaW5rO1xuICB9XG5cbiAgJl9fc3RhdC1pdGVtLXRpdGxlIHtcbiAgICBjb2xvcjogJGdyZXk7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGZvbnQtc2l6ZTogJGZzLXhzO1xuICAgIG1hcmdpbjogMDtcbiAgfVxufVxuIiwiLnByb2plY3Qtc3RhdCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYXJvdW5kO1xuICB3aWR0aDogY2FsYygxMDAlIC0gMTZweCk7XG4gIG1hcmdpbjogMTZweCA4cHg7XG59XG4ucHJvamVjdC1zdGF0X19pdGVtIHtcbiAgaGVpZ2h0OiAyMDhweDtcbiAgbWFyZ2luOiAxNnB4O1xuICB3aWR0aDogMTAwJTtcbiAgYm94LXNoYWRvdzogMCAzcHggMTFweCAwICNFOEVBRkMsIDAgM3B4IDNweCAtMnB4ICNCMkIyQjIxQSwgMCAxcHggOHB4IDAgIzlBOUE5QTFBO1xufVxuQG1lZGlhIChtaW4td2lkdGg6IDU3NnB4KSBhbmQgKG1heC13aWR0aDogOTkycHgpIHtcbiAgLnByb2plY3Qtc3RhdF9faXRlbSB7XG4gICAgd2lkdGg6IDQxLjQlO1xuICB9XG59XG5AbWVkaWEgKG1pbi13aWR0aDogOTkycHgpIGFuZCAobWF4LXdpZHRoOiAxMDI0cHgpIHtcbiAgLnByb2plY3Qtc3RhdF9faXRlbSB7XG4gICAgd2lkdGg6IDQzLjYlO1xuICB9XG59XG4ucHJvamVjdC1zdGF0X190aXRsZSB7XG4gIHBhZGRpbmc6IDhweDtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xufVxuLnByb2plY3Qtc3RhdF9fdGl0bGUtdGV4dCB7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMjFweDtcbiAgY29sb3I6ICM0QTRBNEE7XG4gIG1hcmdpbjogMDtcbn1cbkBtZWRpYSAobWluLXdpZHRoOiA1NzZweCkgYW5kIChtYXgtd2lkdGg6IDEwMjRweCkge1xuICAucHJvamVjdC1zdGF0IHtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IHN0YXJ0O1xuICB9XG59XG5AbWVkaWEgKG1heC13aWR0aDogMTAyNHB4KSB7XG4gIC5wcm9qZWN0LXN0YXQge1xuICAgIGZsZXgtd3JhcDogd3JhcDtcbiAgfVxufVxuXG4ucHJvamVjdC1zdGF0LWNvbnRlbnQge1xuICBwYWRkaW5nOiA4cHg7XG59XG4ucHJvamVjdC1zdGF0LWNvbnRlbnRfX3RvdGFsLWluZm8td3JhcHBlciB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgaGVpZ2h0OiA3MHB4O1xufVxuLnByb2plY3Qtc3RhdC1jb250ZW50X190b3RhbC1pbmZvIHtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICBhbGlnbi1pdGVtczogZmxleC1lbmQ7XG59XG4ucHJvamVjdC1zdGF0LWNvbnRlbnRfX3RvdGFsLWluZm8tdXNlcnMge1xuICBjb2xvcjogIzZFNkU2RTtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgZm9udC1zaXplOiA0MnB4O1xuICBtYXJnaW46IDA7XG4gIGhlaWdodDogNDVweDtcbiAgbGV0dGVyLXNwYWNpbmc6IDAuMTVweDtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fdG90YWwtaW5mby1wZXJjZW50IHtcbiAgY29sb3I6ICMzQ0Q0QTA7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMTRweDtcbiAgbWFyZ2luOiAwIDAgMCA1cHg7XG59XG4ucHJvamVjdC1zdGF0LWNvbnRlbnRfX3RvdGFsLWluZm8tcGVyY2VudC13YXJuIHtcbiAgY29sb3I6ICNmZjQwODE7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMTRweDtcbiAgbWFyZ2luOiAwIDAgMCA1cHg7XG59XG4ucHJvamVjdC1zdGF0LWNvbnRlbnRfX3RvdGFsLWluZm8tY2hhcnQge1xuICBwb3NpdGlvbjogcmVsYXRpdmU7XG4gIHJpZ2h0OiAtOXB4O1xuICB0b3A6IC0ycHg7XG59XG4ucHJvamVjdC1zdGF0LWNvbnRlbnRfX3N0YXQtd3JhcHBlciB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgbWFyZ2luLXRvcDogMjRweDtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fc3RhdC12YWx1ZS13cmFwcGVyIHtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fc3RhdC12YWx1ZSB7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMThweDtcbiAgY29sb3I6ICM0QTRBNEE7XG4gIG1hcmdpbjogMDtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fc3RhdC1pY29uIHtcbiAgdHJhbnNmb3JtOiByb3RhdGUoNDVkZWcpO1xuICBjb2xvcjogIzNDRDRBMDtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fc3RhdC1pY29uLXdhcm4ge1xuICB0cmFuc2Zvcm06IHJvdGF0ZSgxMzVkZWcpO1xuICBjb2xvcjogI2ZmNDA4MTtcbn1cbi5wcm9qZWN0LXN0YXQtY29udGVudF9fc3RhdC1pdGVtLXRpdGxlIHtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMTEuMnB4O1xuICBtYXJnaW46IDA7XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](ProjectStatChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-project-stat-chart',
                            templateUrl: './project-stat-chart.component.html',
                            styleUrls: ['./project-stat-chart.component.scss']
                        }]
                    }], null, {
                        projectsStatsData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/revenue-chart/revenue-chart.component.ts":
            /*!*************************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/revenue-chart/revenue-chart.component.ts ***!
              \*************************************************************************************/
            /*! exports provided: RevenueChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "RevenueChartComponent", function() {
                    return RevenueChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var ngx_echarts__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ngx-echarts */ "./node_modules/ngx-echarts/__ivy_ngcc__/fesm2015/ngx-echarts.js");






                class RevenueChartComponent {
                    constructor() {
                        this.colors = _consts__WEBPACK_IMPORTED_MODULE_1__["colors"];
                    }
                    ngOnInit() {
                        this.initChart();
                    }
                    initChart() {
                        this.revenueChart = {
                            color: [_consts__WEBPACK_IMPORTED_MODULE_1__["colors"].GREEN, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].PINK, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].YELLOW, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].BLUE],
                            tooltip: {
                                trigger: 'item'
                            },
                            legend: {
                                top: 'center',
                                right: 'right',
                                data: ['Group A', 'Group B', 'Group C', 'Group D'],
                                textStyle: {
                                    color: '#6E6E6E'
                                }
                            },
                            series: [{
                                type: 'pie',
                                radius: ['50%', '70%'],
                                center: ['24%', '50%'],
                                label: {
                                    show: false
                                },
                                labelLine: {
                                    normal: {
                                        show: false
                                    }
                                },
                                hoverAnimation: false,
                                avoidLabelOverlap: false,
                                data: [{
                                    name: 'Group A',
                                    value: this.revenueCharData.groupA
                                }, {
                                    name: 'Group B',
                                    value: this.revenueCharData.groupB
                                }, {
                                    name: 'Group C',
                                    value: this.revenueCharData.groupC
                                }, {
                                    name: 'Group D',
                                    value: this.revenueCharData.groupD
                                }, ]
                            }]
                        };
                    }
                }
                RevenueChartComponent.ɵfac = function RevenueChartComponent_Factory(t) {
                    return new(t || RevenueChartComponent)();
                };
                RevenueChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: RevenueChartComponent,
                    selectors: [
                        ["app-revenue-chart"]
                    ],
                    inputs: {
                        revenueCharData: "revenueCharData"
                    },
                    decls: 7,
                    vars: 1,
                    consts: [
                        [1, "revenue-chart"],
                        [1, "revenue-chart__header"],
                        [1, "revenue-chart__header-title"],
                        [1, "revenue-chart__content"],
                        ["echarts", "", 1, "revenue-chart__content-chart", 3, "options"]
                    ],
                    template: function RevenueChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Revenue Breakdown");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](6, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("options", ctx.revenueChart);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardContent"], ngx_echarts__WEBPACK_IMPORTED_MODULE_4__["ɵa"]],
                    styles: [".revenue-chart[_ngcontent-%COMP%] {\n  height: 192px;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n.revenue-chart__header[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n}\n.revenue-chart__header-title[_ngcontent-%COMP%] {\n  font-size: 20px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.revenue-chart__content[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}\n.revenue-chart__content-chart[_ngcontent-%COMP%] {\n  height: 140px;\n  width: 100%;\n  max-width: 218px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcmV2ZW51ZS1jaGFydC9yZXZlbnVlLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy9yZXZlbnVlLWNoYXJ0L3JldmVudWUtY2hhcnQuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9jb2xvcnMuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFJQTtFQUNFLGFBQUE7RUFDQSxpRkFBQTtBQ0hGO0FES0U7RUFDRSxjRUdHO0VGRkgsYUFBQTtFQUNBLDhCQUFBO0FDSEo7QURLSTtFQUNFLGVBQUE7RUFDQSxnQkdmTztFSGdCUCxTQUFBO0VBQ0EsaUJBQUE7QUNITjtBRE9FO0VBQ0UsYUFBQTtFQUNBLG1CQUFBO0VBQ0EsdUJBQUE7QUNMSjtBRE9JO0VBQ0UsYUFBQTtFQUNBLFdBQUE7RUFDQSxnQkFBQTtBQ0xOIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvcmV2ZW51ZS1jaGFydC9yZXZlbnVlLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2NvbG9yc1wiO1xuQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2ZvbnRcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXNcIjtcblxuLnJldmVudWUtY2hhcnQge1xuICBoZWlnaHQ6IDE5MnB4O1xuICBib3gtc2hhZG93OiAwIDNweCAxMXB4IDAgJHNoYWRvdy13aGl0ZSwgMCAzcHggM3B4IC0ycHggJHNoYWRvdy1ncmV5LCAwIDFweCA4cHggMCAkc2hhZG93LWRhcmstZ3JleTtcblxuICAmX19oZWFkZXIge1xuICAgIGNvbG9yOiAkZ3JleTtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcblxuICAgICYtdGl0bGUge1xuICAgICAgZm9udC1zaXplOiAyMHB4O1xuICAgICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgICAgbWFyZ2luOiAwO1xuICAgICAgbGluZS1oZWlnaHQ6IDQwcHg7XG4gICAgfVxuICB9XG5cbiAgJl9fY29udGVudCB7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIGp1c3RpZnktY29udGVudDogY2VudGVyO1xuXG4gICAgJi1jaGFydCB7XG4gICAgICBoZWlnaHQ6IDE0MHB4O1xuICAgICAgd2lkdGg6IDEwMCU7XG4gICAgICBtYXgtd2lkdGg6IDIxOHB4XG4gICAgfVxuICB9XG59XG4iLCIucmV2ZW51ZS1jaGFydCB7XG4gIGhlaWdodDogMTkycHg7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAjRThFQUZDLCAwIDNweCAzcHggLTJweCAjQjJCMkIyMUEsIDAgMXB4IDhweCAwICM5QTlBOUExQTtcbn1cbi5yZXZlbnVlLWNoYXJ0X19oZWFkZXIge1xuICBjb2xvcjogIzZFNkU2RTtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xufVxuLnJldmVudWUtY2hhcnRfX2hlYWRlci10aXRsZSB7XG4gIGZvbnQtc2l6ZTogMjBweDtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgbWFyZ2luOiAwO1xuICBsaW5lLWhlaWdodDogNDBweDtcbn1cbi5yZXZlbnVlLWNoYXJ0X19jb250ZW50IHtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG59XG4ucmV2ZW51ZS1jaGFydF9fY29udGVudC1jaGFydCB7XG4gIGhlaWdodDogMTQwcHg7XG4gIHdpZHRoOiAxMDAlO1xuICBtYXgtd2lkdGg6IDIxOHB4O1xufSIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIiRmdy1saWdodGVyOiA0MDA7XG4kZnctbm9ybWFsOiA1MDA7XG4kZnctYm9sZDogNjAwO1xuXG5cbiRmcy14czogMTEuMnB4O1xuJGZzLXNtYWxsOiAxNHB4O1xuJGZzLW5vcm1hbDogMTZweDtcbiRmcy1yZWd1bGFyOiAxOHB4O1xuJGZzLW1lZGl1bTogMjFweDtcbiRmcy1sYXJnZTogMjRweDtcbiRmcy14bDogMjhweDtcbiRmcy14eGw6IDM4cHg7XG4kZnMteHh4bDogNDJweDtcbiJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](RevenueChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-revenue-chart',
                            templateUrl: './revenue-chart.component.html',
                            styleUrls: ['./revenue-chart.component.scss']
                        }]
                    }], null, {
                        revenueCharData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/server-chart/server-chart.component.ts":
            /*!***********************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/server-chart/server-chart.component.ts ***!
              \***********************************************************************************/
            /*! exports provided: ServerChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "ServerChartComponent", function() {
                    return ServerChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var ng_apexcharts__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! ng-apexcharts */ "./node_modules/ng-apexcharts/__ivy_ngcc__/fesm2015/ng-apexcharts.js");







                function ServerChartComponent_div_6_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 5);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "p", 6);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](3, "apx-chart", 7);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const chart_r1 = ctx.$implicit;
                        const i_r2 = ctx.index;
                        const ctx_r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx_r0.serverDataTitles[i_r2]);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("series", chart_r1.series)("chart", chart_r1.chart)("xaxis", chart_r1.xaxis)("stroke", chart_r1.stroke)("dataLabels", chart_r1.dataLabels)("yaxis", chart_r1.yaxis)("labels", chart_r1.labels)("legend", chart_r1.legend)("grid", chart_r1.grid)("tooltip", chart_r1.tooltip)("colors", chart_r1.colors)("fill", chart_r1.fill);
                    }
                }
                class ServerChartComponent {
                    constructor() {
                        this.colors = _consts__WEBPACK_IMPORTED_MODULE_1__["colors"];
                    }
                    ngOnInit() {
                        this.charts = [
                            this.initChart(this.serverChartData.firstServerChartData, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].PINK),
                            this.initChart(this.serverChartData.secondServerChartData, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].BLUE),
                            this.initChart(this.serverChartData.thirdServerChartData, _consts__WEBPACK_IMPORTED_MODULE_1__["colors"].YELLOW)
                        ];
                        this.serverDataTitles = [
                            this.serverChartData.firstDataTitle,
                            this.serverChartData.secondDataTitle,
                            this.serverChartData.thirdDataTitle,
                        ];
                    }
                    initChart(data, color) {
                        return {
                            chart: {
                                type: 'area',
                                height: 80,
                                zoom: {
                                    enabled: false
                                },
                                toolbar: {
                                    show: false
                                }
                            },
                            series: [{
                                name: 'STOCK ABC',
                                data: data
                            }],
                            colors: [color],
                            fill: {
                                type: 'solid',
                                opacity: 0.3
                            },
                            dataLabels: {
                                enabled: false
                            },
                            stroke: {
                                curve: 'smooth',
                                width: 2
                            },
                            labels: this.serverChartData.dates,
                            xaxis: {
                                type: 'datetime',
                                labels: {
                                    show: false
                                },
                                axisBorder: {
                                    show: false
                                },
                                axisTicks: {
                                    show: false
                                }
                            },
                            yaxis: {
                                max: 50000,
                                show: false
                            },
                            legend: {
                                show: false
                            },
                            grid: {
                                show: false,
                                padding: {
                                    bottom: 0,
                                    left: 0,
                                    right: 0,
                                    top: 0
                                }
                            },
                            tooltip: {
                                enabled: false
                            }
                        };
                    }
                }
                ServerChartComponent.ɵfac = function ServerChartComponent_Factory(t) {
                    return new(t || ServerChartComponent)();
                };
                ServerChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: ServerChartComponent,
                    selectors: [
                        ["app-server-chart"]
                    ],
                    inputs: {
                        serverChartData: "serverChartData"
                    },
                    decls: 7,
                    vars: 1,
                    consts: [
                        [1, "server-chart"],
                        [1, "server-chart__header"],
                        [1, "server-chart__header-title"],
                        [1, "server-chart__content"],
                        ["class", "server-chart__content-item", 4, "ngFor", "ngForOf"],
                        [1, "server-chart__content-item"],
                        [1, "server-chart__content-item-text"],
                        [3, "series", "chart", "xaxis", "stroke", "dataLabels", "yaxis", "labels", "legend", "grid", "tooltip", "colors", "fill"]
                    ],
                    template: function ServerChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Server Overview");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](6, ServerChartComponent_div_6_Template, 4, 13, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.charts);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardContent"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgForOf"], ng_apexcharts__WEBPACK_IMPORTED_MODULE_5__["ChartComponent"]],
                    styles: [".server-chart[_ngcontent-%COMP%] {\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n  display: flex;\n  flex-direction: column;\n  height: 192px;\n}\n.server-chart__header[_ngcontent-%COMP%] {\n  align-items: center;\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n}\n.server-chart__header-title[_ngcontent-%COMP%] {\n  font-size: 21px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.server-chart__content[_ngcontent-%COMP%] {\n  display: flex;\n  flex-direction: column;\n  height: 100%;\n  justify-content: space-between;\n}\n.server-chart__content-item[_ngcontent-%COMP%] {\n  align-items: center;\n  display: flex;\n  height: 50px;\n  justify-content: space-between;\n}\n.server-chart__content-item-text[_ngcontent-%COMP%] {\n  width: 100%;\n  color: #6E6E6E;\n  font-weight: 400;\n  font-size: 14px;\n  padding-right: 16px;\n  margin: 0;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvc2VydmVyLWNoYXJ0L3NlcnZlci1jaGFydC5jb21wb25lbnQuc2NzcyIsInNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvc2VydmVyLWNoYXJ0L3NlcnZlci1jaGFydC5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvZm9udC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UsaUZBQUE7RUFDQSxhQUFBO0VBQ0Esc0JBQUE7RUFDQSxhQUFBO0FDRkY7QURJRTtFQUNFLG1CQUFBO0VBQ0EsY0VDRztFRkFILGFBQUE7RUFDQSw4QkFBQTtBQ0ZKO0FESUk7RUFDRSxlR1BNO0VIUU4sZ0JHakJPO0VIa0JQLFNBQUE7RUFDQSxpQkFBQTtBQ0ZOO0FETUU7RUFDRSxhQUFBO0VBQ0Esc0JBQUE7RUFDQSxZQUFBO0VBQ0EsOEJBQUE7QUNKSjtBRE1JO0VBQ0UsbUJBQUE7RUFDQSxhQUFBO0VBQ0EsWUFBQTtFQUNBLDhCQUFBO0FDSk47QURNTTtFQUNFLFdBQUE7RUFDQSxjRXpCRDtFRjBCQyxnQkd0Q0s7RUh1Q0wsZUdqQ0c7RUhrQ0gsbUJBQUE7RUFDQSxTQUFBO0FDSlIiLCJmaWxlIjoic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy9zZXJ2ZXItY2hhcnQvc2VydmVyLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvY29sb3JzJztcbkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2ZvbnQnO1xuXG4uc2VydmVyLWNoYXJ0IHtcbiAgYm94LXNoYWRvdzogMCAzcHggMTFweCAwICRzaGFkb3ctd2hpdGUsIDAgM3B4IDNweCAtMnB4ICRzaGFkb3ctZ3JleSwgMCAxcHggOHB4IDAgJHNoYWRvdy1kYXJrLWdyZXk7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGhlaWdodDogMTkycHg7XG5cbiAgJl9faGVhZGVyIHtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIGNvbG9yOiAkZ3JleTtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcblxuICAgICYtdGl0bGUge1xuICAgICAgZm9udC1zaXplOiAkZnMtbWVkaXVtO1xuICAgICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgICAgbWFyZ2luOiAwO1xuICAgICAgbGluZS1oZWlnaHQ6IDQwcHg7XG4gICAgfVxuICB9XG5cbiAgJl9fY29udGVudCB7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICAgIGhlaWdodDogMTAwJTtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgICAmLWl0ZW0ge1xuICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgICBoZWlnaHQ6IDUwcHg7XG4gICAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgICAgICYtdGV4dCB7XG4gICAgICAgIHdpZHRoOiAxMDAlO1xuICAgICAgICBjb2xvcjogJGdyZXk7XG4gICAgICAgIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcbiAgICAgICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgICAgIHBhZGRpbmctcmlnaHQ6IDE2cHg7XG4gICAgICAgIG1hcmdpbjogMDtcbiAgICAgIH1cbiAgICB9XG4gIH1cbn1cblxuXG5cbiIsIi5zZXJ2ZXItY2hhcnQge1xuICBib3gtc2hhZG93OiAwIDNweCAxMXB4IDAgI0U4RUFGQywgMCAzcHggM3B4IC0ycHggI0IyQjJCMjFBLCAwIDFweCA4cHggMCAjOUE5QTlBMUE7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGhlaWdodDogMTkycHg7XG59XG4uc2VydmVyLWNoYXJ0X19oZWFkZXIge1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICBjb2xvcjogIzZFNkU2RTtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xufVxuLnNlcnZlci1jaGFydF9faGVhZGVyLXRpdGxlIHtcbiAgZm9udC1zaXplOiAyMXB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBtYXJnaW46IDA7XG4gIGxpbmUtaGVpZ2h0OiA0MHB4O1xufVxuLnNlcnZlci1jaGFydF9fY29udGVudCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGhlaWdodDogMTAwJTtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xufVxuLnNlcnZlci1jaGFydF9fY29udGVudC1pdGVtIHtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgZGlzcGxheTogZmxleDtcbiAgaGVpZ2h0OiA1MHB4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG59XG4uc2VydmVyLWNoYXJ0X19jb250ZW50LWl0ZW0tdGV4dCB7XG4gIHdpZHRoOiAxMDAlO1xuICBjb2xvcjogIzZFNkU2RTtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgZm9udC1zaXplOiAxNHB4O1xuICBwYWRkaW5nLXJpZ2h0OiAxNnB4O1xuICBtYXJnaW46IDA7XG59IiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](ServerChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-server-chart',
                            templateUrl: './server-chart.component.html',
                            styleUrls: ['./server-chart.component.scss']
                        }]
                    }], null, {
                        serverChartData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/support-requests/support-requests.component.ts":
            /*!*******************************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/support-requests/support-requests.component.ts ***!
              \*******************************************************************************************/
            /*! exports provided: SupportRequestsComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SupportRequestsComponent", function() {
                    return SupportRequestsComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var _angular_material_table__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/table */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/table.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");






                function SupportRequestsComponent_ng_container_7_th_1_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "th", 11);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](column_r3);
                    }
                }

                function SupportRequestsComponent_ng_container_7_td_2_span_1_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "span");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r7 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](element_r7[column_r3]);
                    }
                }

                function SupportRequestsComponent_ng_container_7_td_2_div_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 15);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "span");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const element_r7 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", element_r7[column_r3]);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](element_r7[column_r3]);
                    }
                }

                function SupportRequestsComponent_ng_container_7_td_2_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "td", 12);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, SupportRequestsComponent_ng_container_7_td_2_span_1_Template, 2, 1, "span", 13);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, SupportRequestsComponent_ng_container_7_td_2_div_2_Template, 3, 2, "div", 14);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", column_r3 !== "status");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", column_r3 === "status");
                    }
                }

                function SupportRequestsComponent_ng_container_7_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0, 8);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, SupportRequestsComponent_ng_container_7_th_1_Template, 2, 1, "th", 9);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, SupportRequestsComponent_ng_container_7_td_2_Template, 3, 2, "td", 10);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
                    }
                    if (rf & 2) {
                        const column_r3 = ctx.$implicit;
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("matColumnDef", column_r3);
                    }
                }

                function SupportRequestsComponent_tr_8_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 16);
                    }
                }

                function SupportRequestsComponent_tr_9_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "tr", 17);
                    }
                }
                class SupportRequestsComponent {
                    constructor() {
                        this.displayedColumns = ['name', 'email', 'product', 'price', 'date', 'city', 'status'];
                    }
                }
                SupportRequestsComponent.ɵfac = function SupportRequestsComponent_Factory(t) {
                    return new(t || SupportRequestsComponent)();
                };
                SupportRequestsComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: SupportRequestsComponent,
                    selectors: [
                        ["app-support-requests"]
                    ],
                    inputs: {
                        supportRequestData: "supportRequestData"
                    },
                    decls: 10,
                    vars: 4,
                    consts: [
                        [1, "support-requests"],
                        [1, "support-requests__header"],
                        [1, "support-requests__title"],
                        [1, "support-requests__content"],
                        ["mat-table", "", 1, "support-requests__table", 3, "dataSource"],
                        ["class", "support-requests__table-row", 3, "matColumnDef", 4, "ngFor", "ngForOf"],
                        ["mat-header-row", "", 4, "matHeaderRowDef"],
                        ["mat-row", "", 4, "matRowDef", "matRowDefColumns"],
                        [1, "support-requests__table-row", 3, "matColumnDef"],
                        ["mat-header-cell", "", "class", "support-requests__table-row-title", 4, "matHeaderCellDef"],
                        ["mat-cell", "", "class", "support-requests__table-content", 4, "matCellDef"],
                        ["mat-header-cell", "", 1, "support-requests__table-row-title"],
                        ["mat-cell", "", 1, "support-requests__table-content"],
                        [4, "ngIf"],
                        ["class", "support-requests__content-badge", 3, "ngClass", 4, "ngIf"],
                        [1, "support-requests__content-badge", 3, "ngClass"],
                        ["mat-header-row", ""],
                        ["mat-row", ""]
                    ],
                    template: function SupportRequestsComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Support Requests");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "table", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](7, SupportRequestsComponent_ng_container_7_Template, 3, 1, "ng-container", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](8, SupportRequestsComponent_tr_8_Template, 1, 0, "tr", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](9, SupportRequestsComponent_tr_9_Template, 1, 0, "tr", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("dataSource", ctx.supportRequestData);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matHeaderRowDef", ctx.displayedColumns);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matRowDefColumns", ctx.displayedColumns);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_2__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_1__["MatCardContent"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatTable"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgForOf"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatRowDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatColumnDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatCellDef"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderCell"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatCell"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgIf"], _angular_common__WEBPACK_IMPORTED_MODULE_4__["NgClass"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatHeaderRow"], _angular_material_table__WEBPACK_IMPORTED_MODULE_3__["MatRow"]],
                    styles: [".support-requests[_ngcontent-%COMP%] {\n  margin: 0 24px;\n  padding: 0;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n}\n.support-requests__header[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n  padding: 24px 24px 8px;\n  margin-bottom: 0;\n}\n.support-requests__title[_ngcontent-%COMP%] {\n  font-size: 21px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.support-requests__content[_ngcontent-%COMP%] {\n  height: 427px;\n  overflow-y: hidden;\n  overflow-x: scroll;\n}\n@media (max-width: 576px) {\n  .support-requests__content[_ngcontent-%COMP%] {\n    height: auto;\n  }\n}\n.support-requests__table[_ngcontent-%COMP%] {\n  width: 100%;\n}\n.support-requests__table-row[_ngcontent-%COMP%] {\n  height: 64px;\n}\n.support-requests__table-row-title[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n  font-size: 14px;\n  font-weight: 400;\n  line-height: 24px;\n  text-transform: uppercase;\n  padding: 18.4px;\n}\n.support-requests__table-content[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n  font-size: 14px;\n  padding: 20px;\n}\n.support-requests__content-badge[_ngcontent-%COMP%] {\n  width: -webkit-fit-content;\n  width: -moz-fit-content;\n  width: fit-content;\n  border-radius: 32px;\n  color: white;\n  text-align: center;\n  padding: 5px 10px;\n  font-size: 13px;\n  box-sizing: border-box;\n  font-family: \"Roboto\", \"Helvetica\", \"Arial\", sans-serif;\n  font-weight: 400;\n  line-height: 1.75;\n  letter-spacing: 0.45px;\n}\n.support-requests__content-badge[_ngcontent-%COMP%]::first-letter {\n  text-transform: uppercase;\n}\nmat-menu[_ngcontent-%COMP%] {\n  position: absolute;\n}\n.send[_ngcontent-%COMP%] {\n  background-color: #3CD4A0;\n}\n.pending[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n}\n.declined[_ngcontent-%COMP%] {\n  background-color: #ff4081;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvc3VwcG9ydC1yZXF1ZXN0cy9zdXBwb3J0LXJlcXVlc3RzLmNvbXBvbmVudC5zY3NzIiwic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy9zdXBwb3J0LXJlcXVlc3RzL3N1cHBvcnQtcmVxdWVzdHMuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9jb2xvcnMuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFJQTtFQUNFLGNBQUE7RUFDQSxVQUFBO0VBQ0EsaUZBQUE7QUNIRjtBREtFO0VBQ0UsY0VFRztFRkRILGFBQUE7RUFDQSw4QkFBQTtFQUNBLHNCQUFBO0VBQ0EsZ0JBQUE7QUNISjtBRE1FO0VBQ0UsZUdUUTtFSFVSLGdCR25CUztFSG9CVCxTQUFBO0VBQ0EsaUJBQUE7QUNKSjtBRE9FO0VBQ0UsYUFBQTtFQUNBLGtCQUFBO0VBQ0Esa0JBQUE7QUNMSjtBRE9JO0VBTEY7SUFNSSxZQUFBO0VDSko7QUFDRjtBRE9FO0VBQ0UsV0FBQTtBQ0xKO0FEUUU7RUFDRSxZQUFBO0FDTko7QURTRTtFQUNFLGNFakNRO0VGa0NSLGVHdENPO0VIdUNQLGdCRzdDUztFSDhDVCxpQkFBQTtFQUNBLHlCQUFBO0VBQ0EsZUFBQTtBQ1BKO0FEVUU7RUFDRSxjRTFDUTtFRjJDUixlRy9DTztFSGdEUCxhQUFBO0FDUko7QURXRTtFQUNFLDBCQUFBO0VBQUEsdUJBQUE7RUFBQSxrQkFBQTtFQUNBLG1CQUFBO0VBQ0EsWUVuREk7RUZvREosa0JBQUE7RUFDQSxpQkFBQTtFQUNBLGVBQUE7RUFDQSxzQkFBQTtFQUNBLHVEQUFBO0VBQ0EsZ0JHbEVTO0VIbUVULGlCQUFBO0VBQ0Esc0JBQUE7QUNUSjtBRFdJO0VBQ0UseUJBQUE7QUNUTjtBRGNBO0VBQ0Usa0JBQUE7QUNYRjtBRGNBO0VBQ0UseUJFMUVNO0FEK0RSO0FEY0E7RUFDRSx5QkVyRk87QUQwRVQ7QURjQTtFQUNFLHlCRXBGSztBRHlFUCIsImZpbGUiOiJzcmMvYXBwL3BhZ2VzL2Rhc2hib2FyZC9jb21wb25lbnRzL3N1cHBvcnQtcmVxdWVzdHMvc3VwcG9ydC1yZXF1ZXN0cy5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2NvbG9ycyc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9mb250JztcbkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlcyc7XG5cbi5zdXBwb3J0LXJlcXVlc3RzIHtcbiAgbWFyZ2luOiAwIDI0cHg7XG4gIHBhZGRpbmc6IDA7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAkc2hhZG93LXdoaXRlLCAwIDNweCAzcHggLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuXG4gICZfX2hlYWRlciB7XG4gICAgY29sb3I6ICRncmV5O1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIHBhZGRpbmc6IDI0cHggMjRweCA4cHg7XG4gICAgbWFyZ2luLWJvdHRvbTogMDtcbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBmb250LXNpemU6ICRmcy1tZWRpdW07XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIG1hcmdpbjogMDtcbiAgICBsaW5lLWhlaWdodDogNDBweDtcbiAgfVxuXG4gICZfX2NvbnRlbnQge1xuICAgIGhlaWdodDogNDI3cHg7XG4gICAgb3ZlcmZsb3cteTogaGlkZGVuO1xuICAgIG92ZXJmbG93LXg6IHNjcm9sbDtcblxuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgIGhlaWdodDogYXV0bztcbiAgICB9XG4gIH1cblxuICAmX190YWJsZSB7XG4gICAgd2lkdGg6IDEwMCU7XG4gIH1cblxuICAmX190YWJsZS1yb3cge1xuICAgIGhlaWdodDogNjRweDtcbiAgfVxuXG4gICZfX3RhYmxlLXJvdy10aXRsZSB7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGxpbmUtaGVpZ2h0OiAyNHB4O1xuICAgIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG4gICAgcGFkZGluZzogMTguNHB4O1xuICB9XG5cbiAgJl9fdGFibGUtY29udGVudCB7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgcGFkZGluZzogMjBweDtcbiAgfVxuXG4gICZfX2NvbnRlbnQtYmFkZ2Uge1xuICAgIHdpZHRoOiBmaXQtY29udGVudDtcbiAgICBib3JkZXItcmFkaXVzOiAzMnB4O1xuICAgIGNvbG9yOiAkd2hpdGU7XG4gICAgdGV4dC1hbGlnbjogY2VudGVyO1xuICAgIHBhZGRpbmc6IDVweCAxMHB4O1xuICAgIGZvbnQtc2l6ZTogMTNweDtcbiAgICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICAgIGZvbnQtZmFtaWx5OiBcIlJvYm90b1wiLCBcIkhlbHZldGljYVwiLCBcIkFyaWFsXCIsIHNhbnMtc2VyaWY7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGxpbmUtaGVpZ2h0OiAxLjc1O1xuICAgIGxldHRlci1zcGFjaW5nOiAwLjQ1cHg7XG5cbiAgICAmOjpmaXJzdC1sZXR0ZXIge1xuICAgICAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTtcbiAgICB9XG4gIH1cbn1cblxubWF0LW1lbnUge1xuICBwb3NpdGlvbjogYWJzb2x1dGU7XG59XG5cbi5zZW5kIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGdyZWVuO1xufVxuXG4ucGVuZGluZyB7XG4gIGJhY2tncm91bmQtY29sb3I6ICR5ZWxsb3c7XG59XG5cbi5kZWNsaW5lZCB7XG4gIGJhY2tncm91bmQtY29sb3I6ICRwaW5rO1xufVxuIiwiLnN1cHBvcnQtcmVxdWVzdHMge1xuICBtYXJnaW46IDAgMjRweDtcbiAgcGFkZGluZzogMDtcbiAgYm94LXNoYWRvdzogMCAzcHggMTFweCAwICNFOEVBRkMsIDAgM3B4IDNweCAtMnB4ICNCMkIyQjIxQSwgMCAxcHggOHB4IDAgIzlBOUE5QTFBO1xufVxuLnN1cHBvcnQtcmVxdWVzdHNfX2hlYWRlciB7XG4gIGNvbG9yOiAjNkU2RTZFO1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gIHBhZGRpbmc6IDI0cHggMjRweCA4cHg7XG4gIG1hcmdpbi1ib3R0b206IDA7XG59XG4uc3VwcG9ydC1yZXF1ZXN0c19fdGl0bGUge1xuICBmb250LXNpemU6IDIxcHg7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIG1hcmdpbjogMDtcbiAgbGluZS1oZWlnaHQ6IDQwcHg7XG59XG4uc3VwcG9ydC1yZXF1ZXN0c19fY29udGVudCB7XG4gIGhlaWdodDogNDI3cHg7XG4gIG92ZXJmbG93LXk6IGhpZGRlbjtcbiAgb3ZlcmZsb3cteDogc2Nyb2xsO1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5zdXBwb3J0LXJlcXVlc3RzX19jb250ZW50IHtcbiAgICBoZWlnaHQ6IGF1dG87XG4gIH1cbn1cbi5zdXBwb3J0LXJlcXVlc3RzX190YWJsZSB7XG4gIHdpZHRoOiAxMDAlO1xufVxuLnN1cHBvcnQtcmVxdWVzdHNfX3RhYmxlLXJvdyB7XG4gIGhlaWdodDogNjRweDtcbn1cbi5zdXBwb3J0LXJlcXVlc3RzX190YWJsZS1yb3ctdGl0bGUge1xuICBjb2xvcjogIzRBNEE0QTtcbiAgZm9udC1zaXplOiAxNHB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBsaW5lLWhlaWdodDogMjRweDtcbiAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTtcbiAgcGFkZGluZzogMTguNHB4O1xufVxuLnN1cHBvcnQtcmVxdWVzdHNfX3RhYmxlLWNvbnRlbnQge1xuICBjb2xvcjogIzRBNEE0QTtcbiAgZm9udC1zaXplOiAxNHB4O1xuICBwYWRkaW5nOiAyMHB4O1xufVxuLnN1cHBvcnQtcmVxdWVzdHNfX2NvbnRlbnQtYmFkZ2Uge1xuICB3aWR0aDogZml0LWNvbnRlbnQ7XG4gIGJvcmRlci1yYWRpdXM6IDMycHg7XG4gIGNvbG9yOiB3aGl0ZTtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICBwYWRkaW5nOiA1cHggMTBweDtcbiAgZm9udC1zaXplOiAxM3B4O1xuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICBmb250LWZhbWlseTogXCJSb2JvdG9cIiwgXCJIZWx2ZXRpY2FcIiwgXCJBcmlhbFwiLCBzYW5zLXNlcmlmO1xuICBmb250LXdlaWdodDogNDAwO1xuICBsaW5lLWhlaWdodDogMS43NTtcbiAgbGV0dGVyLXNwYWNpbmc6IDAuNDVweDtcbn1cbi5zdXBwb3J0LXJlcXVlc3RzX19jb250ZW50LWJhZGdlOjpmaXJzdC1sZXR0ZXIge1xuICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlO1xufVxuXG5tYXQtbWVudSB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcbn1cblxuLnNlbmQge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjM0NENEEwO1xufVxuXG4ucGVuZGluZyB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZmMyNjA7XG59XG5cbi5kZWNsaW5lZCB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZjQwODE7XG59IiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SupportRequestsComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-support-requests',
                            templateUrl: './support-requests.component.html',
                            styleUrls: ['./support-requests.component.scss']
                        }]
                    }], null, {
                        supportRequestData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/components/visits-chart/visits-chart.component.ts":
            /*!***********************************************************************************!*\
              !*** ./src/app/pages/dashboard/components/visits-chart/visits-chart.component.ts ***!
              \***********************************************************************************/
            /*! exports provided: VisitsChartComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "VisitsChartComponent", function() {
                    return VisitsChartComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ../../../../shared/ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var ngx_trend__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ngx-trend */ "./node_modules/ngx-trend/__ivy_ngcc__/fesm2015/ngx-trend.js");






                const _c0 = function(a0) {
                    return [a0];
                };
                class VisitsChartComponent {
                    constructor() {
                        this.colors = _consts__WEBPACK_IMPORTED_MODULE_1__["colors"];
                    }
                }
                VisitsChartComponent.ɵfac = function VisitsChartComponent_Factory(t) {
                    return new(t || VisitsChartComponent)();
                };
                VisitsChartComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: VisitsChartComponent,
                    selectors: [
                        ["app-visits-chart"]
                    ],
                    inputs: {
                        visitsChartData: "visitsChartData"
                    },
                    decls: 26,
                    vars: 11,
                    consts: [
                        [1, "visits-chart"],
                        [1, "visits-chart__header"],
                        [1, "visits-chart__title"],
                        [1, "visits-chart__content"],
                        [1, "visits-chart__content-info"],
                        [1, "visits-chart__content-info-title"],
                        [1, "visits-chart__content-info-chart", 3, "data", "gradient", "height", "smooth", "strokeWidth"],
                        [1, "visits-chart__content-stats"],
                        [1, "visits-chart__content-stats-title"],
                        [1, "visits-chart__content-stats-data"]
                    ],
                    template: function VisitsChartComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-card", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-card-title", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h5", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Visits Today");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-settings-menu");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-card-content", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "h6", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](9, "ngx-trend", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "div");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](13, "Registration");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](15);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "div");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](18, "Sign Out");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](21, "div");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](23, "Rate");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](24, "p", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](25);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.visitsChartData.all);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("data", ctx.visitsChartData.data)("gradient", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](9, _c0, ctx.colors.GREEN))("height", 44)("smooth", true)("strokeWidth", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.visitsChartData.registration);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](ctx.visitsChartData.signOut);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", ctx.visitsChartData.rate, "%");
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardTitle"], _shared_ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_3__["SettingsMenuComponent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardContent"], ngx_trend__WEBPACK_IMPORTED_MODULE_4__["TrendComponent"]],
                    styles: [".visits-chart[_ngcontent-%COMP%] {\n  display: flex;\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n  height: 192px;\n  flex-direction: column;\n  justify-content: space-between;\n}\n.visits-chart__header[_ngcontent-%COMP%] {\n  align-items: center;\n  color: #6E6E6E;\n  display: flex;\n  justify-content: space-between;\n}\n.visits-chart__title[_ngcontent-%COMP%] {\n  font-size: 20px;\n  font-weight: 400;\n  margin: 0;\n  line-height: 40px;\n}\n.visits-chart__content[_ngcontent-%COMP%] {\n  display: flex;\n  flex-direction: column;\n  justify-content: space-between;\n  height: 75%;\n}\n.visits-chart__content-info[_ngcontent-%COMP%] {\n  align-items: center;\n  display: flex;\n  height: 96px;\n  justify-content: space-between;\n}\n.visits-chart__content-info-title[_ngcontent-%COMP%] {\n  margin: 0;\n  font-weight: 400;\n  font-size: 24px;\n  line-height: 1.5;\n  letter-spacing: 0.15px;\n  color: #4A4A4A;\n}\n.visits-chart__content-info-chart[_ngcontent-%COMP%] {\n  margin-left: 16px;\n}\n.visits-chart__content-stats[_ngcontent-%COMP%] {\n  display: flex;\n  justify-content: space-between;\n}\n.visits-chart__content-stats-title[_ngcontent-%COMP%] {\n  margin: 0;\n  color: #6E6E6E;\n  font-weight: 400;\n  font-size: 14px;\n}\n.visits-chart__content-stats-data[_ngcontent-%COMP%] {\n  margin: 0;\n  line-height: 1.5;\n  font-weight: 400;\n  font-size: 21px;\n  color: #4A4A4A;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvdmlzaXRzLWNoYXJ0L3Zpc2l0cy1jaGFydC5jb21wb25lbnQuc2NzcyIsInNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbXBvbmVudHMvdmlzaXRzLWNoYXJ0L3Zpc2l0cy1jaGFydC5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UsYUFBQTtFQUNBLGlGQUFBO0VBQ0EsYUFBQTtFQUNBLHNCQUFBO0VBQ0EsOEJBQUE7QUNGRjtBRElFO0VBQ0UsbUJBQUE7RUFDQSxjQUFBO0VBQ0EsYUFBQTtFQUNBLDhCQUFBO0FDRko7QURLRTtFQUNFLGVBQUE7RUFDQSxnQkVuQlM7RUZvQlQsU0FBQTtFQUNBLGlCQUFBO0FDSEo7QURNRTtFQUNFLGFBQUE7RUFDQSxzQkFBQTtFQUNBLDhCQUFBO0VBQ0EsV0FBQTtBQ0pKO0FETUk7RUFDRSxtQkFBQTtFQUNBLGFBQUE7RUFDQSxZQUFBO0VBQ0EsOEJBQUE7QUNKTjtBRE1NO0VBQ0UsU0FBQTtFQUNBLGdCRXRDSztFRnVDTCxlRTdCRztFRjhCSCxnQkFBQTtFQUNBLHNCQUFBO0VBQ0EsY0doQ0k7QUY0Qlo7QURPTTtFQUNFLGlCQUFBO0FDTFI7QURTSTtFQUNFLGFBQUE7RUFDQSw4QkFBQTtBQ1BOO0FEU007RUFDRSxTQUFBO0VBQ0EsY0c1Q0Q7RUg2Q0MsZ0JFekRLO0VGMERMLGVFcERHO0FENkNYO0FEVU07RUFDRSxTQUFBO0VBQ0EsZ0JBQUE7RUFDQSxnQkVoRUs7RUZpRUwsZUV4REk7RUZ5REosY0d4REk7QUZnRFoiLCJmaWxlIjoic3JjL2FwcC9wYWdlcy9kYXNoYm9hcmQvY29tcG9uZW50cy92aXNpdHMtY2hhcnQvdmlzaXRzLWNoYXJ0LmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2NvbG9yc1wiO1xuQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2ZvbnRcIjtcblxuLnZpc2l0cy1jaGFydCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAkc2hhZG93LXdoaXRlLCAwIDNweCAzcHggLTJweCAkc2hhZG93LWdyZXksIDAgMXB4IDhweCAwICRzaGFkb3ctZGFyay1ncmV5O1xuICBoZWlnaHQ6IDE5MnB4O1xuICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgJl9faGVhZGVyIHtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICAgIGNvbG9yOiAkZ3JleTtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBmb250LXNpemU6IDIwcHg7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIG1hcmdpbjogMDtcbiAgICBsaW5lLWhlaWdodDogNDBweDtcbiAgfVxuXG4gICZfX2NvbnRlbnQge1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gICAgaGVpZ2h0OiA3NSU7XG5cbiAgICAmLWluZm8ge1xuICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgICBoZWlnaHQ6IDk2cHg7XG4gICAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgICAgICYtdGl0bGUge1xuICAgICAgICBtYXJnaW46MDtcbiAgICAgICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgICAgICBmb250LXNpemU6ICRmcy1sYXJnZTtcbiAgICAgICAgbGluZS1oZWlnaHQ6IDEuNTtcbiAgICAgICAgbGV0dGVyLXNwYWNpbmc6IDAuMTVweDtcbiAgICAgICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gICAgICB9XG5cbiAgICAgICYtY2hhcnQge1xuICAgICAgICBtYXJnaW4tbGVmdDogMTZweDtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAmLXN0YXRzIHtcbiAgICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG5cbiAgICAgICYtdGl0bGUge1xuICAgICAgICBtYXJnaW46MDtcbiAgICAgICAgY29sb3I6ICRncmV5O1xuICAgICAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgICAgIGZvbnQtc2l6ZTogJGZzLXNtYWxsO1xuICAgICAgfVxuXG4gICAgICAmLWRhdGEge1xuICAgICAgICBtYXJnaW46MDtcbiAgICAgICAgbGluZS1oZWlnaHQ6IDEuNTtcbiAgICAgICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgICAgICBmb250LXNpemU6ICRmcy1tZWRpdW07XG4gICAgICAgIGNvbG9yOiAkZGFyay1ncmV5O1xuICAgICAgfVxuICAgIH1cbiAgfVxufVxuIiwiLnZpc2l0cy1jaGFydCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAjRThFQUZDLCAwIDNweCAzcHggLTJweCAjQjJCMkIyMUEsIDAgMXB4IDhweCAwICM5QTlBOUExQTtcbiAgaGVpZ2h0OiAxOTJweDtcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xufVxuLnZpc2l0cy1jaGFydF9faGVhZGVyIHtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi52aXNpdHMtY2hhcnRfX3RpdGxlIHtcbiAgZm9udC1zaXplOiAyMHB4O1xuICBmb250LXdlaWdodDogNDAwO1xuICBtYXJnaW46IDA7XG4gIGxpbmUtaGVpZ2h0OiA0MHB4O1xufVxuLnZpc2l0cy1jaGFydF9fY29udGVudCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgaGVpZ2h0OiA3NSU7XG59XG4udmlzaXRzLWNoYXJ0X19jb250ZW50LWluZm8ge1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICBkaXNwbGF5OiBmbGV4O1xuICBoZWlnaHQ6IDk2cHg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi52aXNpdHMtY2hhcnRfX2NvbnRlbnQtaW5mby10aXRsZSB7XG4gIG1hcmdpbjogMDtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgZm9udC1zaXplOiAyNHB4O1xuICBsaW5lLWhlaWdodDogMS41O1xuICBsZXR0ZXItc3BhY2luZzogMC4xNXB4O1xuICBjb2xvcjogIzRBNEE0QTtcbn1cbi52aXNpdHMtY2hhcnRfX2NvbnRlbnQtaW5mby1jaGFydCB7XG4gIG1hcmdpbi1sZWZ0OiAxNnB4O1xufVxuLnZpc2l0cy1jaGFydF9fY29udGVudC1zdGF0cyB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi52aXNpdHMtY2hhcnRfX2NvbnRlbnQtc3RhdHMtdGl0bGUge1xuICBtYXJnaW46IDA7XG4gIGNvbG9yOiAjNkU2RTZFO1xuICBmb250LXdlaWdodDogNDAwO1xuICBmb250LXNpemU6IDE0cHg7XG59XG4udmlzaXRzLWNoYXJ0X19jb250ZW50LXN0YXRzLWRhdGEge1xuICBtYXJnaW46IDA7XG4gIGxpbmUtaGVpZ2h0OiAxLjU7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMjFweDtcbiAgY29sb3I6ICM0QTRBNEE7XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](VisitsChartComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-visits-chart',
                            templateUrl: './visits-chart.component.html',
                            styleUrls: ['./visits-chart.component.scss']
                        }]
                    }], null, {
                        visitsChartData: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/consts/custom-tooltip.ts":
            /*!**********************************************************!*\
              !*** ./src/app/pages/dashboard/consts/custom-tooltip.ts ***!
              \**********************************************************/
            /*! exports provided: customTooltip */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "customTooltip", function() {
                    return customTooltip;
                });
                const customTooltip = '<div>' +
                    '<div style="padding: 16px; 16px; display: flex; align-items: center;"> <div style="width: 8px; height: 8px; border-radius: 50%; background-color: #FFC260"></div><span style="color: #4A4A4A; margin-left: 8px">' + 'mobile' + '</span></div>' +
                    '<div style="padding: 16px; 16px; display: flex; align-items: center;"> <div style="width: 8px; height: 8px; border-radius: 50%; background-color: #536DFE"></div><span style="color: #4A4A4A; margin-left: 8px">' + 'desktop' + '</span></div>' +
                    '<div style="padding: 16px; 16px; display: flex; align-items: center;"> <div style="width: 8px; height: 8px; border-radius: 50%; background-color: #B1BCFF"></div><span style="color: #4A4A4A; margin-left: 8px">' + 'tablet' + '</span></div>' +
                    '</div>';


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/consts/index.ts":
            /*!*************************************************!*\
              !*** ./src/app/pages/dashboard/consts/index.ts ***!
              \*************************************************/
            /*! exports provided: customTooltip */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _custom_tooltip__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./custom-tooltip */ "./src/app/pages/dashboard/consts/custom-tooltip.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "customTooltip", function() {
                    return _custom_tooltip__WEBPACK_IMPORTED_MODULE_0__["customTooltip"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/dashboard/containers/dashboard-page/dashboard-page.component.ts":
            /*!***************************************************************************************!*\
              !*** ./src/app/pages/dashboard/containers/dashboard-page/dashboard-page.component.ts ***!
              \***************************************************************************************/
            /*! exports provided: DashboardPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "DashboardPageComponent", function() {
                    return DashboardPageComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../services */ "./src/app/pages/dashboard/services/index.ts");
                /* harmony import */
                var _shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../shared/layout/layout.component */ "./src/app/shared/layout/layout.component.ts");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _components_visits_chart_visits_chart_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! ../../components/visits-chart/visits-chart.component */ "./src/app/pages/dashboard/components/visits-chart/visits-chart.component.ts");
                /* harmony import */
                var _components_performance_chart_performance_chart_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ../../components/performance-chart/performance-chart.component */ "./src/app/pages/dashboard/components/performance-chart/performance-chart.component.ts");
                /* harmony import */
                var _components_server_chart_server_chart_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! ../../components/server-chart/server-chart.component */ "./src/app/pages/dashboard/components/server-chart/server-chart.component.ts");
                /* harmony import */
                var _components_revenue_chart_revenue_chart_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! ../../components/revenue-chart/revenue-chart.component */ "./src/app/pages/dashboard/components/revenue-chart/revenue-chart.component.ts");
                /* harmony import */
                var _components_daily_line_chart_daily_line_chart_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! ../../components/daily-line-chart/daily-line-chart.component */ "./src/app/pages/dashboard/components/daily-line-chart/daily-line-chart.component.ts");
                /* harmony import */
                var _components_project_stat_chart_project_stat_chart_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ../../components/project-stat-chart/project-stat-chart.component */ "./src/app/pages/dashboard/components/project-stat-chart/project-stat-chart.component.ts");
                /* harmony import */
                var _components_support_requests_support_requests_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ../../components/support-requests/support-requests.component */ "./src/app/pages/dashboard/components/support-requests/support-requests.component.ts");
                /* harmony import */
                var _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! ../../../../shared/footer/footer.component */ "./src/app/shared/footer/footer.component.ts");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");















                class DashboardPageComponent {
                    constructor(service) {
                        this.service = service;
                        this.dailyLineChartData$ = this.service.loadDailyLineChartData();
                        this.performanceChartData$ = this.service.loadPerformanceChartData();
                        this.revenueChartData$ = this.service.loadRevenueChartData();
                        this.serverChartData$ = this.service.loadServerChartData();
                        this.supportRequestData$ = this.service.loadSupportRequestData();
                        this.visitsChartData$ = this.service.loadVisitsChartData();
                        this.projectsStatsData$ = this.service.loadProjectsStatsData();
                    }
                }
                DashboardPageComponent.ɵfac = function DashboardPageComponent_Factory(t) {
                    return new(t || DashboardPageComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services__WEBPACK_IMPORTED_MODULE_1__["DashboardService"]));
                };
                DashboardPageComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: DashboardPageComponent,
                    selectors: [
                        ["app-dashboard-page"]
                    ],
                    decls: 26,
                    vars: 21,
                    consts: [
                        ["role", "heading", 1, "page-header"],
                        ["mat-flat-button", "", "color", "warn"],
                        [1, "charts-wrapper"],
                        [1, "chart"],
                        [3, "visitsChartData"],
                        [3, "performanceChartData"],
                        [3, "serverChartData"],
                        [3, "revenueCharData"],
                        [3, "dailyLineChartData"],
                        [3, "projectsStatsData"],
                        [3, "supportRequestData"]
                    ],
                    template: function DashboardPageComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "app-layout");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-toolbar", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h1");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Dashboard");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "button", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](5, "Latest Reports");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](8, "app-visits-chart", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](9, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](11, "app-performance-chart", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](12, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](14, "app-server-chart", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](15, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](17, "app-revenue-chart", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](18, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](19, "app-daily-line-chart", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](20, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](21, "app-project-stat-chart", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](22, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](23, "app-support-requests", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](24, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](25, "app-footer");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("visitsChartData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](9, 7, ctx.visitsChartData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("performanceChartData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](12, 9, ctx.performanceChartData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("serverChartData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](15, 11, ctx.serverChartData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("revenueCharData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](18, 13, ctx.revenueChartData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("dailyLineChartData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](20, 15, ctx.dailyLineChartData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("projectsStatsData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](22, 17, ctx.projectsStatsData$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("supportRequestData", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](24, 19, ctx.supportRequestData$));
                        }
                    },
                    directives: [_shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_2__["LayoutComponent"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__["MatToolbar"], _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButton"], _components_visits_chart_visits_chart_component__WEBPACK_IMPORTED_MODULE_5__["VisitsChartComponent"], _components_performance_chart_performance_chart_component__WEBPACK_IMPORTED_MODULE_6__["PerformanceChartComponent"], _components_server_chart_server_chart_component__WEBPACK_IMPORTED_MODULE_7__["ServerChartComponent"], _components_revenue_chart_revenue_chart_component__WEBPACK_IMPORTED_MODULE_8__["RevenueChartComponent"], _components_daily_line_chart_daily_line_chart_component__WEBPACK_IMPORTED_MODULE_9__["DailyLineChartComponent"], _components_project_stat_chart_project_stat_chart_component__WEBPACK_IMPORTED_MODULE_10__["ProjectStatChartComponent"], _components_support_requests_support_requests_component__WEBPACK_IMPORTED_MODULE_11__["SupportRequestsComponent"], _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_12__["FooterComponent"]],
                    pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_13__["AsyncPipe"]],
                    styles: [".charts-wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  margin: 0 8px;\n}\n@media (max-width: 1024px) {\n  .charts-wrapper[_ngcontent-%COMP%] {\n    flex-wrap: wrap;\n  }\n}\n.chart[_ngcontent-%COMP%] {\n  width: 100%;\n}\n@media (max-width: 1024px) {\n  .chart[_ngcontent-%COMP%] {\n    width: 50%;\n  }\n}\n@media (max-width: 576px) {\n  .chart[_ngcontent-%COMP%] {\n    width: 100%;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbnRhaW5lcnMvZGFzaGJvYXJkLXBhZ2UvZGFzaGJvYXJkLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL2Rhc2hib2FyZC9jb250YWluZXJzL2Rhc2hib2FyZC1wYWdlL2Rhc2hib2FyZC1wYWdlLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUVBO0VBQ0UsYUFBQTtFQUNBLGFBQUE7QUNERjtBREdFO0VBSkY7SUFLSSxlQUFBO0VDQUY7QUFDRjtBREdBO0VBQ0UsV0FBQTtBQ0FGO0FERUU7RUFIRjtJQUlJLFVBQUE7RUNDRjtBQUNGO0FEQ0U7RUFQRjtJQVFJLFdBQUE7RUNFRjtBQUNGIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvZGFzaGJvYXJkL2NvbnRhaW5lcnMvZGFzaGJvYXJkLXBhZ2UvZGFzaGJvYXJkLXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4uY2hhcnRzLXdyYXBwZXIge1xuICBkaXNwbGF5OiBmbGV4O1xuICBtYXJnaW46IDAgOHB4O1xuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkbm9ybWFsKSB7XG4gICAgZmxleC13cmFwOiB3cmFwO1xuICB9XG59XG5cbi5jaGFydCB7XG4gIHdpZHRoOiAxMDAlO1xuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkbm9ybWFsKSB7XG4gICAgd2lkdGg6IDUwJTtcbiAgfVxuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICB3aWR0aDogMTAwJTtcbiAgfVxufVxuIiwiLmNoYXJ0cy13cmFwcGVyIHtcbiAgZGlzcGxheTogZmxleDtcbiAgbWFyZ2luOiAwIDhweDtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiAxMDI0cHgpIHtcbiAgLmNoYXJ0cy13cmFwcGVyIHtcbiAgICBmbGV4LXdyYXA6IHdyYXA7XG4gIH1cbn1cblxuLmNoYXJ0IHtcbiAgd2lkdGg6IDEwMCU7XG59XG5AbWVkaWEgKG1heC13aWR0aDogMTAyNHB4KSB7XG4gIC5jaGFydCB7XG4gICAgd2lkdGg6IDUwJTtcbiAgfVxufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5jaGFydCB7XG4gICAgd2lkdGg6IDEwMCU7XG4gIH1cbn0iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DashboardPageComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-dashboard-page',
                            templateUrl: './dashboard-page.component.html',
                            styleUrls: ['./dashboard-page.component.scss']
                        }]
                    }], function() {
                        return [{
                            type: _services__WEBPACK_IMPORTED_MODULE_1__["DashboardService"]
                        }];
                    }, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/containers/index.ts":
            /*!*****************************************************!*\
              !*** ./src/app/pages/dashboard/containers/index.ts ***!
              \*****************************************************/
            /*! exports provided: DashboardPageComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _dashboard_page_dashboard_page_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./dashboard-page/dashboard-page.component */ "./src/app/pages/dashboard/containers/dashboard-page/dashboard-page.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "DashboardPageComponent", function() {
                    return _dashboard_page_dashboard_page_component__WEBPACK_IMPORTED_MODULE_0__["DashboardPageComponent"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/dashboard/dashboard.module.ts":
            /*!*****************************************************!*\
              !*** ./src/app/pages/dashboard/dashboard.module.ts ***!
              \*****************************************************/
            /*! exports provided: DashboardModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "DashboardModule", function() {
                    return DashboardModule;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_table__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/table */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/table.js");
                /* harmony import */
                var ngx_echarts__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ngx-echarts */ "./node_modules/ngx-echarts/__ivy_ngcc__/fesm2015/ngx-echarts.js");
                /* harmony import */
                var ngx_trend__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ngx-trend */ "./node_modules/ngx-trend/__ivy_ngcc__/fesm2015/ngx-trend.js");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! @angular/material/progress-bar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/progress-bar.js");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! @angular/material/grid-list */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/grid-list.js");
                /* harmony import */
                var _angular_material_select__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! @angular/material/select */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/select.js");
                /* harmony import */
                var _angular_material_input__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! @angular/material/input */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/input.js");
                /* harmony import */
                var ng_apexcharts__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__( /*! ng-apexcharts */ "./node_modules/ng-apexcharts/__ivy_ngcc__/fesm2015/ng-apexcharts.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__( /*! ./containers */ "./src/app/pages/dashboard/containers/index.ts");
                /* harmony import */
                var _components__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__( /*! ./components */ "./src/app/pages/dashboard/components/index.ts");
                /* harmony import */
                var _shared_shared_module__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__( /*! ../../shared/shared.module */ "./src/app/shared/shared.module.ts");
                /* harmony import */
                var _services__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__( /*! ./services */ "./src/app/pages/dashboard/services/index.ts");





















                class DashboardModule {}
                DashboardModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: DashboardModule
                });
                DashboardModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function DashboardModule_Factory(t) {
                        return new(t || DashboardModule)();
                    },
                    providers: [
                        _services__WEBPACK_IMPORTED_MODULE_19__["DashboardService"]
                    ],
                    imports: [
                        [
                            _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _angular_material_table__WEBPACK_IMPORTED_MODULE_2__["MatTableModule"],
                            ngx_echarts__WEBPACK_IMPORTED_MODULE_3__["NgxEchartsModule"],
                            ngx_trend__WEBPACK_IMPORTED_MODULE_4__["TrendModule"],
                            _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_7__["MatMenuModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_8__["MatButtonModule"],
                            _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_9__["MatProgressBarModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_10__["MatToolbarModule"],
                            _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
                            _angular_material_select__WEBPACK_IMPORTED_MODULE_12__["MatSelectModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_13__["MatInputModule"],
                            ng_apexcharts__WEBPACK_IMPORTED_MODULE_14__["NgApexchartsModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_15__["FormsModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_18__["SharedModule"]
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](DashboardModule, {
                        declarations: [_containers__WEBPACK_IMPORTED_MODULE_16__["DashboardPageComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["VisitsChartComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["PerformanceChartComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["ServerChartComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["RevenueChartComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["DailyLineChartComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["SupportRequestsComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_17__["ProjectStatChartComponent"]
                        ],
                        imports: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                            _angular_material_table__WEBPACK_IMPORTED_MODULE_2__["MatTableModule"],
                            ngx_echarts__WEBPACK_IMPORTED_MODULE_3__["NgxEchartsModule"],
                            ngx_trend__WEBPACK_IMPORTED_MODULE_4__["TrendModule"],
                            _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_7__["MatMenuModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_8__["MatButtonModule"],
                            _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_9__["MatProgressBarModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_10__["MatToolbarModule"],
                            _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
                            _angular_material_select__WEBPACK_IMPORTED_MODULE_12__["MatSelectModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_13__["MatInputModule"],
                            ng_apexcharts__WEBPACK_IMPORTED_MODULE_14__["NgApexchartsModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_15__["FormsModule"],
                            _shared_shared_module__WEBPACK_IMPORTED_MODULE_18__["SharedModule"]
                        ],
                        exports: [_components__WEBPACK_IMPORTED_MODULE_17__["DailyLineChartComponent"]]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DashboardModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [
                                _containers__WEBPACK_IMPORTED_MODULE_16__["DashboardPageComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["VisitsChartComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["PerformanceChartComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["ServerChartComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["RevenueChartComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["DailyLineChartComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["SupportRequestsComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_17__["ProjectStatChartComponent"]
                            ],
                            imports: [
                                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                                _angular_material_table__WEBPACK_IMPORTED_MODULE_2__["MatTableModule"],
                                ngx_echarts__WEBPACK_IMPORTED_MODULE_3__["NgxEchartsModule"],
                                ngx_trend__WEBPACK_IMPORTED_MODULE_4__["TrendModule"],
                                _angular_material_card__WEBPACK_IMPORTED_MODULE_5__["MatCardModule"],
                                _angular_material_icon__WEBPACK_IMPORTED_MODULE_6__["MatIconModule"],
                                _angular_material_menu__WEBPACK_IMPORTED_MODULE_7__["MatMenuModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_8__["MatButtonModule"],
                                _angular_material_progress_bar__WEBPACK_IMPORTED_MODULE_9__["MatProgressBarModule"],
                                _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_10__["MatToolbarModule"],
                                _angular_material_grid_list__WEBPACK_IMPORTED_MODULE_11__["MatGridListModule"],
                                _angular_material_select__WEBPACK_IMPORTED_MODULE_12__["MatSelectModule"],
                                _angular_material_input__WEBPACK_IMPORTED_MODULE_13__["MatInputModule"],
                                ng_apexcharts__WEBPACK_IMPORTED_MODULE_14__["NgApexchartsModule"],
                                _angular_forms__WEBPACK_IMPORTED_MODULE_15__["FormsModule"],
                                _shared_shared_module__WEBPACK_IMPORTED_MODULE_18__["SharedModule"]
                            ],
                            exports: [
                                _components__WEBPACK_IMPORTED_MODULE_17__["DailyLineChartComponent"]
                            ],
                            providers: [
                                _services__WEBPACK_IMPORTED_MODULE_19__["DashboardService"]
                            ]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/services/dashboard.service.ts":
            /*!***************************************************************!*\
              !*** ./src/app/pages/dashboard/services/dashboard.service.ts ***!
              \***************************************************************/
            /*! exports provided: DashboardService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "DashboardService", function() {
                    return DashboardService;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");



                class DashboardService {
                    loadDailyLineChartData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            dailyData: {
                                mobile: [16, 46, 45, 12, 37, 16, 41, 13, 25, 22, 30],
                                desktop: [42, 60, 49, 50, 13, 15, 16, 57, 56, 27, 43],
                                tablet: [35, 25, 36, 30, 67, 35, 64, 12, 25, 36, 39]
                            },
                            weeklyData: {
                                mobile: [23, 31, 45, 10, 37, 67, 43, 63, 15, 22, 30],
                                desktop: [67, 60, 49, 50, 25, 15, 16, 57, 13, 27, 43],
                                tablet: [56, 48, 23, 48, 13, 35, 64, 12, 45, 36, 39]
                            },
                            monthlyData: {
                                mobile: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
                                desktop: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
                                tablet: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39]
                            },
                            labels: [
                                '01/01/2003',
                                '02/01/2003',
                                '03/01/2003',
                                '04/01/2003',
                                '05/01/2003',
                                '06/01/2003',
                                '07/01/2003',
                                '08/01/2003',
                                '09/01/2003',
                                '10/01/2003',
                                '11/01/2003'
                            ]
                        });
                    }
                    loadPerformanceChartData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            integration: 40,
                            sdk: 75
                        });
                    }
                    loadRevenueChartData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            groupA: Math.round(Math.random() * 100),
                            groupB: Math.round(Math.random() * 100),
                            groupC: Math.round(Math.random() * 100),
                            groupD: Math.round(Math.random() * 100)
                        });
                    }
                    loadServerChartData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            firstServerChartData: [
                                18107.85,
                                49128.0,
                                38122.9,
                                28965.5,
                                49340.7
                            ],
                            firstDataTitle: '45% / 78°С / 78 Ghz',
                            secondServerChartData: [
                                18423.7,
                                48423.5,
                                28514.3,
                                48481.85,
                                18487.7
                            ],
                            secondDataTitle: '57% / 45°С / 54 Ghz',
                            thirdServerChartData: [
                                17114.25,
                                27126.6,
                                47116.95,
                                37203.7,
                                17233.75
                            ],
                            thirdDataTitle: '87% / 55°С / 76 Ghz',
                            dates: [
                                '13 Nov 2017',
                                '14 Nov 2017',
                                '15 Nov 2017',
                                '16 Nov 2017',
                                '17 Nov 2017'
                            ]
                        });
                    }
                    loadSupportRequestData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])([{
                            name: 'Mark Otto',
                            email: 'ottoto@wxample.com',
                            product: 'ON the Road',
                            price: '$25 224.2',
                            date: '11 May 2017',
                            city: 'Otsego',
                            status: 'send'
                        }, {
                            name: 'Jacob Thornton',
                            email: 'thornton@wxample.com',
                            product: 'HP Core i7',
                            price: '$1 254.2',
                            date: '4 Jun 2017',
                            city: 'Fivepointville',
                            status: 'send'
                        }, {
                            name: 'Larry the Bird',
                            email: 'bird@wxample.com',
                            product: 'Air Pro',
                            price: '$1 570.0',
                            date: '27 Aug 2017',
                            city: 'Leadville North',
                            status: 'pending'
                        }, {
                            name: 'Joseph May',
                            email: 'josephmay@wxample.com',
                            product: 'Version Control',
                            price: '$5 224.5',
                            date: '19 Feb 2018',
                            city: 'Seaforth',
                            status: 'declined'
                        }, {
                            name: 'Peter Horadnia',
                            email: 'horadnia@wxample.com',
                            product: 'Let\'s Dance',
                            price: '$43 594.7',
                            date: '1 Mar 2018',
                            city: 'Hanoverton',
                            status: 'send'
                        }]);
                    }
                    loadVisitsChartData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            data: [7, 6, 3, 8, 10, 6, 7, 8, 3, 0, 7, 6, 2, 7, 4, 7, 3, 6, 2, 3, 8, 1, 0, 4, 9],
                            registration: '860',
                            signOut: '32',
                            rate: '3.25',
                            all: '12.678'
                        });
                    }
                    loadProjectsStatsData() {
                        return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["of"])({
                            lightBlue: {
                                daily: {
                                    name: 'Light Blue',
                                    users: '199',
                                    percent: -3.7,
                                    registrations: '33',
                                    bounce: '3.25%',
                                    views: '330',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [210, 95, 155, 200, 61, 135, 63]
                                    }]
                                },
                                week: {
                                    name: 'Light Blue',
                                    users: '1293',
                                    percent: 3.1,
                                    registrations: '233',
                                    bounce: '3.1%',
                                    views: '2310',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [65, 195, 135, 95, 72, 155, 200]
                                    }]
                                },
                                monthly: {
                                    name: 'Light Blue',
                                    users: '9991',
                                    percent: -3.1,
                                    registrations: '725',
                                    bounce: '3.3%',
                                    views: '12301',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [152, 61, 142, 183, 74, 195, 210]
                                    }]
                                }
                            },
                            singApp: {
                                daily: {
                                    name: 'Sing App',
                                    users: '121',
                                    percent: -3.2,
                                    registrations: '15',
                                    bounce: '3.01%',
                                    views: '302',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [135, 65, 192, 215, 85, 154, 75]
                                    }]
                                },
                                week: {
                                    name: 'Sing App',
                                    users: '956',
                                    percent: 2.9,
                                    registrations: '295',
                                    bounce: '3.15%',
                                    views: '2401',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [78, 145, 186, 64, 78, 135, 224]
                                    }]
                                },
                                monthly: {
                                    name: 'Sing App',
                                    users: '9982',
                                    percent: -3.23,
                                    registrations: '712',
                                    bounce: '3.2%',
                                    views: '12256',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [59, 75, 153, 194, 87, 205, 215]
                                    }]
                                }
                            },
                            rns: {
                                daily: {
                                    name: 'RNS',
                                    users: '175',
                                    percent: -3.1,
                                    registrations: '31',
                                    bounce: '3.23%',
                                    views: '301',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [205, 81, 175, 192, 52, 199, 206]
                                    }]
                                },
                                week: {
                                    name: 'RNS',
                                    users: '1395',
                                    percent: 3.21,
                                    registrations: '235',
                                    bounce: '3.23%',
                                    views: '2215',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [51, 186, 159, 201, 72, 86, 212]
                                    }]
                                },
                                monthly: {
                                    name: 'RNS',
                                    users: '9125',
                                    percent: -3.3,
                                    registrations: '756',
                                    bounce: '3.1%',
                                    views: '12025',
                                    series: [{
                                        name: 'Net Profit',
                                        data: [161, 84, 151, 201, 45, 196, 57]
                                    }]
                                }
                            }
                        });
                    }
                }
                DashboardService.ɵfac = function DashboardService_Factory(t) {
                    return new(t || DashboardService)();
                };
                DashboardService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({
                    token: DashboardService,
                    factory: DashboardService.ɵfac,
                    providedIn: 'root'
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DashboardService, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
                        args: [{
                            providedIn: 'root'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/pages/dashboard/services/index.ts":
            /*!***************************************************!*\
              !*** ./src/app/pages/dashboard/services/index.ts ***!
              \***************************************************/
            /*! exports provided: DashboardService */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _dashboard_service__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./dashboard.service */ "./src/app/pages/dashboard/services/dashboard.service.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "DashboardService", function() {
                    return _dashboard_service__WEBPACK_IMPORTED_MODULE_0__["DashboardService"];
                });




                /***/
            }),

        /***/
        "./src/app/pages/not-found/not-found.component.ts":
            /*!********************************************************!*\
              !*** ./src/app/pages/not-found/not-found.component.ts ***!
              \********************************************************/
            /*! exports provided: NotFoundComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "NotFoundComponent", function() {
                    return NotFoundComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/card */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");






                class NotFoundComponent {
                    constructor() {
                        this.routes = _consts__WEBPACK_IMPORTED_MODULE_1__["routes"];
                    }
                }
                NotFoundComponent.ɵfac = function NotFoundComponent_Factory(t) {
                    return new(t || NotFoundComponent)();
                };
                NotFoundComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: NotFoundComponent,
                    selectors: [
                        ["app-not-found"]
                    ],
                    decls: 16,
                    vars: 1,
                    consts: [
                        [1, "not-found-page"],
                        [1, "not-found-page__content"],
                        [1, "not-found-page__title"],
                        ["src", "/angflat/static/tte/assets/hot-found/logo.svg", "alt", "logo", 1, "not-found-page__title-img"],
                        [1, "not-found-page__title-text"],
                        [1, "not-found-page__card"],
                        [1, "not-found-page__card-title"],
                        [1, "not-found-page__card-sub-title"],
                        [1, "not-found-page__card-sub-title-second"],
                        ["mat-raised-button", "", "color", "primary", 1, "not-found-page__card-button", 3, "routerLink"]
                    ],
                    template: function NotFoundComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](3, "img", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "h3", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](5, "Material Admin");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-card", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "mat-card-content", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "h1", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "404");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "p", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11, "Oops. Looks like the page you're looking for no longer exists");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "p", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](13, "But we're here to bring you back to safety");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "button", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](15, "Back to Home");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](14);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", ctx.routes.DASHBOARD);
                        }
                    },
                    directives: [_angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardContent"], _angular_material_button__WEBPACK_IMPORTED_MODULE_3__["MatButton"], _angular_router__WEBPACK_IMPORTED_MODULE_4__["RouterLink"]],
                    styles: [".not-found-page[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  display: flex;\n  justify-content: center;\n  height: 100vh;\n}\n.not-found-page__content[_ngcontent-%COMP%] {\n  width: 355px;\n}\n.not-found-page__title[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  margin-top: 42px;\n  margin-bottom: 67px;\n}\n.not-found-page__title-img[_ngcontent-%COMP%] {\n  width: 48px;\n  margin-left: 20px;\n  margin-top: -6px;\n}\n.not-found-page__title-text[_ngcontent-%COMP%] {\n  color: white;\n  margin: 1px 30px 0 0;\n  font-weight: 500;\n  font-size: 32px;\n  letter-spacing: 0.6px;\n}\n.not-found-page__card[_ngcontent-%COMP%] {\n  box-sizing: border-box;\n  width: 100%;\n  height: 70vh;\n  padding: 56px 0 36px 0;\n  margin: 0;\n}\n.not-found-page__card-content[_ngcontent-%COMP%] {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  justify-content: center;\n}\n.not-found-page__card-title[_ngcontent-%COMP%] {\n  font-size: 107px;\n  font-weight: 500;\n  color: #536DFE;\n  line-height: 108px;\n  text-align: center;\n}\n.not-found-page__card-sub-title[_ngcontent-%COMP%] {\n  margin-top: 30px;\n  font-size: 16px;\n  font-weight: 400;\n  letter-spacing: -0.05px;\n  color: #536DFE;\n  text-align: center;\n}\n.not-found-page__card-sub-title-second[_ngcontent-%COMP%] {\n  margin-top: 30px;\n  font-size: 16px;\n  font-weight: 400;\n  letter-spacing: -0.2px;\n  color: #6E6E6E;\n  text-align: center;\n}\n.not-found-page__card-button[_ngcontent-%COMP%] {\n  margin-top: 40px;\n  margin-left: 36px;\n  width: 150px;\n  line-height: 40px;\n  letter-spacing: 1px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvbm90LWZvdW5kL25vdC1mb3VuZC5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIiwic3JjL2FwcC9wYWdlcy9ub3QtZm91bmQvbm90LWZvdW5kLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvZm9udC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UseUJDSEs7RURJTCxhQUFBO0VBQ0EsdUJBQUE7RUFDQSxhQUFBO0FFRkY7QUZJRTtFQUNFLFlBQUE7QUVGSjtBRktFO0VBQ0UsYUFBQTtFQUNBLG1CQUFBO0VBQ0EsOEJBQUE7RUFDQSxnQkFBQTtFQUNBLG1CQUFBO0FFSEo7QUZLSTtFQUNFLFdBQUE7RUFDQSxpQkFBQTtFQUNBLGdCQUFBO0FFSE47QUZNSTtFQUNFLFlDbEJFO0VEbUJGLG9CQUFBO0VBQ0EsZ0JBQUE7RUFDQSxlQUFBO0VBQ0EscUJBQUE7QUVKTjtBRlFFO0VBQ0Usc0JBQUE7RUFDQSxXQUFBO0VBQ0EsWUFBQTtFQUNBLHNCQUFBO0VBQ0EsU0FBQTtBRU5KO0FGUUk7RUFDRSxhQUFBO0VBQ0Esc0JBQUE7RUFDQSxtQkFBQTtFQUNBLHVCQUFBO0FFTk47QUZTSTtFQUNFLGdCQUFBO0VBQ0EsZ0JBQUE7RUFDQSxjQ25EQztFRG9ERCxrQkFBQTtFQUNBLGtCQUFBO0FFUE47QUZVSTtFQUNFLGdCQUFBO0VBQ0EsZUdwRE07RUhxRE4sZ0JBQUE7RUFDQSx1QkFBQTtFQUNBLGNDN0RDO0VEOERELGtCQUFBO0FFUk47QUZXSTtFQUNFLGdCQUFBO0VBQ0EsZUc3RE07RUg4RE4sZ0JBQUE7RUFDQSxzQkFBQTtFQUNBLGNDM0RDO0VENERELGtCQUFBO0FFVE47QUZZSTtFQUNFLGdCQUFBO0VBQ0EsaUJBQUE7RUFDQSxZQUFBO0VBQ0EsaUJBQUE7RUFDQSxtQkFBQTtBRVZOIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvbm90LWZvdW5kL25vdC1mb3VuZC5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2NvbG9ycyc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9mb250JztcblxuLm5vdC1mb3VuZC1wYWdlIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xuICBoZWlnaHQ6IDEwMHZoO1xuXG4gICZfX2NvbnRlbnQge1xuICAgIHdpZHRoOiAzNTVweDtcbiAgfVxuXG4gICZfX3RpdGxlIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gICAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICAgIG1hcmdpbi10b3A6IDQycHg7XG4gICAgbWFyZ2luLWJvdHRvbTogNjdweDtcblxuICAgICYtaW1nIHtcbiAgICAgIHdpZHRoOiA0OHB4O1xuICAgICAgbWFyZ2luLWxlZnQ6IDIwcHg7XG4gICAgICBtYXJnaW4tdG9wOiAtNnB4O1xuICAgIH1cblxuICAgICYtdGV4dCB7XG4gICAgICBjb2xvcjogJHdoaXRlO1xuICAgICAgbWFyZ2luOiAxcHggMzBweCAwIDA7XG4gICAgICBmb250LXdlaWdodDogNTAwO1xuICAgICAgZm9udC1zaXplOiAzMnB4O1xuICAgICAgbGV0dGVyLXNwYWNpbmc6IDAuNnB4O1xuICAgIH1cbiAgfVxuXG4gICZfX2NhcmQge1xuICAgIGJveC1zaXppbmc6IGJvcmRlci1ib3g7XG4gICAgd2lkdGg6IDEwMCU7XG4gICAgaGVpZ2h0OiA3MHZoO1xuICAgIHBhZGRpbmc6IDU2cHggMCAzNnB4IDA7XG4gICAgbWFyZ2luOiAwO1xuXG4gICAgJi1jb250ZW50IHtcbiAgICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICAgIGp1c3RpZnktY29udGVudDogY2VudGVyO1xuICAgIH1cblxuICAgICYtdGl0bGUge1xuICAgICAgZm9udC1zaXplOiAxMDdweDtcbiAgICAgIGZvbnQtd2VpZ2h0OiA1MDA7XG4gICAgICBjb2xvcjogJGJsdWU7XG4gICAgICBsaW5lLWhlaWdodDogMTA4cHg7XG4gICAgICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gICAgfVxuXG4gICAgJi1zdWItdGl0bGUge1xuICAgICAgbWFyZ2luLXRvcDogMzBweDtcbiAgICAgIGZvbnQtc2l6ZTogJGZzLW5vcm1hbDtcbiAgICAgIGZvbnQtd2VpZ2h0OiA0MDA7XG4gICAgICBsZXR0ZXItc3BhY2luZzogLTAuMDVweDtcbiAgICAgIGNvbG9yOiAkYmx1ZTtcbiAgICAgIHRleHQtYWxpZ246IGNlbnRlcjtcbiAgICB9XG5cbiAgICAmLXN1Yi10aXRsZS1zZWNvbmQge1xuICAgICAgbWFyZ2luLXRvcDogMzBweDtcbiAgICAgIGZvbnQtc2l6ZTogJGZzLW5vcm1hbDtcbiAgICAgIGZvbnQtd2VpZ2h0OiA0MDA7XG4gICAgICBsZXR0ZXItc3BhY2luZzogLTAuMnB4O1xuICAgICAgY29sb3I6ICRncmV5O1xuICAgICAgdGV4dC1hbGlnbjogY2VudGVyO1xuICAgIH1cblxuICAgICYtYnV0dG9uIHtcbiAgICAgIG1hcmdpbi10b3A6IDQwcHg7XG4gICAgICBtYXJnaW4tbGVmdDogMzZweDtcbiAgICAgIHdpZHRoOiAxNTBweDtcbiAgICAgIGxpbmUtaGVpZ2h0OiA0MHB4O1xuICAgICAgbGV0dGVyLXNwYWNpbmc6IDFweDtcbiAgICB9XG4gIH1cbn1cbiIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIi5ub3QtZm91bmQtcGFnZSB7XG4gIGJhY2tncm91bmQtY29sb3I6ICM1MzZERkU7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xuICBoZWlnaHQ6IDEwMHZoO1xufVxuLm5vdC1mb3VuZC1wYWdlX19jb250ZW50IHtcbiAgd2lkdGg6IDM1NXB4O1xufVxuLm5vdC1mb3VuZC1wYWdlX190aXRsZSB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgbWFyZ2luLXRvcDogNDJweDtcbiAgbWFyZ2luLWJvdHRvbTogNjdweDtcbn1cbi5ub3QtZm91bmQtcGFnZV9fdGl0bGUtaW1nIHtcbiAgd2lkdGg6IDQ4cHg7XG4gIG1hcmdpbi1sZWZ0OiAyMHB4O1xuICBtYXJnaW4tdG9wOiAtNnB4O1xufVxuLm5vdC1mb3VuZC1wYWdlX190aXRsZS10ZXh0IHtcbiAgY29sb3I6IHdoaXRlO1xuICBtYXJnaW46IDFweCAzMHB4IDAgMDtcbiAgZm9udC13ZWlnaHQ6IDUwMDtcbiAgZm9udC1zaXplOiAzMnB4O1xuICBsZXR0ZXItc3BhY2luZzogMC42cHg7XG59XG4ubm90LWZvdW5kLXBhZ2VfX2NhcmQge1xuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICB3aWR0aDogMTAwJTtcbiAgaGVpZ2h0OiA3MHZoO1xuICBwYWRkaW5nOiA1NnB4IDAgMzZweCAwO1xuICBtYXJnaW46IDA7XG59XG4ubm90LWZvdW5kLXBhZ2VfX2NhcmQtY29udGVudCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG4gIGp1c3RpZnktY29udGVudDogY2VudGVyO1xufVxuLm5vdC1mb3VuZC1wYWdlX19jYXJkLXRpdGxlIHtcbiAgZm9udC1zaXplOiAxMDdweDtcbiAgZm9udC13ZWlnaHQ6IDUwMDtcbiAgY29sb3I6ICM1MzZERkU7XG4gIGxpbmUtaGVpZ2h0OiAxMDhweDtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xufVxuLm5vdC1mb3VuZC1wYWdlX19jYXJkLXN1Yi10aXRsZSB7XG4gIG1hcmdpbi10b3A6IDMwcHg7XG4gIGZvbnQtc2l6ZTogMTZweDtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgbGV0dGVyLXNwYWNpbmc6IC0wLjA1cHg7XG4gIGNvbG9yOiAjNTM2REZFO1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG59XG4ubm90LWZvdW5kLXBhZ2VfX2NhcmQtc3ViLXRpdGxlLXNlY29uZCB7XG4gIG1hcmdpbi10b3A6IDMwcHg7XG4gIGZvbnQtc2l6ZTogMTZweDtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgbGV0dGVyLXNwYWNpbmc6IC0wLjJweDtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIHRleHQtYWxpZ246IGNlbnRlcjtcbn1cbi5ub3QtZm91bmQtcGFnZV9fY2FyZC1idXR0b24ge1xuICBtYXJnaW4tdG9wOiA0MHB4O1xuICBtYXJnaW4tbGVmdDogMzZweDtcbiAgd2lkdGg6IDE1MHB4O1xuICBsaW5lLWhlaWdodDogNDBweDtcbiAgbGV0dGVyLXNwYWNpbmc6IDFweDtcbn0iLCIkZnctbGlnaHRlcjogNDAwO1xuJGZ3LW5vcm1hbDogNTAwO1xuJGZ3LWJvbGQ6IDYwMDtcblxuXG4kZnMteHM6IDExLjJweDtcbiRmcy1zbWFsbDogMTRweDtcbiRmcy1ub3JtYWw6IDE2cHg7XG4kZnMtcmVndWxhcjogMThweDtcbiRmcy1tZWRpdW06IDIxcHg7XG4kZnMtbGFyZ2U6IDI0cHg7XG4kZnMteGw6IDI4cHg7XG4kZnMteHhsOiAzOHB4O1xuJGZzLXh4eGw6IDQycHg7XG4iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](NotFoundComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-not-found',
                            templateUrl: './not-found.component.html',
                            styleUrls: ['./not-found.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/footer/footer.component.ts":
            /*!***************************************************!*\
              !*** ./src/app/shared/footer/footer.component.ts ***!
              \***************************************************/
            /*! exports provided: FooterComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "FooterComponent", function() {
                    return FooterComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");




                class FooterComponent {
                    constructor() {
                        this.flatlogic = 'https://flatlogic.com/';
                        this.flatlogicAbout = 'https://flatlogic.com/about';
                        this.flatlogicBlog = 'https://flatlogic.com/blog';
                    }
                }
                FooterComponent.ɵfac = function FooterComponent_Factory(t) {
                    return new(t || FooterComponent)();
                };
                FooterComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: FooterComponent,
                    selectors: [
                        ["app-footer"]
                    ],
                    decls: 15,
                    vars: 3,
                    consts: [
                        [1, "footer"],
                        [1, "footer__link"],
                        [1, "footer__link-item", 3, "href"],
                        [1, "footer__icon"],
                        ["mat-mini-fab", ""],
                        ["fontSet", "fa fa-fs", "fontIcon", "fa-facebook-square"],
                        ["fontSet", "fa fa-fs", "fontIcon", "fa-twitter-square"],
                        ["fontSet", "fa fa-fs", "fontIcon", "fa-github-square"]
                    ],
                    template: function FooterComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "a", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Flatlogic");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "a", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](5, "About Us");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "a", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Blog");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](10, "mat-icon", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "mat-icon", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](14, "mat-icon", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("href", ctx.flatlogic, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("href", ctx.flatlogicAbout, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("href", ctx.flatlogicBlog, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
                        }
                    },
                    directives: [_angular_material_button__WEBPACK_IMPORTED_MODULE_1__["MatButton"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__["MatIcon"]],
                    styles: [".footer[_ngcontent-%COMP%] {\n  height: 48px;\n  margin-top: 40px;\n  width: calc(100% - 48px);\n  display: flex;\n  justify-content: space-between;\n  padding: 0 24px 24px 24px;\n}\n@media (max-width: 576px) {\n  .footer[_ngcontent-%COMP%] {\n    flex-direction: column;\n    align-items: start;\n  }\n}\n.footer__link[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n}\n@media (max-width: 576px) {\n  .footer__link[_ngcontent-%COMP%] {\n    margin-bottom: 8px;\n  }\n}\n@media (max-width: 576px) {\n  .footer__icon[_ngcontent-%COMP%] {\n    margin: 0 0 8px -14px;\n  }\n}\n.footer__link-item[_ngcontent-%COMP%] {\n  margin-right: 16px;\n  color: #536DFE;\n  text-decoration: none;\n}\n.footer__link-item[_ngcontent-%COMP%]:hover {\n  text-decoration: underline;\n}\n.mat-mini-fab[_ngcontent-%COMP%] {\n  box-shadow: none;\n  background-color: inherit;\n  width: 46px;\n  height: 46px;\n}\n.mat-mini-fab[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n.mat-icon[_ngcontent-%COMP%] {\n  color: rgba(110, 110, 110, 0.6);\n  padding: 3px 0 0 0;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2Zvb3Rlci9mb290ZXIuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMuc2NzcyIsInNyYy9hcHAvc2hhcmVkL2Zvb3Rlci9mb290ZXIuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9jb2xvcnMuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFHQTtFQUNFLFlDb0VjO0VEbkVkLGdCQUFBO0VBQ0Esd0JDbUVhO0VEbEViLGFBQUE7RUFDQSw4QkFBQTtFQUNBLHlCQUFBO0FFRkY7QUZJRTtFQVJGO0lBU0ksc0JBQUE7SUFDQSxrQkFBQTtFRURGO0FBQ0Y7QUZHRTtFQUNFLGFBQUE7RUFDQSxtQkFBQTtBRURKO0FGR0k7RUFKRjtJQUtJLGtCQUFBO0VFQUo7QUFDRjtBRklJO0VBREY7SUFFSSxxQkFBQTtFRURKO0FBQ0Y7QUZJRTtFQUNFLGtCQUFBO0VBQ0EsY0doQ0c7RUhpQ0gscUJBQUE7QUVGSjtBRklJO0VBQ0UsMEJBQUE7QUVGTjtBRk9BO0VBQ0UsZ0JBQUE7RUFDQSx5QkFBQTtFQUNBLFdBQUE7RUFDQSxZQUFBO0FFSkY7QUZNRTtFQUNFLHFDRzFCTztBRHNCWDtBRlFBO0VBQ0UsK0JHakNRO0VIa0NSLGtCQUFBO0FFTEYiLCJmaWxlIjoic3JjL2FwcC9zaGFyZWQvZm9vdGVyL2Zvb3Rlci5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2NvbG9ycyc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4uZm9vdGVyIHtcbiAgaGVpZ2h0OiAkZm9vdGVyLWhlaWdodDtcbiAgbWFyZ2luLXRvcDogNDBweDtcbiAgd2lkdGg6ICRmb290ZXItd2lkdGg7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcbiAgcGFkZGluZzogMCAyNHB4IDI0cHggMjRweDtcblxuICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAgICBhbGlnbi1pdGVtczogc3RhcnQ7XG4gIH1cblxuICAmX19saW5rIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG5cbiAgICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgICBtYXJnaW4tYm90dG9tOiA4cHg7XG4gICAgfVxuICB9XG5cbiAgJl9faWNvbiB7XG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgbWFyZ2luOiAwIDAgOHB4IC0xNHB4O1xuICAgIH1cbiAgfVxuXG4gICZfX2xpbmstaXRlbSB7XG4gICAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICAgIGNvbG9yOiAkZm9vdGVyLWxpbmstY29sb3I7XG4gICAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xuXG4gICAgJjpob3ZlciB7XG4gICAgICB0ZXh0LWRlY29yYXRpb246IHVuZGVybGluZTtcbiAgICB9XG4gIH1cbn1cblxuLm1hdC1taW5pLWZhYiB7XG4gIGJveC1zaGFkb3c6IG5vbmU7XG4gIGJhY2tncm91bmQtY29sb3I6IGluaGVyaXQ7XG4gIHdpZHRoOiA0NnB4O1xuICBoZWlnaHQ6IDQ2cHg7XG5cbiAgJjpob3ZlciB7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJGZvb3Rlci1pY29uLWJhY2tncm91bmQtY29sb3ItaG92ZXI7XG4gIH1cbn1cblxuLm1hdC1pY29uIHtcbiAgY29sb3I6ICRmb290ZXItaWNvbi1jb2xvcjtcbiAgcGFkZGluZzogM3B4IDAgMCAwO1xufVxuIiwiQGltcG9ydCBcImNvbG9yc1wiO1xuXG4vLz09IFZpZXdwb3J0c1xuXG4kZXh0cmEtc21hbGw6IDU3NnB4O1xuJHNtYWxsOiA1NzZweDtcbiRtZWRpdW06IDc2OHB4O1xuJG5vcm1hbDogMTAyNHB4O1xuJGxhcmdlOiA5OTJweDtcbiRleHRyYS1sYXJnZTogMTIwMHB4O1xuXG5cbi8vPT0gU2lkZWJhclxuXG4kc2lkZWJhci13aWR0aDogMjEwcHg7XG4kc2lkZWJhci1mb250LWNvbG9yOiAkZ3JheS0wODtcbiRzaWRlYmFyLWZvbnQtY29sb3ItYWN0aXZlOiAkZGFyay1ncmV5O1xuJHNpZGViYXItYmFja2dyb3VuZC1jb2xvci1hY3RpdmU6ICRibHVlLXdoaXRlO1xuJHNpZGViYXItYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsdWUtd2hpdGU7XG4kc2lkZWJhci1pY29uLWNvbG9yLWFjdGl2ZTogJGJsdWU7XG4kc2lkZWJhci1pY29uLWNvbG9yOiAkZ3JheS0wNjtcbiRzaWRlYmFyLXRpdGxlLWNvbG9yOiAkc2lkZWJhci1mb250LWNvbG9yO1xuJHNpZGViYXItY2lyY2xlLWNvbG9yOiAkbGlnaHQtZ3JleTtcblxuLy89PSBNYXRlcmlhbCBDYXJkXG4vL1xuXG4kY2FyZC1mb250LWNvbG9yOiAkZGFyay1ncmV5O1xuJGNhcmQtdGl0bGUtZm9udC1jb2xvcjogJGdyZXk7XG5cbi8vPT0gTWF0ZXJpYWwgVG9vbGJhclxuXG4kdG9vbGJhci10aXRsZS1mb250LWNvbG9yOiAkbGlnaHQtZ3JleTtcbiR0b29sYmFyLWJ1dHRvbi1mb250LWNvbG9yOiAkd2hpdGU7XG4kdG9vbGJhci1idXR0b24tYmFja2dyb3VuZC1jb2xvcjogJHBpbms7XG4kdG9vbGJhci1idXR0b24tYmFja2dyb3VuZC1jb2xvci1hY3RpdmU6ICRkYXJrLXBpbms7XG5cbi8vPT0gTWF0ZXJpYWwgU2lkZWJhciBDb250ZW50XG5cbiRzaWRlYmFyLWNvbnRlbnQtcGFkZGluZzogNDhweDtcblxuLy89PSBNYXRlcmlhbCBUYWJzXG5cbiR0YWJzLWhlYWRlci1mb250LWNvbG9yOiAkbGlnaHQtZ3JleTtcbiR0YWJzLWhlYWRlci1mb250LWNvbG9yLWFjdGl2ZTogJGJsdWU7XG4kdGFicy1pbmstYmFyLWNvbG9yOiAkYmx1ZTtcblxuXG4vLz09IEFwZXggQ2hhcnQgWCBheGlzIHRvb2x0aXBcblxuJGNoYXJ0LXRvb2x0aXAtYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4kY2hhcnQtdG9vbHRpcC1ib3JkZXItY29sb3I6ICRibHVlO1xuJGNoYXJ0LXRvb2x0aXAtZm9udC1jb2xvcjogJHdoaXRlO1xuXG4vLz09IFNjcm9sbCBiYXJcblxuJHNjcm9sbGJhci10cmFjay1jb2xvcjogJGxpZ2h0LWdyZXk7XG4kc2Nyb2xsYmFyLXRyYWNrLXBpZWNlLWNvbG9yOiAkd2hpdGU7XG4kc2Nyb2xsYmFyLXRodW1iLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiRzY3JvbGxiYXItY29ybmVyLWNvbG9yOiAkbGlnaHQtZ3JleTtcblxuLy89PSBIZWFkZXJcblxuJGhlYWRlci1iYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiRoZWFkZXItaGVpZ2h0OiA2NHB4O1xuJGhlYWRlci1idXR0b24tYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4kaGVhZGVyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmxhY2stMDg7XG4kaGVhZGVyLWJ1dHRvbi1mb250LWNvbG9yOiAkd2hpdGU7XG4kaGVhZGVyLXRpdGxlLWZvbnQtY29sb3I6ICR3aGl0ZTtcblxuLy89PSBGb290ZXJcblxuJGZvb3Rlci1oZWlnaHQ6IDQ4cHg7XG4kZm9vdGVyLXdpZHRoOiBjYWxjKDEwMCUgLSAjeyRzaWRlYmFyLWNvbnRlbnQtcGFkZGluZ30pO1xuJGZvb3Rlci1saW5rLWNvbG9yOiAkYmx1ZTtcbiRmb290ZXItaWNvbi1jb2xvcjogJGdyYXktMDY7XG4kZm9vdGVyLWljb24tYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsYWNrLTA4O1xuXG4vLz09IFNldHRpbmdzIG1lbnUgZWxlbWVudFxuXG4kc2V0dGluZ3MtYnV0dG9uLWJhY2tncm91bmQtY29sb3I6ICR3aGl0ZTtcbiRzZXR0aW5ncy1idXR0b24tYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsdWU7XG4kc2V0dGluZ3MtYnV0dG9uLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiRzZXR0aW5ncy1idXR0b24tY29sb3ItaG92ZXI6ICR3aGl0ZS0zNTtcbiRzZXR0aW5ncy1tZW51LWZvbnQtY29sb3I6ICRkYXJrLWdyZXk7XG4kc2V0dGluZ3MtbWVudS1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmx1ZS13aGl0ZTtcbiIsIi5mb290ZXIge1xuICBoZWlnaHQ6IDQ4cHg7XG4gIG1hcmdpbi10b3A6IDQwcHg7XG4gIHdpZHRoOiBjYWxjKDEwMCUgLSA0OHB4KTtcbiAgZGlzcGxheTogZmxleDtcbiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuO1xuICBwYWRkaW5nOiAwIDI0cHggMjRweCAyNHB4O1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5mb290ZXIge1xuICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47XG4gICAgYWxpZ24taXRlbXM6IHN0YXJ0O1xuICB9XG59XG4uZm9vdGVyX19saW5rIHtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuZm9vdGVyX19saW5rIHtcbiAgICBtYXJnaW4tYm90dG9tOiA4cHg7XG4gIH1cbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuZm9vdGVyX19pY29uIHtcbiAgICBtYXJnaW46IDAgMCA4cHggLTE0cHg7XG4gIH1cbn1cbi5mb290ZXJfX2xpbmstaXRlbSB7XG4gIG1hcmdpbi1yaWdodDogMTZweDtcbiAgY29sb3I6ICM1MzZERkU7XG4gIHRleHQtZGVjb3JhdGlvbjogbm9uZTtcbn1cbi5mb290ZXJfX2xpbmstaXRlbTpob3ZlciB7XG4gIHRleHQtZGVjb3JhdGlvbjogdW5kZXJsaW5lO1xufVxuXG4ubWF0LW1pbmktZmFiIHtcbiAgYm94LXNoYWRvdzogbm9uZTtcbiAgYmFja2dyb3VuZC1jb2xvcjogaW5oZXJpdDtcbiAgd2lkdGg6IDQ2cHg7XG4gIGhlaWdodDogNDZweDtcbn1cbi5tYXQtbWluaS1mYWI6aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xufVxuXG4ubWF0LWljb24ge1xuICBjb2xvcjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuICBwYWRkaW5nOiAzcHggMCAwIDA7XG59IiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](FooterComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-footer',
                            templateUrl: './footer.component.html',
                            styleUrls: ['./footer.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/components/email/email.component.ts":
            /*!*******************************************************************!*\
              !*** ./src/app/shared/header/components/email/email.component.ts ***!
              \*******************************************************************/
            /*! exports provided: EmailComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "EmailComponent", function() {
                    return EmailComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_badge__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/badge */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/badge.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _pipes_short_name__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! ../../pipes/short-name */ "./src/app/shared/header/pipes/short-name.ts");








                function EmailComponent_div_10_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 11);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 12);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "button", 13);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](4, "shortName");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "span", 14);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 15);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "span", 16);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "span", 17);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                    if (rf & 2) {
                        const email_r2 = ctx.$implicit;
                        const i_r3 = ctx.index;
                        const ctx_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", ctx_r1.colors[i_r3]);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](4, 5, email_r2.name));
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](email_r2.time);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](email_r2.name);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](email_r2.message);
                    }
                }
                class EmailComponent {
                    constructor() {
                        this.colors = [
                            'yellow',
                            'green',
                            'blue',
                            'ping'
                        ];
                    }
                }
                EmailComponent.ɵfac = function EmailComponent_Factory(t) {
                    return new(t || EmailComponent)();
                };
                EmailComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: EmailComponent,
                    selectors: [
                        ["app-email"]
                    ],
                    inputs: {
                        emails: "emails"
                    },
                    decls: 16,
                    vars: 3,
                    consts: [
                        ["mat-mini-fab", "", 1, "email-button", 3, "matMenuTriggerFor"],
                        ["matBadge", "4", "matBadgeColor", "accent", 1, "email-button__icon"],
                        ["xPosition", "before"],
                        ["email", "matMenu"],
                        [1, "email-menu-header"],
                        [1, "email-menu-header__title"],
                        [1, "email-menu-header__subtitle"],
                        ["class", "mail-wrapper", 4, "ngFor", "ngForOf"],
                        [1, "send-message-button-wrapper"],
                        ["mat-fab", "", 1, "send-message-button"],
                        [1, "send-message-button__icon"],
                        [1, "mail-wrapper"],
                        [1, "mail-wrapper__icon-wrapper"],
                        ["mat-mini-fab", "", 1, "mail-wrapper__icon", 3, "ngClass"],
                        [1, "mail-wrapper__time"],
                        [1, "mail-content"],
                        [1, "mail-content__user"],
                        [1, "mail-content__message"]
                    ],
                    template: function EmailComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "button", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-icon", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "mail_outline");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-menu", 2, 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "h4", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "New Messages");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "p", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](10, EmailComponent_div_10_Template, 12, 7, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "div", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "button", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](13, " Send New Message ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "mat-icon", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](15, "send");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matMenuTriggerFor", _r0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"]("", ctx.emails.length, " New Messages");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.emails);
                        }
                    },
                    directives: [_angular_material_button__WEBPACK_IMPORTED_MODULE_1__["MatButton"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["MatMenuTrigger"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIcon"], _angular_material_badge__WEBPACK_IMPORTED_MODULE_4__["MatBadge"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["_MatMenu"], _angular_common__WEBPACK_IMPORTED_MODULE_5__["NgForOf"], _angular_common__WEBPACK_IMPORTED_MODULE_5__["NgClass"]],
                    pipes: [_pipes_short_name__WEBPACK_IMPORTED_MODULE_6__["ShortNamePipe"]],
                    styles: [".email-button[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  box-shadow: none;\n  margin-left: 16px;\n}\n.email-button__icon[_ngcontent-%COMP%] {\n  color: rgba(255, 255, 255, 0.35);\n}\n.email-button[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n@media (max-width: 576px) {\n  .email-button[_ngcontent-%COMP%] {\n    margin-top: 0;\n  }\n}\n.email-menu-header[_ngcontent-%COMP%] {\n  padding: 16px 16px 0 16px;\n}\n.email-menu-header__title[_ngcontent-%COMP%] {\n  margin: 0;\n  font-weight: 400;\n  font-size: 24px;\n  color: #4A4A4A;\n}\n.email-menu-header__subtitle[_ngcontent-%COMP%] {\n  color: #ff4081;\n  font-weight: 400;\n  font-size: 14px;\n  margin: 4px 0 16px 0;\n}\n.mail-wrapper[_ngcontent-%COMP%] {\n  cursor: pointer;\n  display: flex;\n  padding: 6px 16px;\n}\n.mail-wrapper[_ngcontent-%COMP%]:hover {\n  background-color: #F3F5FF;\n}\n.mail-wrapper__icon-wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  flex-direction: column;\n}\n.mail-wrapper__icon[_ngcontent-%COMP%] {\n  font-weight: 400;\n  font-size: 14px;\n  color: white;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  box-shadow: none;\n  width: 30px;\n  height: 30px;\n}\n.mail-wrapper__time[_ngcontent-%COMP%] {\n  text-align: center;\n  color: #6E6E6E;\n  font-weight: 400;\n  font-size: 11.2px;\n}\n.mail-content[_ngcontent-%COMP%] {\n  display: flex;\n  flex-direction: column;\n  overflow: hidden;\n  padding-left: 16px;\n  justify-content: space-between;\n}\n.mail-content__user[_ngcontent-%COMP%] {\n  margin-top: 3px;\n  font-weight: 500;\n  font-size: 14px;\n  color: #4A4A4A;\n}\n.mail-content__message[_ngcontent-%COMP%] {\n  color: #6E6E6E;\n  font-weight: 14px;\n  font-size: 14px;\n  white-space: nowrap;\n  text-overflow: ellipsis;\n  overflow: hidden;\n}\n.send-message-button-wrapper[_ngcontent-%COMP%] {\n  margin: 16px 0;\n  text-align: center;\n  padding: 0 16px;\n}\n.send-message-button[_ngcontent-%COMP%] {\n  width: 224px;\n  height: 48px;\n  padding: 0 16px;\n  border-radius: 32px;\n  color: white;\n  background-color: #536DFE;\n}\n.send-message-button[_ngcontent-%COMP%]   .mat-button-wrapper[_ngcontent-%COMP%] {\n  padding: 0;\n}\n.send-message-button__icon[_ngcontent-%COMP%] {\n  color: white;\n  margin-left: 16px;\n}\n.yellow[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n}\n.green[_ngcontent-%COMP%] {\n  background-color: #3CD4A0;\n}\n.blue[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n}\n.ping[_ngcontent-%COMP%] {\n  background-color: #ff4081;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2hlYWRlci9jb21wb25lbnRzL2VtYWlsL2VtYWlsLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCJzcmMvYXBwL3NoYXJlZC9oZWFkZXIvY29tcG9uZW50cy9lbWFpbC9lbWFpbC5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFJQTtFQUNFLHlCQ0pLO0VES0wsZ0JBQUE7RUFDQSxpQkFBQTtBRUhGO0FGS0U7RUFDRSxnQ0NNTztBQ1RYO0FGTUU7RUFDRSxxQ0NTTztBQ2JYO0FGT0U7RUFiRjtJQWNJLGFBQUE7RUVKRjtBQUNGO0FGT0E7RUFDRSx5QkFBQTtBRUpGO0FGTUU7RUFDRSxTQUFBO0VBQ0EsZ0JHM0JTO0VINEJULGVHbEJPO0VIbUJQLGNDbkJRO0FDZVo7QUZPRTtFQUNFLGNDNUJHO0VENkJILGdCR2xDUztFSG1DVCxlRzdCTztFSDhCUCxvQkFBQTtBRUxKO0FGU0E7RUFDRSxlQUFBO0VBQ0EsYUFBQTtFQUNBLGlCQUFBO0FFTkY7QUZRRTtFQUNFLHlCQzFDUztBQ29DYjtBRlNFO0VBQ0UsYUFBQTtFQUNBLHNCQUFBO0FFUEo7QUZVRTtFQUNFLGdCR3ZEUztFSHdEVCxlR2xETztFSG1EUCxZQ2hESTtFRGlESixhQUFBO0VBQ0EsbUJBQUE7RUFDQSx1QkFBQTtFQUNBLGdCQUFBO0VBQ0EsV0FBQTtFQUNBLFlBQUE7QUVSSjtBRldFO0VBQ0Usa0JBQUE7RUFDQSxjQ3hERztFRHlESCxnQkdyRVM7RUhzRVQsaUJHakVJO0FEd0RSO0FGYUE7RUFDRSxhQUFBO0VBQ0Esc0JBQUE7RUFDQSxnQkFBQTtFQUNBLGtCQUFBO0VBQ0EsOEJBQUE7QUVWRjtBRllFO0VBQ0UsZUFBQTtFQUNBLGdCR2xGUTtFSG1GUixlRzlFTztFSCtFUCxjQzNFUTtBQ2lFWjtBRmFFO0VBQ0UsY0M3RUc7RUQ4RUgsaUJHcEZPO0VIcUZQLGVHckZPO0VIc0ZQLG1CQUFBO0VBQ0EsdUJBQUE7RUFDQSxnQkFBQTtBRVhKO0FGZUE7RUFDRSxjQUFBO0VBQ0Esa0JBQUE7RUFDQSxlQUFBO0FFWkY7QUZlQTtFQUNFLFlBQUE7RUFDQSxZQUFBO0VBQ0EsZUFBQTtFQUNBLG1CQUFBO0VBQ0EsWUNwR007RURxR04seUJDN0dLO0FDaUdQO0FGY0U7RUFDRSxVQUFBO0FFWko7QUZlRTtFQUNFLFlDNUdJO0VENkdKLGlCQUFBO0FFYko7QUZpQkE7RUFDRSx5QkMzSE87QUM2R1Q7QUZpQkE7RUFDRSx5QkN4SE07QUMwR1I7QUZpQkE7RUFDRSx5QkNsSUs7QUNvSFA7QUZpQkE7RUFDRSx5QkNsSUs7QUNvSFAiLCJmaWxlIjoic3JjL2FwcC9zaGFyZWQvaGVhZGVyL2NvbXBvbmVudHMvZW1haWwvZW1haWwuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvZm9udCc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4uZW1haWwtYnV0dG9uIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4gIGJveC1zaGFkb3c6IG5vbmU7XG4gIG1hcmdpbi1sZWZ0OiAxNnB4O1xuXG4gICZfX2ljb24ge1xuICAgIGNvbG9yOiAkd2hpdGUtMzU7XG4gIH1cblxuICAmOmhvdmVyIHtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmxhY2stMDg7XG4gIH1cblxuICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgbWFyZ2luLXRvcDogMDtcbiAgfVxufVxuXG4uZW1haWwtbWVudS1oZWFkZXIge1xuICBwYWRkaW5nOiAxNnB4IDE2cHggMCAxNnB4O1xuXG4gICZfX3RpdGxlIHtcbiAgICBtYXJnaW46IDA7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGZvbnQtc2l6ZTogJGZzLWxhcmdlO1xuICAgIGNvbG9yOiAkZGFyay1ncmV5O1xuICB9XG5cbiAgJl9fc3VidGl0bGUge1xuICAgIGNvbG9yOiAkcGluaztcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgbWFyZ2luOiA0cHggMCAxNnB4IDA7XG4gIH1cbn1cblxuLm1haWwtd3JhcHBlciB7XG4gIGN1cnNvcjogcG9pbnRlcjtcbiAgZGlzcGxheTogZmxleDtcbiAgcGFkZGluZzogNnB4IDE2cHg7XG5cbiAgJjpob3ZlciB7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWUtd2hpdGU7XG4gIH1cblxuICAmX19pY29uLXdyYXBwZXIge1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbiAgfVxuXG4gICZfX2ljb24ge1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcbiAgICBmb250LXNpemU6ICRmcy1zbWFsbDtcbiAgICBjb2xvcjogJHdoaXRlO1xuICAgIGRpc3BsYXk6IGZsZXg7XG4gICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjtcbiAgICBib3gtc2hhZG93OiBub25lO1xuICAgIHdpZHRoOiAzMHB4O1xuICAgIGhlaWdodDogMzBweDtcbiAgfVxuXG4gICZfX3RpbWUge1xuICAgIHRleHQtYWxpZ246IGNlbnRlcjtcbiAgICBjb2xvcjogJGdyZXk7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1saWdodGVyO1xuICAgIGZvbnQtc2l6ZTogJGZzLXhzO1xuICB9XG59XG5cbi5tYWlsLWNvbnRlbnQge1xuICBkaXNwbGF5OiBmbGV4O1xuICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICBvdmVyZmxvdzogaGlkZGVuO1xuICBwYWRkaW5nLWxlZnQ6IDE2cHg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjtcblxuICAmX191c2VyIHtcbiAgICBtYXJnaW4tdG9wOiAzcHg7XG4gICAgZm9udC13ZWlnaHQ6ICRmdy1ub3JtYWw7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgY29sb3I6ICRkYXJrLWdyZXk7XG4gIH1cblxuICAmX19tZXNzYWdlIHtcbiAgICBjb2xvcjogJGdyZXk7XG4gICAgZm9udC13ZWlnaHQ6ICRmcy1zbWFsbDtcbiAgICBmb250LXNpemU6ICRmcy1zbWFsbDtcbiAgICB3aGl0ZS1zcGFjZTogbm93cmFwO1xuICAgIHRleHQtb3ZlcmZsb3c6IGVsbGlwc2lzO1xuICAgIG92ZXJmbG93OiBoaWRkZW47XG4gIH1cbn1cblxuLnNlbmQtbWVzc2FnZS1idXR0b24td3JhcHBlciB7XG4gIG1hcmdpbjogMTZweCAwO1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gIHBhZGRpbmc6IDAgMTZweDtcbn1cblxuLnNlbmQtbWVzc2FnZS1idXR0b24ge1xuICB3aWR0aDogMjI0cHg7XG4gIGhlaWdodDogNDhweDtcbiAgcGFkZGluZzogMCAxNnB4O1xuICBib3JkZXItcmFkaXVzOiAzMnB4O1xuICBjb2xvcjogJHdoaXRlO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcblxuICAmIC5tYXQtYnV0dG9uLXdyYXBwZXIge1xuICAgIHBhZGRpbmc6IDA7XG4gIH1cblxuICAmX19pY29uIHtcbiAgICBjb2xvcjogJHdoaXRlO1xuICAgIG1hcmdpbi1sZWZ0OiAxNnB4O1xuICB9XG59XG5cbi55ZWxsb3cge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkeWVsbG93O1xufVxuXG4uZ3JlZW4ge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkZ3JlZW47XG59XG5cbi5ibHVlIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG59XG5cbi5waW5nIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJHBpbms7XG59XG4iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iLCIuZW1haWwtYnV0dG9uIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzUzNkRGRTtcbiAgYm94LXNoYWRvdzogbm9uZTtcbiAgbWFyZ2luLWxlZnQ6IDE2cHg7XG59XG4uZW1haWwtYnV0dG9uX19pY29uIHtcbiAgY29sb3I6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG59XG4uZW1haWwtYnV0dG9uOmhvdmVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogcmdiYSgwLCAwLCAwLCAwLjA4KTtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAuZW1haWwtYnV0dG9uIHtcbiAgICBtYXJnaW4tdG9wOiAwO1xuICB9XG59XG5cbi5lbWFpbC1tZW51LWhlYWRlciB7XG4gIHBhZGRpbmc6IDE2cHggMTZweCAwIDE2cHg7XG59XG4uZW1haWwtbWVudS1oZWFkZXJfX3RpdGxlIHtcbiAgbWFyZ2luOiAwO1xuICBmb250LXdlaWdodDogNDAwO1xuICBmb250LXNpemU6IDI0cHg7XG4gIGNvbG9yOiAjNEE0QTRBO1xufVxuLmVtYWlsLW1lbnUtaGVhZGVyX19zdWJ0aXRsZSB7XG4gIGNvbG9yOiAjZmY0MDgxO1xuICBmb250LXdlaWdodDogNDAwO1xuICBmb250LXNpemU6IDE0cHg7XG4gIG1hcmdpbjogNHB4IDAgMTZweCAwO1xufVxuXG4ubWFpbC13cmFwcGVyIHtcbiAgY3Vyc29yOiBwb2ludGVyO1xuICBkaXNwbGF5OiBmbGV4O1xuICBwYWRkaW5nOiA2cHggMTZweDtcbn1cbi5tYWlsLXdyYXBwZXI6aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjRjNGNUZGO1xufVxuLm1haWwtd3JhcHBlcl9faWNvbi13cmFwcGVyIHtcbiAgZGlzcGxheTogZmxleDtcbiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjtcbn1cbi5tYWlsLXdyYXBwZXJfX2ljb24ge1xuICBmb250LXdlaWdodDogNDAwO1xuICBmb250LXNpemU6IDE0cHg7XG4gIGNvbG9yOiB3aGl0ZTtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XG4gIGJveC1zaGFkb3c6IG5vbmU7XG4gIHdpZHRoOiAzMHB4O1xuICBoZWlnaHQ6IDMwcHg7XG59XG4ubWFpbC13cmFwcGVyX190aW1lIHtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICBjb2xvcjogIzZFNkU2RTtcbiAgZm9udC13ZWlnaHQ6IDQwMDtcbiAgZm9udC1zaXplOiAxMS4ycHg7XG59XG5cbi5tYWlsLWNvbnRlbnQge1xuICBkaXNwbGF5OiBmbGV4O1xuICBmbGV4LWRpcmVjdGlvbjogY29sdW1uO1xuICBvdmVyZmxvdzogaGlkZGVuO1xuICBwYWRkaW5nLWxlZnQ6IDE2cHg7XG4gIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2Vlbjtcbn1cbi5tYWlsLWNvbnRlbnRfX3VzZXIge1xuICBtYXJnaW4tdG9wOiAzcHg7XG4gIGZvbnQtd2VpZ2h0OiA1MDA7XG4gIGZvbnQtc2l6ZTogMTRweDtcbiAgY29sb3I6ICM0QTRBNEE7XG59XG4ubWFpbC1jb250ZW50X19tZXNzYWdlIHtcbiAgY29sb3I6ICM2RTZFNkU7XG4gIGZvbnQtd2VpZ2h0OiAxNHB4O1xuICBmb250LXNpemU6IDE0cHg7XG4gIHdoaXRlLXNwYWNlOiBub3dyYXA7XG4gIHRleHQtb3ZlcmZsb3c6IGVsbGlwc2lzO1xuICBvdmVyZmxvdzogaGlkZGVuO1xufVxuXG4uc2VuZC1tZXNzYWdlLWJ1dHRvbi13cmFwcGVyIHtcbiAgbWFyZ2luOiAxNnB4IDA7XG4gIHRleHQtYWxpZ246IGNlbnRlcjtcbiAgcGFkZGluZzogMCAxNnB4O1xufVxuXG4uc2VuZC1tZXNzYWdlLWJ1dHRvbiB7XG4gIHdpZHRoOiAyMjRweDtcbiAgaGVpZ2h0OiA0OHB4O1xuICBwYWRkaW5nOiAwIDE2cHg7XG4gIGJvcmRlci1yYWRpdXM6IDMycHg7XG4gIGNvbG9yOiB3aGl0ZTtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzUzNkRGRTtcbn1cbi5zZW5kLW1lc3NhZ2UtYnV0dG9uIC5tYXQtYnV0dG9uLXdyYXBwZXIge1xuICBwYWRkaW5nOiAwO1xufVxuLnNlbmQtbWVzc2FnZS1idXR0b25fX2ljb24ge1xuICBjb2xvcjogd2hpdGU7XG4gIG1hcmdpbi1sZWZ0OiAxNnB4O1xufVxuXG4ueWVsbG93IHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI2ZmYzI2MDtcbn1cblxuLmdyZWVuIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzNDRDRBMDtcbn1cblxuLmJsdWUge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNTM2REZFO1xufVxuXG4ucGluZyB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZjQwODE7XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](EmailComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-email',
                            templateUrl: './email.component.html',
                            styleUrls: ['./email.component.scss']
                        }]
                    }], null, {
                        emails: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/components/index.ts":
            /*!***************************************************!*\
              !*** ./src/app/shared/header/components/index.ts ***!
              \***************************************************/
            /*! exports provided: UserComponent, EmailComponent, NotificationsComponent, SearchComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _user_user_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./user/user.component */ "./src/app/shared/header/components/user/user.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "UserComponent", function() {
                    return _user_user_component__WEBPACK_IMPORTED_MODULE_0__["UserComponent"];
                });

                /* harmony import */
                var _email_email_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ./email/email.component */ "./src/app/shared/header/components/email/email.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "EmailComponent", function() {
                    return _email_email_component__WEBPACK_IMPORTED_MODULE_1__["EmailComponent"];
                });

                /* harmony import */
                var _notifications_notifications_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./notifications/notifications.component */ "./src/app/shared/header/components/notifications/notifications.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "NotificationsComponent", function() {
                    return _notifications_notifications_component__WEBPACK_IMPORTED_MODULE_2__["NotificationsComponent"];
                });

                /* harmony import */
                var _search_search_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ./search/search.component */ "./src/app/shared/header/components/search/search.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "SearchComponent", function() {
                    return _search_search_component__WEBPACK_IMPORTED_MODULE_3__["SearchComponent"];
                });







                /***/
            }),

        /***/
        "./src/app/shared/header/components/notifications/notifications.component.ts":
            /*!***********************************************************************************!*\
              !*** ./src/app/shared/header/components/notifications/notifications.component.ts ***!
              \***********************************************************************************/
            /*! exports provided: NotificationsComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "NotificationsComponent", function() {
                    return NotificationsComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_badge__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/badge */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/badge.js");






                class NotificationsComponent {}
                NotificationsComponent.ɵfac = function NotificationsComponent_Factory(t) {
                    return new(t || NotificationsComponent)();
                };
                NotificationsComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: NotificationsComponent,
                    selectors: [
                        ["app-notifications"]
                    ],
                    decls: 21,
                    vars: 1,
                    consts: [
                        ["mat-mini-fab", "", 1, "notification-button", 3, "matMenuTriggerFor"],
                        ["matBadge", "4", "matBadgeColor", "warn", 1, "notification-button__icon"],
                        ["xPosition", "before", 1, "notification-menu"],
                        ["bell", "matMenu"],
                        ["mat-menu-item", "", 1, "notification-menu__button"],
                        [1, "notification-menu__icon_yellow"],
                        [1, "notification-menu__icon_green"],
                        [1, "notification-menu__icon_pink"],
                        [1, "notification-menu__icon_blue"]
                    ],
                    template: function NotificationsComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "button", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-icon", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "notifications_none");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-menu", 2, 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-icon", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "local_offer");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](8, "Check out this awesome ticket ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "mat-icon", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11, "thumb_up");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, "What is the best way to get ... ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "mat-icon", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](15, "notifications_none");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, "This is just a simple notification ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "button", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "mat-icon", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](19, "local_grocery_store");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "12 new orders has arrived today ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matMenuTriggerFor", _r0);
                        }
                    },
                    directives: [_angular_material_button__WEBPACK_IMPORTED_MODULE_1__["MatButton"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["MatMenuTrigger"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIcon"], _angular_material_badge__WEBPACK_IMPORTED_MODULE_4__["MatBadge"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["_MatMenu"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["MatMenuItem"]],
                    styles: [".notification-button[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  box-shadow: none;\n  margin-left: 16px;\n}\n.notification-button__icon[_ngcontent-%COMP%] {\n  color: rgba(255, 255, 255, 0.35);\n}\n.notification-button[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n@media (max-width: 576px) {\n  .notification-button[_ngcontent-%COMP%] {\n    margin-top: 0;\n  }\n}\n.notification-menu__button[_ngcontent-%COMP%]:hover {\n  background-color: #F3F5FF;\n}\n.notification-menu__icon_yellow[_ngcontent-%COMP%] {\n  color: #ffc260;\n}\n.notification-menu__icon_green[_ngcontent-%COMP%] {\n  color: #3CD4A0;\n}\n.notification-menu__icon_pink[_ngcontent-%COMP%] {\n  color: #ff4081;\n}\n.notification-menu__icon_blue[_ngcontent-%COMP%] {\n  color: #536DFE;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2hlYWRlci9jb21wb25lbnRzL25vdGlmaWNhdGlvbnMvbm90aWZpY2F0aW9ucy5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIiwic3JjL2FwcC9zaGFyZWQvaGVhZGVyL2NvbXBvbmVudHMvbm90aWZpY2F0aW9ucy9ub3RpZmljYXRpb25zLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UseUJDSEs7RURJTCxnQkFBQTtFQUNBLGlCQUFBO0FFRkY7QUZJRTtFQUNFLGdDQ09PO0FDVFg7QUZLRTtFQUNFLHFDQ1VPO0FDYlg7QUZNRTtFQWJGO0lBY0ksYUFBQTtFRUhGO0FBQ0Y7QUZRSTtFQUNFLHlCQ3BCTztBQ2ViO0FGVUk7RUFDRSxjQzlCRztBQ3NCVDtBRldJO0VBQ0UsY0MzQkU7QUNrQlI7QUZZSTtFQUNFLGNDakNDO0FDdUJQO0FGYUk7RUFDRSxjQ3pDQztBQzhCUCIsImZpbGUiOiJzcmMvYXBwL3NoYXJlZC9oZWFkZXIvY29tcG9uZW50cy9ub3RpZmljYXRpb25zL25vdGlmaWNhdGlvbnMuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvdmFyaWFibGVzJztcblxuLm5vdGlmaWNhdGlvbi1idXR0b24ge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiAgYm94LXNoYWRvdzogbm9uZTtcbiAgbWFyZ2luLWxlZnQ6IDE2cHg7XG5cbiAgJl9faWNvbiB7XG4gICAgY29sb3I6ICR3aGl0ZS0zNTtcbiAgfVxuXG4gICY6aG92ZXIge1xuICAgIGJhY2tncm91bmQtY29sb3I6ICRibGFjay0wODtcbiAgfVxuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICBtYXJnaW4tdG9wOiAwO1xuICB9XG59XG5cbi5ub3RpZmljYXRpb24tbWVudSB7XG4gICZfX2J1dHRvbiB7XG4gICAgJjpob3ZlciB7XG4gICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZS13aGl0ZTtcbiAgICB9XG4gIH1cblxuICAmX19pY29uIHtcbiAgICAmX3llbGxvdyB7XG4gICAgICBjb2xvcjogJHllbGxvdztcbiAgICB9XG5cbiAgICAmX2dyZWVuIHtcbiAgICAgIGNvbG9yOiAkZ3JlZW47XG4gICAgfVxuXG4gICAgJl9waW5rIHtcbiAgICAgIGNvbG9yOiAkcGluaztcbiAgICB9XG5cbiAgICAmX2JsdWUge1xuICAgICAgY29sb3I6ICRibHVlO1xuICAgIH1cbiAgfVxufVxuIiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIiwiLm5vdGlmaWNhdGlvbi1idXR0b24ge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNTM2REZFO1xuICBib3gtc2hhZG93OiBub25lO1xuICBtYXJnaW4tbGVmdDogMTZweDtcbn1cbi5ub3RpZmljYXRpb24tYnV0dG9uX19pY29uIHtcbiAgY29sb3I6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG59XG4ubm90aWZpY2F0aW9uLWJ1dHRvbjpob3ZlciB7XG4gIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLm5vdGlmaWNhdGlvbi1idXR0b24ge1xuICAgIG1hcmdpbi10b3A6IDA7XG4gIH1cbn1cblxuLm5vdGlmaWNhdGlvbi1tZW51X19idXR0b246aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjRjNGNUZGO1xufVxuLm5vdGlmaWNhdGlvbi1tZW51X19pY29uX3llbGxvdyB7XG4gIGNvbG9yOiAjZmZjMjYwO1xufVxuLm5vdGlmaWNhdGlvbi1tZW51X19pY29uX2dyZWVuIHtcbiAgY29sb3I6ICMzQ0Q0QTA7XG59XG4ubm90aWZpY2F0aW9uLW1lbnVfX2ljb25fcGluayB7XG4gIGNvbG9yOiAjZmY0MDgxO1xufVxuLm5vdGlmaWNhdGlvbi1tZW51X19pY29uX2JsdWUge1xuICBjb2xvcjogIzUzNkRGRTtcbn0iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](NotificationsComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-notifications',
                            templateUrl: './notifications.component.html',
                            styleUrls: ['./notifications.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/components/search/search.component.ts":
            /*!*********************************************************************!*\
              !*** ./src/app/shared/header/components/search/search.component.ts ***!
              \*********************************************************************/
            /*! exports provided: SearchComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SearchComponent", function() {
                    return SearchComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");




                function SearchComponent_input_3_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "input", 3);
                    }
                }
                const _c0 = function(a0) {
                    return {
                        "show-search-input": a0
                    };
                };
                const _c1 = function(a0) {
                    return {
                        "open-search": a0
                    };
                };
                class SearchComponent {
                    constructor() {
                        this.isShowInput = false;
                    }
                    showInput() {
                        this.isShowInput = true;
                    }
                }
                SearchComponent.ɵfac = function SearchComponent_Factory(t) {
                    return new(t || SearchComponent)();
                };
                SearchComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: SearchComponent,
                    selectors: [
                        ["app-search"]
                    ],
                    decls: 4,
                    vars: 7,
                    consts: [
                        [1, "search", 3, "ngClass", "click"],
                        [1, "search-icon", 3, "ngClass"],
                        ["class", "search-input", "placeholder", "Search...", 4, "ngIf"],
                        ["placeholder", "Search...", 1, "search-input"]
                    ],
                    template: function SearchComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function SearchComponent_Template_div_click_0_listener() {
                                return ctx.showInput();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-icon", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "search");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](3, SearchComponent_input_3_Template, 1, 0, "input", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](3, _c0, ctx.isShowInput));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](5, _c1, ctx.isShowInput));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.isShowInput);
                        }
                    },
                    directives: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["NgClass"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__["MatIcon"], _angular_common__WEBPACK_IMPORTED_MODULE_1__["NgIf"]],
                    styles: [".search[_ngcontent-%COMP%] {\n  display: flex;\n  height: 36px;\n  border-radius: 32px;\n  box-sizing: border-box;\n  align-items: center;\n  width: 36px;\n  padding-left: 4px;\n  cursor: pointer;\n  flex-direction: row-reverse;\n}\n.search[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n@media (max-width: 576px) {\n  .search[_ngcontent-%COMP%] {\n    display: none;\n  }\n}\n.show-search-input[_ngcontent-%COMP%] {\n  -webkit-animation: 0.3s open_search;\n          animation: 0.3s open_search;\n  width: 250px;\n  padding-left: 22.4px;\n  background-color: rgba(0, 0, 0, 0.08);\n}\n.search-input[_ngcontent-%COMP%] {\n  color: white;\n  font-family: \"Roboto\", \"Helvetica\", \"Arial\", sans-serif;\n  line-height: 19px;\n  font-size: 14px;\n  background-color: transparent;\n  border: none;\n  outline: none;\n  height: 36px;\n  width: 100%;\n}\n.search-input[_ngcontent-%COMP%]::-webkit-input-placeholder {\n  color: rgba(255, 255, 255, 0.35);\n}\n.search-icon[_ngcontent-%COMP%] {\n  padding: 0 7px 3px 0;\n  color: rgba(255, 255, 255, 0.35);\n}\n.open-search[_ngcontent-%COMP%] {\n  -webkit-animation: 0.3s move_search-icon;\n          animation: 0.3s move_search-icon;\n  padding-right: 16px;\n  padding-left: 4px;\n}\n@-webkit-keyframes open_search {\n  from {\n    width: 36px;\n  }\n  to {\n    width: 250px;\n  }\n}\n@keyframes open_search {\n  from {\n    width: 36px;\n  }\n  to {\n    width: 250px;\n  }\n}\n@-webkit-keyframes open_search_large {\n  from {\n    width: 36px;\n  }\n  to {\n    width: 150px;\n  }\n}\n@keyframes open_search_large {\n  from {\n    width: 36px;\n  }\n  to {\n    width: 150px;\n  }\n}\n@-webkit-keyframes move_search-icon {\n  from {\n    padding: 0 7px 3px 0;\n  }\n  to {\n    padding-right: 16px;\n  }\n}\n@keyframes move_search-icon {\n  from {\n    padding: 0 7px 3px 0;\n  }\n  to {\n    padding-right: 16px;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2hlYWRlci9jb21wb25lbnRzL3NlYXJjaC9zZWFyY2guY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3NoYXJlZC9oZWFkZXIvY29tcG9uZW50cy9zZWFyY2gvc2VhcmNoLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxhQUFBO0VBQ0EsWUFBQTtFQUNBLG1CQUFBO0VBQ0Esc0JBQUE7RUFDQSxtQkFBQTtFQUNBLFdBQUE7RUFDQSxpQkFBQTtFQUNBLGVBQUE7RUFDQSwyQkFBQTtBQ0hGO0FES0U7RUFDRSxxQ0VPTztBRFZYO0FETUU7RUFmRjtJQWdCSSxhQUFBO0VDSEY7QUFDRjtBRE1BO0VBQ0UsbUNBQUE7VUFBQSwyQkFBQTtFQUNBLFlBQUE7RUFDQSxvQkFBQTtFQUNBLHFDRUxTO0FERVg7QURNQTtFQUNFLFlFdkJNO0VGd0JOLHVEQUFBO0VBQ0EsaUJBQUE7RUFDQSxlRzdCUztFSDhCVCw2QkFBQTtFQUNBLFlBQUE7RUFDQSxhQUFBO0VBQ0EsWUFBQTtFQUNBLFdBQUE7QUNIRjtBREtFO0VBQ0UsZ0NFM0JPO0FEd0JYO0FET0E7RUFDRSxvQkFBQTtFQUNBLGdDRWpDUztBRDZCWDtBRE9BO0VBQ0Usd0NBQUE7VUFBQSxnQ0FBQTtFQUNBLG1CQUFBO0VBQ0EsaUJBQUE7QUNKRjtBRE9BO0VBQXlCO0lBQU8sV0FBQTtFQ0Y5QjtFREU2QztJQUFLLFlBQUE7RUNDbEQ7QUFDRjtBREZBO0VBQXlCO0lBQU8sV0FBQTtFQ0Y5QjtFREU2QztJQUFLLFlBQUE7RUNDbEQ7QUFDRjtBRERBO0VBQStCO0lBQU8sV0FBQTtFQ0twQztFRExtRDtJQUFLLFlBQUE7RUNReEQ7QUFDRjtBRFRBO0VBQStCO0lBQU8sV0FBQTtFQ0twQztFRExtRDtJQUFLLFlBQUE7RUNReEQ7QUFDRjtBRFJBO0VBQThCO0lBQU8sb0JBQUE7RUNZbkM7RURaMkQ7SUFBSyxtQkFBQTtFQ2VoRTtBQUNGO0FEaEJBO0VBQThCO0lBQU8sb0JBQUE7RUNZbkM7RURaMkQ7SUFBSyxtQkFBQTtFQ2VoRTtBQUNGIiwiZmlsZSI6InNyYy9hcHAvc2hhcmVkL2hlYWRlci9jb21wb25lbnRzL3NlYXJjaC9zZWFyY2guY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvY29sb3JzXCI7XG5AaW1wb3J0IFwic3JjL2FwcC9zdHlsZXMvZm9udFwiO1xuQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlc1wiO1xuXG4uc2VhcmNoIHtcbiAgZGlzcGxheTogZmxleDtcbiAgaGVpZ2h0OiAzNnB4O1xuICBib3JkZXItcmFkaXVzOiAzMnB4O1xuICBib3gtc2l6aW5nOiBib3JkZXItYm94O1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xuICB3aWR0aDogMzZweDtcbiAgcGFkZGluZy1sZWZ0OiA0cHg7XG4gIGN1cnNvcjogcG9pbnRlcjtcbiAgZmxleC1kaXJlY3Rpb246IHJvdy1yZXZlcnNlO1xuXG4gICY6aG92ZXIge1xuICAgIGJhY2tncm91bmQtY29sb3I6ICRibGFjay0wODtcbiAgfVxuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICBkaXNwbGF5OiBub25lO1xuICB9XG59XG5cbi5zaG93LXNlYXJjaC1pbnB1dCB7XG4gIGFuaW1hdGlvbjogMC4zcyBvcGVuX3NlYXJjaDtcbiAgd2lkdGg6IDI1MHB4O1xuICBwYWRkaW5nLWxlZnQ6IDIyLjRweDtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGJsYWNrLTA4O1xufVxuXG4uc2VhcmNoLWlucHV0IHtcbiAgY29sb3I6ICR3aGl0ZTtcbiAgZm9udC1mYW1pbHk6IFwiUm9ib3RvXCIsIFwiSGVsdmV0aWNhXCIsIFwiQXJpYWxcIiwgc2Fucy1zZXJpZjtcbiAgbGluZS1oZWlnaHQ6IDE5cHg7XG4gIGZvbnQtc2l6ZTogJGZzLXNtYWxsO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiB0cmFuc3BhcmVudDtcbiAgYm9yZGVyOiBub25lO1xuICBvdXRsaW5lOiBub25lO1xuICBoZWlnaHQ6IDM2cHg7XG4gIHdpZHRoOiAxMDAlO1xuXG4gICY6Oi13ZWJraXQtaW5wdXQtcGxhY2Vob2xkZXIge1xuICAgIGNvbG9yOiAkd2hpdGUtMzU7XG4gIH1cbn1cblxuLnNlYXJjaC1pY29uIHtcbiAgcGFkZGluZzogMCA3cHggM3B4IDA7XG4gIGNvbG9yOiAkd2hpdGUtMzU7XG59XG5cbi5vcGVuLXNlYXJjaCB7XG4gIGFuaW1hdGlvbjogMC4zcyBtb3ZlX3NlYXJjaC1pY29uO1xuICBwYWRkaW5nLXJpZ2h0OiAxNnB4O1xuICBwYWRkaW5nLWxlZnQ6IDRweDtcbn1cblxuQGtleWZyYW1lcyBvcGVuX3NlYXJjaCB7IGZyb20geyB3aWR0aDogMzZweDsgfSB0byB7IHdpZHRoOiAyNTBweDsgfSAgfVxuQGtleWZyYW1lcyBvcGVuX3NlYXJjaF9sYXJnZSB7IGZyb20geyB3aWR0aDogMzZweDsgfSB0byB7IHdpZHRoOiAxNTBweDsgfSAgfVxuQGtleWZyYW1lcyBtb3ZlX3NlYXJjaC1pY29uIHsgZnJvbSB7IHBhZGRpbmc6IDAgN3B4IDNweCAwOyB9IHRvIHsgcGFkZGluZy1yaWdodDogMTZweDsgfSAgfVxuIiwiLnNlYXJjaCB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGhlaWdodDogMzZweDtcbiAgYm9yZGVyLXJhZGl1czogMzJweDtcbiAgYm94LXNpemluZzogYm9yZGVyLWJveDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbiAgd2lkdGg6IDM2cHg7XG4gIHBhZGRpbmctbGVmdDogNHB4O1xuICBjdXJzb3I6IHBvaW50ZXI7XG4gIGZsZXgtZGlyZWN0aW9uOiByb3ctcmV2ZXJzZTtcbn1cbi5zZWFyY2g6aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5zZWFyY2gge1xuICAgIGRpc3BsYXk6IG5vbmU7XG4gIH1cbn1cblxuLnNob3ctc2VhcmNoLWlucHV0IHtcbiAgYW5pbWF0aW9uOiAwLjNzIG9wZW5fc2VhcmNoO1xuICB3aWR0aDogMjUwcHg7XG4gIHBhZGRpbmctbGVmdDogMjIuNHB4O1xuICBiYWNrZ3JvdW5kLWNvbG9yOiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xufVxuXG4uc2VhcmNoLWlucHV0IHtcbiAgY29sb3I6IHdoaXRlO1xuICBmb250LWZhbWlseTogXCJSb2JvdG9cIiwgXCJIZWx2ZXRpY2FcIiwgXCJBcmlhbFwiLCBzYW5zLXNlcmlmO1xuICBsaW5lLWhlaWdodDogMTlweDtcbiAgZm9udC1zaXplOiAxNHB4O1xuICBiYWNrZ3JvdW5kLWNvbG9yOiB0cmFuc3BhcmVudDtcbiAgYm9yZGVyOiBub25lO1xuICBvdXRsaW5lOiBub25lO1xuICBoZWlnaHQ6IDM2cHg7XG4gIHdpZHRoOiAxMDAlO1xufVxuLnNlYXJjaC1pbnB1dDo6LXdlYmtpdC1pbnB1dC1wbGFjZWhvbGRlciB7XG4gIGNvbG9yOiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xufVxuXG4uc2VhcmNoLWljb24ge1xuICBwYWRkaW5nOiAwIDdweCAzcHggMDtcbiAgY29sb3I6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG59XG5cbi5vcGVuLXNlYXJjaCB7XG4gIGFuaW1hdGlvbjogMC4zcyBtb3ZlX3NlYXJjaC1pY29uO1xuICBwYWRkaW5nLXJpZ2h0OiAxNnB4O1xuICBwYWRkaW5nLWxlZnQ6IDRweDtcbn1cblxuQGtleWZyYW1lcyBvcGVuX3NlYXJjaCB7XG4gIGZyb20ge1xuICAgIHdpZHRoOiAzNnB4O1xuICB9XG4gIHRvIHtcbiAgICB3aWR0aDogMjUwcHg7XG4gIH1cbn1cbkBrZXlmcmFtZXMgb3Blbl9zZWFyY2hfbGFyZ2Uge1xuICBmcm9tIHtcbiAgICB3aWR0aDogMzZweDtcbiAgfVxuICB0byB7XG4gICAgd2lkdGg6IDE1MHB4O1xuICB9XG59XG5Aa2V5ZnJhbWVzIG1vdmVfc2VhcmNoLWljb24ge1xuICBmcm9tIHtcbiAgICBwYWRkaW5nOiAwIDdweCAzcHggMDtcbiAgfVxuICB0byB7XG4gICAgcGFkZGluZy1yaWdodDogMTZweDtcbiAgfVxufSIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIiRmdy1saWdodGVyOiA0MDA7XG4kZnctbm9ybWFsOiA1MDA7XG4kZnctYm9sZDogNjAwO1xuXG5cbiRmcy14czogMTEuMnB4O1xuJGZzLXNtYWxsOiAxNHB4O1xuJGZzLW5vcm1hbDogMTZweDtcbiRmcy1yZWd1bGFyOiAxOHB4O1xuJGZzLW1lZGl1bTogMjFweDtcbiRmcy1sYXJnZTogMjRweDtcbiRmcy14bDogMjhweDtcbiRmcy14eGw6IDM4cHg7XG4kZnMteHh4bDogNDJweDtcbiJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SearchComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-search',
                            templateUrl: './search.component.html',
                            styleUrls: ['./search.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/components/user/user.component.ts":
            /*!*****************************************************************!*\
              !*** ./src/app/shared/header/components/user/user.component.ts ***!
              \*****************************************************************/
            /*! exports provided: UserComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "UserComponent", function() {
                    return UserComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");






                class UserComponent {
                    constructor() {
                        this.signOut = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
                        this.routes = _consts__WEBPACK_IMPORTED_MODULE_1__["routes"];
                        this.flatlogicEmail = "https://flatlogic.com";
                    }
                    signOutEmit() {
                        this.signOut.emit();
                    }
                }
                UserComponent.ɵfac = function UserComponent_Factory(t) {
                    return new(t || UserComponent)();
                };
                UserComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: UserComponent,
                    selectors: [
                        ["app-user"]
                    ],
                    inputs: {
                        user: "user"
                    },
                    outputs: {
                        signOut: "signOut"
                    },
                    decls: 25,
                    vars: 4,
                    consts: [
                        ["mat-mini-fab", "", 1, "user-button", 3, "matMenuTriggerFor"],
                        [1, "user-button__icon"],
                        ["xPosition", "before"],
                        ["userMenu", "matMenu"],
                        [1, "user-menu-title"],
                        [1, "user-menu-title__name"],
                        [1, "user-menu-title__link", 3, "href"],
                        ["mat-menu-item", "", 1, "user-menu__item-title"],
                        [1, "user-menu-icon"],
                        [1, "sign-button-wrapper"],
                        ["mat-flat-button", "", 1, "sign-button", 3, "click"]
                    ],
                    template: function UserComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "button", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-icon", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "person");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-menu", 2, 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "h4", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "a", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Flatlogic.com");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "button", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "mat-icon", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, "person");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](13, "Profile ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "button", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "mat-icon", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, "description");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "Tasks ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "button", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "mat-icon", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "email");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](21, "Messages ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "div", 9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](23, "button", 10);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function UserComponent_Template_button_click_23_listener() {
                                return ctx.signOutEmit();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](24, "Sign out");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matMenuTriggerFor", _r0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate2"]("", ctx.user.name, " ", ctx.user.lastName, "");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("href", ctx.flatlogicEmail, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
                        }
                    },
                    directives: [_angular_material_button__WEBPACK_IMPORTED_MODULE_2__["MatButton"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_3__["MatMenuTrigger"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__["MatIcon"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_3__["_MatMenu"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_3__["MatMenuItem"]],
                    styles: [".user-button[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  box-shadow: none;\n  margin-left: 16px;\n}\n.user-button__icon[_ngcontent-%COMP%] {\n  color: rgba(255, 255, 255, 0.35);\n}\n.user-button[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n@media (max-width: 576px) {\n  .user-button[_ngcontent-%COMP%] {\n    margin-top: 0;\n  }\n}\n.user-menu-title[_ngcontent-%COMP%] {\n  padding: 16px 48px 0 16px;\n  margin-bottom: 4px;\n}\n.user-menu-title__name[_ngcontent-%COMP%] {\n  margin-bottom: 4px;\n  font-weight: 400;\n  font-size: 24px;\n  color: #4A4A4A;\n}\n.user-menu-title__link[_ngcontent-%COMP%] {\n  color: #536DFE;\n  font-weight: 400;\n  font-size: 14px;\n  text-decoration: none;\n}\n.user-menu-icon[_ngcontent-%COMP%] {\n  color: #B9B9B9;\n  margin-right: 16px;\n  opacity: 0.8;\n}\n.sign-button-wrapper[_ngcontent-%COMP%] {\n  text-align: center;\n  padding: 8px 0 16px 0;\n  width: 100%;\n}\n.sign-button[_ngcontent-%COMP%] {\n  border: 1px solid;\n  color: #536DFE;\n  width: 80%;\n}\n.user-menu__item-title[_ngcontent-%COMP%] {\n  color: #B9B9B9;\n}\n.user-menu__item-title[_ngcontent-%COMP%]:hover {\n  color: #4A4A4A;\n  background-color: #F3F5FF;\n}\n.user-menu__item-title[_ngcontent-%COMP%]:hover   .user-menu-icon[_ngcontent-%COMP%] {\n  color: #536DFE;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2hlYWRlci9jb21wb25lbnRzL3VzZXIvdXNlci5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIiwic3JjL2FwcC9zaGFyZWQvaGVhZGVyL2NvbXBvbmVudHMvdXNlci91c2VyLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvZm9udC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUlBO0VBQ0UseUJDSks7RURLTCxnQkFBQTtFQUNBLGlCQUFBO0FFSEY7QUZLRTtFQUNFLGdDQ01PO0FDVFg7QUZNRTtFQUNFLHFDQ1NPO0FDYlg7QUZPRTtFQWJGO0lBY0ksYUFBQTtFRUpGO0FBQ0Y7QUZPQTtFQUNFLHlCQUFBO0VBQ0Esa0JBQUE7QUVKRjtBRk1FO0VBQ0Usa0JBQUE7RUFDQSxnQkc1QlM7RUg2QlQsZUduQk87RUhvQlAsY0NwQlE7QUNnQlo7QUZPRTtFQUNFLGNDakNHO0VEa0NILGdCR25DUztFSG9DVCxlRzlCTztFSCtCUCxxQkFBQTtBRUxKO0FGU0E7RUFDRSxjQy9CVztFRGdDWCxrQkFBQTtFQUNBLFlBQUE7QUVORjtBRlNBO0VBQ0Usa0JBQUE7RUFDQSxxQkFBQTtFQUNBLFdBQUE7QUVORjtBRlNBO0VBQ0UsaUJBQUE7RUFDQSxjQ3RESztFRHVETCxVQUFBO0FFTkY7QUZVRTtFQUNFLGNDbERTO0FDMkNiO0FGU0k7RUFDRSxjQ3RETTtFRHVETix5QkM3RE87QUNzRGI7QUZTTTtFQUNFLGNBQUE7QUVQUiIsImZpbGUiOiJzcmMvYXBwL3NoYXJlZC9oZWFkZXIvY29tcG9uZW50cy91c2VyL3VzZXIuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvZm9udCc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4udXNlci1idXR0b24ge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiAgYm94LXNoYWRvdzogbm9uZTtcbiAgbWFyZ2luLWxlZnQ6IDE2cHg7XG5cbiAgJl9faWNvbiB7XG4gICAgY29sb3I6ICR3aGl0ZS0zNTtcbiAgfVxuXG4gICY6aG92ZXIge1xuICAgIGJhY2tncm91bmQtY29sb3I6ICRibGFjay0wODtcbiAgfVxuXG4gIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICBtYXJnaW4tdG9wOiAwO1xuICB9XG59XG5cbi51c2VyLW1lbnUtdGl0bGUge1xuICBwYWRkaW5nOiAxNnB4IDQ4cHggMCAxNnB4O1xuICBtYXJnaW4tYm90dG9tOiA0cHg7XG5cbiAgJl9fbmFtZSB7XG4gICAgbWFyZ2luLWJvdHRvbTogNHB4O1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcbiAgICBmb250LXNpemU6ICRmcy1sYXJnZTtcbiAgICBjb2xvcjogJGRhcmstZ3JleTtcbiAgfVxuXG4gICZfX2xpbmsge1xuICAgIGNvbG9yOiAkYmx1ZTtcbiAgICBmb250LXdlaWdodDogJGZ3LWxpZ2h0ZXI7XG4gICAgZm9udC1zaXplOiAkZnMtc21hbGw7XG4gICAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xuICB9XG59XG5cbi51c2VyLW1lbnUtaWNvbiB7XG4gIGNvbG9yOiAkbGlnaHQtZ3JleTtcbiAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICBvcGFjaXR5OiAuODtcbn1cblxuLnNpZ24tYnV0dG9uLXdyYXBwZXIge1xuICB0ZXh0LWFsaWduOiBjZW50ZXI7XG4gIHBhZGRpbmc6IDhweCAwIDE2cHggMDtcbiAgd2lkdGg6IDEwMCU7XG59XG5cbi5zaWduLWJ1dHRvbiB7XG4gIGJvcmRlcjogMXB4IHNvbGlkO1xuICBjb2xvcjogJGJsdWU7XG4gIHdpZHRoOiA4MCU7XG59XG5cbi51c2VyLW1lbnUge1xuICAmX19pdGVtLXRpdGxlIHtcbiAgICBjb2xvcjogJGxpZ2h0LWdyZXk7XG5cbiAgICAmOmhvdmVyIHtcbiAgICAgIGNvbG9yOiAkZGFyay1ncmV5O1xuICAgICAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWUtd2hpdGU7XG5cbiAgICAgICYgLnVzZXItbWVudS1pY29uIHtcbiAgICAgICAgY29sb3I6ICM1MzZERkU7XG4gICAgICB9XG4gICAgfVxuICB9XG59XG4iLCIkeWVsbG93OiAjZmZjMjYwO1xuJGJsdWU6ICM1MzZERkU7XG4kbGlnaHQtYmx1ZTogIzc5OERGRTtcbiR3aGl0ZS1ibHVlOiAjQjFCQ0ZGO1xuJGJsdWUtd2hpdGU6ICNGM0Y1RkY7XG4kcGluazogI2ZmNDA4MTtcbiRkYXJrLXBpbms6ICNmZjBmNjA7XG4kZ3JlZW46ICMzQ0Q0QTA7XG4kdmlvbGV0OiAjOTAxM0ZFO1xuJHdoaXRlOiB3aGl0ZTtcbiRkYXJrLWdyZXk6ICM0QTRBNEE7XG4kbGlnaHQtZ3JleTogI0I5QjlCOTtcbiRncmV5OiAjNkU2RTZFO1xuJHNreTogI2MwY2FmZjtcblxuXG4kd2hpdGUtMzU6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG4kd2hpdGUtODA6ICNGRkZGRkY4MDtcblxuJGdyYXktMDg6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiRncmF5LTgwOiAjRDhEOEQ4ODA7XG4kZ3JheS0wNjogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjYpO1xuXG4kYmxhY2stMDg6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG5cbiRwaW5rLTE1OiByZ2JhKDI1NSwgOTIsIDE0NywgMC4xNSk7XG4kYmx1ZS0xNTogcmdiYSg4MywgMTA5LCAyNTQsIDAuMTUpO1xuJGdyZWVuLTE1OiByZ2JhKDYwLCAyMTIsIDE2MCwgMC4xNSk7XG4keWVsbG93LTE1OiByZ2JhKDI1NSwgMTk0LCA5NiwgMC4xNSk7XG4kdmlvbGV0LTE1OiByZ2JhKDE0NCwgMTksIDI1NCwgMC4xNSk7XG5cblxuJHNoYWRvdy13aGl0ZTogI0U4RUFGQztcbiRzaGFkb3ctZ3JleTogI0IyQjJCMjFBO1xuJHNoYWRvdy1kYXJrLWdyZXk6ICM5QTlBOUExQTtcblxuJGJhY2tncm91bmQtY29sb3I6ICNGNkY3RkY7XG4iLCIudXNlci1idXR0b24ge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNTM2REZFO1xuICBib3gtc2hhZG93OiBub25lO1xuICBtYXJnaW4tbGVmdDogMTZweDtcbn1cbi51c2VyLWJ1dHRvbl9faWNvbiB7XG4gIGNvbG9yOiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xufVxuLnVzZXItYnV0dG9uOmhvdmVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogcmdiYSgwLCAwLCAwLCAwLjA4KTtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAudXNlci1idXR0b24ge1xuICAgIG1hcmdpbi10b3A6IDA7XG4gIH1cbn1cblxuLnVzZXItbWVudS10aXRsZSB7XG4gIHBhZGRpbmc6IDE2cHggNDhweCAwIDE2cHg7XG4gIG1hcmdpbi1ib3R0b206IDRweDtcbn1cbi51c2VyLW1lbnUtdGl0bGVfX25hbWUge1xuICBtYXJnaW4tYm90dG9tOiA0cHg7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMjRweDtcbiAgY29sb3I6ICM0QTRBNEE7XG59XG4udXNlci1tZW51LXRpdGxlX19saW5rIHtcbiAgY29sb3I6ICM1MzZERkU7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG4gIGZvbnQtc2l6ZTogMTRweDtcbiAgdGV4dC1kZWNvcmF0aW9uOiBub25lO1xufVxuXG4udXNlci1tZW51LWljb24ge1xuICBjb2xvcjogI0I5QjlCOTtcbiAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICBvcGFjaXR5OiAwLjg7XG59XG5cbi5zaWduLWJ1dHRvbi13cmFwcGVyIHtcbiAgdGV4dC1hbGlnbjogY2VudGVyO1xuICBwYWRkaW5nOiA4cHggMCAxNnB4IDA7XG4gIHdpZHRoOiAxMDAlO1xufVxuXG4uc2lnbi1idXR0b24ge1xuICBib3JkZXI6IDFweCBzb2xpZDtcbiAgY29sb3I6ICM1MzZERkU7XG4gIHdpZHRoOiA4MCU7XG59XG5cbi51c2VyLW1lbnVfX2l0ZW0tdGl0bGUge1xuICBjb2xvcjogI0I5QjlCOTtcbn1cbi51c2VyLW1lbnVfX2l0ZW0tdGl0bGU6aG92ZXIge1xuICBjb2xvcjogIzRBNEE0QTtcbiAgYmFja2dyb3VuZC1jb2xvcjogI0YzRjVGRjtcbn1cbi51c2VyLW1lbnVfX2l0ZW0tdGl0bGU6aG92ZXIgLnVzZXItbWVudS1pY29uIHtcbiAgY29sb3I6ICM1MzZERkU7XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](UserComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-user',
                            templateUrl: './user.component.html',
                            styleUrls: ['./user.component.scss']
                        }]
                    }], null, {
                        user: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }],
                        signOut: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/containers/header/header.component.ts":
            /*!*********************************************************************!*\
              !*** ./src/app/shared/header/containers/header/header.component.ts ***!
              \*********************************************************************/
            /*! exports provided: HeaderComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() {
                    return HeaderComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../../../consts */ "./src/app/consts/index.ts");
                /* harmony import */
                var _pages_auth_services__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../../../../pages/auth/services */ "./src/app/pages/auth/services/index.ts");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _components_search_search_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! ../../components/search/search.component */ "./src/app/shared/header/components/search/search.component.ts");
                /* harmony import */
                var _components_notifications_notifications_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! ../../components/notifications/notifications.component */ "./src/app/shared/header/components/notifications/notifications.component.ts");
                /* harmony import */
                var _components_email_email_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! ../../components/email/email.component */ "./src/app/shared/header/components/email/email.component.ts");
                /* harmony import */
                var _components_user_user_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ../../components/user/user.component */ "./src/app/shared/header/components/user/user.component.ts");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");













                function HeaderComponent_mat_icon_3_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-icon", 9);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "menu");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }

                function HeaderComponent_mat_icon_4_Template(rf, ctx) {
                    if (rf & 1) {
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-icon", 9);
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "arrow_back");
                        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                    }
                }
                class HeaderComponent {
                    constructor(userService, emailService, router) {
                        this.userService = userService;
                        this.emailService = emailService;
                        this.router = router;
                        this.isShowSidebar = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
                        this.routers = _consts__WEBPACK_IMPORTED_MODULE_1__["routes"];
                        this.user$ = this.userService.getUser();
                        this.emails$ = this.emailService.loadEmails();
                    }
                    openMenu() {
                        this.isMenuOpened = !this.isMenuOpened;
                        this.isShowSidebar.emit(this.isMenuOpened);
                    }
                    signOut() {
                        this.userService.signOut();
                        this.router.navigate([this.routers.LOGIN]);
                    }
                }
                HeaderComponent.ɵfac = function HeaderComponent_Factory(t) {
                    return new(t || HeaderComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_pages_auth_services__WEBPACK_IMPORTED_MODULE_2__["AuthService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_pages_auth_services__WEBPACK_IMPORTED_MODULE_2__["EmailService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]));
                };
                HeaderComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: HeaderComponent,
                    selectors: [
                        ["app-header"]
                    ],
                    inputs: {
                        isMenuOpened: "isMenuOpened"
                    },
                    outputs: {
                        isShowSidebar: "isShowSidebar"
                    },
                    decls: 16,
                    vars: 8,
                    consts: [
                        [1, "header"],
                        [1, "header__title"],
                        ["mat-mini-fab", "", 1, "header__title-button", 3, "click"],
                        ["class", "header__title-button-icon", 4, "ngIf"],
                        [1, "header__title-text"],
                        [1, "header-toolbar"],
                        ["mat-stroked-button", "", "color", "error", "href", "https://flatlogic.com/templates/angular-material-admin-full/demo", "target", "_blank", 1, "unlock-button"],
                        [3, "emails"],
                        [3, "user", "signOut"],
                        [1, "header__title-button-icon"]
                    ],
                    template: function HeaderComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-toolbar", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "button", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function HeaderComponent_Template_button_click_2_listener() {
                                return ctx.openMenu();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](3, HeaderComponent_mat_icon_3_Template, 2, 0, "mat-icon", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](4, HeaderComponent_mat_icon_4_Template, 2, 0, "mat-icon", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "h6", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, "Angular Material Admin");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "a", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Unlock Full Version");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](10, "app-search");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](11, "app-notifications");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "app-email", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](13, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "app-user", 8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("signOut", function HeaderComponent_Template_app_user_signOut_14_listener() {
                                return ctx.signOut();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](15, "async");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", !ctx.isMenuOpened);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.isMenuOpened);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](8);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("emails", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](13, 4, ctx.emails$));
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("user", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](15, 6, ctx.user$));
                        }
                    },
                    directives: [_angular_material_toolbar__WEBPACK_IMPORTED_MODULE_4__["MatToolbar"], _angular_material_button__WEBPACK_IMPORTED_MODULE_5__["MatButton"], _angular_common__WEBPACK_IMPORTED_MODULE_6__["NgIf"], _angular_material_button__WEBPACK_IMPORTED_MODULE_5__["MatAnchor"], _components_search_search_component__WEBPACK_IMPORTED_MODULE_7__["SearchComponent"], _components_notifications_notifications_component__WEBPACK_IMPORTED_MODULE_8__["NotificationsComponent"], _components_email_email_component__WEBPACK_IMPORTED_MODULE_9__["EmailComponent"], _components_user_user_component__WEBPACK_IMPORTED_MODULE_10__["UserComponent"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_11__["MatIcon"]],
                    pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_6__["AsyncPipe"]],
                    styles: [".header[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  display: flex;\n  justify-content: space-between;\n  position: fixed;\n  z-index: 2;\n  height: 64px;\n}\n.header__title[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n}\n.header__title-button[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n  box-shadow: none;\n}\n.header__title-button[_ngcontent-%COMP%]:hover {\n  background-color: rgba(0, 0, 0, 0.08);\n}\n@media (max-width: 576px) {\n  .header__title-button[_ngcontent-%COMP%] {\n    margin-top: 0;\n  }\n}\n.header__title-button-icon[_ngcontent-%COMP%] {\n  color: white;\n}\n.header__title-text[_ngcontent-%COMP%] {\n  color: white;\n  margin-left: 32px;\n  font-weight: 400;\n}\n@media (max-width: 576px) {\n  .header__title-text[_ngcontent-%COMP%] {\n    display: none;\n  }\n}\n.header-toolbar[_ngcontent-%COMP%] {\n  display: flex;\n  align-items: center;\n}\n.header-toolbar[_ngcontent-%COMP%]   .unlock-button[_ngcontent-%COMP%] {\n  border-color: #ff4081;\n  margin-right: 16px;\n  text-transform: uppercase;\n  letter-spacing: 0.0892857143em;\n}\n@media (max-width: 576px) {\n  .header-toolbar[_ngcontent-%COMP%]   .unlock-button[_ngcontent-%COMP%] {\n    display: none;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2hlYWRlci9jb250YWluZXJzL2hlYWRlci9oZWFkZXIuY29tcG9uZW50LnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9jb2xvcnMuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlcy5zY3NzIiwic3JjL2FwcC9zaGFyZWQvaGVhZGVyL2NvbnRhaW5lcnMvaGVhZGVyL2hlYWRlci5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2ZvbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFJQTtFQUNFLHlCQ0pLO0VES0wsYUFBQTtFQUNBLDhCQUFBO0VBQ0EsZUFBQTtFQUNBLFVBQUE7RUFDQSxZRXNEYztBQ3pEaEI7QUhLRTtFQUNFLGFBQUE7RUFDQSxtQkFBQTtBR0hKO0FITUU7RUFDRSx5QkNqQkc7RURrQkgsZ0JBQUE7QUdKSjtBSE1JO0VBQ0UscUNDQ0s7QUVMWDtBSE9JO0VBUkY7SUFTSSxhQUFBO0VHSko7QUFDRjtBSE9FO0VBQ0UsWUN0Qkk7QUVpQlI7QUhRRTtFQUNFLFlDMUJJO0VEMkJKLGlCQUFBO0VBQ0EsZ0JJckNTO0FEK0JiO0FIUUk7RUFMRjtJQU1JLGFBQUE7RUdMSjtBQUNGO0FIU0E7RUFDRSxhQUFBO0VBQ0EsbUJBQUE7QUdORjtBSFFFO0VBQ0UscUJDN0NHO0VEOENILGtCQUFBO0VBQ0EseUJBQUE7RUFFQSw4QkFBQTtBR1BKO0FIUUk7RUFORjtJQU9JLGFBQUE7RUdMSjtBQUNGIiwiZmlsZSI6InNyYy9hcHAvc2hhcmVkL2hlYWRlci9jb250YWluZXJzL2hlYWRlci9oZWFkZXIuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvZm9udCc7XG5AaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXMnO1xuXG4uaGVhZGVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogJGhlYWRlci1iYWNrZ3JvdW5kLWNvbG9yO1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gIHBvc2l0aW9uOiBmaXhlZDtcbiAgei1pbmRleDogMjtcbiAgaGVpZ2h0OiAkaGVhZGVyLWhlaWdodDtcblxuICAmX190aXRsZSB7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xuICB9XG5cbiAgJl9fdGl0bGUtYnV0dG9uIHtcbiAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkaGVhZGVyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yO1xuICAgIGJveC1zaGFkb3c6IG5vbmU7XG5cbiAgICAmOmhvdmVyIHtcbiAgICAgIGJhY2tncm91bmQtY29sb3I6ICRoZWFkZXItYnV0dG9uLWJhY2tncm91bmQtY29sb3ItaG92ZXI7XG4gICAgfVxuXG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgbWFyZ2luLXRvcDogMDtcbiAgICB9XG4gIH1cblxuICAmX190aXRsZS1idXR0b24taWNvbiB7XG4gICAgY29sb3I6ICRoZWFkZXItYnV0dG9uLWZvbnQtY29sb3I7XG4gIH1cblxuICAmX190aXRsZS10ZXh0IHtcbiAgICBjb2xvcjogJGhlYWRlci10aXRsZS1mb250LWNvbG9yO1xuICAgIG1hcmdpbi1sZWZ0OiAzMnB4O1xuICAgIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcblxuICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgIGRpc3BsYXk6IG5vbmU7XG4gICAgfVxuICB9XG59XG5cbi5oZWFkZXItdG9vbGJhciB7XG4gIGRpc3BsYXk6IGZsZXg7XG4gIGFsaWduLWl0ZW1zOiBjZW50ZXI7XG5cbiAgLnVubG9jay1idXR0b24ge1xuICAgIGJvcmRlci1jb2xvcjogJHBpbms7XG4gICAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICAgIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG5cbiAgICBsZXR0ZXItc3BhY2luZzogLjA4OTI4NTcxNDNlbTtcbiAgICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgICBkaXNwbGF5OiBub25lO1xuICAgIH1cbiAgfVxufVxuIiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIiwiQGltcG9ydCBcImNvbG9yc1wiO1xuXG4vLz09IFZpZXdwb3J0c1xuXG4kZXh0cmEtc21hbGw6IDU3NnB4O1xuJHNtYWxsOiA1NzZweDtcbiRtZWRpdW06IDc2OHB4O1xuJG5vcm1hbDogMTAyNHB4O1xuJGxhcmdlOiA5OTJweDtcbiRleHRyYS1sYXJnZTogMTIwMHB4O1xuXG5cbi8vPT0gU2lkZWJhclxuXG4kc2lkZWJhci13aWR0aDogMjEwcHg7XG4kc2lkZWJhci1mb250LWNvbG9yOiAkZ3JheS0wODtcbiRzaWRlYmFyLWZvbnQtY29sb3ItYWN0aXZlOiAkZGFyay1ncmV5O1xuJHNpZGViYXItYmFja2dyb3VuZC1jb2xvci1hY3RpdmU6ICRibHVlLXdoaXRlO1xuJHNpZGViYXItYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsdWUtd2hpdGU7XG4kc2lkZWJhci1pY29uLWNvbG9yLWFjdGl2ZTogJGJsdWU7XG4kc2lkZWJhci1pY29uLWNvbG9yOiAkZ3JheS0wNjtcbiRzaWRlYmFyLXRpdGxlLWNvbG9yOiAkc2lkZWJhci1mb250LWNvbG9yO1xuJHNpZGViYXItY2lyY2xlLWNvbG9yOiAkbGlnaHQtZ3JleTtcblxuLy89PSBNYXRlcmlhbCBDYXJkXG4vL1xuXG4kY2FyZC1mb250LWNvbG9yOiAkZGFyay1ncmV5O1xuJGNhcmQtdGl0bGUtZm9udC1jb2xvcjogJGdyZXk7XG5cbi8vPT0gTWF0ZXJpYWwgVG9vbGJhclxuXG4kdG9vbGJhci10aXRsZS1mb250LWNvbG9yOiAkbGlnaHQtZ3JleTtcbiR0b29sYmFyLWJ1dHRvbi1mb250LWNvbG9yOiAkd2hpdGU7XG4kdG9vbGJhci1idXR0b24tYmFja2dyb3VuZC1jb2xvcjogJHBpbms7XG4kdG9vbGJhci1idXR0b24tYmFja2dyb3VuZC1jb2xvci1hY3RpdmU6ICRkYXJrLXBpbms7XG5cbi8vPT0gTWF0ZXJpYWwgU2lkZWJhciBDb250ZW50XG5cbiRzaWRlYmFyLWNvbnRlbnQtcGFkZGluZzogNDhweDtcblxuLy89PSBNYXRlcmlhbCBUYWJzXG5cbiR0YWJzLWhlYWRlci1mb250LWNvbG9yOiAkbGlnaHQtZ3JleTtcbiR0YWJzLWhlYWRlci1mb250LWNvbG9yLWFjdGl2ZTogJGJsdWU7XG4kdGFicy1pbmstYmFyLWNvbG9yOiAkYmx1ZTtcblxuXG4vLz09IEFwZXggQ2hhcnQgWCBheGlzIHRvb2x0aXBcblxuJGNoYXJ0LXRvb2x0aXAtYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4kY2hhcnQtdG9vbHRpcC1ib3JkZXItY29sb3I6ICRibHVlO1xuJGNoYXJ0LXRvb2x0aXAtZm9udC1jb2xvcjogJHdoaXRlO1xuXG4vLz09IFNjcm9sbCBiYXJcblxuJHNjcm9sbGJhci10cmFjay1jb2xvcjogJGxpZ2h0LWdyZXk7XG4kc2Nyb2xsYmFyLXRyYWNrLXBpZWNlLWNvbG9yOiAkd2hpdGU7XG4kc2Nyb2xsYmFyLXRodW1iLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiRzY3JvbGxiYXItY29ybmVyLWNvbG9yOiAkbGlnaHQtZ3JleTtcblxuLy89PSBIZWFkZXJcblxuJGhlYWRlci1iYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiRoZWFkZXItaGVpZ2h0OiA2NHB4O1xuJGhlYWRlci1idXR0b24tYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4kaGVhZGVyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmxhY2stMDg7XG4kaGVhZGVyLWJ1dHRvbi1mb250LWNvbG9yOiAkd2hpdGU7XG4kaGVhZGVyLXRpdGxlLWZvbnQtY29sb3I6ICR3aGl0ZTtcblxuLy89PSBGb290ZXJcblxuJGZvb3Rlci1oZWlnaHQ6IDQ4cHg7XG4kZm9vdGVyLXdpZHRoOiBjYWxjKDEwMCUgLSAjeyRzaWRlYmFyLWNvbnRlbnQtcGFkZGluZ30pO1xuJGZvb3Rlci1saW5rLWNvbG9yOiAkYmx1ZTtcbiRmb290ZXItaWNvbi1jb2xvcjogJGdyYXktMDY7XG4kZm9vdGVyLWljb24tYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsYWNrLTA4O1xuXG4vLz09IFNldHRpbmdzIG1lbnUgZWxlbWVudFxuXG4kc2V0dGluZ3MtYnV0dG9uLWJhY2tncm91bmQtY29sb3I6ICR3aGl0ZTtcbiRzZXR0aW5ncy1idXR0b24tYmFja2dyb3VuZC1jb2xvci1ob3ZlcjogJGJsdWU7XG4kc2V0dGluZ3MtYnV0dG9uLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiRzZXR0aW5ncy1idXR0b24tY29sb3ItaG92ZXI6ICR3aGl0ZS0zNTtcbiRzZXR0aW5ncy1tZW51LWZvbnQtY29sb3I6ICRkYXJrLWdyZXk7XG4kc2V0dGluZ3MtbWVudS1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmx1ZS13aGl0ZTtcbiIsIi5oZWFkZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNTM2REZFO1xuICBkaXNwbGF5OiBmbGV4O1xuICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47XG4gIHBvc2l0aW9uOiBmaXhlZDtcbiAgei1pbmRleDogMjtcbiAgaGVpZ2h0OiA2NHB4O1xufVxuLmhlYWRlcl9fdGl0bGUge1xuICBkaXNwbGF5OiBmbGV4O1xuICBhbGlnbi1pdGVtczogY2VudGVyO1xufVxuLmhlYWRlcl9fdGl0bGUtYnV0dG9uIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzUzNkRGRTtcbiAgYm94LXNoYWRvdzogbm9uZTtcbn1cbi5oZWFkZXJfX3RpdGxlLWJ1dHRvbjpob3ZlciB7XG4gIGJhY2tncm91bmQtY29sb3I6IHJnYmEoMCwgMCwgMCwgMC4wOCk7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmhlYWRlcl9fdGl0bGUtYnV0dG9uIHtcbiAgICBtYXJnaW4tdG9wOiAwO1xuICB9XG59XG4uaGVhZGVyX190aXRsZS1idXR0b24taWNvbiB7XG4gIGNvbG9yOiB3aGl0ZTtcbn1cbi5oZWFkZXJfX3RpdGxlLXRleHQge1xuICBjb2xvcjogd2hpdGU7XG4gIG1hcmdpbi1sZWZ0OiAzMnB4O1xuICBmb250LXdlaWdodDogNDAwO1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC5oZWFkZXJfX3RpdGxlLXRleHQge1xuICAgIGRpc3BsYXk6IG5vbmU7XG4gIH1cbn1cblxuLmhlYWRlci10b29sYmFyIHtcbiAgZGlzcGxheTogZmxleDtcbiAgYWxpZ24taXRlbXM6IGNlbnRlcjtcbn1cbi5oZWFkZXItdG9vbGJhciAudW5sb2NrLWJ1dHRvbiB7XG4gIGJvcmRlci1jb2xvcjogI2ZmNDA4MTtcbiAgbWFyZ2luLXJpZ2h0OiAxNnB4O1xuICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlO1xuICBsZXR0ZXItc3BhY2luZzogMC4wODkyODU3MTQzZW07XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmhlYWRlci10b29sYmFyIC51bmxvY2stYnV0dG9uIHtcbiAgICBkaXNwbGF5OiBub25lO1xuICB9XG59IiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](HeaderComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-header',
                            templateUrl: './header.component.html',
                            styleUrls: ['./header.component.scss']
                        }]
                    }], function() {
                        return [{
                            type: _pages_auth_services__WEBPACK_IMPORTED_MODULE_2__["AuthService"]
                        }, {
                            type: _pages_auth_services__WEBPACK_IMPORTED_MODULE_2__["EmailService"]
                        }, {
                            type: _angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]
                        }];
                    }, {
                        isMenuOpened: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
                        }],
                        isShowSidebar: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/containers/index.ts":
            /*!***************************************************!*\
              !*** ./src/app/shared/header/containers/index.ts ***!
              \***************************************************/
            /*! exports provided: HeaderComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _header_header_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./header/header.component */ "./src/app/shared/header/containers/header/header.component.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "HeaderComponent", function() {
                    return _header_header_component__WEBPACK_IMPORTED_MODULE_0__["HeaderComponent"];
                });




                /***/
            }),

        /***/
        "./src/app/shared/header/header.module.ts":
            /*!************************************************!*\
              !*** ./src/app/shared/header/header.module.ts ***!
              \************************************************/
            /*! exports provided: HeaderModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "HeaderModule", function() {
                    return HeaderModule;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/toolbar */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */
                var _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/form-field */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/form-field.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_input__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/input */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/input.js");
                /* harmony import */
                var _angular_material_badge__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/material/badge */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/badge.js");
                /* harmony import */
                var _containers__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! ./containers */ "./src/app/shared/header/containers/index.ts");
                /* harmony import */
                var _components__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ./components */ "./src/app/shared/header/components/index.ts");
                /* harmony import */
                var _components_notifications_notifications_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ./components/notifications/notifications.component */ "./src/app/shared/header/components/notifications/notifications.component.ts");
                /* harmony import */
                var _components_search_search_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! ./components/search/search.component */ "./src/app/shared/header/components/search/search.component.ts");
                /* harmony import */
                var _pipes__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! ./pipes */ "./src/app/shared/header/pipes/index.ts");















                class HeaderModule {}
                HeaderModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: HeaderModule
                });
                HeaderModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function HeaderModule_Factory(t) {
                        return new(t || HeaderModule)();
                    },
                    imports: [
                        [
                            _angular_common__WEBPACK_IMPORTED_MODULE_3__["CommonModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_1__["MatToolbarModule"],
                            _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__["MatFormFieldModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_5__["MatMenuModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_7__["MatInputModule"],
                            _angular_material_badge__WEBPACK_IMPORTED_MODULE_8__["MatBadgeModule"]
                        ]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](HeaderModule, {
                        declarations: [_containers__WEBPACK_IMPORTED_MODULE_9__["HeaderComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_10__["UserComponent"],
                            _components__WEBPACK_IMPORTED_MODULE_10__["EmailComponent"],
                            _components_notifications_notifications_component__WEBPACK_IMPORTED_MODULE_11__["NotificationsComponent"],
                            _components_search_search_component__WEBPACK_IMPORTED_MODULE_12__["SearchComponent"],
                            _pipes__WEBPACK_IMPORTED_MODULE_13__["ShortNamePipe"]
                        ],
                        imports: [_angular_common__WEBPACK_IMPORTED_MODULE_3__["CommonModule"],
                            _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_1__["MatToolbarModule"],
                            _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__["MatFormFieldModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__["MatIconModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_5__["MatMenuModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                            _angular_material_input__WEBPACK_IMPORTED_MODULE_7__["MatInputModule"],
                            _angular_material_badge__WEBPACK_IMPORTED_MODULE_8__["MatBadgeModule"]
                        ],
                        exports: [_containers__WEBPACK_IMPORTED_MODULE_9__["HeaderComponent"]]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](HeaderModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [
                                _containers__WEBPACK_IMPORTED_MODULE_9__["HeaderComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_10__["UserComponent"],
                                _components__WEBPACK_IMPORTED_MODULE_10__["EmailComponent"],
                                _components_notifications_notifications_component__WEBPACK_IMPORTED_MODULE_11__["NotificationsComponent"],
                                _components_search_search_component__WEBPACK_IMPORTED_MODULE_12__["SearchComponent"],
                                _pipes__WEBPACK_IMPORTED_MODULE_13__["ShortNamePipe"]
                            ],
                            exports: [
                                _containers__WEBPACK_IMPORTED_MODULE_9__["HeaderComponent"]
                            ],
                            imports: [
                                _angular_common__WEBPACK_IMPORTED_MODULE_3__["CommonModule"],
                                _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_1__["MatToolbarModule"],
                                _angular_material_form_field__WEBPACK_IMPORTED_MODULE_2__["MatFormFieldModule"],
                                _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__["MatIconModule"],
                                _angular_material_menu__WEBPACK_IMPORTED_MODULE_5__["MatMenuModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_6__["MatButtonModule"],
                                _angular_material_input__WEBPACK_IMPORTED_MODULE_7__["MatInputModule"],
                                _angular_material_badge__WEBPACK_IMPORTED_MODULE_8__["MatBadgeModule"]
                            ]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/header/pipes/index.ts":
            /*!**********************************************!*\
              !*** ./src/app/shared/header/pipes/index.ts ***!
              \**********************************************/
            /*! exports provided: ShortNamePipe */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _short_name__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! ./short-name */ "./src/app/shared/header/pipes/short-name.ts");
                /* harmony reexport (safe) */
                __webpack_require__.d(__webpack_exports__, "ShortNamePipe", function() {
                    return _short_name__WEBPACK_IMPORTED_MODULE_0__["ShortNamePipe"];
                });




                /***/
            }),

        /***/
        "./src/app/shared/header/pipes/short-name.ts":
            /*!***************************************************!*\
              !*** ./src/app/shared/header/pipes/short-name.ts ***!
              \***************************************************/
            /*! exports provided: ShortNamePipe */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "ShortNamePipe", function() {
                    return ShortNamePipe;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");


                class ShortNamePipe {
                    transform(value) {
                        const commaIndex = value.search('\\s');
                        return '' + value[0].toUpperCase() + value[commaIndex + 1].toUpperCase();
                    }
                }
                ShortNamePipe.ɵfac = function ShortNamePipe_Factory(t) {
                    return new(t || ShortNamePipe)();
                };
                ShortNamePipe.ɵpipe = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefinePipe"]({
                    name: "shortName",
                    type: ShortNamePipe,
                    pure: true
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](ShortNamePipe, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Pipe"],
                        args: [{
                            name: 'shortName'
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/layout/layout.component.ts":
            /*!***************************************************!*\
              !*** ./src/app/shared/layout/layout.component.ts ***!
              \***************************************************/
            /*! exports provided: LayoutComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "LayoutComponent", function() {
                    return LayoutComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_cdk_layout__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/cdk/layout */ "./node_modules/@angular/cdk/__ivy_ngcc__/fesm2015/layout.js");
                /* harmony import */
                var _header_containers_header_header_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ../header/containers/header/header.component */ "./src/app/shared/header/containers/header/header.component.ts");
                /* harmony import */
                var _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/sidenav */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/sidenav.js");
                /* harmony import */
                var _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ../sidebar/sidebar.component */ "./src/app/shared/sidebar/sidebar.component.ts");






                const _c0 = ["sidenav"];
                const _c1 = ["*"];
                class LayoutComponent {
                    constructor(changeDetectorRef, media) {
                        this.mobileQuery = media.matchMedia('(max-width: 1024px)');
                        this.mobileQueryListener = () => changeDetectorRef.detectChanges();
                        this.mobileQuery.addListener(this.mobileQueryListener);
                        this.isShowSidebar = !this.mobileQuery.matches;
                    }
                    ngOnDestroy() {
                        this.mobileQuery.removeListener(this.mobileQueryListener);
                        this.sidenav.close();
                    }
                }
                LayoutComponent.ɵfac = function LayoutComponent_Factory(t) {
                    return new(t || LayoutComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ChangeDetectorRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_cdk_layout__WEBPACK_IMPORTED_MODULE_1__["MediaMatcher"]));
                };
                LayoutComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: LayoutComponent,
                    selectors: [
                        ["app-layout"]
                    ],
                    viewQuery: function LayoutComponent_Query(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵviewQuery"](_c0, true);
                        }
                        if (rf & 2) {
                            var _t;
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.sidenav = _t.first);
                        }
                    },
                    ngContentSelectors: _c1,
                    decls: 7,
                    vars: 4,
                    consts: [
                        [3, "isMenuOpened", "isShowSidebar"],
                        [1, "layout"],
                        ["mode", "side", 1, "layout-sidebar", 3, "opened", "mode", "fixedInViewport", "openedChange"],
                        ["sidenav", ""],
                        [1, "layout-content"]
                    ],
                    template: function LayoutComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            const _r1 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵprojectionDef"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "app-header", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("isShowSidebar", function LayoutComponent_Template_app_header_isShowSidebar_0_listener($event) {
                                _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r1);
                                const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](3);
                                return _r0.toggle($event);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-sidenav-container", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "mat-sidenav", 2, 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("openedChange", function LayoutComponent_Template_mat_sidenav_openedChange_2_listener($event) {
                                return ctx.isShowSidebar = $event;
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "app-sidebar");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-sidenav-content", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵprojection"](6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("isMenuOpened", ctx.isShowSidebar);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("opened", ctx.isShowSidebar)("mode", ctx.mobileQuery.matches ? "over" : "side")("fixedInViewport", ctx.mobileQuery.matches);
                        }
                    },
                    directives: [_header_containers_header_header_component__WEBPACK_IMPORTED_MODULE_2__["HeaderComponent"], _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_3__["MatSidenavContainer"], _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_3__["MatSidenav"], _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_4__["SidebarComponent"], _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_3__["MatSidenavContent"]],
                    styles: [".layout[_ngcontent-%COMP%] {\n  width: 100%;\n}\n\n.layout-sidebar[_ngcontent-%COMP%] {\n  height: calc(100vh - 64px);\n  margin-top: 64px;\n}\n\n@media (max-width: 576px) {\n  .layout-sidebar[_ngcontent-%COMP%] {\n    width: 218px;\n  }\n}\n\n.layout-content[_ngcontent-%COMP%] {\n  background-color: #F6F7FF;\n  height: calc(100vh - 64px);\n  margin-top: 64px;\n}\n\n@media (max-width: 576px) {\n  .layout-content[_ngcontent-%COMP%] {\n    width: 100%;\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL2xheW91dC9sYXlvdXQuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3NoYXJlZC9sYXlvdXQvbGF5b3V0LmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBR0E7RUFDRSxXQUFBO0FDRkY7O0FES0E7RUFDRSwwQkFBQTtFQUNBLGdCQUFBO0FDRkY7O0FESUU7RUFKRjtJQUtJLFlBQUE7RUNERjtBQUNGOztBRElBO0VBQ0UseUJFbUJpQjtFRmxCakIsMEJBQUE7RUFDQSxnQkFBQTtBQ0RGOztBREdFO0VBTEY7SUFNSSxXQUFBO0VDQUY7QUFDRiIsImZpbGUiOiJzcmMvYXBwL3NoYXJlZC9sYXlvdXQvbGF5b3V0LmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlc1wiO1xuQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2NvbG9yc1wiO1xuXG4ubGF5b3V0IHtcbiAgd2lkdGg6IDEwMCU7XG59XG5cbi5sYXlvdXQtc2lkZWJhciB7XG4gIGhlaWdodDpjYWxjKDEwMHZoIC0gNjRweCk7XG4gIG1hcmdpbi10b3A6IDY0cHg7XG5cbiAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgIHdpZHRoOiAyMThweDtcbiAgfVxufVxuXG4ubGF5b3V0LWNvbnRlbnQge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAkYmFja2dyb3VuZC1jb2xvcjtcbiAgaGVpZ2h0OmNhbGMoMTAwdmggLSA2NHB4KTtcbiAgbWFyZ2luLXRvcDogNjRweDtcblxuICBAbWVkaWEgKG1heC13aWR0aDogJHNtYWxsKSB7XG4gICAgd2lkdGg6IDEwMCU7XG4gIH1cbn1cbiIsIi5sYXlvdXQge1xuICB3aWR0aDogMTAwJTtcbn1cblxuLmxheW91dC1zaWRlYmFyIHtcbiAgaGVpZ2h0OiBjYWxjKDEwMHZoIC0gNjRweCk7XG4gIG1hcmdpbi10b3A6IDY0cHg7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmxheW91dC1zaWRlYmFyIHtcbiAgICB3aWR0aDogMjE4cHg7XG4gIH1cbn1cblxuLmxheW91dC1jb250ZW50IHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiAgaGVpZ2h0OiBjYWxjKDEwMHZoIC0gNjRweCk7XG4gIG1hcmdpbi10b3A6IDY0cHg7XG59XG5AbWVkaWEgKG1heC13aWR0aDogNTc2cHgpIHtcbiAgLmxheW91dC1jb250ZW50IHtcbiAgICB3aWR0aDogMTAwJTtcbiAgfVxufSIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](LayoutComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-layout',
                            templateUrl: './layout.component.html',
                            styleUrls: ['./layout.component.scss']
                        }]
                    }], function() {
                        return [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ChangeDetectorRef"]
                        }, {
                            type: _angular_cdk_layout__WEBPACK_IMPORTED_MODULE_1__["MediaMatcher"]
                        }];
                    }, {
                        sidenav: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"],
                            args: ['sidenav']
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/shared/shared.module.ts":
            /*!*****************************************!*\
              !*** ./src/app/shared/shared.module.ts ***!
              \*****************************************/
            /*! exports provided: SharedModule */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SharedModule", function() {
                    return SharedModule;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_list__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/list */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/list.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_common__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__( /*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_select__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__( /*! @angular/material/select */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/select.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__( /*! @angular/material/sidenav */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/sidenav.js");
                /* harmony import */
                var _header_header_module__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__( /*! ./header/header.module */ "./src/app/shared/header/header.module.ts");
                /* harmony import */
                var _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__( /*! ./sidebar/sidebar.component */ "./src/app/shared/sidebar/sidebar.component.ts");
                /* harmony import */
                var _footer_footer_component__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__( /*! ./footer/footer.component */ "./src/app/shared/footer/footer.component.ts");
                /* harmony import */
                var _ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__( /*! ./ui-elements/settings-menu/settings-menu.component */ "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts");
                /* harmony import */
                var _ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__( /*! ./ui-elements/date-menu/date-menu.component */ "./src/app/shared/ui-elements/date-menu/date-menu.component.ts");
                /* harmony import */
                var _layout_layout_component__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__( /*! ./layout/layout.component */ "./src/app/shared/layout/layout.component.ts");

















                class SharedModule {}
                SharedModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: SharedModule
                });
                SharedModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function SharedModule_Factory(t) {
                        return new(t || SharedModule)();
                    },
                    imports: [
                        [
                            _header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"],
                            _angular_material_list__WEBPACK_IMPORTED_MODULE_1__["MatListModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__["MatIconModule"],
                            _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButtonModule"],
                            _angular_common__WEBPACK_IMPORTED_MODULE_5__["CommonModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_6__["MatMenuModule"],
                            _angular_material_select__WEBPACK_IMPORTED_MODULE_7__["MatSelectModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_8__["FormsModule"],
                            _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_9__["MatSidenavModule"]
                        ],
                        _header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"]
                    ]
                });
                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](SharedModule, {
                        declarations: [_sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_11__["SidebarComponent"],
                            _footer_footer_component__WEBPACK_IMPORTED_MODULE_12__["FooterComponent"],
                            _ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_13__["SettingsMenuComponent"],
                            _ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_14__["DateMenuComponent"],
                            _layout_layout_component__WEBPACK_IMPORTED_MODULE_15__["LayoutComponent"]
                        ],
                        imports: [_header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"],
                            _angular_material_list__WEBPACK_IMPORTED_MODULE_1__["MatListModule"],
                            _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__["MatIconModule"],
                            _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                            _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButtonModule"],
                            _angular_common__WEBPACK_IMPORTED_MODULE_5__["CommonModule"],
                            _angular_material_menu__WEBPACK_IMPORTED_MODULE_6__["MatMenuModule"],
                            _angular_material_select__WEBPACK_IMPORTED_MODULE_7__["MatSelectModule"],
                            _angular_forms__WEBPACK_IMPORTED_MODULE_8__["FormsModule"],
                            _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_9__["MatSidenavModule"]
                        ],
                        exports: [_header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"],
                            _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_11__["SidebarComponent"],
                            _footer_footer_component__WEBPACK_IMPORTED_MODULE_12__["FooterComponent"],
                            _ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_13__["SettingsMenuComponent"],
                            _ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_14__["DateMenuComponent"],
                            _layout_layout_component__WEBPACK_IMPORTED_MODULE_15__["LayoutComponent"]
                        ]
                    });
                })();
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SharedModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [
                                _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_11__["SidebarComponent"],
                                _footer_footer_component__WEBPACK_IMPORTED_MODULE_12__["FooterComponent"],
                                _ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_13__["SettingsMenuComponent"],
                                _ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_14__["DateMenuComponent"],
                                _layout_layout_component__WEBPACK_IMPORTED_MODULE_15__["LayoutComponent"]
                            ],
                            imports: [
                                _header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"],
                                _angular_material_list__WEBPACK_IMPORTED_MODULE_1__["MatListModule"],
                                _angular_material_icon__WEBPACK_IMPORTED_MODULE_2__["MatIconModule"],
                                _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterModule"],
                                _angular_material_button__WEBPACK_IMPORTED_MODULE_4__["MatButtonModule"],
                                _angular_common__WEBPACK_IMPORTED_MODULE_5__["CommonModule"],
                                _angular_material_menu__WEBPACK_IMPORTED_MODULE_6__["MatMenuModule"],
                                _angular_material_select__WEBPACK_IMPORTED_MODULE_7__["MatSelectModule"],
                                _angular_forms__WEBPACK_IMPORTED_MODULE_8__["FormsModule"],
                                _angular_material_sidenav__WEBPACK_IMPORTED_MODULE_9__["MatSidenavModule"]
                            ],
                            exports: [
                                _header_header_module__WEBPACK_IMPORTED_MODULE_10__["HeaderModule"],
                                _sidebar_sidebar_component__WEBPACK_IMPORTED_MODULE_11__["SidebarComponent"],
                                _footer_footer_component__WEBPACK_IMPORTED_MODULE_12__["FooterComponent"],
                                _ui_elements_settings_menu_settings_menu_component__WEBPACK_IMPORTED_MODULE_13__["SettingsMenuComponent"],
                                _ui_elements_date_menu_date_menu_component__WEBPACK_IMPORTED_MODULE_14__["DateMenuComponent"],
                                _layout_layout_component__WEBPACK_IMPORTED_MODULE_15__["LayoutComponent"]
                            ]
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/sidebar/sidebar.component.ts":
            /*!*****************************************************!*\
              !*** ./src/app/shared/sidebar/sidebar.component.ts ***!
              \*****************************************************/
            /*! exports provided: SidebarComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SidebarComponent", function() {
                    return SidebarComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _consts_routes__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! ../../consts/routes */ "./src/app/consts/routes.ts");
                /* harmony import */
                var _angular_material_list__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/list */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/list.js");
                /* harmony import */
                var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");






                class SidebarComponent {
                    constructor() {
                        this.routes = _consts_routes__WEBPACK_IMPORTED_MODULE_1__["routes"];
                        this.isOpenUiElements = false;
                    }
                    openUiElements() {
                        this.isOpenUiElements = !this.isOpenUiElements;
                    }
                }
                SidebarComponent.ɵfac = function SidebarComponent_Factory(t) {
                    return new(t || SidebarComponent)();
                };
                SidebarComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: SidebarComponent,
                    selectors: [
                        ["app-sidebar"]
                    ],
                    decls: 58,
                    vars: 7,
                    consts: [
                        ["routerLinkActive", "active", 3, "routerLink"],
                        [3, "click"],
                        ["routerLinkActive", "active", 1, "ui-element", 3, "routerLink"],
                        [1, "circle"],
                        [1, "sidebar-title"],
                        [1, "project-circle", "project-circle_yellow"],
                        [1, "project-circle", "project-circle_blue"],
                        [1, "project-circle", "project-circle_pink"]
                    ],
                    template: function SidebarComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-list");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-list-item", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "home");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, " Dashboard ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-list-item", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "text_fields");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](8, " Typography ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "mat-list-item", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11, "border_all");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, " Tables ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "mat-list-item", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](15, "notifications_none");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, " Notification ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "mat-list-item", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function SidebarComponent_Template_mat_list_item_click_17_listener() {
                                return ctx.openUiElements();
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](19, "filter_none");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, " UI Elements ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](21, "div");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "mat-list-item", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](23, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](24, "Icons ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](25, "mat-list-item", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](26, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](27, "Charts ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](28, "mat-list-item", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](29, "div", 3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](30, "Map ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](31, "p", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](32, "Help");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](33, "mat-list");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](34, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](35, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](36, "library_books");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](37, " Library ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](38, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](39, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](40, "question_answer");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](41, " Support ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](42, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](43, "mat-icon");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](44, "help_outline");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](45, " FAQ ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](46, "p", 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](47, "Projects");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](48, "mat-list");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](49, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](50, "div", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](51, " My resend ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](52, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](53, "div", 6);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](54, " Starred");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](55, "mat-list-item");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](56, "div", 7);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](57, " Background ");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.DASHBOARD);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.TYPOGRAPHY);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.TABLES);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.NOTIFICATION);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](9);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.UI_ELEMENTS_ICONS);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.UI_ELEMENTS_CHARTS);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("routerLink", ctx.routes.UI_ELEMENTS_MAP);
                        }
                    },
                    directives: [_angular_material_list__WEBPACK_IMPORTED_MODULE_2__["MatList"], _angular_material_list__WEBPACK_IMPORTED_MODULE_2__["MatListItem"], _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterLinkActive"], _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterLink"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_4__["MatIcon"]],
                    styles: [".mat-list-base[_ngcontent-%COMP%] {\n  border-bottom: 1px solid #D8D8D880;\n  width: 210px;\n  padding-bottom: 16px;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item[_ngcontent-%COMP%] {\n  display: flex;\n  cursor: pointer;\n  color: rgba(110, 110, 110, 0.8);\n  width: auto;\n  padding-left: 4px;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item.active[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n  background-color: #F3F5FF;\n  outline: none;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item.active[_ngcontent-%COMP%]   .mat-icon[_ngcontent-%COMP%] {\n  color: #536DFE;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item.active[_ngcontent-%COMP%]   .circle[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item[_ngcontent-%COMP%]:hover {\n  background-color: #F3F5FF;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item[_ngcontent-%COMP%]:focus {\n  outline: none;\n}\n.mat-icon[_ngcontent-%COMP%] {\n  margin-right: 15px;\n  color: rgba(110, 110, 110, 0.6);\n}\n.sidebar-title[_ngcontent-%COMP%] {\n  color: rgba(110, 110, 110, 0.8);\n  font-size: 16px;\n  text-transform: uppercase;\n  margin-top: 32px;\n  margin-left: 24px;\n  margin-bottom: 16px;\n}\n.mat-list-base[_ngcontent-%COMP%]   .mat-list-item.ui-element[_ngcontent-%COMP%] {\n  padding-left: 40px;\n}\n.circle[_ngcontent-%COMP%] {\n  width: 5px;\n  height: 5px;\n  border-radius: 50%;\n  background-color: #B9B9B9;\n  margin-right: 30px;\n}\n.project-circle[_ngcontent-%COMP%] {\n  width: 8px;\n  height: 8px;\n  border-radius: 50%;\n  margin-right: 15px;\n  margin-left: 8px;\n}\n.project-circle_yellow[_ngcontent-%COMP%] {\n  background-color: #ffc260;\n}\n.project-circle_blue[_ngcontent-%COMP%] {\n  background-color: #536DFE;\n}\n.project-circle_pink[_ngcontent-%COMP%] {\n  background-color: #ff4081;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL3NpZGViYXIvc2lkZWJhci5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL3ZhcmlhYmxlcy5zY3NzIiwic3JjL2FwcC9zaGFyZWQvc2lkZWJhci9zaWRlYmFyLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBSUE7RUFDRSxrQ0FBQTtFQUNBLFlDUWM7RURQZCxvQkFBQTtBRUhGO0FGS0U7RUFDRSxhQUFBO0VBQ0EsZUFBQTtFQUNBLCtCR09NO0VITk4sV0FBQTtFQUNBLGlCQUFBO0FFSEo7QUZLSTtFQUNFLGNHUE07RUhRTix5QkdkTztFSGVQLGFBQUE7QUVITjtBRktNO0VBQ0UsY0dyQkQ7QURrQlA7QUZNTTtFQUNFLHlCR3pCRDtBRHFCUDtBRlFJO0VBQ0UseUJHM0JPO0FEcUJiO0FGU0k7RUFDRSxhQUFBO0FFUE47QUZZQTtFQUNFLGtCQUFBO0VBQ0EsK0JHckJRO0FEWVY7QUZhQTtFQUNFLCtCRzVCUTtFSDZCUixlSXpDVTtFSjBDVix5QkFBQTtFQUNBLGdCQUFBO0VBQ0EsaUJBQUE7RUFDQSxtQkFBQTtBRVZGO0FGYUE7RUFDRSxrQkFBQTtBRVZGO0FGYUE7RUFDRSxVQUFBO0VBQ0EsV0FBQTtFQUNBLGtCQUFBO0VBQ0EseUJHcERXO0VIcURYLGtCQUFBO0FFVkY7QUZhQTtFQUNFLFVBQUE7RUFDQSxXQUFBO0VBQ0Esa0JBQUE7RUFDQSxrQkFBQTtFQUNBLGdCQUFBO0FFVkY7QUZZRTtFQUNFLHlCRzNFSztBRGlFVDtBRmFFO0VBQ0UseUJHOUVHO0FEbUVQO0FGY0U7RUFDRSx5Qkc5RUc7QURrRVAiLCJmaWxlIjoic3JjL2FwcC9zaGFyZWQvc2lkZWJhci9zaWRlYmFyLmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2NvbG9yc1wiO1xuQGltcG9ydCBcInNyYy9hcHAvc3R5bGVzL2ZvbnRcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXNcIjtcblxuLm1hdC1saXN0LWJhc2Uge1xuICBib3JkZXItYm90dG9tOiAxcHggc29saWQgJGdyYXktODA7XG4gIHdpZHRoOiAkc2lkZWJhci13aWR0aDtcbiAgcGFkZGluZy1ib3R0b206IDE2cHg7XG5cbiAgJiAubWF0LWxpc3QtaXRlbSB7XG4gICAgZGlzcGxheTogZmxleDtcbiAgICBjdXJzb3I6IHBvaW50ZXI7XG4gICAgY29sb3I6ICRzaWRlYmFyLWZvbnQtY29sb3I7XG4gICAgd2lkdGg6IGF1dG87XG4gICAgcGFkZGluZy1sZWZ0OiA0cHg7XG5cbiAgICAmLmFjdGl2ZSB7XG4gICAgICBjb2xvcjogJHNpZGViYXItZm9udC1jb2xvci1hY3RpdmU7XG4gICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkc2lkZWJhci1iYWNrZ3JvdW5kLWNvbG9yLWFjdGl2ZTtcbiAgICAgIG91dGxpbmU6IG5vbmU7XG5cbiAgICAgICYgLm1hdC1pY29uIHtcbiAgICAgICAgY29sb3I6ICRzaWRlYmFyLWljb24tY29sb3ItYWN0aXZlO1xuICAgICAgfVxuXG4gICAgICAmIC5jaXJjbGUge1xuICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAkc2lkZWJhci1pY29uLWNvbG9yLWFjdGl2ZTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAmOmhvdmVyIHtcbiAgICAgIGJhY2tncm91bmQtY29sb3I6ICRzaWRlYmFyLWJhY2tncm91bmQtY29sb3ItaG92ZXI7XG4gICAgfVxuXG4gICAgJjpmb2N1cyB7XG4gICAgICBvdXRsaW5lOiBub25lO1xuICAgIH1cbiAgfVxufVxuXG4ubWF0LWljb24ge1xuICBtYXJnaW4tcmlnaHQ6IDE1cHg7XG4gIGNvbG9yOiAkc2lkZWJhci1pY29uLWNvbG9yO1xufVxuXG5cbi5zaWRlYmFyLXRpdGxlIHtcbiAgY29sb3I6ICRzaWRlYmFyLXRpdGxlLWNvbG9yO1xuICBmb250LXNpemU6ICRmcy1ub3JtYWw7XG4gIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG4gIG1hcmdpbi10b3A6IDMycHg7XG4gIG1hcmdpbi1sZWZ0OiAyNHB4O1xuICBtYXJnaW4tYm90dG9tOiAxNnB4O1xufVxuXG4ubWF0LWxpc3QtYmFzZSAubWF0LWxpc3QtaXRlbS51aS1lbGVtZW50IHtcbiAgcGFkZGluZy1sZWZ0OiA0MHB4O1xufVxuXG4uY2lyY2xlIHtcbiAgd2lkdGg6IDVweDtcbiAgaGVpZ2h0OiA1cHg7XG4gIGJvcmRlci1yYWRpdXM6IDUwJTtcbiAgYmFja2dyb3VuZC1jb2xvcjogJHNpZGViYXItY2lyY2xlLWNvbG9yO1xuICBtYXJnaW4tcmlnaHQ6IDMwcHg7XG59XG5cbi5wcm9qZWN0LWNpcmNsZSB7XG4gIHdpZHRoOiA4cHg7XG4gIGhlaWdodDogOHB4O1xuICBib3JkZXItcmFkaXVzOiA1MCU7XG4gIG1hcmdpbi1yaWdodDogMTVweDtcbiAgbWFyZ2luLWxlZnQ6IDhweDtcblxuICAmX3llbGxvdyB7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJHllbGxvdztcbiAgfVxuXG4gICZfYmx1ZSB7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4gIH1cblxuICAmX3Bpbmsge1xuICAgIGJhY2tncm91bmQtY29sb3I6ICRwaW5rO1xuICB9XG59XG4iLCJAaW1wb3J0IFwiY29sb3JzXCI7XG5cbi8vPT0gVmlld3BvcnRzXG5cbiRleHRyYS1zbWFsbDogNTc2cHg7XG4kc21hbGw6IDU3NnB4O1xuJG1lZGl1bTogNzY4cHg7XG4kbm9ybWFsOiAxMDI0cHg7XG4kbGFyZ2U6IDk5MnB4O1xuJGV4dHJhLWxhcmdlOiAxMjAwcHg7XG5cblxuLy89PSBTaWRlYmFyXG5cbiRzaWRlYmFyLXdpZHRoOiAyMTBweDtcbiRzaWRlYmFyLWZvbnQtY29sb3I6ICRncmF5LTA4O1xuJHNpZGViYXItZm9udC1jb2xvci1hY3RpdmU6ICRkYXJrLWdyZXk7XG4kc2lkZWJhci1iYWNrZ3JvdW5kLWNvbG9yLWFjdGl2ZTogJGJsdWUtd2hpdGU7XG4kc2lkZWJhci1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmx1ZS13aGl0ZTtcbiRzaWRlYmFyLWljb24tY29sb3ItYWN0aXZlOiAkYmx1ZTtcbiRzaWRlYmFyLWljb24tY29sb3I6ICRncmF5LTA2O1xuJHNpZGViYXItdGl0bGUtY29sb3I6ICRzaWRlYmFyLWZvbnQtY29sb3I7XG4kc2lkZWJhci1jaXJjbGUtY29sb3I6ICRsaWdodC1ncmV5O1xuXG4vLz09IE1hdGVyaWFsIENhcmRcbi8vXG5cbiRjYXJkLWZvbnQtY29sb3I6ICRkYXJrLWdyZXk7XG4kY2FyZC10aXRsZS1mb250LWNvbG9yOiAkZ3JleTtcblxuLy89PSBNYXRlcmlhbCBUb29sYmFyXG5cbiR0b29sYmFyLXRpdGxlLWZvbnQtY29sb3I6ICRsaWdodC1ncmV5O1xuJHRvb2xiYXItYnV0dG9uLWZvbnQtY29sb3I6ICR3aGl0ZTtcbiR0b29sYmFyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yOiAkcGluaztcbiR0b29sYmFyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yLWFjdGl2ZTogJGRhcmstcGluaztcblxuLy89PSBNYXRlcmlhbCBTaWRlYmFyIENvbnRlbnRcblxuJHNpZGViYXItY29udGVudC1wYWRkaW5nOiA0OHB4O1xuXG4vLz09IE1hdGVyaWFsIFRhYnNcblxuJHRhYnMtaGVhZGVyLWZvbnQtY29sb3I6ICRsaWdodC1ncmV5O1xuJHRhYnMtaGVhZGVyLWZvbnQtY29sb3ItYWN0aXZlOiAkYmx1ZTtcbiR0YWJzLWluay1iYXItY29sb3I6ICRibHVlO1xuXG5cbi8vPT0gQXBleCBDaGFydCBYIGF4aXMgdG9vbHRpcFxuXG4kY2hhcnQtdG9vbHRpcC1iYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiRjaGFydC10b29sdGlwLWJvcmRlci1jb2xvcjogJGJsdWU7XG4kY2hhcnQtdG9vbHRpcC1mb250LWNvbG9yOiAkd2hpdGU7XG5cbi8vPT0gU2Nyb2xsIGJhclxuXG4kc2Nyb2xsYmFyLXRyYWNrLWNvbG9yOiAkbGlnaHQtZ3JleTtcbiRzY3JvbGxiYXItdHJhY2stcGllY2UtY29sb3I6ICR3aGl0ZTtcbiRzY3JvbGxiYXItdGh1bWItY29sb3I6ICRsaWdodC1ncmV5O1xuJHNjcm9sbGJhci1jb3JuZXItY29sb3I6ICRsaWdodC1ncmV5O1xuXG4vLz09IEhlYWRlclxuXG4kaGVhZGVyLWJhY2tncm91bmQtY29sb3I6ICRibHVlO1xuJGhlYWRlci1oZWlnaHQ6IDY0cHg7XG4kaGVhZGVyLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yOiAkYmx1ZTtcbiRoZWFkZXItYnV0dG9uLWJhY2tncm91bmQtY29sb3ItaG92ZXI6ICRibGFjay0wODtcbiRoZWFkZXItYnV0dG9uLWZvbnQtY29sb3I6ICR3aGl0ZTtcbiRoZWFkZXItdGl0bGUtZm9udC1jb2xvcjogJHdoaXRlO1xuXG4vLz09IEZvb3RlclxuXG4kZm9vdGVyLWhlaWdodDogNDhweDtcbiRmb290ZXItd2lkdGg6IGNhbGMoMTAwJSAtICN7JHNpZGViYXItY29udGVudC1wYWRkaW5nfSk7XG4kZm9vdGVyLWxpbmstY29sb3I6ICRibHVlO1xuJGZvb3Rlci1pY29uLWNvbG9yOiAkZ3JheS0wNjtcbiRmb290ZXItaWNvbi1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmxhY2stMDg7XG5cbi8vPT0gU2V0dGluZ3MgbWVudSBlbGVtZW50XG5cbiRzZXR0aW5ncy1idXR0b24tYmFja2dyb3VuZC1jb2xvcjogJHdoaXRlO1xuJHNldHRpbmdzLWJ1dHRvbi1iYWNrZ3JvdW5kLWNvbG9yLWhvdmVyOiAkYmx1ZTtcbiRzZXR0aW5ncy1idXR0b24tY29sb3I6ICRsaWdodC1ncmV5O1xuJHNldHRpbmdzLWJ1dHRvbi1jb2xvci1ob3ZlcjogJHdoaXRlLTM1O1xuJHNldHRpbmdzLW1lbnUtZm9udC1jb2xvcjogJGRhcmstZ3JleTtcbiRzZXR0aW5ncy1tZW51LWJhY2tncm91bmQtY29sb3ItaG92ZXI6ICRibHVlLXdoaXRlO1xuIiwiLm1hdC1saXN0LWJhc2Uge1xuICBib3JkZXItYm90dG9tOiAxcHggc29saWQgI0Q4RDhEODgwO1xuICB3aWR0aDogMjEwcHg7XG4gIHBhZGRpbmctYm90dG9tOiAxNnB4O1xufVxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW0ge1xuICBkaXNwbGF5OiBmbGV4O1xuICBjdXJzb3I6IHBvaW50ZXI7XG4gIGNvbG9yOiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4gIHdpZHRoOiBhdXRvO1xuICBwYWRkaW5nLWxlZnQ6IDRweDtcbn1cbi5tYXQtbGlzdC1iYXNlIC5tYXQtbGlzdC1pdGVtLmFjdGl2ZSB7XG4gIGNvbG9yOiAjNEE0QTRBO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjRjNGNUZGO1xuICBvdXRsaW5lOiBub25lO1xufVxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW0uYWN0aXZlIC5tYXQtaWNvbiB7XG4gIGNvbG9yOiAjNTM2REZFO1xufVxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW0uYWN0aXZlIC5jaXJjbGUge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjNTM2REZFO1xufVxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW06aG92ZXIge1xuICBiYWNrZ3JvdW5kLWNvbG9yOiAjRjNGNUZGO1xufVxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW06Zm9jdXMge1xuICBvdXRsaW5lOiBub25lO1xufVxuXG4ubWF0LWljb24ge1xuICBtYXJnaW4tcmlnaHQ6IDE1cHg7XG4gIGNvbG9yOiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG59XG5cbi5zaWRlYmFyLXRpdGxlIHtcbiAgY29sb3I6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC44KTtcbiAgZm9udC1zaXplOiAxNnB4O1xuICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlO1xuICBtYXJnaW4tdG9wOiAzMnB4O1xuICBtYXJnaW4tbGVmdDogMjRweDtcbiAgbWFyZ2luLWJvdHRvbTogMTZweDtcbn1cblxuLm1hdC1saXN0LWJhc2UgLm1hdC1saXN0LWl0ZW0udWktZWxlbWVudCB7XG4gIHBhZGRpbmctbGVmdDogNDBweDtcbn1cblxuLmNpcmNsZSB7XG4gIHdpZHRoOiA1cHg7XG4gIGhlaWdodDogNXB4O1xuICBib3JkZXItcmFkaXVzOiA1MCU7XG4gIGJhY2tncm91bmQtY29sb3I6ICNCOUI5Qjk7XG4gIG1hcmdpbi1yaWdodDogMzBweDtcbn1cblxuLnByb2plY3QtY2lyY2xlIHtcbiAgd2lkdGg6IDhweDtcbiAgaGVpZ2h0OiA4cHg7XG4gIGJvcmRlci1yYWRpdXM6IDUwJTtcbiAgbWFyZ2luLXJpZ2h0OiAxNXB4O1xuICBtYXJnaW4tbGVmdDogOHB4O1xufVxuLnByb2plY3QtY2lyY2xlX3llbGxvdyB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZmMyNjA7XG59XG4ucHJvamVjdC1jaXJjbGVfYmx1ZSB7XG4gIGJhY2tncm91bmQtY29sb3I6ICM1MzZERkU7XG59XG4ucHJvamVjdC1jaXJjbGVfcGluayB7XG4gIGJhY2tncm91bmQtY29sb3I6ICNmZjQwODE7XG59IiwiJHllbGxvdzogI2ZmYzI2MDtcbiRibHVlOiAjNTM2REZFO1xuJGxpZ2h0LWJsdWU6ICM3OThERkU7XG4kd2hpdGUtYmx1ZTogI0IxQkNGRjtcbiRibHVlLXdoaXRlOiAjRjNGNUZGO1xuJHBpbms6ICNmZjQwODE7XG4kZGFyay1waW5rOiAjZmYwZjYwO1xuJGdyZWVuOiAjM0NENEEwO1xuJHZpb2xldDogIzkwMTNGRTtcbiR3aGl0ZTogd2hpdGU7XG4kZGFyay1ncmV5OiAjNEE0QTRBO1xuJGxpZ2h0LWdyZXk6ICNCOUI5Qjk7XG4kZ3JleTogIzZFNkU2RTtcbiRza3k6ICNjMGNhZmY7XG5cblxuJHdoaXRlLTM1OiByZ2JhKDI1NSwgMjU1LCAyNTUsIDAuMzUpO1xuJHdoaXRlLTgwOiAjRkZGRkZGODA7XG5cbiRncmF5LTA4OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuOCk7XG4kZ3JheS04MDogI0Q4RDhEODgwO1xuJGdyYXktMDY6IHJnYmEoMTEwLCAxMTAsIDExMCwgMC42KTtcblxuJGJsYWNrLTA4OiByZ2JhKDAsIDAsIDAsIDAuMDgpO1xuXG4kcGluay0xNTogcmdiYSgyNTUsIDkyLCAxNDcsIDAuMTUpO1xuJGJsdWUtMTU6IHJnYmEoODMsIDEwOSwgMjU0LCAwLjE1KTtcbiRncmVlbi0xNTogcmdiYSg2MCwgMjEyLCAxNjAsIDAuMTUpO1xuJHllbGxvdy0xNTogcmdiYSgyNTUsIDE5NCwgOTYsIDAuMTUpO1xuJHZpb2xldC0xNTogcmdiYSgxNDQsIDE5LCAyNTQsIDAuMTUpO1xuXG5cbiRzaGFkb3ctd2hpdGU6ICNFOEVBRkM7XG4kc2hhZG93LWdyZXk6ICNCMkIyQjIxQTtcbiRzaGFkb3ctZGFyay1ncmV5OiAjOUE5QTlBMUE7XG5cbiRiYWNrZ3JvdW5kLWNvbG9yOiAjRjZGN0ZGO1xuIiwiJGZ3LWxpZ2h0ZXI6IDQwMDtcbiRmdy1ub3JtYWw6IDUwMDtcbiRmdy1ib2xkOiA2MDA7XG5cblxuJGZzLXhzOiAxMS4ycHg7XG4kZnMtc21hbGw6IDE0cHg7XG4kZnMtbm9ybWFsOiAxNnB4O1xuJGZzLXJlZ3VsYXI6IDE4cHg7XG4kZnMtbWVkaXVtOiAyMXB4O1xuJGZzLWxhcmdlOiAyNHB4O1xuJGZzLXhsOiAyOHB4O1xuJGZzLXh4bDogMzhweDtcbiRmcy14eHhsOiA0MnB4O1xuIl19 */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SidebarComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-sidebar',
                            templateUrl: './sidebar.component.html',
                            styleUrls: ['./sidebar.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/app/shared/ui-elements/date-menu/date-menu.component.ts":
            /*!*********************************************************************!*\
              !*** ./src/app/shared/ui-elements/date-menu/date-menu.component.ts ***!
              \*********************************************************************/
            /*! exports provided: DateMenuComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "DateMenuComponent", function() {
                    return DateMenuComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_select__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/select */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/select.js");
                /* harmony import */
                var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
                /* harmony import */
                var _angular_material_core__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/core */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/core.js");





                var matSelectedFields;
                (function(matSelectedFields) {
                    matSelectedFields["daily"] = "Daily";
                    matSelectedFields["weekly"] = "Weekly";
                    matSelectedFields["monthly"] = "Monthly";
                })(matSelectedFields || (matSelectedFields = {}));
                class DateMenuComponent {
                    constructor() {
                        this.changeDateType = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
                        this.matSelectFields = matSelectedFields;
                        this.selectedMatSelectValue = matSelectedFields.daily;
                    }
                    changedMatSelectionValue(dateType) {
                        this.changeDateType.emit(dateType);
                    }
                }
                DateMenuComponent.ɵfac = function DateMenuComponent_Factory(t) {
                    return new(t || DateMenuComponent)();
                };
                DateMenuComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: DateMenuComponent,
                    selectors: [
                        ["app-date-menu"]
                    ],
                    outputs: {
                        changeDateType: "changeDateType"
                    },
                    decls: 7,
                    vars: 4,
                    consts: [
                        [1, "date-menu", 3, "ngModel", "ngModelChange", "selectionChange"],
                        [3, "value"]
                    ],
                    template: function DateMenuComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "mat-select", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("ngModelChange", function DateMenuComponent_Template_mat_select_ngModelChange_0_listener($event) {
                                return ctx.selectedMatSelectValue = $event;
                            })("selectionChange", function DateMenuComponent_Template_mat_select_selectionChange_0_listener($event) {
                                return ctx.changedMatSelectionValue($event.value);
                            });
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-option", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "Daily");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "mat-option", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, "Weekly");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "mat-option", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, "Monthly");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngModel", ctx.selectedMatSelectValue);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.daily);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.weekly);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("value", ctx.matSelectFields.monthly);
                        }
                    },
                    directives: [_angular_material_select__WEBPACK_IMPORTED_MODULE_1__["MatSelect"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgModel"], _angular_material_core__WEBPACK_IMPORTED_MODULE_3__["MatOption"]],
                    styles: [".date-menu[_ngcontent-%COMP%] {\n  border: none;\n  width: 55px;\n  padding: 8px 0 8px 4px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL3VpLWVsZW1lbnRzL2RhdGUtbWVudS9kYXRlLW1lbnUuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3NoYXJlZC91aS1lbGVtZW50cy9kYXRlLW1lbnUvZGF0ZS1tZW51LmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0VBQ0UsWUFBQTtFQUNBLFdBQUE7RUFDQSxzQkFBQTtBQ0NGIiwiZmlsZSI6InNyYy9hcHAvc2hhcmVkL3VpLWVsZW1lbnRzL2RhdGUtbWVudS9kYXRlLW1lbnUuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyIuZGF0ZS1tZW51IHtcbiAgYm9yZGVyOiBub25lO1xuICB3aWR0aDogNTVweDtcbiAgcGFkZGluZzogOHB4IDAgOHB4IDRweDtcbn1cbiIsIi5kYXRlLW1lbnUge1xuICBib3JkZXI6IG5vbmU7XG4gIHdpZHRoOiA1NXB4O1xuICBwYWRkaW5nOiA4cHggMCA4cHggNHB4O1xufSJdfQ== */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DateMenuComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-date-menu',
                            templateUrl: './date-menu.component.html',
                            styleUrls: ['./date-menu.component.scss']
                        }]
                    }], null, {
                        changeDateType: [{
                            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
                        }]
                    });
                })();


                /***/
            }),

        /***/
        "./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts":
            /*!*****************************************************************************!*\
              !*** ./src/app/shared/ui-elements/settings-menu/settings-menu.component.ts ***!
              \*****************************************************************************/
            /*! exports provided: SettingsMenuComponent */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "SettingsMenuComponent", function() {
                    return SettingsMenuComponent;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_material_button__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/material/button */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/button.js");
                /* harmony import */
                var _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! @angular/material/menu */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/menu.js");
                /* harmony import */
                var _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! @angular/material/icon */ "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/icon.js");





                class SettingsMenuComponent {}
                SettingsMenuComponent.ɵfac = function SettingsMenuComponent_Factory(t) {
                    return new(t || SettingsMenuComponent)();
                };
                SettingsMenuComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: SettingsMenuComponent,
                    selectors: [
                        ["app-settings-menu"]
                    ],
                    decls: 14,
                    vars: 1,
                    consts: [
                        ["mat-mini-fab", "", 1, "settings-button", 3, "matMenuTriggerFor"],
                        [1, "settings-button__icon"],
                        [1, "settings-menu"],
                        ["xPosition", "before"],
                        ["settings", "matMenu"],
                        ["mat-menu-item", "", 1, "settings-menu__item"]
                    ],
                    template: function SettingsMenuComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "button", 0);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-icon", 1);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "more_vert");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 2);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "mat-menu", 3, 4);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Edit");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Copy");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11, "Delete");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "button", 5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](13, "Print");
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                        if (rf & 2) {
                            const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](5);
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("matMenuTriggerFor", _r0);
                        }
                    },
                    directives: [_angular_material_button__WEBPACK_IMPORTED_MODULE_1__["MatButton"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["MatMenuTrigger"], _angular_material_icon__WEBPACK_IMPORTED_MODULE_3__["MatIcon"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["_MatMenu"], _angular_material_menu__WEBPACK_IMPORTED_MODULE_2__["MatMenuItem"]],
                    styles: [".settings-button[_ngcontent-%COMP%] {\n  box-shadow: none;\n  background-color: white;\n  color: #B9B9B9;\n}\n.settings-button[_ngcontent-%COMP%]:hover {\n  background-color: #536DFE;\n  color: rgba(255, 255, 255, 0.35);\n}\n.settings-button__icon[_ngcontent-%COMP%] {\n  color: inherit;\n}\n.settings-menu[_ngcontent-%COMP%] {\n  position: absolute;\n}\n.settings-menu__item[_ngcontent-%COMP%] {\n  color: #4A4A4A;\n}\n.settings-menu__item[_ngcontent-%COMP%]:hover {\n  background-color: #F3F5FF;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc2hhcmVkL3VpLWVsZW1lbnRzL3NldHRpbmdzLW1lbnUvc2V0dGluZ3MtbWVudS5jb21wb25lbnQuc2NzcyIsIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvc3R5bGVzL2NvbG9ycy5zY3NzIiwic3JjL2FwcC9zaGFyZWQvdWktZWxlbWVudHMvc2V0dGluZ3MtbWVudS9zZXR0aW5ncy1tZW51LmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUdBO0VBQ0UsZ0JBQUE7RUFDQSx1QkNJTTtFREhOLGNDS1c7QUNQYjtBRklFO0VBQ0UseUJDUkc7RURTSCxnQ0NNTztBQ1JYO0FGS0U7RUFDRSxjQUFBO0FFSEo7QUZPQTtFQUNFLGtCQUFBO0FFSkY7QUZNRTtFQUNFLGNDWlE7QUNRWjtBRk1JO0VBQ0UseUJDckJPO0FDaUJiIiwiZmlsZSI6InNyYy9hcHAvc2hhcmVkL3VpLWVsZW1lbnRzL3NldHRpbmdzLW1lbnUvc2V0dGluZ3MtbWVudS5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy9jb2xvcnNcIjtcbkBpbXBvcnQgXCJzcmMvYXBwL3N0eWxlcy92YXJpYWJsZXNcIjtcblxuLnNldHRpbmdzLWJ1dHRvbiB7XG4gIGJveC1zaGFkb3c6IG5vbmU7XG4gIGJhY2tncm91bmQtY29sb3I6ICRzZXR0aW5ncy1idXR0b24tYmFja2dyb3VuZC1jb2xvcjtcbiAgY29sb3I6ICRzZXR0aW5ncy1idXR0b24tY29sb3I7XG5cbiAgJjpob3ZlciB7XG4gICAgYmFja2dyb3VuZC1jb2xvcjogJGJsdWU7XG4gICAgY29sb3I6ICRzZXR0aW5ncy1idXR0b24tY29sb3ItaG92ZXI7XG4gIH1cblxuICAmX19pY29uIHtcbiAgICBjb2xvcjogaW5oZXJpdDtcbiAgfVxufVxuXG4uc2V0dGluZ3MtbWVudSB7XG4gIHBvc2l0aW9uOiBhYnNvbHV0ZTtcblxuICAmX19pdGVtIHtcbiAgICBjb2xvcjogJGRhcmstZ3JleTtcblxuICAgICY6aG92ZXIge1xuICAgICAgYmFja2dyb3VuZC1jb2xvcjogJHNldHRpbmdzLW1lbnUtYmFja2dyb3VuZC1jb2xvci1ob3ZlcjtcbiAgICB9XG4gIH1cbn1cbiIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIi5zZXR0aW5ncy1idXR0b24ge1xuICBib3gtc2hhZG93OiBub25lO1xuICBiYWNrZ3JvdW5kLWNvbG9yOiB3aGl0ZTtcbiAgY29sb3I6ICNCOUI5Qjk7XG59XG4uc2V0dGluZ3MtYnV0dG9uOmhvdmVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogIzUzNkRGRTtcbiAgY29sb3I6IHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4zNSk7XG59XG4uc2V0dGluZ3MtYnV0dG9uX19pY29uIHtcbiAgY29sb3I6IGluaGVyaXQ7XG59XG5cbi5zZXR0aW5ncy1tZW51IHtcbiAgcG9zaXRpb246IGFic29sdXRlO1xufVxuLnNldHRpbmdzLW1lbnVfX2l0ZW0ge1xuICBjb2xvcjogIzRBNEE0QTtcbn1cbi5zZXR0aW5ncy1tZW51X19pdGVtOmhvdmVyIHtcbiAgYmFja2dyb3VuZC1jb2xvcjogI0YzRjVGRjtcbn0iXX0= */"]
                });
                /*@__PURE__*/
                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SettingsMenuComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-settings-menu',
                            templateUrl: './settings-menu.component.html',
                            styleUrls: ['./settings-menu.component.scss']
                        }]
                    }], null, null);
                })();


                /***/
            }),

        /***/
        "./src/environments/environment.ts":
            /*!*****************************************!*\
              !*** ./src/environments/environment.ts ***!
              \*****************************************/
            /*! exports provided: environment */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "environment", function() {
                    return environment;
                });
                // This file can be replaced during build by using the `fileReplacements` array.
                // `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
                // The list of file replacements can be found in `angular.json`.
                const environment = {
                    production: false,
                    hmr: false
                };
                /*
                 * For easier debugging in development mode, you can import the following file
                 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
                 *
                 * This import should be commented out in production mode because it will have a negative impact
                 * on performance if an error is thrown.
                 */
                // import 'zone.js/dist/zone-error';  // Included with Angular CLI.


                /***/
            }),

        /***/
        "./src/hmr.ts":
            /*!********************!*\
              !*** ./src/hmr.ts ***!
              \********************/
            /*! exports provided: hmrBootstrap */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */
                __webpack_require__.d(__webpack_exports__, "hmrBootstrap", function() {
                    return hmrBootstrap;
                });
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angularclass_hmr__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angularclass/hmr */ "./node_modules/@angularclass/hmr/dist/index.js");
                /* harmony import */
                var _angularclass_hmr__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/ __webpack_require__.n(_angularclass_hmr__WEBPACK_IMPORTED_MODULE_1__);


                const hmrBootstrap = (module, bootstrap) => {
                    let ngModule;
                    module.hot.accept();
                    bootstrap().then(mod => ngModule = mod);
                    module.hot.dispose(() => {
                        const appRef = ngModule.injector.get(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ApplicationRef"]);
                        const elements = appRef.components.map(c => c.location.nativeElement);
                        const makeVisible = Object(_angularclass_hmr__WEBPACK_IMPORTED_MODULE_1__["createNewHosts"])(elements);
                        ngModule.destroy();
                        makeVisible();
                    });
                };


                /***/
            }),

        /***/
        "./src/main.ts":
            /*!*********************!*\
              !*** ./src/main.ts ***!
              \*********************/
            /*! no exports provided */
            /***/
            (function(module, __webpack_exports__, __webpack_require__) {

                "use strict";
                __webpack_require__.r(__webpack_exports__);
                /* harmony import */
                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__( /*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */
                var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__( /*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/__ivy_ngcc__/fesm2015/platform-browser-dynamic.js");
                /* harmony import */
                var _hmr__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__( /*! ./hmr */ "./src/hmr.ts");
                /* harmony import */
                var _app_app_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__( /*! ./app/app.module */ "./src/app/app.module.ts");
                /* harmony import */
                var _environments_environment__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__( /*! ./environments/environment */ "./src/environments/environment.ts");





                if (_environments_environment__WEBPACK_IMPORTED_MODULE_4__["environment"].production) {
                    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
                }
                const bootstrap = () => Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_3__["AppModule"]);
                if (_environments_environment__WEBPACK_IMPORTED_MODULE_4__["environment"].hmr) {
                    if (false) {} else {
                        console.error('HMR is not enabled for webpack-dev-server!');
                        console.log('Are you using the --hmr flag for ng serve?');
                    }
                } else {
                    bootstrap().catch(err => console.log(err));
                }
                Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_3__["AppModule"])
                    .catch(err => console.error(err));


                /***/
            }),

        /***/
        0:
            /*!***************************!*\
              !*** multi ./src/main.ts ***!
              \***************************/
            /*! no static exports found */
            /***/
            (function(module, exports, __webpack_require__) {

                module.exports = __webpack_require__( /*! /home/w3p/set1/py4web/apps/angflat/static/tte/angular-material-admin/src/main.ts */ "./src/main.ts");


                /***/
            })

    },
    [
        [0, "runtime", "vendor"]
    ]
]);
