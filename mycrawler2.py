from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\gyawa\Downloads\chromedriver_win32\chromedriver')
driver.get('file:///C:/Users/gyawa/OneDrive/Desktop/sisam/Project-PhaseIV/index.html')
button = driver.find_element_by_xpath('//button[@class="btn btn-info my-2"]')
button.click()
button1xpath = driver.find_elements_by_xpath('//button[@class="page btn btn-sm btn-info"]')
page_number = len(button1xpath)
print(page_number)

for i in range(1,page_number+1):
    xpathofbutton = '//button[@value="'
    xpathofbutton += str(i)
    print(xpathofbutton)
    xpathofbutton+= '"]'
    button1 = driver.find_element_by_xpath(xpathofbutton)
    button1.click()
    header = driver.find_elements_by_xpath('//table[@class="table table-dark table-bordered"]')
    print(header[0].text)
    print(header)