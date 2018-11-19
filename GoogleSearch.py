import selenium.webdriver as webdriver
from selenium import webdriver
# import GoogleSearch

def get_results(search_term):
    url = "https://www.google.com"
    browser = webdriver.Chrome()
    browser.get(url)
    search_box = browser.find_elements_by_id("query")
    search_box.send_keys(search_term)
    search_box.submit()
    try:
        links = browser.find_element_by_xpath("//ol[@class='web_regular_results']//h3//a")

    except:
        links = browser.find_element_by_xpath("//h3//a")
    results = []
    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)
    browser.close()
    return results

get_results("dog")
#print(get_results("dog"))

# import GoogleSearch
# from google import search

# ip=raw_input("What would you like to search for? ")

# for url in search(ip, stop=20):
#      print(url)