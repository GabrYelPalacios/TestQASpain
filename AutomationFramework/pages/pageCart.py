

def increaseItem(driver, anItem):
    listaProductos = driver.find_element_by_xpath('activeCartViewForm')
    for elem in listaProductos:
      item = elem.driver.find_element_by_name(
          'data-itemid="Cc2237e3d-976e-442a-a0d3-0406d7f0a0a4"')
    return firstItem
