const SerialPort = require('serialport');
const readline = require('readline');
const sPort = new SerialPort('/dev/ttyACM0', {
    baudRate: 9600
});
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let i = '';
// while (true) {
const askInput = async () => {
    rl.question('Type input ', (ans) => {
        if (ans == 'exit') {
            return rl.close();
        }
        i = ans;
        sPort.write(i, (err) => {
            if (err) {
              return console.log('Error on write: ', err.message)
            }
            console.log('msg written \n')
        });
        sPort.on('error', function(err) {
            console.log('Error: ', err.message)
        });
        askInput();
    });
}

askInput();
// }
