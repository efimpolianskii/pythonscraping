import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

#create an empty list for further appending
list = []

#website i am going to parse
url = 'https://www.blockchain.com/btc/unconfirmed-transactions'

#get html from the website
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

#i want to look for each row on website out of loop
blocks = soup.findAll('div', class_='sc-1g6z4xm-0 hXyplo')

#the common objects i want to place in a loop
for i in range(0,20000):
    for block in blocks:
        hash = block.find('a', class_='sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK').text
        date = block.find('span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC').text
        sum_btc = block.findAll('span',class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[1].text
        sum_usd = block.findAll('span',class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[2].text
        list.append([hash, date, sum_btc, sum_usd])
    i=i+1
    
    #just for convinience lets make short summary about scrapper work and print out the number of a loop...
    print(f'This is loop #{i}')
    p = i*50
    
    #...the quantity of rows in a future dataset and when it sleeps
    print(f'There are {p} rows on the dataset \nI am sleeping \n+++++++++++++++++++++++')
    
    #wait until the transactions refresh on the website and then the loop repeats
    time.sleep(15)
    
#create and safe dataset as a csv file
headers = ['hash', 'date', 'sum_btc', 'sum_usd']
df = pd.DataFrame(data = list, columns=headers)
df.to_csv(r'C:\Users\polianskii\Desktop\bitcoin_transactions.csv')
