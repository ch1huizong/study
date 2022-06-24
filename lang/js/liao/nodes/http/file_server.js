'use strict';

const 
  fs = require('fs'),
  url = require('url'),
  path = require('path'),
  http = require('http');

var root = path.resolve(process.argv[2] || '.');

console.log('Static root dir: ' + root);

var server = http.createServer(function(request, response) {
  var pathname = url.parse(request.url).pathname;
  var filepath = path.join(root, pathname);

  fs.stat(filepath, function(err, stats) {
    if (!err && stats.isFile()) {
      console.log('200 ' + request.url);
      response.writeHead(200);
      fs.createReadStream(filepath).pipe(response); // good!
    } else if (!err && stats.isDirectory()){
      console.log('200 ' + request.url);
      response.writeHead(200);

      if(fs.existsSync(path.join(filepath, 'index.html'))) {
        fs.createReadStream(path.join(filepath, 'index.html')).pipe(response) 
      } else if(fs.existsSync(path.join(filepath, 'default.html'))) {
        fs.createReadStream(path.join(filepath, 'default.html')).pipe(response) 
      } else {
        console.log('444 ' + request.url);
        response.writeHead(444);
        response.end('444 Request Others');
      }
    } else {
      console.log('404 ' + request.url);
      response.writeHead(404);
      response.end('404 Not Found');
    }
  });
});

server.listen(9999);
console.log('Server is running at http://127.0.0.1:9999/');
