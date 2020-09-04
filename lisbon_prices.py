from urllib.request import Request, urlopen
import re
from csv import writer
from datetime import date

x='idea'

req = Request('https://www.'+x+'lista.pt/comprar-casas/lisboa/', headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(req).read().decode("utf-8")
price=re.findall('Preço médio nesta zona \d*[.]\d* eur',f)
print(price)
price=re.findall('\d*[.]\d*',price[0])
today = date.today()
d1 = today.strftime("%d/%m/%Y")
price.append(d1)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        
append_list_as_row('lisbon_prices.csv',price)
