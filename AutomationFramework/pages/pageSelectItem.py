

def locateItem(driver):
    firstItem = driver.find_element_by_xpath(
        '//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]')
    return firstItem


def addItemToCart(driver, anItem):
    anItem.click()
    #driver.implicity_wait(5)
    cartButtom = driver.find_element_by_id('add-to-cart-button')
    cartButtom.click()
