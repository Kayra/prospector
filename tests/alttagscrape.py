from bs4 import BeautifulSoup

htmltext = """
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]-->
<!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--><html lang="en"> <!--<![endif]-->



	<!-- Cheeky message
  ================================================== -->

  <!-- 
	  You may have noticed a lack of copyright notice on my
	  page. If you feel like taking any code, or infact the
	  entire website, go right ahead. 
	  
	  While stealing the whole thing and filling it with your 
	  own content wont exactly help you (and a silly little 
	  bit of text isnt going to stop you), I am a firm believer 
	  in learning from others, so if there is something that 
	  Ive done that you would like to use feel free to
	  take it apart, have fun and make it your own. 
	  
	  If you find something that Ive done wrong, or can be
	  improved upon, Id be very grateful if you could drop me 
	  a message letting me know. 
	  
	  All the code for my website can be found here:
	  
	  https://github.com/Kayra/PersonalSite
  -->


<head>

	<!-- Basic Page Needs
  ================================================== -->
	<meta charset="utf-8">
	<title>Kayra</title>
	<meta name="description" content="Portfolio for Kayra Alat">
	<meta name="author" content="Kayra Alat">

	<!-- Mobile Specific Metas
  ================================================== -->
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

	<!-- CSS
  ================================================== -->
	<link rel="stylesheet" href="/stylesheets/base.css">
	<link rel="stylesheet" href="/stylesheets/skeleton.css">
	<link rel="stylesheet" href="/stylesheets/layout.css">
	<link href=http://fonts.googleapis.com/css?family=Noto+Serif rel=stylesheet type=text/css>
	<link href=http://fonts.googleapis.com/css?family=Merriweather+Sans rel=stylesheet type=text/css>

	<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->

	<!-- Favicons
	================================================== -->
	<link rel="shortcut icon" href="/images/favicon.ico">
	<link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
	<link rel="apple-touch-icon" sizes="72x72" href="/images/apple-touch-icon-72x72.png">
	<link rel="apple-touch-icon" sizes="114x114" href="/images/apple-touch-icon-114x114.png">

	<!-- Scripts
	================================================== -->
	<script type="text/javascript" src="/scripts/jquery-1.10.2.min.js"></script>
	<script type="text/javascript" src="/scripts/bxslider.js"></script>
	<script type="text/javascript" src="/scripts/jquery.form.min.js"></script>
	<script type="text/javascript" src="/scripts/custom.js"></script>
	
	<!-- Fancybox
	================================================== -->
	<link rel="stylesheet" href="/fancybox/jquery.fancybox.css?v=2.1.5" type="text/css" media="screen" />
	<script type="text/javascript" src="/fancybox/jquery.fancybox.pack.js?v=2.1.5"></script>

</head>
<body>


	<!-- Primary Page Layout
	================================================== -->

	<!-- 					HEADER 					-->
	<div class="wrapper blue headerblock">
		<div class="container">
			<section class="sixteen columns">
				<div id="header">
					<h1>kayra</h1>
					<h2>web developer</h2>
					<hr />
					<section class="sixteen columns">
						<nav class="pagenav">
							<ul>
								<li><a href="#ethic" class="scroll">ethic</a></li>
								<li><a href="#work" class="scroll">work</a></li>
								<li><a href="#cv" class="scroll">cv</a></li>
								<li><a href="#contact" class="scroll">contact</a></li>
							</ul>
						</nav>
					</section>
				</div>
			</section>
		</div><!-- container -->
	</div><!-- wrapper -->
		
		
	<!-- 					ABOUTME 					-->
	<a name="aboutme" id="aboutme"></a>
	<div class="wrapper lightblue aboutmeblock">
		<div class="container">
			<section class="sixteen columns">
				<div class="aboutme">
					<img id="bigpicture" src="../images/rubix3.png" class="scale-with-grid" alt="A very artistic and pretentious picture of a Rubix Cube family. " />
					<img id="mediumpicture" src="../images/rubix2.png" class="scale-with-grid" alt="A very artistic and pretentious picture of a Rubix Cube family that is having some problems. " />	
					<img id="smallpicture" src="../images/rubix1.png" class="scale-with-grid" alt="A very artistic and pretentious picture of a Rubix orphan :(. " />	
					<p>Im currently a final year computing student attending Bournemouth university. While I am most interested in solving logical problems (in the form of back-end development), I also enjoy learning about front-end development, design, and user experience; I find it much easier to work when I have an understanding of the bigger picture of web development. <br/> <br/> When Im not at my computer screen, I am lifting heavy objects at the gym, <a class="textlink" target="_blank" href="http://www.youtube.com/watch?v=d9TciGxsCvc">and have been known to do both at the same time.</a> I also enjoy taking my computer screen out of the house <a class="textlink" target="_blank" href="http://hackbmth.org/">every</a> <a class="textlink" target="_blank" href="http://bwmeet.co.uk/">now</a> <a class="textlink" target="_blank" href="http://www.hacksoton.com/">and</a> <a class="textlink" target="_blank" href="http://barcampbournemouth.org/">then.</a> </p>
				</div>
			</section>
		</div><!-- container -->
	</div><!-- wrapper -->
	
	
	<!-- 					ETHIC 					-->
	<a name="ethic" id="ethic"></a> 
	<div class="wrapper purple ethicblock">	
		<div class="container">
			<section class="one-third column">
				<div class="ethic">
					<h2>communication</h2>
					<i class="foundicon-mic"></i>
					<p>I believe communication is one of lifes most important skills. To communicate effectively, all parties should be in complete understanding throughout each stage of a project; not just the beginning.</p>
				</div>
			</section>
			<section class="one-third column">
				<div class="ethic middle">
					<h2>thought</h2>
					<i class="foundicon-idea"></i>
					<p>I like to think out every aspect of a problem before solving it; every action I take will have a reason behind it to maximise the efficiency of my work and the effectiveness of the outcome.</p>
				</div>
			</section>
			<section class="one-third column">
				<div class="ethic">
					<h2>work</h2>
					<i class="foundicon-tools"></i>
					<p>I work incredibly hard for what I believe in. Learning a new programming language, staying up for consecutive nights or starting an entire project completely from scratch; whatever it takes to achieve the perfect result. </p>
				</div>
			</section>
		</div><!-- container -->
	</div><!-- wrapper -->
	
	
	<!-- 					WORK 					-->
	<a name="work" id="work"></a>
	<div class="wrapper green workblock">
		<div class="container">
			<!-- first row -->
			<div class="row">
			<section class="seven columns">
				<div class="workimg first">
					<ul class="slideshow">
						<li><a target="_blank" href="https://play.google.com/store/apps/details?id=mastermind.kayra.com"><img src="../images/mastermind1.gif" class="scale-with-grid" alt="Screenshot of the Mastermind Android application" /></a></li>
						<li><a target="_blank" href="https://play.google.com/store/apps/details?id=mastermind.kayra.com"><img src="../images/mastermind2.gif" class="scale-with-grid" alt="Screenshot of the Mastermind Android application" /></a></li>
						<li><a target="_blank" href="https://play.google.com/store/apps/details?id=mastermind.kayra.com"><img src="../images/mastermind3.gif" class="scale-with-grid" alt="Screenshot of the Mastermind Android application" /></a></li>
					</ul>
				</div>
			</section>
			<section class="nine columns">
				<div class="firstwork">
					<h2><a target="_blank" href="https://play.google.com/store/apps/details?id=mastermind.kayra.com">mastermind ></a></h2>
					<p>Itching to get into mobile app development, I took to bringing the classic Mastermind game to Android screens. A very rewarding experience not only from a learning perspective but also motivationally; it will be a long time before I forget the excitement as I saw my creation brought to life by an actual phone screen. </p>
				</div>
			</section>
			</div>
			<!-- second row -->
			<div class="row middle">
			<section class="nine columns">
				<div class="secondwork">
					<h2><a target="_blank" href="https://github.com/Kayra/Portfolio/blob/master/Search/search.py">super search ></a></h2>
					<p>Growing up in the tech industry you cant help but admire Google. I felt I could learn a lot by putting myself in their shoes, and decided to create a basic search engine. A challenging and interesting way to learn a new language (Python), it only increased my respect for the company and the amount of thought and effort that must go into perfecting their flagship product.</p>
				</div>
			</section>
			<section class="seven columns">
				<div class="workimg second">
					<ul class="static">
						<li><a target="_blank" href="https://github.com/Kayra/Portfolio/blob/master/Search/search.py"><img src="../images/supersearch.png" class="scale-with-grid" alt="Logo to represent how sweet the search engine would look if I made it into a web application" /></a></li>
					</ul>
				</div>
			</section>
			</div>
			<!-- third row -->
			<div class="row middle">
			<section class="seven columns">
				<div class="workimg third">
					<ul class="slideshow">
						<li><a class="fancybox" rel="group" href="../images/scouredbig1.png"><img src="../images/scoured1.png" class="scale-with-grid" alt="Screenshot of the Scoured application" /></a></li>
						<li><a class="fancybox" rel="group" href="../images/scouredbig2.png"><img src="../images/scoured2.png" class="scale-with-grid" alt="Screenshot of the Scoured application" /></a></li>
						<li><a class="fancybox" rel="group" href="../images/scouredbig3.png"><img src="../images/scoured3.png" class="scale-with-grid" alt="Screenshot of the Scoured application" /></a></li>
					</ul>
				</div>
			</section>
			<section class="nine columns">
				<div class="thirdwork">
					<h2>scoured</h2>
					<p>Created during my placement at Redweb, this app saved the search department vast amounts of time by automating a complex task. After being provided a list of websites, scoured would spider said sites and analyse the HTML to find out how much effort had been put in to make the sites SEO friendly. This afforded the search team an easy way to see who was a potential client. </p>
				</div>
			</section>
			</div>
			<!-- forth row -->
			<div class="row middle">
			<section class="nine columns">
				<div class="secondwork">
					<h2><a target="_blank" href="http://simpoll.co.uk/">simpoll ></a></h2>
					<p>Trying to solve the problem of getting meaningful information when asking questions at events, a group of us at Redweb created Simpoll in a two day hack. Using geolocation to position the user and SignalR to ensure compatibility between all phones; Simpoll allows a speaker to ask a question, give listeners the <a class="textlink" href="http://simpoll.co.uk/" >URL</a> and see the results in sixty seconds. </p>
				</div>
			</section>
			<section class="seven columns">
				<div class="workimg forth">
					<ul class="slideshow">
						<li><a target="_blank" href="https://simpoll.co.uk/"><img src="../images/simpoll1.png" class="scale-with-grid" alt="Screenshot of the Simpoll application" /></a></li>
						<li><a target="_blank" href="https://simpoll.co.uk/"><img src="../images/simpoll2.png" class="scale-with-grid" alt="Screenshot of the Simpoll application" /></a></li>
						<li><a target="_blank" href="https://simpoll.co.uk/"><img src="../images/simpoll3.png" class="scale-with-grid" alt="Screenshot of the Simpoll application" /></a></li>
					</ul>
				</div>
			</section>
			</div>
			<!-- fifth row -->
			<div class="row middle">
			<section class="seven columns">
				<div class="workimg fifth">
					<ul class="slideshow">
						<li><a target="_blank" href="https://github.com/Kayra/SimsTwitter/blob/master/simstwitter.py"><img src="../images/sims1.png" class="scale-with-grid" alt="Cover of the first Sims game" /></a></li>
						<li><a target="_blank" href="https://github.com/Kayra/SimsTwitter/blob/master/simstwitter.py"><img src="../images/sims2.png" class="scale-with-grid" alt="Iconic crystal from the Sims franchise" /></a></li>
						<li><a target="_blank" href="https://github.com/Kayra/SimsTwitter/blob/master/simstwitter.py"><img src="../images/sims3.png" class="scale-with-grid" alt="A sim on fire with no escape. Oh dear." /></a></li>
					</ul>
				</div>
			</section>
			<section class="nine columns">
				<div class="thirdwork">
					<h2><a target="_blank" href="https://github.com/Kayra/SimsTwitter/blob/master/simstwitter.py">sims twitter bot ></a></h2>
					<p>My goal with this project was to get to grips with the Twitter API and learn how to host and run code online (in this instance using Heroku). Inspired perhaps by the mental scarring I experienced in my younger years, I created a twitter bot that would tweet creepy messages from The Sims at early hours of the morning hoping to scare anyone still awake. </p>
				</div>
			</section>
			</div>
			<!-- sixth row -->
			<div class="row">
			<section class="nine columns">
				<div class="secondwork">
					<h2><a target="_blank" href="http://hacks.rewiredstate.org/events/National%20Hack%20the%20Government%202014%20Bournemouth/try-not-to-die" >try not to die ></a></h2>
					<p>During a recent <a class="textlink" target="_blank" href="http://hackbmth.org/">HackBmth</a>, we were lucky enough to be provided with data by the council to see what we could come up with. My good friend <a class="textlink" target="_blank" href="http://robbycowell.com/">Robby</a> and I decided to take 5 star food ratings and plot them on map so people could make an educated decision regarding their hunger and personal health. As a result of the hacks created during that weekend, <a class="textlink" target="_blank" href="http://bournemouthdata.io/">bournemouthdata.io</a> was born. </p>
				</div>
			</section>
			<section class="seven columns">
				<div class="workimg sixth">
					<ul class="slideshow">
						<li><a target="_blank" href="http://hacks.rewiredstate.org/events/National%20Hack%20the%20Government%202014%20Bournemouth/try-not-to-die"><img src="../images/try1.png" class="scale-with-grid" alt="Screenshot of the try not to die application" /></a></li>
						<li><a target="_blank" href="http://hacks.rewiredstate.org/events/National%20Hack%20the%20Government%202014%20Bournemouth/try-not-to-die"><img src="../images/try2.png" class="scale-with-grid" alt="Rewired State logo" /></a></li>
						<li><a target="_blank" href="http://bournemouthdata.io/"><img src="../images/try3.png" class="scale-with-grid" alt="Bournemouthdata.io website" /></a></li>
					</ul>
				</div>
			</section>
			</div>
			
			</div>
		</div><!-- container -->
	</div><!-- wrapper -->
	
	
	<!-- 					VIDEO 					-->
	<a name="cv" id="cv"></a>
	<div class="wrapper yellow cvblock">
		<div class="container">
			<section class="sixteen columns">
				<div class="video-container">
					<iframe width="960" height="540" src="//www.youtube.com/embed/2PEXhT-V3Fc?rel=0" frameborder="0" allowfullscreen></iframe>
				</div>
				<div class="cvtext">
					<p> A written copy of my CV is <a target="_blank" class="textlink" href="../KayraAlatWebCV.pdf">also available.</a></p>
				</div>
			</section>
		</div><!-- container -->
	</div><!-- wrapper -->
	
	<!-- 					CONTACT 					-->
	<a name="contact" id="contact"></a>
	<div class="wrapper red contactblock">
		<div class="container">
		<form action="howaremyscraperhomies" method="post" id="contactform">
			<section class="eight columns">
				<input type="text" name="name" placeholder="name" id="name">
			</section>
			<section class="eight columns">
				<input name="email" type="email" placeholder="email">
			</section>
			<section class="sixteen columns">
				<textarea rows="3" placeholder="drop me a message" name="message"></textarea>
			</section>
			<section class="six columns offset-by-ten">
				<input type="submit" value="submit" class="button">
			</section>
		</form>
		</div><!-- container -->
	</div><!-- wrapper -->
	
	
	<!-- 					FOOTER 					-->
	<div class="wrapper blue footerblock">
		<div class="container">
			<section class="sixteen columns">
				<div id="bottomnav">
					<nav class="pagenav">
						<ul>
							<li><a href="#aboutme">about me</a></li>
							<li><a href="#ethic">ethic</a></li>
							<li><a href="#work">work</a></li>
							<li><a href="#cv">cv</a></li>
						</ul>
					</nav>
				</div>
			</section>
			<hr />
			<section class="eight columns">
				<nav class="links">
					<ul>
						<li><a href="#">adventures</a></li>
						<li><a href="#">research and development</a></li>
						<li><a href="#">fitness</a></li>
					</ul>
				</nav>
			</section>
			<section class="eight columns">
				<nav id="social">
					<ul>
						<li><a class="linkedin" target="_blank" href="http://www.linkedin.com/pub/kayra-alat/55/16b/aa6">linkedin</a></li>
						<li><a class="github" target="_blank" href="http://www.github.com/kayra">github</a></li>
						<li><a class="twitter" target="_blank" href="http://www.twitter.com/kayraalat">twitter</a></li>
						<li><a class="google" target="_blank" href="http://www.google.com/+KayraAlat">google</a></li>
					</ul>
				</nav>
			</section>
		</div>
	</div>
	


<!-- End Document
================================================== -->
</body>
</html>"""

soup = BeautifulSoup(htmltext)

alttags = ""
for alttag in soup.find_all('img'):
	if alttag:
		alttags += alttag['alt'] + '#'

print alttags

#List split test
alttags = alttags.split('#')

print alttags