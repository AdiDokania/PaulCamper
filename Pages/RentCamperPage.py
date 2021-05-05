import time
from selenium.webdriver.common.by import By
from Configuration.config import TestData
from Pages.BasePage import BasePage


class RentCamperPage(BasePage):

    BodyStyle = (By.XPATH, "//div[text()= 'Body style']")
    CamperBus = (By.XPATH, "//div[text()= 'Camper bus']")
    Caravan = (By.XPATH, "//div[text()= 'Caravan']")
    Price = (By.XPATH, "//div[text()= 'Price']")
    StartingPrice = (By.XPATH, "//div[@aria-valuenow='30']")
    EndingPrice = (By.XPATH, "//div[@aria-valuenow='180']")

    def __init__(self, driver):
        super().__init__(driver)

    def selectBodyStyle(self):
        self.do_click(self.BodyStyle)
        time.sleep(1)
        self.do_click(self.CamperBus)
        time.sleep(1)
        self.do_click(self.CamperBus)

    def selectPrice(self):
        self.do_click(self.Price)
        time.sleep(1)
        self.drag_drop(self.StartingPrice, "-9", "0")
        time.sleep(1)
        self.drag_drop(self.EndingPrice, "-51", "0")
        time.sleep(2)

    def verifyPageTitle(self):
        return self.get_title()

