import os
import time
import requests
import bs4
import random
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style

init()
os.system('cls')
 
monitor = {
 
}
 
 
 
 
 
 
 
 
def parse(prod_data):
    for link in prod_data:
        try:
            new_link = link.get('href')
        
            pardata = requests.get(new_link).text
            soup1 = BeautifulSoup(pardata, 'html.parser')
            try:
                price = soup1.find('span', class_='item-price').get_text()
                title = soup1.find('h1', class_='product-title').get_text()
            except:
                price = soup1.find(id='prcIsum').get_text()
                title = soup1.find(id='itemTitle').get_text()
            monitor.update({title:price})
            print(title, price)
        except:
            print('void')
   
    for x, y in monitor.items():
       
            pric = y.split('$', 1)
            price = pric[1]
            b = price.split('.')[0]
            c = int(b)
            name_short = x.split('  ',1)
            name_short1 = name_short[1]
        
            if c < 299:
                
                vardms = (Fore.GREEN + 'hit')
                print(vardms,Fore.WHITE + name_short1,y)
            else:
                print('error')
                pass
 
 
def Scan_ebay(url):
    data = requests.get(url)
    pdata = data.text
    soup = BeautifulSoup(pdata, 'html.parser')
    prod_data = soup.find_all('a', class_='s-item__link')
    parse(prod_data)
 
 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/86.0.4240.99 Safari/537.36"
}
 
 
 
#keywords = ['Acer', '24 inch', '27 inch', 'Nitro', 'Widescreen', 'LCD', '22"', 'HP', 'Dell', 'IPS', '144hz', '144HZ', '60hz', '60HZ']
 
 
#scanlist = ['https://www.ebay.com/b/Computer-Monitors/80053/bn_317528', 'https://www.amazon.com/primeday/ref=gbpp_itr___ALLDEALS?ie=UTF8']
 
Scan_ebay('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=monitors&_sacat=0')
 