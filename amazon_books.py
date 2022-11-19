import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime

books= []

for i in range(1,5):

    url = f'https://www.amazon.com/kindle-dbs/browse/ref=dbs_b_def_rwt_brws_ts_recs_pg_1?metadata=cardAppType%3ADESKTOP%24deviceTypeID%3AA2Y8LFC259B97P%24clientRequestId%3AFVB8QJP1RXH94F5ZX10R%24deviceAppType%3ADESKTOP%24ipAddress%3A10.89.191.28%24userAgent%3AMozilla%2F5.0+%28X11%3B+Ubuntu%3B+Linux+x86_64%3B+rv%3A106.0%29+Gecko%2F20100101+Firefox%2F106.0%24deviceFamily%3AWhiskeytown%24cardSurfaceType%3Adesktop%24cardMobileOS%3AUnknown%24deviceSurfaceType%3Adesktop&storeType=ebooks&widgetId=unified-ebooks-storefront-default_TopSellersStrategy&sourceAsin=&content-id=amzn1.sym.bb33addf-488a-4e99-909f-3acc87146400&refTagFromService=ts&title=Best+sellers+&pf_rd_p=bb33addf-488a-4e99-909f-3acc87146400&sourceType=recs&pf_rd_r=FVB8QJP1RXH94F5ZX10R&pd_rd_wg=zhqwA&ref_=dbs_f_def_rwt_wigo_ts_recs_wigo&SkipDeviceExclusion=true&pd_rd_w=CWDpm&pd_rd_r=961e4b48-dd22-42bb-82ac-344d1a60475b&page={i}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html')
    blocks = soup.findAll('div', class_='a-column a-span12 a-spacing-none a-spacing-top-small browse-grid-view-info a-span-last')

    for block in blocks:
        title = block.find('span',class_='a-size-base a-color-base browse-text-line browse-larger-text-one-line').text.replace("\n",'').strip()
        try:
            stars = block.find('span',class_='dbs-icon-alt').text.replace(' stars','').strip()
        except:
            stars = '0.0'
        try:
            reviews = block.find('span',class_='a-size-small a-color-secondary').text.replace('(','').replace(')','').strip()
        except:
            reviews = '0'
        try:
            amazon_chart = block.find('span',class_='p13n-amz-charts-qualifier-text').text.replace("\n",'').strip()
        except:
            amazon_chart = '-'
        try:
            price = block.find('span',class_='a-color-price a-text-bold').text.replace("$",'').strip()
        except:
            price = '-'
        books.append([title,stars,reviews,amazon_chart,price])

    print('I am waiting...')
    time.sleep(3)
    i=i+1

headers = ['title','stars','reviews','amazon_chart','price']
df = pd.DataFrame(data = books, columns = headers)
df
