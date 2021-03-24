#!/usr/bin/node
const Square2 = require('./5-square');
module.exports = class Square extends Square2 {
  charPrint (charr) {
    if (charr === undefined) {
      charr = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write(charr);
      }
      console.log('');
    }
  }
};
