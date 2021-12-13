#!/usr/bin/node
let maxSecond = 0;
const myArgs = process.argv.slice(2);
if (myArgs.length > 1) {
  myArgs.sort();
  maxSecond = myArgs[myArgs.length - 2];
}
console.log(maxSecond);
