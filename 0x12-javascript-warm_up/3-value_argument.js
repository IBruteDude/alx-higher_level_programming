#!/usr/bin/node
const { argv } = require('node:process');

let printed = false;

argv.slice(2).forEach((variable, value) => {printed = true; console.log(variable);});
if (!printed) console.log('No argument');
