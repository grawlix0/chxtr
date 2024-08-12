const http = require("http");
const fs = require("fs");

// const hostname = "127.0.0.1";
const hostname = "192.168.145.155";
const port = 3000;

const server = http.createServer((req, res) => {
  fs.readFile("./output/out.txt", "utf8", (err, data) => {
    if (err) {
      res.statusCode = 500;
      res.setHeader("Content-Type", "text/plain");
      res.end("Error reading file");
    } else {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/plain");
      res.end(data);
    }
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
