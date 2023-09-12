#!/usr/bin/node
if (process.argv.length < 3) console.log('Missing number of occurrences');
else {
  let noIters = parseInt(process.argv[2]);

  while (noIters > 0) {
    console.log('C is fun');
    noIters--;
  }
}
