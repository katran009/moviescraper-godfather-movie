Best Movie Matcher - 2nd Version

Automatic web scraper using BeautifulSoupmoviescraper-godfather-movie

#Installation
You need to have Google Chrome, Python3,& BeautifulSoup
Clone this repo or download and extract the zip file and navigate to its location.

##Run the main program:
python manage.py

###Expected Output:
Searching for movie with string filter 'godfather' The best match for movie search string 'godfather' is: Title: THE GODFATHER Release Year: 1972 Critic Score: 98% User Score: 98% URL: https://rottentomatoes.com/m/godfather

####Actual Ouput:
[<h1 class="scoreboard__title" data-qa="score-panel-movie-title" slot="title">The Godfather</h1>]
[<p class="scoreboard__info" slot="info">1972, Crime/Drama, 2h 57m</p>]
[<a class="scoreboard__link scoreboard__link--tomatometer" data-qa="tomatometer-review-count" href="/m/godfather/reviews?intcmp=rt-scorecard_tomatometer-reviews" slot="critics-count">102 Reviews</a>]
[<a class="scoreboard__link scoreboard__link--audience" data-qa="audience-rating-count" href="/m/godfather/reviews?type=user&amp;intcmp=rt-scorecard_audience-score-reviews" slot="audience-count">250,000+ Ratings</a>]

#####Citation
I used the following resources to do research on how to do the challenge.

Title: Scraping Data with BeautifulSoup and SelectorGadget in Python 3
Author: Dev Sharma
Availability: https://medium.com/@devkosal/scraping-data-with-beautifulsoup-and-selectorgadget-in-python-3-decf798e1a1e
