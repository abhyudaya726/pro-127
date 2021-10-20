from bs4 import BeautifulSoup
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)

Soup = BeautifulSoup(page.text,'html.parser')

starTable = Soup.find('table')

tempList= []
table_rows = starTable.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)



StarNames = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(tempList)):
    StarNames.append(tempList[i][1])
    Distance.append(tempList[i][3])
    Mass.append(tempList[i][5])
    Radius.append(tempList[i][6])
    Lum.append(tempList[i][7])
    
data_frame_2 = pd.DataFrame(list(zip(StarNames,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

data_frame_2.to_csv('data.csv')