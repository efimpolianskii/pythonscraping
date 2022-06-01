import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

s = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
            'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
            'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
            'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
            'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

def lower_state(s):
    for i in range(len(s)):
        s[i] = s[i].lower()
    return(s)

def urls(s):
    data = []
    global links
    for state in s:
        url = f'https://locations.pizzahut.com/{state}/'   
        r=requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        st = soup.findAll('span',class_='c-bread-crumbs-name')[1].text.lower()
        blocks = soup.findAll('li',class_='Directory-listItem')
        for block in blocks:
            city = block.find('span','Directory-listLinkText').text.lower().replace(' ','-')
            data.append([st,city])

    headers = ['st','city']
    df = pd.DataFrame(data = data, columns = headers)
    df['url'] = 'https://locations.pizzahut.com/'+df['st']+'/'+df['city']
    links = df.url.to_list()
    return(links)

def dataset(links):
    data = []
    n=0
    for link in links:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        blocks = soup.findAll('li',class_='Directory-listTeaser')
        n+=1
        print(f'{n} Loop is over...')
        time.sleep(2)
        for block in blocks:
            try:
                address_1 = block.find('span',class_='LocationName-geo').text
            except:
                address_1 = None
            try:
                type = block.find('div',class_='Teaser-storeType').text
            except:
                type = None
            try:
                open_hours = block.find('span',class_='c-location-hours-today-day-hours-intervals-instance js-location-hours-interval-instance').text
            except:
                open_hours = None
            try:
                address_2 = block.find('span',class_='c-address-street-2').text
            except:
                address_2 = None 
            try:
                city = block.find('span',class_='c-address-city').text
            except:
                city = None 
            try:
                state = block.find('abbr',class_='c-address-state').text
            except:
                state = None  
            try:
                postal_code = block.find('span',class_='c-address-postal-code').text
            except:
                postal_code = None   
            data.append([type, address_1, address_2, open_hours, city, state, postal_code])
    headers = ['type', 'address_1', 'address_2', 'open_hours', 'city', 'state', 'postal_code']
    df = pd.DataFrame(data = data, columns=headers)
    return(df)

dataset(urls(lower_state(s)))
