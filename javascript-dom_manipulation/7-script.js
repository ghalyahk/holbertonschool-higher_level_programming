// Fetch the list of Star Wars films
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results; // Array of movie objects
    const ul = document.querySelector('#list_movies');

    // Loop through each movie and create a li element
    movies.forEach(function (movie) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    });
  })
  .catch(function (error) {
    console.error('Error fetching movies:', error);
  });
