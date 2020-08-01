from behave import fixture
from selenium import webdriver
import os
from pages.common import Common

# Run Before the Feature testing execution
def before_all(context):
    option = webdriver.ChromeOptions()
    option.add_argument(" — incognito")
    option.add_argument("--headless")
    chrome_dir = '' + os.getcwd() + '/pages/chromedriver'
    context.driver = webdriver.Chrome(executable_path = chrome_dir, options = option)


# Run after every scenario of the feature
def before_scenario(context, sceanrio):
    context.common = Common(context.driver)


# Run after all scenarios are tested
def after_all(context):
    context.common.browser_close()

