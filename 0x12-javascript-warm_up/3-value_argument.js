#!/usr/bin/node
const firstVar = process.argv[2];
if (firstVar === undefined) {
  console.log('No argument');
} else {
  console.log(firstVar);
}
