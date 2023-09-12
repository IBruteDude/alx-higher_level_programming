#!/usr/bin/node
let printed = false;

process.argv.slice(2).forEach((variable, value) => { printed = true; console.log(variable); });
if (!printed) console.log('No argument');
