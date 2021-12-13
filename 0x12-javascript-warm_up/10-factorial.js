#!/usr/bin/node
const myArgs = process.argv[2];
function factorial (myArgs) {
  if (isNaN(myArgs) || myArgs === 1) {
    return (1);
  } else {
    return (myArgs * factorial(myArgs - 1));
  }
}
console.log(factorial(parseInt(myArgs)));
