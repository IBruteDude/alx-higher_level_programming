#!/usr/bin/node
const { argv } = require('node:process');

const result = Number.parseInt(argv[2]);
if (isNaN(result)) console.log('Not a number');
else console.log('My number: ' + result.toString());
