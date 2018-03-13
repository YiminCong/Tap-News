var client = require('./rpc_client');

// mongoexport --db news --collection news --out a.json
// mongoinmport --db --test --collection test --file /Users/congyimin/Desktop/a.js
// invoke 'add'
client.add(1, 2, function(response) {
  console.assert(response == 3);
});