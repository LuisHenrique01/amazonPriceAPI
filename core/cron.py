import requests
from bs4 import BeautifulSoup as bs
from core.models import Desejos, Item
from datetime import date

def scrap_itens():
    desejos = Desejos.objects.all()
    for desejo in desejos:
        url = desejo.url
        headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

        page = requests.get(url, headers=headers)

        soup = bs(page.content, 'html.parser')
        soup2 = bs(soup.prettify(), 'html.parser')

        spans = soup2.find_all('span', class_='a-price-whole') 
        prices = [str(price.get_text()).replace(' ', '').replace('\n', '').replace(',', '') for price in spans] 
        links = soup2.find_all('a', class_='a-link-normal') 
        titles = [link['title'] for link in links if 'itemName_' in str(link)]
        ids = [link['id'] for link in links if 'itemName_' in str(link)]
        
        bulkCreate = []
        bulkUpdate = []
        for id_, price, title in zip(ids, prices, titles):
            if Item.objects.filter(id=id_).exists():
                item = Item.objects.get(id=id_)
                if (item.minPrice > price and (item.dateCreated - date.today()).days >= 7) or (price <= (((100 - desejo.percent)/100) * item.priceDayAdd)):
                    bulkUpdate.append(Item(id=id_, minPrice=price))
                    #Notificar por email
            else:
                bulkCreate.append(Item(id=id_, lista=desejo, minPrice=price, priceDayAdd=price, title=title))
        
        if len(bulkCreate) > 0:
            Item.objects.bulk_create(bulkCreate)
        if len(bulkUpdate) > 0:
            Item.objects.bulk_update(bulkUpdate, fields=['minPrice']) 