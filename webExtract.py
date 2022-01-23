#!/bin/usr/python3
from urllib.request import urlopen as URL
from bs4 import BeautifulSoup as soup
from time import sleep

get_URL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
print("Entered URL is ",get_URL)
print("Starting URL...")
client_URL = URL(get_URL)
print("Creating Client...")
data_URL = client_URL.read()
print("Obtaining Data from Client")
client_URL.close()
print("Client Released...")
page_data = soup(data_URL,"html.parser")
print("Putting data in Container..")
sleep(1)
containers = page_data.findAll("div",{"class":"item-container"})
print("Listing the Contents")
print(len(containers))
i = 1
for container in containers:
	item_name = container.findAll("a",{"class":"item-title"})
	print("#"+str(i),"-",item_name[0].text)
	i = i+1

