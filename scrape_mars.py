from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser
def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', headless=True, **exec_path)