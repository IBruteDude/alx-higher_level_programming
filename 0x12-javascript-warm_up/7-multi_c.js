#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 3) console.log('Missing number of occurrences');
else {
  let noIters = parseInt(argv[2]);

  while (noIters > 0) {
    console.log('C is fun');
    noIters--;
  }
}
