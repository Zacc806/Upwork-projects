# importing necessary modules
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json

# getting the necessary info for scraping
link=input('Please enter the app link to scrape: ')
howMany=input('Please enter how many reviews you wanna scrape: ')
appName=link.split('/')[-2]
appId=link.split('/')[-1][2:]

# get the list of all countries
countries = pd.read_csv('countries.csv')
twoCode=countries.Code
countryName=countries.Name

# loop through the list of all the countries
for i in twoCode:
    applicationName = AppStore(country=i, app_name=appName, app_id = appId)
    applicationName.review(how_many=howMany)
    df = pd.DataFrame(np.array(applicationName.reviews),columns=['review'])
    df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    
# export it all to the csv
df2.to_csv('C:/Users/LEGION/Desktop/appstore_scraper/App Store Review {}.csv'.format(appName))
