#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
const wedge = '18';

request(URL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  const results = JSON.parse(body).results;
  let count = 0;
  let i = 0;

  for (i; i < results.length; i++) {
    const characters = results[i].characters;
    let j = 0;

    for (j; j < characters.length; j++) {
      if (characters[j].includes(wedge)) {
        count++;
      }
    }
  }

  console.log(count);
});
