#!/usr/bin/node
const number = parseInt(process.argv[2]);

const fac = function fac (i) {
  if (!(i > 0)) { return 1; }
  return i * fac(i - 1);
};
console.log(fac(number));
