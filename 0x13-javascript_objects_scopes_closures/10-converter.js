#!/usr/bin/node
exports.converter = function (base) {
  return function closure (n) {
    return Number(n).toString(base);
  };
};
