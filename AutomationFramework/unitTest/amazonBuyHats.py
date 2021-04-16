from AutomationFramework.pages import pageHome, pageSelectItem, pageCart
from AutomationFramework.unitTest import amazonCommons


# class AmazonButHatsTest(unittest.TestCase):

# Inicializo el driver e in
driver = amazonCommons.setUp()
#self.page_Home = PageHome(self.driver)


def amazonBuyHats():

    # Busco y agrego los sombreros de Hombre
    menhatstr = "sombreros de hombres"
    pageHome.serchItem(driver, menhatstr)
    amazonCommons.wait(driver, 10)
    maleHat = pageSelectItem.locateItem(driver)
    print(maleHat)
    pageSelectItem.addItemToCart(driver, maleHat)
    #voy al home para realizar la nueva busqueda
    amazonCommons.goHome(driver)
    # Busco y agrego los sombreros de mujer
    womanhatstr = "sombreros de mujer"
    pageHome.serchItem(driver, womanhatstr)
    amazonCommons.wait(driver, 5)
    womanHat = pageSelectItem.locateItem(driver)
    pageSelectItem.addItemToCart(driver, womanHat)
    #Voy al carro de compras
    amazonCommons.goCart(driver)
    #Modifico el carrito
    pageCart.increaseItem(driver, maleHat)

    #Cierro el driver
   # tearDown(driver)
