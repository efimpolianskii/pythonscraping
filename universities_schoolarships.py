#import some libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
#create an empty list to append it later
list = []
#create a list of countries which are presented on website
locations = ['united-states','united-kingdom','canada','europe','south-africa','nigeria','pakistan','india']
#first loop - scraping all the pages from website
for n in range(1,30):
    print(n)
    #sleep, in order not to be baned
    time.sleep(1)
    #second loop - scraping suggestions from different countries
    for location in locations:
    
        url = f'https://www.scholarshipportal.com/scholarships/{location}?page={n}'

        r = requests.get(url)
        soup = BeautifulSoup(r.text,'lxml')

        articles = soup.findAll('a', class_='flex flex-col p-8 text-black no-underline bg-white rounded shadow md:flex-row hover:text-black group mb-4')
        #third loop - scraping all the necessary information for each suggextion
        for article in articles:
            #also, add except in order to get error in empty 'find'
            try:
                title = article.find('h3', class_='font-bold text-xl group-hover:underline group-hover:text-primary-500').text
            except:
                title = None
            try:
                degrees = article.findAll('span', class_='bg-gray-100 inline-block mr-2 py-1 px-3 text-sm text-gray-600 rounded mb-1')[0].text
            except:
                degrees = None
            try:
                funds = article.findAll('span', class_='bg-gray-100 inline-block mr-2 py-1 px-3 text-sm text-gray-600 rounded mb-1')[1].text
            except:
                funds = None
            try:
                date = article.findAll('span', class_='bg-gray-100 inline-block mr-2 py-1 px-3 text-sm text-gray-600 rounded')[0].text
            except:
                date = None
            country = location
            
            #append the empty list
            list.append([title, degrees, funds, date, location])
#create titles for future table
headers = ['title', 'degrees', 'funds', 'date', 'location']
#create dataframe from scrapped data
schoolarships = pd.DataFrame(data = list, columns = headers)
