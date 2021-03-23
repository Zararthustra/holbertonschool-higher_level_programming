#!/usr/bin/node
const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    let i = 0;

    while (i < this.width) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
      i++;
    }
  }
}
module.exports = Square;
