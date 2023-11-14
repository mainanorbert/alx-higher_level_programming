#!/usr/bin/node
exports.esrever = function (list) {
  revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revList.push(list[i])
  }
  return revList;
  };
