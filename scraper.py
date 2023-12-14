from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
browser = webdriver.Chrome("/Users/amritsaha/Downloads/PRO-C127-Student-Boilerplate-Code-main/chromedriver")
browser.get(START_URL)
#s = Service(r"/Users/amritsaha/Downloads/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe") 
#browser=webdriver.Chrome(service=s) 
#browser.get(START_URL)

time.sleep(10)

planets_data = []
scrap_data = []
# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source,"html.parser")
        table1 = soup.find("table",attrs={"class","wikitable"})  
        table1_body = table1.find("tbody")
        table1_rows = table1_body.find_all("tr") 
        for row in table1_rows: 
            table1_columns = row.find_all("td")
            temp_list = []
            for col in table1_columns:
                data = col.text.strip()
                temp_list.append(data)
            scrap_data.append(temp_list)
scrape()





        


# Define Header
headers = ["rank", "visual magnitude", "proper name", "bayer designation", "distance","spectral type"]

# Define pandas DataFrame   
df = pd.DataFrame(scrap_data,columns=headers)


# Convert to CSV
df.to_csv("scrapedata.csv",index=True,index_label="Id")
    


