#!/usr/bin/node
const request = require('request');
const swapi = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get({ url: swapi }, function (error, response, body) {
  if (error) console.error(error);
  const chars = JSON.parse(body).characters;
  for (const charapi of chars) {
    request.get({ url: charapi }, function (error, response, body) {
      if (error) console.error(error);
      console.log(JSON.parse(body).name);
    });
  }
});
