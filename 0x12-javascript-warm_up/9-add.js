#!/usr/bin/node
// Prints the addition of 2 integers using a defined function

const add = (a, b) => a + b;

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (isNaN(arg1) || isNaN(arg2)) {
  console.log('Missing or invalid input. Please provide two integers.');
} else {
  console.log(add(arg1, arg2));
}
