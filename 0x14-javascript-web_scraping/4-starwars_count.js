#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(data).results;
    console.log(movies.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
