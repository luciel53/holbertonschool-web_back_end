const http = require('http');

const app = http.createServer(function(req, res) {
  console.log('Hello Holberton School!');
});
app.listen(1245);
