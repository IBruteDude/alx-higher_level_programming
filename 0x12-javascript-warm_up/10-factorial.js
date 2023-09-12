#!/usr/bin/node
let number = parseInt(process.argv[2]);

let fac = function fac(i) {
	if (!(i > 0))
		return 1;
	return i * fac(i - 1);
}
console.log(fac(number));
