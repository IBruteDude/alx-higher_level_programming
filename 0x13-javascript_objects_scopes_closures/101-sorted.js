#!/usr/bin/node
let data = require("./101-data").dict;
let obj = {};
if (data) {
	for (let element in data) {
		if (obj[data[element]]) {
			obj[data[element]].push(element);
		} else {
			obj[data[element]] = [element];
		}
	};
}
console.log(obj);
