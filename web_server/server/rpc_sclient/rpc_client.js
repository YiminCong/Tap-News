var jayson = require('jayson');

// create a client
var client = jayson.client.http({
  hostname: 'localhost',
  port: 4040
});

// Test Rpc method
function add(a, b, callback) {
  client.request('add', [a, b], function(err, response) {
    if(err) throw err;
    callback(response.result);
  });
};


function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, response) {
    if(err) throw err;
    callback(response.result);
  });
};

function logNewsClickForUser(user_id, news_id) {
  client.request('logNewsClickForUser', [user_id, news_id], function(err, response) {
    if(err) throw err;
  });
};

module.exports = {
  add : add,
  getNewsSummariesForUser : getNewsSummariesForUser,
  logNewsClickForUser : logNewsClickForUser
};