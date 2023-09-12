#!/usr/bin/node
const noIters = parseInt(process.argv[2]);
if (isNaN(noIters)) console.log('Missing size');
for (let i = 0; i < noIters; i++) {
  console.log('X'.repeat(noIters));
}
