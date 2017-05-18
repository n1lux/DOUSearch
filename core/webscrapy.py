from selenium import webdriver
import time
from core.config import WEBDRIVER_PATH, SEARCH_ROOT, DEFAULT_WEBDRIVER


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


class ScrapeDOU:
    def __init__(self, default_webdriver=DEFAULT_WEBDRIVER):
        self.browser = WebDriver(default_driver=default_webdriver).get_driver()

    def _get(self, url):
        self.browser.get(url=url)

    def search(self, term):
        self._get(url=SEARCH_ROOT)

        input_search = self.browser.find_element_by_id("txt_pesquisa_avancada")
        input_search.send_keys('"{}"'.format(term))

        chk_box_all = self.browser.find_element_by_xpath("//input[@name='edicao.jornal']")
        chk_box_all.click()
        time.sleep(2)

        btn_search = self.browser.find_element_by_xpath("//input[@value='BUSCAR']")
        btn_search.click()

        if len(self.browser.window_handles) > 1:
            self.browser.switch_to.window(self.browser.window_handles[1])

        return self.browser.page_source

    def exit(self):
        self.browser.quit()







