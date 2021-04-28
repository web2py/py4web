function _classCallCheck(instance, Constructor) {
    if (!(instance instanceof Constructor)) {
        throw new TypeError("Cannot call a class as a function");
    }
}

(window["webpackJsonp"] = window["webpackJsonp"] || []).push([
    ["pages-typography-typography-module"], {
        /***/
        "./src/app/pages/typography/containers/index.ts":
            /*!******************************************************!*\
              !*** ./src/app/pages/typography/containers/index.ts ***!
              \******************************************************/

            /*! exports provided: TypographyPageComponent */

            /***/
            function srcAppPagesTypographyContainersIndexTs(module, __webpack_exports__, __webpack_require__) {
                "use strict";

                __webpack_require__.r(__webpack_exports__);
                /* harmony import */


                var _typography_page_typography_page_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
                    /*! ./typography-page/typography-page.component */
                    "./src/app/pages/typography/containers/typography-page/typography-page.component.ts");
                /* harmony reexport (safe) */


                __webpack_require__.d(__webpack_exports__, "TypographyPageComponent", function() {
                    return _typography_page_typography_page_component__WEBPACK_IMPORTED_MODULE_0__["TypographyPageComponent"];
                });
                /***/

            },

        /***/
        "./src/app/pages/typography/containers/typography-page/typography-page.component.ts":
            /*!******************************************************************************************!*\
              !*** ./src/app/pages/typography/containers/typography-page/typography-page.component.ts ***!
              \******************************************************************************************/

            /*! exports provided: TypographyPageComponent */

            /***/
            function srcAppPagesTypographyContainersTypographyPageTypographyPageComponentTs(module, __webpack_exports__, __webpack_require__) {
                "use strict";

                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */


                __webpack_require__.d(__webpack_exports__, "TypographyPageComponent", function() {
                    return TypographyPageComponent;
                });
                /* harmony import */


                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
                    /*! @angular/core */
                    "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */


                var _shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
                    /*! ../../../../shared/layout/layout.component */
                    "./src/app/shared/layout/layout.component.ts");
                /* harmony import */


                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
                    /*! @angular/material/toolbar */
                    "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */


                var _angular_material_card__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
                    /*! @angular/material/card */
                    "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */


                var _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
                    /*! ../../../../shared/footer/footer.component */
                    "./src/app/shared/footer/footer.component.ts");

                var TypographyPageComponent = function TypographyPageComponent() {
                    _classCallCheck(this, TypographyPageComponent);
                };

                TypographyPageComponent.ɵfac = function TypographyPageComponent_Factory(t) {
                    return new(t || TypographyPageComponent)();
                };

                TypographyPageComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({
                    type: TypographyPageComponent,
                    selectors: [
                        ["app-typography-page"]
                    ],
                    decls: 78,
                    vars: 0,
                    consts: [
                        ["role", "heading", 1, "page-header"],
                        [1, "typography-content"],
                        [1, "typography-content__wrapper"],
                        [1, "typography-content__item-wrapper"],
                        [1, "typography-content__headings"],
                        [1, "typography-content__colors"],
                        [1, "typography-content__colors_blue"],
                        [1, "typography-content__colors_green"],
                        [1, "typography-content__colors_pink"],
                        [1, "typography-content__colors_yellow"],
                        [1, "typography-content__colors_light-blue"],
                        [1, "typography-content__colors_violet"],
                        [1, "typography-content__settings"],
                        [1, "fw-light"],
                        [1, "fw-medium"],
                        [1, "fw-bold"],
                        [1, "font-uppercase"],
                        [1, "font-lowercase"],
                        [1, "fst-italic"],
                        [1, "typography-content__size"],
                        [1, "fs-sm"],
                        [1, "fs-regular"],
                        [1, "fs-md"],
                        [1, "fs-xl"],
                        [1, "fs-xxl"]
                    ],
                    template: function TypographyPageComponent_Template(rf, ctx) {
                        if (rf & 1) {
                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "app-layout");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "mat-toolbar", 0);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "h1");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Typography");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "mat-card-content", 1);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 2);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "mat-card", 3);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "mat-card-title");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](9, "Headings");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "div", 4);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "h1");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, "h1. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "h2");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "h2. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "h3");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, "h3. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "h4");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](18, "h4. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "h5");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "h5. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](21, "h6");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](22, "h6. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](23, "mat-card", 3);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](24, "mat-card-title");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](25, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](26, "Typography Colors");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](27, "div", 5);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](28, "h1", 6);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](29, "h1. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](30, "h2", 7);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](31, "h2. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](32, "h3", 8);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](33, "h3. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](34, "h4", 9);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](35, "h4. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](36, "h5", 10);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](37, "h5. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](38, "h6", 11);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](39, "h6. Heading");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](40, "div", 2);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](41, "mat-card", 3);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](42, "mat-card-title");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](43, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](44, "Basic Text Settings");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](45, "div", 12);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](46, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](47, "Basic text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](48, "p", 13);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](49, "Basic light text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](50, "p", 14);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](51, "Basic medium text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](52, "p", 15);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](53, "Basic bold text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](54, "p", 16);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](55, "basic lowercase text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](56, "p", 17);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](57, "basic lowercase text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](58, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](59, "Basic Capitalized Text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](60, "p", 18);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](61, "Basic Cursive Text");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](62, "mat-card", 3);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](63, "mat-card-title");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](64, "p");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](65, "Text Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](66, "div", 19);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](67, "p", 20);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](68, "Heading Typography SM Font Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](69, "p", 21);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](70, "Heading Typography Regular Font Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](71, "p", 22);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](72, "Heading Typography MD Font Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](73, "p", 23);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](74, "Heading Typography XL Font Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](75, "p", 24);

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](76, " Heading Typography XXL Font Size");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](77, "app-footer");

                            _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
                        }
                    },
                    directives: [_shared_layout_layout_component__WEBPACK_IMPORTED_MODULE_1__["LayoutComponent"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_2__["MatToolbar"], _angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCardContent"], _angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCard"], _angular_material_card__WEBPACK_IMPORTED_MODULE_3__["MatCardTitle"], _shared_footer_footer_component__WEBPACK_IMPORTED_MODULE_4__["FooterComponent"]],
                    styles: [".typography-content__wrapper[_ngcontent-%COMP%] {\n  display: flex;\n  padding: 0 8px;\n}\n@media (max-width: 576px) {\n  .typography-content__wrapper[_ngcontent-%COMP%] {\n    flex-wrap: wrap;\n  }\n}\n.typography-content__item-wrapper[_ngcontent-%COMP%] {\n  box-shadow: 0 3px 11px 0 #E8EAFC, 0 3px 3px -2px #B2B2B21A, 0 1px 8px 0 #9A9A9A1A;\n  width: 100%;\n  margin: 16px;\n}\n.typography-content__headings[_ngcontent-%COMP%], .typography-content__colors[_ngcontent-%COMP%], .typography-content__settings[_ngcontent-%COMP%], .typography-content__size[_ngcontent-%COMP%] {\n  margin-top: 8px;\n  border: 1px dashed #536DFE;\n  padding: 32px 16px;\n}\n@media (max-width: 576px) {\n  .typography-content__headings[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__colors[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__settings[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%], .typography-content__size[_ngcontent-%COMP%]   h1[_ngcontent-%COMP%] {\n    line-height: 46px;\n  }\n}\n.typography-content__colors_blue[_ngcontent-%COMP%] {\n  color: #536DFE;\n}\n.typography-content__colors_green[_ngcontent-%COMP%] {\n  color: #3CD4A0;\n}\n.typography-content__colors_pink[_ngcontent-%COMP%] {\n  color: #ff4081;\n}\n.typography-content__colors_yellow[_ngcontent-%COMP%] {\n  color: #ffc260;\n}\n.typography-content__colors_light-blue[_ngcontent-%COMP%] {\n  color: #798DFE;\n}\n.typography-content__colors_violet[_ngcontent-%COMP%] {\n  color: #9013FE;\n}\n.fw-light[_ngcontent-%COMP%] {\n  font-weight: 400;\n}\n.fw-medium[_ngcontent-%COMP%] {\n  font-weight: 500;\n}\n.fw-bold[_ngcontent-%COMP%] {\n  font-weight: 600;\n}\n.font-uppercase[_ngcontent-%COMP%] {\n  text-transform: uppercase;\n}\n.font-lowercase[_ngcontent-%COMP%] {\n  text-transform: lowercase;\n}\n.fst-italic[_ngcontent-%COMP%] {\n  font-style: italic;\n}\n.fs-sm[_ngcontent-%COMP%] {\n  font-size: 11.2px;\n}\n.fs-regular[_ngcontent-%COMP%] {\n  font-size: 14px;\n}\n.fs-md[_ngcontent-%COMP%] {\n  font-size: 21px;\n}\n.fs-xl[_ngcontent-%COMP%] {\n  font-size: 28px;\n}\n.fs-xxl[_ngcontent-%COMP%] {\n  font-size: 42px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIi9ob21lL3czcC9zZXQxL3B5NHdlYi9hcHBzL2FuZ2ZsYXQvc3RhdGljL3R0ZS9hbmd1bGFyLW1hdGVyaWFsLWFkbWluL3NyYy9hcHAvcGFnZXMvdHlwb2dyYXBoeS9jb250YWluZXJzL3R5cG9ncmFwaHktcGFnZS90eXBvZ3JhcGh5LXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzcmMvYXBwL3BhZ2VzL3R5cG9ncmFwaHkvY29udGFpbmVycy90eXBvZ3JhcGh5LXBhZ2UvdHlwb2dyYXBoeS1wYWdlLmNvbXBvbmVudC5zY3NzIiwiL2hvbWUvdzNwL3NldDEvcHk0d2ViL2FwcHMvYW5nZmxhdC9zdGF0aWMvdHRlL2FuZ3VsYXItbWF0ZXJpYWwtYWRtaW4vc3JjL2FwcC9zdHlsZXMvY29sb3JzLnNjc3MiLCIvaG9tZS93M3Avc2V0MS9weTR3ZWIvYXBwcy9hbmdmbGF0L3N0YXRpYy90dGUvYW5ndWxhci1tYXRlcmlhbC1hZG1pbi9zcmMvYXBwL3N0eWxlcy9mb250LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBTUU7RUFDRSxhQUFBO0VBQ0EsY0FBQTtBQ0xKO0FET0k7RUFKRjtJQUtJLGVBQUE7RUNKSjtBQUNGO0FET0U7RUFDRSxpRkFBQTtFQUNBLFdBQUE7RUFDQSxZQUFBO0FDTEo7QURRRTtFQUNFLGVBQUE7RUFDQSwwQkFBQTtFQUNBLGtCQUFBO0FDTko7QURTTTtFQURGO0lBRUksaUJBQUE7RUNOTjtBQUNGO0FEV0k7RUFDRSxjRWxDQztBRHlCUDtBRFlJO0VBQ0UsY0VoQ0U7QURzQlI7QURhSTtFQUNFLGNFdENDO0FEMkJQO0FEY0k7RUFDRSxjRS9DRztBRG1DVDtBRGVJO0VBQ0UsY0VqRE87QURvQ2I7QURnQkk7RUFDRSxjRS9DRztBRGlDVDtBRG1CQTtFQUNFLGdCRzdEVztBRjZDYjtBRG1CQTtFQUNFLGdCR2hFVTtBRmdEWjtBRG1CQTtFQUNFLGdCR25FUTtBRm1EVjtBRG1CQTtFQUNFLHlCQUFBO0FDaEJGO0FEbUJBO0VBQ0UseUJBQUE7QUNoQkY7QURtQkE7RUFDRSxrQkFBQTtBQ2hCRjtBRG1CQTtFQUNFLGlCR2hGTTtBRmdFUjtBRG1CQTtFQUNFLGVHbkZTO0FGbUVYO0FEbUJBO0VBQ0UsZUdwRlU7QUZvRVo7QURtQkE7RUFDRSxlR3RGTTtBRnNFUjtBRG1CQTtFQUNFLGVHeEZRO0FGd0VWIiwiZmlsZSI6InNyYy9hcHAvcGFnZXMvdHlwb2dyYXBoeS9jb250YWluZXJzL3R5cG9ncmFwaHktcGFnZS90eXBvZ3JhcGh5LXBhZ2UuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyJAaW1wb3J0ICdzcmMvYXBwL3N0eWxlcy9jb2xvcnMnO1xuQGltcG9ydCAnc3JjL2FwcC9zdHlsZXMvdmFyaWFibGVzJztcbkBpbXBvcnQgJ3NyYy9hcHAvc3R5bGVzL2ZvbnQnO1xuXG4udHlwb2dyYXBoeS1jb250ZW50IHtcblxuICAmX193cmFwcGVyIHtcbiAgICBkaXNwbGF5OiBmbGV4O1xuICAgIHBhZGRpbmc6IDAgOHB4O1xuXG4gICAgQG1lZGlhIChtYXgtd2lkdGg6ICRzbWFsbCkge1xuICAgICAgZmxleC13cmFwOiB3cmFwO1xuICAgIH1cbiAgfVxuXG4gICZfX2l0ZW0td3JhcHBlciB7XG4gICAgYm94LXNoYWRvdzogMCAzcHggMTFweCAwICRzaGFkb3ctd2hpdGUsIDAgM3B4IDNweCAtMnB4ICNCMkIyQjIxQSwgMCAxcHggOHB4IDAgIzlBOUE5QTFBO1xuICAgIHdpZHRoOiAxMDAlO1xuICAgIG1hcmdpbjogMTZweDtcbiAgfVxuXG4gICZfX2hlYWRpbmdzLCAmX19jb2xvcnMsICZfX3NldHRpbmdzLCAmX19zaXplIHtcbiAgICBtYXJnaW4tdG9wOiA4cHg7XG4gICAgYm9yZGVyOiAxcHggZGFzaGVkICRibHVlO1xuICAgIHBhZGRpbmc6IDMycHggMTZweDtcblxuICAgIGgxIHtcbiAgICAgIEBtZWRpYSAobWF4LXdpZHRoOiAkc21hbGwpIHtcbiAgICAgICAgbGluZS1oZWlnaHQ6IDQ2cHg7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgJl9fY29sb3JzIHtcbiAgICAmX2JsdWUge1xuICAgICAgY29sb3I6ICRibHVlO1xuICAgIH1cblxuICAgICZfZ3JlZW4ge1xuICAgICAgY29sb3I6ICRncmVlbjtcbiAgICB9XG5cbiAgICAmX3Bpbmsge1xuICAgICAgY29sb3I6ICRwaW5rO1xuICAgIH1cblxuICAgICZfeWVsbG93IHtcbiAgICAgIGNvbG9yOiAkeWVsbG93O1xuICAgIH1cblxuICAgICZfbGlnaHQtYmx1ZSB7XG4gICAgICBjb2xvcjogJGxpZ2h0LWJsdWU7XG4gICAgfVxuXG4gICAgJl92aW9sZXQge1xuICAgICAgY29sb3I6ICR2aW9sZXQ7XG4gICAgfVxuICB9XG59XG5cbi5mdy1saWdodCB7XG4gIGZvbnQtd2VpZ2h0OiAkZnctbGlnaHRlcjtcbn1cblxuLmZ3LW1lZGl1bSB7XG4gIGZvbnQtd2VpZ2h0OiAkZnctbm9ybWFsO1xufVxuXG4uZnctYm9sZCB7XG4gIGZvbnQtd2VpZ2h0OiAkZnctYm9sZDtcbn1cblxuLmZvbnQtdXBwZXJjYXNlIHtcbiAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTtcbn1cblxuLmZvbnQtbG93ZXJjYXNlIHtcbiAgdGV4dC10cmFuc2Zvcm06IGxvd2VyY2FzZTtcbn1cblxuLmZzdC1pdGFsaWMge1xuICBmb250LXN0eWxlOiBpdGFsaWM7XG59XG5cbi5mcy1zbSB7XG4gIGZvbnQtc2l6ZTogJGZzLXhzO1xufVxuXG4uZnMtcmVndWxhciB7XG4gIGZvbnQtc2l6ZTogJGZzLXNtYWxsO1xufVxuXG4uZnMtbWQge1xuICBmb250LXNpemU6ICRmcy1tZWRpdW07XG59XG5cbi5mcy14bCB7XG4gIGZvbnQtc2l6ZTogJGZzLXhsO1xufVxuXG4uZnMteHhsIHtcbiAgZm9udC1zaXplOiAkZnMteHh4bDtcbn1cbiIsIi50eXBvZ3JhcGh5LWNvbnRlbnRfX3dyYXBwZXIge1xuICBkaXNwbGF5OiBmbGV4O1xuICBwYWRkaW5nOiAwIDhweDtcbn1cbkBtZWRpYSAobWF4LXdpZHRoOiA1NzZweCkge1xuICAudHlwb2dyYXBoeS1jb250ZW50X193cmFwcGVyIHtcbiAgICBmbGV4LXdyYXA6IHdyYXA7XG4gIH1cbn1cbi50eXBvZ3JhcGh5LWNvbnRlbnRfX2l0ZW0td3JhcHBlciB7XG4gIGJveC1zaGFkb3c6IDAgM3B4IDExcHggMCAjRThFQUZDLCAwIDNweCAzcHggLTJweCAjQjJCMkIyMUEsIDAgMXB4IDhweCAwICM5QTlBOUExQTtcbiAgd2lkdGg6IDEwMCU7XG4gIG1hcmdpbjogMTZweDtcbn1cbi50eXBvZ3JhcGh5LWNvbnRlbnRfX2hlYWRpbmdzLCAudHlwb2dyYXBoeS1jb250ZW50X19jb2xvcnMsIC50eXBvZ3JhcGh5LWNvbnRlbnRfX3NldHRpbmdzLCAudHlwb2dyYXBoeS1jb250ZW50X19zaXplIHtcbiAgbWFyZ2luLXRvcDogOHB4O1xuICBib3JkZXI6IDFweCBkYXNoZWQgIzUzNkRGRTtcbiAgcGFkZGluZzogMzJweCAxNnB4O1xufVxuQG1lZGlhIChtYXgtd2lkdGg6IDU3NnB4KSB7XG4gIC50eXBvZ3JhcGh5LWNvbnRlbnRfX2hlYWRpbmdzIGgxLCAudHlwb2dyYXBoeS1jb250ZW50X19jb2xvcnMgaDEsIC50eXBvZ3JhcGh5LWNvbnRlbnRfX3NldHRpbmdzIGgxLCAudHlwb2dyYXBoeS1jb250ZW50X19zaXplIGgxIHtcbiAgICBsaW5lLWhlaWdodDogNDZweDtcbiAgfVxufVxuLnR5cG9ncmFwaHktY29udGVudF9fY29sb3JzX2JsdWUge1xuICBjb2xvcjogIzUzNkRGRTtcbn1cbi50eXBvZ3JhcGh5LWNvbnRlbnRfX2NvbG9yc19ncmVlbiB7XG4gIGNvbG9yOiAjM0NENEEwO1xufVxuLnR5cG9ncmFwaHktY29udGVudF9fY29sb3JzX3Bpbmsge1xuICBjb2xvcjogI2ZmNDA4MTtcbn1cbi50eXBvZ3JhcGh5LWNvbnRlbnRfX2NvbG9yc195ZWxsb3cge1xuICBjb2xvcjogI2ZmYzI2MDtcbn1cbi50eXBvZ3JhcGh5LWNvbnRlbnRfX2NvbG9yc19saWdodC1ibHVlIHtcbiAgY29sb3I6ICM3OThERkU7XG59XG4udHlwb2dyYXBoeS1jb250ZW50X19jb2xvcnNfdmlvbGV0IHtcbiAgY29sb3I6ICM5MDEzRkU7XG59XG5cbi5mdy1saWdodCB7XG4gIGZvbnQtd2VpZ2h0OiA0MDA7XG59XG5cbi5mdy1tZWRpdW0ge1xuICBmb250LXdlaWdodDogNTAwO1xufVxuXG4uZnctYm9sZCB7XG4gIGZvbnQtd2VpZ2h0OiA2MDA7XG59XG5cbi5mb250LXVwcGVyY2FzZSB7XG4gIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7XG59XG5cbi5mb250LWxvd2VyY2FzZSB7XG4gIHRleHQtdHJhbnNmb3JtOiBsb3dlcmNhc2U7XG59XG5cbi5mc3QtaXRhbGljIHtcbiAgZm9udC1zdHlsZTogaXRhbGljO1xufVxuXG4uZnMtc20ge1xuICBmb250LXNpemU6IDExLjJweDtcbn1cblxuLmZzLXJlZ3VsYXIge1xuICBmb250LXNpemU6IDE0cHg7XG59XG5cbi5mcy1tZCB7XG4gIGZvbnQtc2l6ZTogMjFweDtcbn1cblxuLmZzLXhsIHtcbiAgZm9udC1zaXplOiAyOHB4O1xufVxuXG4uZnMteHhsIHtcbiAgZm9udC1zaXplOiA0MnB4O1xufSIsIiR5ZWxsb3c6ICNmZmMyNjA7XG4kYmx1ZTogIzUzNkRGRTtcbiRsaWdodC1ibHVlOiAjNzk4REZFO1xuJHdoaXRlLWJsdWU6ICNCMUJDRkY7XG4kYmx1ZS13aGl0ZTogI0YzRjVGRjtcbiRwaW5rOiAjZmY0MDgxO1xuJGRhcmstcGluazogI2ZmMGY2MDtcbiRncmVlbjogIzNDRDRBMDtcbiR2aW9sZXQ6ICM5MDEzRkU7XG4kd2hpdGU6IHdoaXRlO1xuJGRhcmstZ3JleTogIzRBNEE0QTtcbiRsaWdodC1ncmV5OiAjQjlCOUI5O1xuJGdyZXk6ICM2RTZFNkU7XG4kc2t5OiAjYzBjYWZmO1xuXG5cbiR3aGl0ZS0zNTogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjM1KTtcbiR3aGl0ZS04MDogI0ZGRkZGRjgwO1xuXG4kZ3JheS0wODogcmdiYSgxMTAsIDExMCwgMTEwLCAwLjgpO1xuJGdyYXktODA6ICNEOEQ4RDg4MDtcbiRncmF5LTA2OiByZ2JhKDExMCwgMTEwLCAxMTAsIDAuNik7XG5cbiRibGFjay0wODogcmdiYSgwLCAwLCAwLCAwLjA4KTtcblxuJHBpbmstMTU6IHJnYmEoMjU1LCA5MiwgMTQ3LCAwLjE1KTtcbiRibHVlLTE1OiByZ2JhKDgzLCAxMDksIDI1NCwgMC4xNSk7XG4kZ3JlZW4tMTU6IHJnYmEoNjAsIDIxMiwgMTYwLCAwLjE1KTtcbiR5ZWxsb3ctMTU6IHJnYmEoMjU1LCAxOTQsIDk2LCAwLjE1KTtcbiR2aW9sZXQtMTU6IHJnYmEoMTQ0LCAxOSwgMjU0LCAwLjE1KTtcblxuXG4kc2hhZG93LXdoaXRlOiAjRThFQUZDO1xuJHNoYWRvdy1ncmV5OiAjQjJCMkIyMUE7XG4kc2hhZG93LWRhcmstZ3JleTogIzlBOUE5QTFBO1xuXG4kYmFja2dyb3VuZC1jb2xvcjogI0Y2RjdGRjtcbiIsIiRmdy1saWdodGVyOiA0MDA7XG4kZnctbm9ybWFsOiA1MDA7XG4kZnctYm9sZDogNjAwO1xuXG5cbiRmcy14czogMTEuMnB4O1xuJGZzLXNtYWxsOiAxNHB4O1xuJGZzLW5vcm1hbDogMTZweDtcbiRmcy1yZWd1bGFyOiAxOHB4O1xuJGZzLW1lZGl1bTogMjFweDtcbiRmcy1sYXJnZTogMjRweDtcbiRmcy14bDogMjhweDtcbiRmcy14eGw6IDM4cHg7XG4kZnMteHh4bDogNDJweDtcbiJdfQ== */"]
                });
                /*@__PURE__*/

                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](TypographyPageComponent, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
                        args: [{
                            selector: 'app-typography-page',
                            templateUrl: './typography-page.component.html',
                            styleUrls: ['./typography-page.component.scss']
                        }]
                    }], null, null);
                })();
                /***/

            },

        /***/
        "./src/app/pages/typography/typography-routing.module.ts":
            /*!***************************************************************!*\
              !*** ./src/app/pages/typography/typography-routing.module.ts ***!
              \***************************************************************/

            /*! exports provided: TypographyRoutingModule */

            /***/
            function srcAppPagesTypographyTypographyRoutingModuleTs(module, __webpack_exports__, __webpack_require__) {
                "use strict";

                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */


                __webpack_require__.d(__webpack_exports__, "TypographyRoutingModule", function() {
                    return TypographyRoutingModule;
                });
                /* harmony import */


                var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
                    /*! @angular/router */
                    "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
                /* harmony import */


                var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
                    /*! @angular/core */
                    "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */


                var _containers__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
                    /*! ./containers */
                    "./src/app/pages/typography/containers/index.ts");

                var routes = [{
                    path: '',
                    component: _containers__WEBPACK_IMPORTED_MODULE_2__["TypographyPageComponent"]
                }];

                var TypographyRoutingModule = function TypographyRoutingModule() {
                    _classCallCheck(this, TypographyRoutingModule);
                };

                TypographyRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({
                    type: TypographyRoutingModule
                });
                TypographyRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({
                    factory: function TypographyRoutingModule_Factory(t) {
                        return new(t || TypographyRoutingModule)();
                    },
                    imports: [
                        [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]
                    ]
                });

                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](TypographyRoutingModule, {
                        imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]],
                        exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                    });
                })();
                /*@__PURE__*/


                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](TypographyRoutingModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"],
                        args: [{
                            imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forChild(routes)],
                            exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]]
                        }]
                    }], null, null);
                })();
                /***/

            },

        /***/
        "./src/app/pages/typography/typography.module.ts":
            /*!*******************************************************!*\
              !*** ./src/app/pages/typography/typography.module.ts ***!
              \*******************************************************/

            /*! exports provided: TypographyModule */

            /***/
            function srcAppPagesTypographyTypographyModuleTs(module, __webpack_exports__, __webpack_require__) {
                "use strict";

                __webpack_require__.r(__webpack_exports__);
                /* harmony export (binding) */


                __webpack_require__.d(__webpack_exports__, "TypographyModule", function() {
                    return TypographyModule;
                });
                /* harmony import */


                var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(
                    /*! @angular/core */
                    "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
                /* harmony import */


                var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(
                    /*! @angular/common */
                    "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
                /* harmony import */


                var _angular_material_card__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(
                    /*! @angular/material/card */
                    "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/card.js");
                /* harmony import */


                var _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(
                    /*! @angular/material/toolbar */
                    "./node_modules/@angular/material/__ivy_ngcc__/fesm2015/toolbar.js");
                /* harmony import */


                var _containers__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(
                    /*! ./containers */
                    "./src/app/pages/typography/containers/index.ts");
                /* harmony import */


                var _typography_routing_module__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(
                    /*! ./typography-routing.module */
                    "./src/app/pages/typography/typography-routing.module.ts");
                /* harmony import */


                var _shared_shared_module__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(
                    /*! ../../shared/shared.module */
                    "./src/app/shared/shared.module.ts");

                var TypographyModule = function TypographyModule() {
                    _classCallCheck(this, TypographyModule);
                };

                TypographyModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineNgModule"]({
                    type: TypographyModule
                });
                TypographyModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjector"]({
                    factory: function TypographyModule_Factory(t) {
                        return new(t || TypographyModule)();
                    },
                    imports: [
                        [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"], _typography_routing_module__WEBPACK_IMPORTED_MODULE_5__["TypographyRoutingModule"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__["MatToolbarModule"], _shared_shared_module__WEBPACK_IMPORTED_MODULE_6__["SharedModule"]]
                    ]
                });

                (function() {
                    (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsetNgModuleScope"](TypographyModule, {
                        declarations: [_containers__WEBPACK_IMPORTED_MODULE_4__["TypographyPageComponent"]],
                        imports: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"], _typography_routing_module__WEBPACK_IMPORTED_MODULE_5__["TypographyRoutingModule"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__["MatToolbarModule"], _shared_shared_module__WEBPACK_IMPORTED_MODULE_6__["SharedModule"]]
                    });
                })();
                /*@__PURE__*/


                (function() {
                    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](TypographyModule, [{
                        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"],
                        args: [{
                            declarations: [_containers__WEBPACK_IMPORTED_MODULE_4__["TypographyPageComponent"]],
                            imports: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"], _typography_routing_module__WEBPACK_IMPORTED_MODULE_5__["TypographyRoutingModule"], _angular_material_card__WEBPACK_IMPORTED_MODULE_2__["MatCardModule"], _angular_material_toolbar__WEBPACK_IMPORTED_MODULE_3__["MatToolbarModule"], _shared_shared_module__WEBPACK_IMPORTED_MODULE_6__["SharedModule"]]
                        }]
                    }], null, null);
                })();
                /***/

            }
    }
]);
