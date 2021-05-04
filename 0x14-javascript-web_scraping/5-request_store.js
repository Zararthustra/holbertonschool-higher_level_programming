#!/usr/bin/node

const URL = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(URL, function (error, response, body) {
	if (error) {
		console.error('error:', error);
	}
	
	fs.writeFile(file, body, 'utf-8', function (err) {
		if (err) {
			console.log(err);
		}
	});
});
