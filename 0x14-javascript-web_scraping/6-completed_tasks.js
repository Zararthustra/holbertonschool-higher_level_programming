#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    const dict = {};
    let i = 0;

    for (i; i < json.length; i++) {
      if (!(json[i].userId in dict)) {
        if (json[i].completed === true) {
          dict[json[i].userId] = 0;
        }
      }
      if (json[i].completed === true) {
        dict[json[i].userId] += 1;
      }
    }

    console.log(dict);
  }
});
