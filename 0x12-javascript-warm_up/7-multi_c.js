#!/usr/bin/node
let i;

const my_args = process.argv[2];
if (!my_args) {
	console.log('Missing number of occurrences');
} else {
	for (i = 0; i < my_args; i++) {
		console.log('C is fun');
	}
}
