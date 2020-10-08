from urllib.request import Request, urlopen
import re
from csv import writer
from datetime import date
import time
from random import randrange

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

x='idea'
base_url = 'https://www.'+x+'lista.pt/comprar-casas/lisboa/'
areas = ['','belem/','ajuda/','alcantara/','estrela/','campo-de-ourique/','misericordia/','santo-antonio/','santa-maria-maior/']

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Connection': 'keep-alive'}

today = date.today()
d1 = today.strftime("%d/%m/%Y")
for area in areas:
    print(area)
    time.sleep(60+randrange(60))
    req = Request(base_url+area, headers=headers)
    f = urlopen(req).read().decode("utf-8")
    price=re.findall('Preço médio nesta zona \d*[.]\d* eur',f)
    price=re.findall('\d*[.]\d*',price[0])
    price.append(area)
    price.append(d1)
    append_list_as_row('lisbon_prices.csv',price)

