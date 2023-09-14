#!/usr/bin/node
const data = require('./101-data').dict;
const obj = {};
if (data) {
  for (const element in data) {
    if (obj[data[element]]) {
      obj[data[element]].push(element);
    } else {
      obj[data[element]] = [element];
    }
  }
}
console.log(obj);
