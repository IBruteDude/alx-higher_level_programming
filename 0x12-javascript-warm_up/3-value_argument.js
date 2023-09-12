#!/usr/bin/node
args = process.argv.slice(2)
if (!args[2]) console.log('No argument');
args.forEach((variable, value) => { printed = true; console.log(variable); });
