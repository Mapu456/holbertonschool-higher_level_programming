#!/usr/bin/node
const my_args = process.argv[2];
if (!my_args) {
	console.log('No argument');
} else {
	console.log(my_args);
}
