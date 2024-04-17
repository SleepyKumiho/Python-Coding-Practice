from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.fcc.gov/media/radio/dms-decimal")
print(driver.title)
assert "Decimal Degrees" in driver.title
elem = driver.find_element(By.ID, "DegreesLat")
elem.send_keys("32.2158186")
elem2 = driver.find_element(By.ID, "DegreesLon")
elem2.send_keys("-86.3949582")
button = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div/div/article/div/div/div[1]/div[1]/div/div[1]/center/table[2]/tbody/tr/td[2]/form/table/tbody/tr[3]/td/input[1]")
button.click()
lat = driver.find_element(By.ID, "deglathere")
lon = driver.find_element(By.ID, "deglonhere")
print(lat.get_attribute("value"), lon.get_attribute("value"))
driver.close()
