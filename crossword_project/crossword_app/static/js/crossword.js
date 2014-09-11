$( document ).ready(function() {
    var prev = $("#prev"),
        next = $("#next"),
        max = 20,
        offset = parseInt(prev.attr('offset')),
        limit = parseInt(next.attr('limit')),
        showHide = function () {
            if (offset === 0) {
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
        getWords = function (url) {
            $.ajax({
                url: url,
                data: {
                    'offset': offset + 20,
                    'limit': limit + 20
                },
                success: function(result){
                    max = result.max;
                    offset += 20;
                    limit += 20;
                    prev.attr('offset', offset);
                    next.attr('limit', limit);
                    showHide();
                }
            });
        };

    showHide();
    $(prev, next).click(function(event) {
        var url = $(event.currentTarget).attr('url');
        getWords(url)
    });
    $(next).click(function() {
        var url = $(event.currentTarget).attr('url');
        getWords(url)
    });
});
