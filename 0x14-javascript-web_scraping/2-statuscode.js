#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  console.log('code:', response && response.statusCode);
});
