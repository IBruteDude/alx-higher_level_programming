$.get({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json'
}
).done(
  (json) => $('DIV#character').text(json.name)
);
