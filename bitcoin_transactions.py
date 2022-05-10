import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime

list = []

for i in range(0,2000):

    now = datetime.now()
    current_time = now.strftime("%D %H:%M:%S")
    url = 'https://www.blockchain.com/btc/unconfirmed-transactions'

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    blocks = soup.findAll('div', class_='sc-1g6z4xm-0 hXyplo')

    for block in blocks:
        hash = block.find('div', class_='sc-6nt7oh-0 PtIAf').text
        date = block.find('span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC').text
        sum_btc = block.findAll('span',class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[1].text
        sum_usd = block.findAll('span',class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC')[2].text
        list.append([hash, date, sum_btc, sum_usd])
        
    i=i+1
    print(f'This is loop #{i}')
    print(f'There are {i*50} rows in the dataset \nTime: {current_time} \n+++++++++++++++++++++++')
    time.sleep(50)

headers = ['hash', 'date', 'sum_btc', 'sum_usd']

df = pd.DataFrame(data = list, columns=headers)
df.to_csv(r'C:\Users\polianskii\Desktop\bitcoin_transactions.csv')
