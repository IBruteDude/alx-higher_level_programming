#!/usr/bin/node
let data = require('./100-data').list;
if (data) {
  console.log(data);
  data = data.map((val, idx) => val * idx);
  console.log(data);
}
