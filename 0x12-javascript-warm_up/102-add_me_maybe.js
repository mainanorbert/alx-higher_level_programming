#!/usr/bin/node
exports.incrFunc = function (number, theFunction) {
	theFunction(++number);
};
