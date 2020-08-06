from behave import fixture
from selenium import webdriver
import os
from pages.common import Common


# Run Before the Feature testing execution
def before_all(context):
    context.option = webdriver.ChromeOptions()
    context.option.add_argument(" — incognito")
    context.option.add_argument("--headless")
    context.chrome_dir = '' + os.getcwd() + '/pages/chromedriver'


# Run before every scenario of the feature
def before_scenario(context, sceanrio):
    sceanrio.driver = webdriver.Chrome(executable_path = context.chrome_dir, options = context.option)
    context.common = Common(sceanrio.driver)


# Run after each scenarios are tested
def after_scenario(context, scenario):
    # close browsers
    context.common.browser_close()



