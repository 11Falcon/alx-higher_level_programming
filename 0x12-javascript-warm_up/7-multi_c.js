#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (arg) {
  let i = 0;
  for (i; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
