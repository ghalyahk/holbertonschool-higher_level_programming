// When clicking on the element with id update_header
document.querySelector('#update_header').addEventListener('click', function () {
  // Update the header text
  document.querySelector('header').textContent = 'New Header!!!';
});
