#!/usr/bin/node
const list = process.argv.slice(2).map(Number);
let result = 0;
if (list.length < 2) {
  result = 0;
} else {
  let big = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] > big) {
      big = list[i];
    }
    i++;
  }
  i = 0;
  result = 0;
  while (i < list.length) {
    if (result < list[i] && list[i] !== big) {
      result = list[i];
    }
    i++;
  }
}
console.log(result);
