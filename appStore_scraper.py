from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json

link=input('Please enter the app link to scrape: ')
howMany=input('Please enter how many reviews you wanna scrape: ')
appName=link.split('/')[-2]
appId=link.split('/')[-1][2:]
countries = pd.read_csv('countries.csv')
twoCode=countries.Code
countryName=countries.Name

for i in twoCode:
    applicationName = AppStore(country=i, app_name=appName, app_id = appId)
    applicationName.review(how_many=howMany)
    df = pd.DataFrame(np.array(applicationName.reviews),columns=['review'])
    df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    
df2.to_csv('C:/Users/LEGION/Desktop/appstore_scraper/App Store Review {}.csv'.format(appName))