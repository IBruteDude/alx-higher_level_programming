#!/usr/bin/node
const SquareBase = require('./5-square');
module.exports = class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = c ?? 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
