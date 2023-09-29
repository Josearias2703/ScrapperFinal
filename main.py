from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from db import MongoDriver


consulta = 'manchester city primera equipacion'

driver = webdriver.Chrome()
driver.get("https://www.camisetasfutboleses.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search > input")
search_box.send_keys(consulta)

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#search > span > button > span > i")
search_button.click()

select_element = driver.find_element(By.CSS_SELECTOR, "#input-limit")
select = Select(select_element)
select.select_by_index(1)

camiseta = driver.find_elements(By.CSS_SELECTOR, "#content > div:nth-child(9) > div ")

mongodb = MongoDriver()

for card in camiseta:
    try:
        nombre = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > h4").text
        precioof = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > p.price > span.price-new").text
        descuento = card.find_element(By.CSS_SELECTOR, "div > div > div.product-details > div.caption > p.price > span.percentsaving").text
        precion = card.find_element(By.CSS_SELECTOR,"div > div > div.product-details > div.caption > p.price > span.price-old").text

        print(nombre)
        print(precioof)
        print(descuento)
        print(precion)

        Camiseta = {
            "Nombre": nombre,
            "Resultado": {
                "Precio Oferta": precioof,
                "Descuento": descuento,
                "Precio Normal": precion,
            }

        }

        mongodb.insert_record(record=Camiseta, username="Camisetas Manchester City")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()
