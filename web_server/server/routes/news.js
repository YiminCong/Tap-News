var express = require('express');
var rpc_client = require('../rpc_client/rpc_client');
var router = express.Router();

/* GET users listing. */
router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
  user_id = req.params['userId'];
  page_num = req.params['pageNum'];

  rpc_client.getNewsSummariesForUser(user_id, page_num, function(response) {
    res.json(response);
  });
});

router.post('/userId/:userId/newsId/:newsId', function(req, res, next) {
  user_id = req.params['userId'];
  newsId = req.params['newsId'];

  rpc_client.logNewsClickForUser(user_id, newsId);
  res.status(200);
});

module.exports = router;
