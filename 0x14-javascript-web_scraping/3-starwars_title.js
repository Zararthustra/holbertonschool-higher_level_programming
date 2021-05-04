#!/usr/bin/node

const episode = process.argv[2];
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + episode;

request(URL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const data = JSON.parse(body);

  console.log(data.title);
});
