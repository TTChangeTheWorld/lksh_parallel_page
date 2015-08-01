dictionary = {
    "load" : function(showTags) {
        $.getJSON('data/dictionary.json', function(words) {
            var searchResults = $('.sis-dictionary .search-results').empty();

            words.sort(function(a, b) {
                if (a.word < b.word) return -1;
                if (a.word > b.word) return 1;
                return 0;
            });

            addedWords = {};
            for (var i = 0; i < words.length; ++i) {
                var show = false;
                for (var sti = 0; sti < showTags.length; ++sti) {
                    var tag = showTags[sti];
                    if ($.inArray(tag, words[i].tags) !== -1) {
                        show = true;
                        break;
                    }
                }

                if (show) {
                    if (typeof(addedWords[words[i].word]) === "undefined") {
                        addedWords[words[i].word] = $('<tr>').append(
                            $('<td>').html(words[i].word)
                        ).append(
                            $('<td>').html(words[i].translation)
                        ).appendTo(searchResults);
                    } else {
                        // Add tags
                    }
                }
            }

            var searchFieldContent = '';
            var res = $('.sis-dictionary .search-field').on('change keydown paste input', function() {
                var newSearchFieldContent = this.value.toLowerCase();
                if (newSearchFieldContent !== searchFieldContent) {
                    searchFieldContent = newSearchFieldContent;
                    $('.sis-dictionary .search-results').children().each(function(tr) {
                        // Check for substring
                        if ($(this).text().toLowerCase().indexOf(searchFieldContent) === -1) {
                            $(this).addClass('hide');
                        } else {
                            $(this).removeClass('hide');
                        }
                    });
                }
            });
        })
    }
};
