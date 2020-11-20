import requests
import time
import bs4
from bs4 import BeautifulSoup


keyword = 'matcha'
headers = {
    'user_agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0'
}

results=[]
#r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword, headers=headers)
#useforlater
for i in range(10):
    r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'&_sacat=0&_pgn='+str(i+1), headers=headers)
    print ( 'r.status_code=',r.status_code)
    print('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'&_sacat=0&_pgn='+str(i+1))
    soup = BeautifulSoup(r.text,'html.parser')

    #print('r.text=', r.text)
    '''
    items = soup.select('.s-item__title')
    for item in items:
        print('item=',item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)

    statuses = soup.select('.SECONDARY_INFO')
    for status in statuses:
        print('status=',status.text)
    '''
    counter = 0
    boxes = soup.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper')
    print(boxes)
    for box in boxes:
        counter += 1
        #print("box", box)
        result = {}
        print('---')
        items = box.select('.s-item__title')

        for item in items:
            print('item=',item.text)
            result['item'] = item.text
        prices= box.select('.s-item__price')
        for price in prices:
            #print('price=',price.text)
            result['price'] = price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
           # print('status=',status.text)
            result['status'] = status.text
        #print(result)
        results.append(result)    

    print("count", counter)
    #print('results loop'+str(i)+'=', result)
    print('len(results)=',len(results))

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
#print('j=',j)