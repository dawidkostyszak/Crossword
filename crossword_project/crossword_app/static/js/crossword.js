$( document ).ready(function() {
    var prev = $("#prev"),
        next = $("#next"),
        pagination = $('.paggination'),
        max = 20,
        offset = parseInt(prev.attr('offset')),
        limit = parseInt(next.attr('limit')),
        url = prev.attr('url'),
        showHide = function () {
            if (offset === 20) {
                prev.hide();
            } else {
                prev.show();
            }

            if (limit === (max - 20)) {
                next.hide();
            } else {
                next.show();
            }
        },
        renderWords = function (words) {
            var html,
                table = $('.words');
            table.html('');
            if (words) {
                $.each(words, function(index, word) {
                    html = '<tr class="crossword-table-ingridients-words"><td>' + word.word + '</td>' +
                        '<td>' + word.question + '</td>' +
                        '<td class="difficulty">' + word.difficulty + '</td></tr>';
                    table.append(html);
                });

            } else {
                table.html('<td colspan="3">No existing words.</td>');
            }
        },
        renderQuestions = function (questions) {
            var html,
                table = $('.questions');
            table.html('');
            if (questions) {
                $.each(questions, function (index, question) {
                    html = '<tr class="crossword-table-ingridients-words"><td>' + question.question + '</td>' +
                        '<td class="difficulty">' + question.difficulty + '</td></tr>';
                    table.append(html);
                });
            } else {
                table.html('<td colspan="3">No existing questions.</td>');
            }
        },
        getWords = function (url) {
            $.ajax({
                url: url,
                data: {
                    'offset': offset,
                    'limit': limit
                },
                success: function(result){
                    max = result.max;
                    pagination.text('Page ' + ((offset/20) + 1) + ' of ' + Math.ceil(max/20));
                    offset += 20;
                    limit += 20;
                    prev.attr('offset', offset);
                    next.attr('limit', limit);
                    renderWords(result.words);
                    renderQuestions(result.questions);
                    showHide();
                }
            });
        };

    showHide();
    getWords(url);
    $(prev).click(function() {
        getWords(url)
    });
    $(next).click(function() {
        getWords(url)
    });
});
