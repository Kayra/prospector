from bs4 import BeautifulSoup


htmltext = """ 
<!DOCTYPE html>
<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title>Robby Cowell</title>
    <meta name="viewport" content="width=device-width">
    <!--<meta content="width=device-width, initial-scale=1.0" name="viewport"></meta>-->

    <link href="/css/kube.min.css" rel="stylesheet">
    <link href="/css/style.css" rel="stylesheet">
    <link href="/css/social.css" rel="stylesheet">
    <link href="http://fonts.googleapis.com/css?family=Open+Sans|Lato:300" rel="stylesheet" type="text/css">

    <script type="text/javascript" src="../js/vendor/jquery.js"></script>
    <script type="text/javascript" src="../js/vendor/modernizer.js"></script>
    
    <script src="//fightforthefuture.github.io/reset-the-net-widget/widget/rtn.js" async></script>


</head>
<body>
    <section>
        <div class="units-row">
    <div class="unit-centered unit-40 text-centered">
        <img class="circular" src="http://distilleryimage2.ak.instagram.com/b87a33a0cd5a11e3917e0002c99cbb0a_8.jpg">
    </div>
</div>

<div class="units-row">
    <div class="unit-centered unit-40 text-centered">
        <hgroup>
            <h1>Robby Cowell</h1>
            <h1 class="subheading">web developer</h1>
        </hgroup>
        <a href="https://twitter.com/RobbyCowell"><i class="icon-twitter"></i></a>
        <a href="https://github.com/RobbyCowell"><i class="icon-github-circled"></i></a>
        <a href="https://www.linkedin.com/pub/robert-cowell/52/6a/15a"><i class="icon-linkedin"></i></a>
        <a href="mailto:hi@rocoweb.com"><i class="icon-email"></i></a>
    </div>
</div>

<div class="units-row">
    <div class="unit-push-20 unit-30 text-centered">
        <h2>About</h2>
        <p class="about">
        
            Hi, Im Robby Cowell; a web developer based in Bournemouth. Ive been programming
            for 3 years, and have been employed as a Web Developer for about a year. Im currently work as a C#
            .NET developer. I build stuff in Ruby, C#, and
            JavaScript, and am learning C and Android Java; as well as design theory.
            
        </p>
        
        <p class="about">

            Im a regular attendee at local hack events and meet-ups, and also work as a freelance
            developer. Check out my project list to see what Ive worked on. All of the projects were
            designed and built by myself. If youd like to work with me; then Id love to <a href="mailto:hi@rocoweb.com">hear from you</a>.

        </p>
        
        <p class="about">
        
            The technologies I work with are:
            <ul>
                <li>Ruby on Rails</li>
                <li>Sinatra</li>
                <li>AngularJS</li>
                <li>HTML & CSS (SASS)</li>
                <li>Umbraco CMS</li>
                <li>Refinery CMS</li>
                <li>Testing frameworks such as RSpec and NuUnit</li>
            </ul>
  
        </p>
        <p class="about">
        
            In terms of approach, Ive recently adopted the Agile Scrum methodology to my projects, coupled with
            test/behaviour-driven development. I aim to make my code adhere to SOLID and DRY programming principles,
            but do not follow them blindly or dogmatically; I know where to draw the line.
            
            <br>
            <br>
            
            This site is currently under-construction, a blog, better design, and better project list are all in the
            works.

        </p>
    </div>
    <div class="unit-push-20 unit-30 text-centered">
        <h2>Projects</h2>
        <h3 class="subheading">Client projects</h3>
        <p>Harbinger Intelligence (under construction)</p>
        <p>Tiger Trained (<a href="http://tigertrained.com/">visit site</a>)</p>
        <p>Ace Media (<a href="http://ace-media.info/">visit site</a>)</p>
        <p>Torque Productions</p>
        <p>Custom Google Analytics A-B testing platform</p>
        <p>Custom Umbraco 6/7 build</p>
        <h3 class="subheading">Personal projects and hacks</h3>
        <p>Schedulr (<a href="http://hacked.io/">HACKED</a>)</p>
        <p>Try Not to Die (<a href="http://rewiredstate.org/hacks/NHTG14">NHTG 2014</a>)</p>
        <p>UNO CSS Card (<a href="http://hackbmth.org/">HACKBMTH</a>)</p>
    </div>
</div>

    </section>
    <footer></footer>
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
</body>
</html>
"""

soup = BeautifulSoup(htmltext)

h1s = ""
for h1 in soup.find_all('h1'):
	if h1:
		h1s += h1.string + '#'

print "H1 tags: %s" % h1s

h2s = ""
for h2 in soup.find_all('h2'):
	if h2:
		h2s += h2.string + '#'

print "H2 tags: %s" % h2s

h3s = ""
for h3 in soup.find_all('h3'):
	if h3:
		h3s += h3.string + '#'

print "H3 tags: %s" % h3s