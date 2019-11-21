var express = require('express');
var router = express.Router();

var path = require('path');

/* GET js assets */
router.get('/js/:file', function(req, res, next) {
  let fileName = req.params.file;
  res.sendFile(path.join(__dirname, "../assets/js", fileName));
});

/* GET js assets */
router.get('/css/:file', function(req, res, next) {
  let fileName = req.params.file;
  res.sendFile(path.join(__dirname, "../assets/css/", fileName));
});

module.exports = router;
