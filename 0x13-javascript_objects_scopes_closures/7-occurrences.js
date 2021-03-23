#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  let i = 0;

  while (list[i]) {
    if (list[i] === searchElement) {
      occ++;
    }
    i++;
  }
  return occ;
}
