#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    }
      print () {
       for (let i = 0; i < this.height; i++) {
         let rect = '';
	 for (let x = 0; x < this.width; x++) {
	   rect += "X";
	 }
	   console.log(rect);
       }
      }
  };
