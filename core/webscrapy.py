from selenium import webdriver
import time

class WebDriver:
    pass


class ScrapyDOU:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="/home/n1lux/Downloads/chromedriver")

    def get(self, url):
        self.browser.get(url=url)

    def search(self, term):
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


if __name__ == "__main__":
    url = "http://portal.imprensanacional.gov.br/pesquisa"
    term = "universidade federal dos vales do jequitinhonha e mucuri"
    dou = ScrapyDOU()
    dou.get(url=url)
    dou.search(term=term)
    #dou.exit()






