from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

uri = 'https://duckduckgo.com'
title = 'DuckDuckGo'

opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts, executable_path='browsers/geckodriver')
browser.get(uri)
assert title in browser.title
browser.implicitly_wait(2)
search_bar = browser.find_element_by_id('search_form_input_homepage')

print('Element Details: ', search_bar)
search_bar.send_keys('lava chdum')
search_button = browser.find_element_by_id('search_button_homepage')
search_button.click()

results = browser.find_elements_by_class_name('result')

print("Found " + str(len(results)) + " results:")

print('----------- RESULTS -----------')
for x in results:
    print(x.get_attribute('innerHTML'))
browser.close()
