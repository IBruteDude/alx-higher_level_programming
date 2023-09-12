#!/usr/bin/node
if (process.argv.length < 3) console.log('Missing size');
else {
  const noIters = parseInt(process.argv[2]);

  for (let i = 0; i < noIters; i++) {
    console.log('X'.repeat(noIters));
  }
}
