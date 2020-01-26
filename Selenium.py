from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.apple.com/")
dropdown = driver.find_element_by_id("ac-ls-dropdown-select")
dropdown.click()
option = driver.find_element_by_id("ac-ls-dropdown-option-1")
option.click()
icon = driver.find_element_by_class_name("ac-gn-link-text")
continue_button = driver.find_element_by_link_text("Continue")
continue_button.click()
driver.close()


