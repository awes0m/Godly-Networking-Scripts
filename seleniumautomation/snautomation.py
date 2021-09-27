from selenium import webdriver

driver = webdriver.Edge('msedgedriver.exe')
driver.get('https://williams.service-now.com')
driver.find_element_by_xpath('//*[@id="allApps_tab"]').click()
driver.find_element_by_xpath('//*[@id="e660172ac611227b00fa88fb47ae3fad"]').click()