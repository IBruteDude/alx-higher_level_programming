#!/usr/bin/node
const { argv } = require('node:process');
let i = parseInt(argv[2]);
let prod = 1;

while (i > 0) {
	prod *= i;
	i--;
}
console.log(prod);
