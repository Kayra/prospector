
class TestHTML:

    def __init__(self):

        self.google_analytics_valid_html = """
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

        self.bing_analytics_valid_html = """
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

        self.header_tag_valid_html = """
            <h1>Test</h1>
            <h2>Test</h2>
            <h3>Test</h3>
            <h4>Test</h4>
            <h5>Test</h5>
            <h6>Test</h6>
        """

        self.alt_tag_valid_html = """
            <img id="test" src="../test/test.png" alt="Test" />
        """

        self.meta_description_valid_html = """
            <meta name="description" content"Test">
        """

        self.title_text_valid_html = """
            <title>Test</title>
        """

        self.view_state_valid_html = """
            <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="Test" />
        """

        self.pagination_valid_html = """
            <link rel="prev" href="http://www.site.com/page1.html"> <link rel="next" href="http://www.site.com/page3.html">
        """

        self.iframe_content_valid_html = """
            <iframe width="960" height="540" src="Test" frameborder="0" allowfullscreen></iframe>
        """

        self.flash_attribute_valid_html = """
            <embed src="Test" quality="high" name="test" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"></embed>
        """

        self.no_index_no_follow_attribute_valid_html = """
            <meta name="robots" content="noindex, nofollow">
        """

        self.schema_tags_valid_html = """
            <div itemscope itemtype="http://schema.org/Movie">
              <h1>Avatar</h1>
              <span>Director: James Cameron (born August 16, 1954)</span>
              <span>Science fiction</span>
              <a href="../movies/avatar-theatrical-trailer.html">Trailer</a>
            </div>
        """
