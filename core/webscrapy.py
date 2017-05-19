import time

from selenium import webdriver

from dousearch.config import WEBDRIVER_PATH, SEARCH_ROOT, DEFAULT_WEBDRIVER


class WebDriver:
    def __init__(self, default_driver):
        self.default_driver = default_driver
        self.path_driver = "{}{}"

    def get_driver(self):

        if self.default_driver == 0:
            drv = self.path_driver.format(WEBDRIVER_PATH, 'phantomjs')
            return webdriver.PhantomJS(executable_path=drv)

        if self.default_driver == 1:
            drv = self.path_driver.format(WEBDRIVER_PATH, 'chromedriver')
            return webdriver.Chrome(executable_path=drv)


class DOU:
    def __init__(self, web_driver=DEFAULT_WEBDRIVER):
        self.browser = WebDriver(default_driver=web_driver).get_driver()

    def _get(self, url):
        self.browser.get(url=url)

    def search(self, term, start=None, end=None, year=None):
        self._get(url=SEARCH_ROOT)

        input_search_term = self.browser.find_element_by_id("txt_pesquisa_avancada")
        input_search_term.send_keys('"{}"'.format(term))

        chk_box_all = self.browser.find_element_by_xpath("//input[@name='edicao.jornal']")
        chk_box_all.click()
        time.sleep(2)

        if start:
            digits = start.replace('/', '')
            input_start = self.browser.find_element_by_id("dt_inicio_pesquisa_avancada")
            input_start.click()
            input_start.clear()
            for d in digits:
                input_start = self.browser.find_element_by_id("dt_inicio_pesquisa_avancada")
                input_start.send_keys(d)

        if end:
            digits = end.replace('/', '')
            input_end = self.browser.find_element_by_id("dt_fim_pesquisa_avancada")
            input_end.click()
            input_end.clear()
            for d in digits:
                input_end = self.browser.find_element_by_id("dt_fim_pesquisa_avancada")
                input_end.send_keys(d)

        if year:
            select_year = self.browser.find_element_by_id("ano_pesquisa_avancada")
            options = [o for o in select_year.find_elements_by_tag_name("option")]
            for el in options:
                if el.text == str(year):
                    el.click()
                    break

        btn_search = self.browser.find_element_by_xpath("//input[@value='BUSCAR']")
        btn_search.click()
        time.sleep(5)

        if len(self.browser.window_handles) > 1:
            self.browser.switch_to.window(self.browser.window_handles[1])

        return self.browser.page_source

    def exit(self):
        self.browser.quit()







