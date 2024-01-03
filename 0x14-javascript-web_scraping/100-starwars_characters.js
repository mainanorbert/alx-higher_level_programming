#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi.co/api/films/' + id;
request(url, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(data).characters;
    characters.forEach((character) => {
      request(character, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
