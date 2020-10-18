# nba-position-classification

nba-position-classification is an exploration into using K-Means clustering to accurately predict what position an NBA player plays based on their height and weight. 

## Data Scraping

The data was scraped from [Basketball-Reference](basketball-reference.com) using a custom built webscraper that leverages [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Analysis and Predictions

The data cleaning, analysis, and predictions were made in a [Jupyter Notebook](https://jupyter.org/). K-Means clustering was used to predict each player's position based on their height and weight.

Once the prediction was made, we compared their actual position to their predicted position. Based on our results, we were able to draw a conclusion on if weight and height can be used to accurately predict position or if additional data is needed.

