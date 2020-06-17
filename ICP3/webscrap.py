#importing requests and bs4 pacakages
import requests
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/Deep_learning'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.string)
rows = soup.find_all('a') #finding the links in the page
print(rows)
my_data_file = open('data.txt', 'w')#opening the file to store the links in write mode
for link in rows:
    filtered_data = link.get('href')
    print(filtered_data)
    my_data_file.write(str(filtered_data))
    my_data_file.write("\n")

my_data_file.close()
#for row in rows:          # Print all occurrences
 #   print(row.get_text())
