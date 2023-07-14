function submitGenre() {
    var genreSelect = document.getElementById('genre');
    var selectedGenre = genreSelect.value;
    if (selectedGenre) {
        alert('Selected genre: ' + selectedGenre);
        // Perform further actions based on the selected genre
    } else {
        alert('Please select a genre.');
    }
}
