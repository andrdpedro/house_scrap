import time
from selenium import webdriver

CHROME_DRIVER_PATH = "C:/Users/User/PycharmProjects/SeleniumChrome/chromedriver"
URL = "https://forms.gle/XTsZHQzpw5Ry79sX9"


class FillForms:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def fill(self, address, prices, links):
        self.driver.get(URL)
        time.sleep(2)
        for i in range(len(address)):
            address_entry = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_entry.send_keys(address[i])
            price_entry = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_entry.send_keys(prices[i])
            link_entry = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_entry.send_keys(links[i])
            send = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            send.click()
            return_link = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            return_link.click()
