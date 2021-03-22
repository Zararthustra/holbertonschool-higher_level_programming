#!/usr/bin/node
const string = 'C is fun';
const times = Number(process.argv[2]);
let i = 0;

if (!Number(times)) {
  console.log('Missing number of occurrences');
} else {
  while (i < times) {
    console.log(string);
    i++;
  }
}
