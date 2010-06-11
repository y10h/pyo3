function putFFUrl(postUrl, user, selector) {
    $.getJSON(
        'http://friendfeed-api.com/v2/url?url='+postUrl+'&from='+user+'&maxcomments=0&maxlikes=0&callback=?',
        function (feed, status) {
            if (feed.entries.length > 0) {
                $(selector+' a').attr('href', feed.entries[0].url);
                $(selector).fadeIn();
            }
        }
    )
}
