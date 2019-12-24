const SerialPort = require('serialport');
const sPort = new SerialPort('/dev/ttyACM0', {
    baudRate: 9600
});

sPort.write('1', (err) => {
    if (err) {
      return console.log('Error on write: ', err.message)
    }
    console.log('message written')
});

sPort.on('error', function(err) {
    console.log('Error: ', err.message)
});
