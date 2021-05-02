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

# Mars Hemisphere

def scrape_mars_hemispheres():

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://marshemispheres.com/'
        browser.visit(hemispheres_url)

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        main_url = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hem_url = []

        # Store the main_url 
        hemispheres_main_url = 'https://marshemispheres.com/'

        # Loop through the items previously stored
        for x in main_url: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = bs( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hem_url.append({"title" : title, "img_url" : img_url})

        mars_info['hem_url'] = hem_url
        

        # Return mars_data dictionary 

        return mars_info

        browser.quit()




