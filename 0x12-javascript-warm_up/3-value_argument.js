#!/usr/bin/node
// prints the first argument passed to it
// if no argument passed it is undefined
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
