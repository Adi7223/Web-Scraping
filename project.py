from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

if not os.path.exists("data"):
    os.makedirs("data")

driver = webdriver.Chrome()
query="laptop"
file=0
for i in range(1,5): 
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2I7BLW1VEKK58&qid=1725367740&sprefix=laptop%2Caps%2C210&ref=sr_pg_{i}")
    elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")
    print("\n")
    print(f"{len(elems)} items found")
    print("\n")
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w", encoding="utf-8") as f:
            f.write(d)
            file +=1
    #  print(elem.text)
    print("\n")
    time.sleep(10)
driver.close()

    