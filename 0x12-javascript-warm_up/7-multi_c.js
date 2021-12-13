#!/usr/bin/node
const myArgs = process.argv[2];
if (!myArgs) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArgs; i++) {
    console.log('C is fun');
  }
}
