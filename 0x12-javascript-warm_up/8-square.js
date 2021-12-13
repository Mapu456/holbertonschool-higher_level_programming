#!/usr/bin/node
const myArgs = process.argv[2];
if (!myArgs) {
  console.log('Missing size');
} else if (isNaN(myArgs)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs; i++) {
    console.log('X'.repeat(myArgs));
  }
}
