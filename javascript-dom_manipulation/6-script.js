// Fetch the Star Wars character data
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    // Display the character name in the div with id character
    document.querySelector('#character').textContent = data.name;
  });
