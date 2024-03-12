#!/usr/bin/node
const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  let i = 0;
  for (i; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
