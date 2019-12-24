const Gpio = require('onoff').Gpio;
const LEDPin = new Gpio(22, 'out');
const fs = require('fs');
const https = require('https').createServer((req, res) => {
    fs.readFile(__dirname + '/index.html', function (err, data) { //read html file
        if (err) {
          res.writeHead(500);
          return res.end('Error loading socket.io.html');
        }
    })
})