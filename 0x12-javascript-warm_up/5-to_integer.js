#!/usr/bin/node
const number = process.argv[2];
if (!isNaN(parseInt(number))) {
  console.log(`My number: ${parseInt(number)}`);
} else {
  console.log('Not a number');
}
