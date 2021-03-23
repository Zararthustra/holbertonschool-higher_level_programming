#!/usr/bin/node
const Parent = require('./4-rectangle');
class Square extends Parent {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
