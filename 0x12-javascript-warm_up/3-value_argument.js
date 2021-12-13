#!/usr/bin/node
const myArgs = process.argv[2];
if (!myArgs) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
