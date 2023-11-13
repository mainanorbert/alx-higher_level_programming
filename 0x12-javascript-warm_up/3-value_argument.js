#!/usr/bin/node
const arg1 = process.argv[2];
console.log(typeof arg1 === 'undefined' ? 'No argument' : arg1);
