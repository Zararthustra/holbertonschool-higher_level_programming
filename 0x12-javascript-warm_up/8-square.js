#!/usr/bin/node
const size = Number(process.argv[2]);
let i = 0;

if (!Number(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
