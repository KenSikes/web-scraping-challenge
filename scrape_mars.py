from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser
def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', headless=True, **exec_path)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA Mars News
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("div.content_title", wait_time=1)

        #visit Nasa URL 
        url = 'https://redplanetscience.com/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        news_title = (soup.find_all('div', class_='content_title'))[0].get_text()
        news_p = (soup.find_all('div', class_='article_teaser_body'))[0].get_text()

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info

        browser.quit()

# Mars Facts
def scrape_mars_facts():

    # Visit Mars facts url 
    mars_facts_url = 'https://galaxyfacts-mars.com/'

    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    # Save html code to folder Assets
    data = mars_df.to_html()

    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = data

    return mars_info