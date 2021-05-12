#!/usr/bin/node
const $ = window.$;
$(document).ready(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr',
    data => $('#hello').text(data.hello));
});
