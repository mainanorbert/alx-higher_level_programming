#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedgeAntId = 18;
request(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(data).results;
    const wAntM = movies.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntId}/`);
    });
    console.log(wAntM.length);
  }
});
