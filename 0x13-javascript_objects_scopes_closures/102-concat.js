#!/usr/bin/node
const fs = require("node:fs");
const f1 = fs.readFileSync(process.argv[2], 'utf-8');
const f2 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(String(process.argv[4]), f1);
fs.appendFileSync(String(process.argv[4]), f2);
