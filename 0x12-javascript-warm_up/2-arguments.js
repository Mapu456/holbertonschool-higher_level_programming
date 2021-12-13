#!/usr/bin/node
const my_args = process.argv;
console.log(my_args);
if (my_args.length == 2) {
  console.log('No argument');
} else if (my_args.length == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
