
google_analytics_valid_html = """
    <script>
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
            m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
        ga('create', 'UA-49558923-1', 'robbycowell.com');
        ga('send', 'pageview');
    </script>

    <script type="text/javascript">
        var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
        document.write(unescape("3Cscript src='" + gaJsHost + "googleanalytics.com/ga.js' type='text/javascript'3E3C/script3E"));
    </script>

    <script type="text/javascript">
        var pageTracker = _gat._getTracker("UA-1234567-8");
        pageTracker._setLocalRemoteServerMode();
        pageTracker._trackPageview();
    </script>

    <script src="/urchin.js" type="text/javascript"></script>

    <script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>

    <script type="text/javascript">
    _uacct = "UA-1234567-8";
    _userv = 2;
    urchinTracker();
    </script>
"""

bing_analytics_valid_html = """
    <head>
        <meta name="msvalidate.01" content="67432G234FR634H326543F" />
    </head>

    <body>
    <script type="text/javascript">
        if (!window.mstag)
        mstag = {loadTag : function(){},time
    </script>
    </body>
"""

header_tag_valid_html = """
    <h1>Test</h1>
    <h2>Test</h2>
    <h3>Test</h3>
    <h4>Test</h4>
    <h5>Test</h5>
    <h6>Test</h6>
"""

alt_tag_valid_html = """
    <img id="test" src="../test/test.png" alt="Test" />
"""

meta_description_valid_html = """
    <meta name="description" content"Test">
"""

title_text_valid_html = """
    <title>Test</title>
"""

view_state_valid_html = """
    <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="Test" />
"""

pagination_valid_html = """
    <link rel="prev" href="http://www.site.com/page1.html"> <link rel="next" href="http://www.site.com/page3.html">
"""

iframe_content_valid_html = """
    <iframe width="960" height="540" src="Test" frameborder="0" allowfullscreen></iframe>
"""

flash_attribute_valid_html = """
    <embed src="Test" quality="high" name="test" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>
"""

no_index_no_follow_attribute_valid_html = """
    <meta name="robots" content="noindex, nofollow">
"""

schema_tags_valid_html = """
    <div itemscope itemtype="http://schema.org/Movie">
      <h1>Avatar</h1>
      <span>Director: James Cameron (born August 16, 1954)</span>
      <span>Science fiction</span>
      <a href="../movies/avatar-theatrical-trailer.html">Trailer</a>
    </div>
"""

blog_location_valid_html = """
    <ul>
        <li><a href="#">blog</a></li>
        <li><a href="blog">research and development</a></li>
        <li><a href="#">fitness</a></li>
    </ul>
"""

number_of_internal_links_valid_url = "www.test.com"

number_of_internal_links_valid_html = """
    <a href="/">valid</a>
    <a href="test.com">valid</a>
    <a href="www.test.com">valid</a>
    <a href="http://www.test.com">valid</a>
    <a href="http://test.com">valid</a>
    <a href="https://www.test.com">valud</a>
    <a href="https://test.com">valid</a>
    <a href="http://google.com">invalid</a>
    <a href="gnrioiwo3253456;'t?%$G$TW">invalid</a>
    <a href="">invalid</a>
"""
