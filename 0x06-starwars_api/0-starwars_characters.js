#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let res = await (await request(endpoint)).body;
  res = JSON.parse(res);
  const characters = res.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlcter = characters[i];
    let chart = await (await request(urlcter)).body;
    chart = JSON.parse(chart);
    console.log(chart.name);
  }
}

starwarsCharacters(filmID);
