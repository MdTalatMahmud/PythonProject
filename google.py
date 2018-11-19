import selenium.webdriver as webdriver

def  get_results(search_term):
    url="htttps://www.google.com"
    browser=webdriver.Chrome()
    browser.get(url)
    search_box=browser.find_element_by_id("gb")
    search_box.send_keys(search_term)
    search_box.submit()
    try:
        links=browser.find_element_by_xpath("//ol[@class='web_regular-results']//h3//a");
    except :
        links=browser.find_element_by_xpath("//h3//a")
    results=[] 
    for link in links:
        href =links.getattribute("href")
        print(href)
        results.append(href)
browser.close()   
return results
get_results("dog")