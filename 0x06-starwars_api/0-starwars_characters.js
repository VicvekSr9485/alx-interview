#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const index = 0;
    const data = JSON.parse(body).characters;

    printCharacters(data, index);
  }
});
const printCharacters = function (url, index) {
  request(url[index], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const charactersNames = JSON.parse(body);
      console.log(charactersNames.name);
    }

    if (++index < url.length) {
      printCharacters(url, index++);
    }
  });
};
