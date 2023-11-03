$.get({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json'
}
).done(
  (response) => {
    const movies = response.results;
    for (const movie of movies) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  }
);
