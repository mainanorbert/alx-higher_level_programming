#!/usr/bin/node
const mylist = require('./100-data.js').list;
console.log(mylist);
const newlist = mylist.map((val, idx) => val * idx)
console.log(newlist)
