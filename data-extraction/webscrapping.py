import pandas as pd
import requests as req
from bs4 import  BeautifulSoup
from features import extract_features
import re
names_list_new =[]
prices_list_new =[]
features_list = []
def fill_product_details(url = "" , soup = "") :
    product = {
        "name" : "KzDlHZ" ,
        "price" : "Nx9bqj _4b5DiR",
        "specifications" : "G4BRas",
        "rating_reviews" : "Wphh3N" ,
    }
    products_names_list = soup.find_all("div" , class_ = product["name"])
    for products_names in products_names_list:
        names_list_new.append(products_names.text)
    products_price_list = soup.find_all("div" , class_ = product["price"])
    for price_desc in products_price_list:
         prices_list_new.append(price_desc.text)
    products_price_description_list = soup.find_all("ul" , class_ = product["specifications"])
    products_price_description_new = []
    for product_desc in products_price_description_list :
        products_price_description_new.append(product_desc.text)
    for i in range(len(products_price_description_new)):
        features_list.append(extract_features(products_price_description_new[i] ,price_range= prices_list_new[i]))
url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

while 1 :
    r = req.get(url)
    soup = BeautifulSoup(r.text , "lxml")
    fill_product_details(url , soup)
    found = soup.find("a", class_="_9QVEpD")
    if found :
        found = found.get('href')
        url = "https://flipkart.com" + found
    else :
        break;

df = pd.DataFrame( {
    "features" : features_list,
})
priceDF = pd.DataFrame({
    "prices" : prices_list_new
})
df.to_csv("train_data_without_index.csv" , index=0 )
print('updated dataframe ')
df.to_csv("train_data.csv" , index=0 )
# priceDF.to_csv("price_data.csv" , index= 0);


