
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
