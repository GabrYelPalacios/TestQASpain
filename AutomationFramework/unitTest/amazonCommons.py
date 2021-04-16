from selenium import webdriver
from selenium.webdriver.common.by import By


def setUp():
    driver = webdriver.Chrome(
        'C:\GabrYel\Tutoriales\Python\TestQASpain\AutomationFramework\webdrivers\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.com/')
    return driver


def tearDown(driver):
    driver.quit()


def goHome(driver):
    homeButtom = driver.find_element_by_id('nav-logo-sprites')
    homeButtom.click()


def goCart(driver):
    cartButtom = driver.find_element_by_id('nav-cart-count-container')
    cartButtom.click()


def wait(driver, seconds):
    driver.implicitly_wait(seconds)
