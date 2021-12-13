#!/usr/bin/node
const my_args = process.argv[2];
if (!my_args) {
	console.log('Not a number');
} else if (parseInt(my_args)) {
	console.log('My number: ' + Math.floor(my_args));
} else {
	console.log('Not a number');
}
