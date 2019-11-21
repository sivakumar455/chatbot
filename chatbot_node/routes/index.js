var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express', _mainContentPartial: 'web/home', pageMeta: { assets: { js: ['/assets/js/home.js'] } } });
});

module.exports = router;
