$(document).ready(function() {
    var searchInput = $('#search');
    var searchIcon = $('#search-icon');
    var searchResults = $('#search-results');

    function performSearch(query) {
        $.get('/search-food/?query=' + query, function(data) {
            searchResults.empty();
            if (data.results.length === 0) {
                searchResults.append('<p>No results found.</p>');
            } else {
                $.each(data.results, function(index, item) {
                    var resultItem = $('<div class="search-result-item"><a href="' + item.url + '">' + item.name + '</a></div>');
                    searchResults.append(resultItem);
                });
            }
        });
    }

    searchInput.on('input', function() {
        var query = $(this).val();
        if (query.length >= 3) {
            performSearch(query);
        } else {
            searchResults.empty();
        }
    });

    // Handle Enter key press
    searchInput.on('keydown', function(event) {
        if (event.keyCode === 13) {  // Enter key
            // Redirect to the first search result's URL
            var firstResultLink = searchResults.find('a:first');
            if (firstResultLink.length > 0) {
                window.location.href = firstResultLink.attr('href');
            }
        }
    });

    // Handle click on the search icon
    searchIcon.on('click', function() {
        var query = searchInput.val();
        if (query.length >= 3) {
            performSearch(query);
        }
    });
});