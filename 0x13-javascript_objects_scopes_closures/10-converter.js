#!/usr/bin/node
exports.converter = function (base) {
  return myNum => myNum.toString(base);
};
