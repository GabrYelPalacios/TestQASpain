

# class PageHome:
#    def __init__(self, myDriver):
#        self.driver = myDriver

def clickCart(driver):
    cartButtom = driver.find_element_by_id('nav-cart-count-container')
    cartButtom.click()


def clickSerch(driver):
    serchButtom = driver.find_element_by_id('nav-search-submit-button')
    serchButtom.click()


def serchItem(driver, textToSearch):
    serchBox = driver.find_element_by_id('twotabsearchtextbox')
    serchBox.send_keys(textToSearch)
    clickSerch(driver)
