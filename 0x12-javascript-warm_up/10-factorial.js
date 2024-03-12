#!/usr/bin/node
const n = parseInt(process.argv[2]);
let result = 1;
if (!isNaN(n)) {
  let i = 1;
  for (i; i <= n; i++) {
    result *= i;
  }
} else {
  result = 1;
}
console.log(result);
