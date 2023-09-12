#!/usr/bin/node
let result = Number.parseInt(process.argv[2])
if (isNaN(result)) console.log("Not a number");
else console.log(result);
