#!/usr/bin/node
const $ = window.$;
$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json',
    data => data.results.forEach(result =>
      $('UL#list_movies').append('<li>' + result.title + '</li>')));
});
