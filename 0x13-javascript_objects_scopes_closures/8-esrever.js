#!/usr/bin/node
exports.esrever = function (list) {
  const rev = new Array;
  let i = list.length - 1;

  while ( i >= 0) {
    rev.push(list[i]);
    i--;
  }
  return rev;
}
