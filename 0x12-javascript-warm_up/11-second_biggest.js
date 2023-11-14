#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let myArgs = args.slice(2).map(Number);
  myArgs = myArgs.sort((a, b) => b - a);
  console.log(myArgs[1]);
}
