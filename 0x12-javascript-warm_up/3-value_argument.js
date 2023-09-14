#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] === undefined) console.log('No argument');
else args.forEach((variable) => { console.log(variable); });
