#!/usr/bin/node
const string = 'My number: ';
const num = Number(process.argv[2]);

if (num) {
  console.log(string + num);
} else {
  console.log('Not a number');
}
