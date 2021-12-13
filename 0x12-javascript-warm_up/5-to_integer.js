#!/usr/bin/node
const myArgs = process.argv[2];
if (!myArgs) {
  console.log('Not a number');
} else if (parseInt(myArgs)) {
  console.log('My number: ' + Math.floor(myArgs));
} else {
  console.log('Not a number');
}
