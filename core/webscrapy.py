from selenium import webdriver
import time
from core.config import WEBDRIVER_PATH, SEARCH_ROOT

class WebDriver:
    pass


class ScrapyDOU:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=WEBDRIVER_PATH)

    def get(self, url):
        self.browser.get(url=url)

    def search(self, term):
        self.get(url=SEARCH_ROOT)

        input_search = self.browser.find_element_by_id("txt_pesquisa_avancada")
        input_search.send_keys('"{}"'.format(term))

        chk_box_all = self.browser.find_element_by_xpath("//input[@name='edicao.jornal']")
        chk_box_all.click()
        time.sleep(2)

        btn_search = self.browser.find_element_by_xpath("//input[@value='BUSCAR']")
        btn_search.click()

        self.browser.page_source

    def exit(self):
        self.browser.quit()







