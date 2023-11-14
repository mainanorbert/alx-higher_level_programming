#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((cnt, currentEle) => {
    if (currentEle === searchElement) {
      return cnt + 1;
    } else {
	    return cnt;
    }
  }, 0)
};
