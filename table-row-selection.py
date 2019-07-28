import selenium
from selenium import webdriver

uri = 'https://www.ultimateqa.com/simple-html-elements-for-automation/'
browser = webdriver.Chrome('chromedriver.exe')
browser.get(uri)
assert "Simple HTML" in browser.title
search_for = 'quality'
print("Search TEXT: ", "//td[contains(text(), '"+search_for+"')]")
rows = browser.find_elements_by_xpath("//*[@id='et-boc']/div/div[3]/div/div[2]/div[5]/div/table/tbody/tr")
print('Size: ', len(rows), 'ROWS: ', rows)
for id,item in enumerate(rows):
    print('Row has: => ', item.get_attribute('innerHTML'), 'at position ', id)
    if search_for.lower() in item.get_attribute('innerHTML').lower():
        interested_in = id - 1

main_column = browser.find_elements_by_xpath("//*[@id='et-boc']/div/div[3]/div/div[2]/div[5]/div/table/tbody/tr/td[3]")
for id,item in enumerate(main_column):
    print('column has element :', item.get_attribute('innerHTML'), 'at position ', id)
    if id == interested_in:
        print('We need ', item.get_attribute('innerHTML'))
browser.close()
browser.quit()

# TABLE IN THIS EXAMPLE
# Title	Work	Salary
# Software Development Engineer in Test	Automation	$150,000+
# Automation Testing Architect	Automation	$120,000+
# Quality Assurance Engineer	Manual	$50,000+
