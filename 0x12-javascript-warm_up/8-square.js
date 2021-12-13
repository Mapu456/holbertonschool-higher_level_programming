#!/usr/bin/node
let i;

const my_args = process.argv[2];
if (!my_args) {
	console.log('Missing size');
} else if (isNaN(my_args)) {
	console.log('Missing size');
}
else {
	for (i = 0; i < my_args; i++) {
		console.log('X'.repeat(my_args));
	}
}
