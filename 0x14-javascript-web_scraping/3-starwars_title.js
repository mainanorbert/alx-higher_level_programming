#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
req(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
