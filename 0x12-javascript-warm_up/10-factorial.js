#!/usr/bin/node
let i = parseInt(process.argv[2]);
let prod = 1;

while (i > 0) {
	prod *= i;
	i--;
}
console.log(prod);
