'use strict'

var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var sass = require('gulp-sass');
var del = require('del');
var replace = require('gulp-replace');
var injectPartials = require('gulp-inject-partials');
var inject = require('gulp-inject');
var sourcemaps = require('gulp-sourcemaps');
var concat = require('gulp-concat');
var merge = require('merge-stream');



gulp.task('sass', function () {
    return gulp.src('./scss/**/style.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({outputStyle: 'expanded'}).on('error', sass.logError))
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest('./css'))
        .pipe(browserSync.stream());
});

// Static Server + watching scss/html files
gulp.task('serve', gulp.series('sass', function() {

    browserSync.init({
        port: 3001,
        server: "./",
        ghostMode: false,
        notify: false
    });

    gulp.watch('scss/**/*.scss', gulp.series('sass'));
    gulp.watch('**/*.html').on('change', browserSync.reload);
    gulp.watch('js/**/*.js').on('change', browserSync.reload);

}));



// Static Server without watching scss files
gulp.task('serve:lite', function() {

    browserSync.init({
        server: "./",
        ghostMode: false,
        notify: false
    });

    gulp.watch('**/*.css').on('change', browserSync.reload);
    gulp.watch('**/*.html').on('change', browserSync.reload);
    gulp.watch('js/**/*.js').on('change', browserSync.reload);

});


/* inject partials like sidebar and navbar */
gulp.task('injectPartial', function () {
  return gulp.src("./**/*.html", { base: "./" })
    .pipe(injectPartials())
    .pipe(gulp.dest("."));
});



/* inject Js and CCS assets into HTML */
gulp.task('injectCommonAssets', function () {
  return gulp.src('./**/*.html')
    .pipe(inject(gulp.src([ 
        './vendors/mdi/css/materialdesignicons.min.css',
        './vendors/base/vendor.bundle.base.css', 
        './vendors/base/vendor.bundle.base.js',
        
    ], {read: false}), {name: 'base', relative: true}))
    .pipe(inject(gulp.src([
        './css/*.css', 
        './js/template.js',
    ], {read: false}), {relative: true}))
    .pipe(gulp.dest('.'));
});

/* inject Js and CCS assets into HTML */
gulp.task('injectLayoutStyles', function () {
    return gulp.src('./**/*.html')
        .pipe(inject(gulp.src([
            './css/style.css', 
        ], {read: false}), {relative: true}))
        .pipe(gulp.dest('.'));
});

/*replace image path and linking after injection*/
gulp.task('replacePath', function(){
    var replacePath1 = gulp.src(['./pages/*/*.html'], { base: "./" })
        .pipe(replace('="images/', '="../../images/'))
        .pipe(replace('href="pages/', 'href="../../pages/'))
        .pipe(replace('href="docs/', 'href="../../docs/'))
        .pipe(replace('href="index.html"', 'href="../../index.html"'))
        .pipe(gulp.dest('.'));
    var replacePath2 = gulp.src(['./pages/*.html'], { base: "./" })
        .pipe(replace('="images/', '="../images/'))
        .pipe(replace('"pages/', '"../pages/'))
        .pipe(replace('href="index.html"', 'href="../index.html"'))
        .pipe(gulp.dest('.'));
    var replacePath3 = gulp.src(['./index.html'], { base: "./" })
        .pipe(replace('="images/', '="images/'))
        .pipe(gulp.dest('.'));
    return merge(replacePath1, replacePath2, replacePath3);
});

/*sequence for injecting partials and replacing paths*/
gulp.task('inject', gulp.series('injectPartial' , 'injectCommonAssets' , 'injectLayoutStyles', 'replacePath'));

gulp.task('clean:vendors', function () {
    return del([
      'vendors/**/*'
    ]);
});

/*Building vendor scripts needed for basic template rendering*/
gulp.task('buildBaseVendorScripts', function() {
    return gulp.src([
        './node_modules/jquery/dist/jquery.min.js', 
        './node_modules/popper.js/dist/umd/popper.min.js', 
        './node_modules/bootstrap/dist/js/bootstrap.min.js', 
        './node_modules/perfect-scrollbar/dist/perfect-scrollbar.min.js'
    ])
      .pipe(concat('vendor.bundle.base.js'))
      .pipe(gulp.dest('./vendors/base'));
});

/*Building vendor styles needed for basic template rendering*/
gulp.task('buildBaseVendorStyles', function() {
    return gulp.src(['./node_modules/perfect-scrollbar/css/perfect-scrollbar.css'])
      .pipe(concat('vendor.bundle.base.css'))
      .pipe(gulp.dest('./vendors/base'));
});

/*Scripts for addons*/
gulp.task('copyAddonsScripts', function() {
    var aScript1 = gulp.src(['node_modules/chart.js/dist/Chart.min.js'])
        .pipe(gulp.dest('./vendors/chart.js'));
    var aScript2 = gulp.src(['node_modules/justgage/raphael-2.1.4.min.js'])
        .pipe(gulp.dest('./vendors/justgage'));
    var aScript3 = gulp.src(['node_modules/justgage/justgage.js'])
        .pipe(gulp.dest('./vendors/justgage'));
    var aScript4 = gulp.src(['node_modules/raphael/raphael.min.js'])
        .pipe(gulp.dest('./vendors/raphael'));
    var aScript13 = gulp.src(['node_modules/jvectormap/jquery-jvectormap.min.js'])
        .pipe(gulp.dest('./vendors/jvectormap'));
    var aScript14 = gulp.src(['node_modules/jvectormap/tests/assets/jquery-jvectormap-world-mill-en.js'])
        .pipe(gulp.dest('./vendors/jvectormap'));
    var aScript18 = gulp.src(['node_modules/chartjs-plugin-datalabels/dist/**/*'])
        .pipe(gulp.dest('./vendors/chartjs-plugin-datalabels'));
    var aScript19 = gulp.src(['node_modules/progressbar.js/dist/progressbar.min.js'])
        .pipe(gulp.dest('./vendors/progressbar.js'));
    var aScript20 = gulp.src(['node_modules/typeahead.js/dist/typeahead.bundle.min.js'])
        .pipe(gulp.dest('./vendors/typeahead.js'));
    var aScript21 = gulp.src(['node_modules/select2/dist/js/select2.min.js'])
        .pipe(gulp.dest('./vendors/select2'));
    return merge(aScript1, aScript2, aScript3, aScript4, aScript13, aScript14, aScript18, aScript19, aScript20, aScript21);
});


/*Styles for addons*/
gulp.task('copyAddonsStyles', function() {
    var aStyle1 = gulp.src(['./node_modules/@mdi/font/css/materialdesignicons.min.css'])
        .pipe(gulp.dest('./vendors/mdi/css'));
    var aStyle2 = gulp.src(['./node_modules/@mdi/font/fonts/*'])
        .pipe(gulp.dest('./vendors/mdi/fonts'));
    var aStyle9 = gulp.src(['node_modules/jvectormap/jquery-jvectormap.css'])
        .pipe(gulp.dest('./vendors/jvectormap'));
    var aStyle10 = gulp.src(['node_modules/select2/dist/css/select2.min.css'])
        .pipe(gulp.dest('./vendors/select2')); 
    var aStyle11 = gulp.src(['node_modules/select2-bootstrap-theme/dist/select2-bootstrap.min.css'])
        .pipe(gulp.dest('./vendors/select2-bootstrap-theme'));
    var aStyle12 = gulp.src(['node_modules/jquery-file-upload/css/uploadfile.css'])
        .pipe(gulp.dest('./vendors/jquery-file-upload'));
    return merge(aStyle1, aStyle2, aStyle9, aStyle10, aStyle11, aStyle12);
});

//Copy essential map files
gulp.task('copyMapFiles', function() {
    var map1 = gulp.src('node_modules/bootstrap/dist/js/bootstrap.min.js.map')
        .pipe(gulp.dest('./vendors/base'));
    var map2 = gulp.src('node_modules/@mdi/font/css/materialdesignicons.min.css.map')
        .pipe(gulp.dest('./vendors/mdi/css'));
    var map3 = gulp.src('node_modules/progressbar.js/dist/progressbar.min.js.map')
        .pipe(gulp.dest('./vendors/progressbar.js'));
    return merge(map1, map2, map3);
});

/*sequence for building vendor scripts and styles*/
gulp.task('bundleVendors', gulp.series('clean:vendors', 'buildBaseVendorStyles','buildBaseVendorScripts', 'copyAddonsStyles', 'copyAddonsScripts', 'copyMapFiles'));

gulp.task('default', gulp.series('serve'));
