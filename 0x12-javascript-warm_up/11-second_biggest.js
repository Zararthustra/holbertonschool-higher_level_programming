#!/usr/bin/node
const array = [];
const arg = process.argv;
let i;
let j;
let tmp;
let max;
let second;

i = 2;
j = 0;
while (arg[i]) {
  array[j] = Number(arg[i]);
  i++;
  j++;
}

if (array.length < 2) {
  console.log('0');
} else {
  max = array[0];
  second = array[1];
  if (max < second) {
    tmp = max;
    max = second;
    second = tmp;
  }

  i = 2;
  while (array[i]) {
    if (array[i] >= max) {
      tmp = max;
      max = array[i];
      second = tmp;
    }
    i++;
  }
  console.log(second);
}
