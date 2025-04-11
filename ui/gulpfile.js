/// <binding BeforeBuild='default' />
import gulp from 'gulp';

import yargs from 'yargs'
import { hideBin } from 'yargs/helpers'
const argv = yargs(hideBin(process.argv))
  .option('environment', {
    alias: 'e',
    type: 'string',
    description: 'What environment to build for [production || test]',
    default: 'development',
    demandOption: false
  }).argv;

  console.log(`Environment: ${argv.environment}`);


gulp.task('clean', function () {
    return gulp.src('./public', { read: false, allowEmpty: true })
        .pipe(clean());
});

import clean from 'gulp-clean';
gulp.task('clean', function () {
    return gulp.src('./public', { read: false, allowEmpty: true })
        .pipe(clean());
});

import pug from 'gulp-pug';
gulp.task('pug', function () {
    return gulp.src('./source/pug/pages/**/*.pug')
        .pipe(pug({ pretty: true }))
        .pipe(gulp.dest('./public'));
});

gulp.task('scripts', function () {
    return gulp.src('./source/scripts/**/*.js')
        .pipe(gulp.dest('./public/scripts'));
});

gulp.task('styles', function () {
    return gulp.src('./source/styles/**/*.css')
        .pipe(gulp.dest('./public/styles'));
});

gulp.task('favicon', function () {
    return gulp.src('./source/images/favicon.ico')
        .pipe(gulp.dest('./public'));
});

gulp.task('configurations', function () {
    return gulp.src('./source/configurations/'+argv.environment+'/configuration.js')
        .pipe(gulp.dest('./public/scripts/'))
});

gulp.task('watch', function () {
    gulp.watch('source/pug/**/*.pug', gulp.series('pug'));
    gulp.watch('source/styles/**/*.css', gulp.series('styles'));
    gulp.watch('source/scripts/**/*.js', gulp.series('scripts'));
});

gulp.task('default', gulp.series('clean', 'pug', 'styles', 'scripts', 'configurations','favicon', function (done) {
    done();
}));
