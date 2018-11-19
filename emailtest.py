


from selenium import webdriver
import re 
x=input('type the email address   \n')
driver=webdriver.Chrome()
driver.get(x)
doc=driver.page_source
emails=re.findall(r'[\w\.-]+@[\w\.-]+',doc)
for email in emails:
        print(email)







