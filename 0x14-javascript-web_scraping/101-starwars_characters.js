#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/';
request(baseUrl + 'films/' + id, (err, res, data) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(data).characters;
    if (characters.length === 0) {
      console.log('no characters');
    }
    characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, data) => {
        if (err) {
          console.log(err);
        } else {
          const charData = JSON.parse(data);
          console.log(charData.name);
        }
      });
    });
  }
});
