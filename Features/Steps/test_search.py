import time
from behave import *
from selenium import webdriver
from Utilities.CustomLogger import LogGen
from Configuration.config import TestData
from Pages.RentCamperPage import RentCamperPage


global camppage
mylogger = LogGen.logger()


@given('We Launch the Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(10)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(10)
    mylogger.info("** URL Launched **")

@then('We verify Page Title')
def verify_page_title(context):
    camppage = RentCamperPage(context.driver)
    Title = camppage.verifyPageTitle()
    if Title == TestData.PageTitle:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\PageTitle.png")
        mylogger.info("** PageTitle Verified **")
    else:
        mylogger.info("** PageTitle Not Verified **")
        context.driver.save_screenshot(".\\Screenshots\\PageTitleIncorrect.png")
        assert False


@when('We select Body Style as Camper Bus')
def select_body_style(context):
    camppage = RentCamperPage(context.driver)
    camppage.selectBodyStyle()

@when('Price Between Euro 25-150')
def select_price(context):
    camppage = RentCamperPage(context.driver)
    camppage.selectPrice()
