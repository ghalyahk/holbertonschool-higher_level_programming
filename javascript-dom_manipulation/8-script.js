// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // Fetch the "hello" translation in French
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Display the translation in the element with id "hello"
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(function (error) {
      console.error('Error fetching hello:', error);
    });
});
