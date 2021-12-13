#!/usr/bin/node
const myArgs = process.argv[2];
const args = process.argv[3];
if (!myArgs || !args) {
  console.log('NaN');
} else {
  const sum = parseInt(myArgs) + parseInt(args);
  console.log(sum);
}
