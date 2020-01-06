const { Client } = require('node-osc');
const client = new Client('127.0.0.1', 5005);

setInterval(function() {
    client.send('/info', "Hello This is Osc Test from Node.js");
    console.log("osc msg send");
}, 500);