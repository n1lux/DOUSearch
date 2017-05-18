from bs4 import BeautifulSoup as bs
import re


class DouParser:
    def __init__(self, source):
        self.source = source

    def _soup(self):
        return bs(self.source, 'html.parser')

    @staticmethod
    def _clean_text(text):
        return re.sub('\s+', ' ', text)

    def parser(self):
        soup = self._soup()
        info = {}

        tb_info = soup.find(name='table', attrs={'id': 'ResultadoConsulta'})

        if tb_info:
            for tr in tb_info.find_all('tr'):
                try:
                    th = tr.find('th')
                    info['preview'] = self._clean_text(th.a.get_text(strip=True))
                    info['pdf_dou_url'] = th.a.get('href')
                    continue
                except AttributeError:
                    print("Tag has not info")

                try:
                    td = tr.find('td')
                    info['resume'] = self._clean_text(td.get_text(strip=True))
                except AttributeError:
                    print("Tag has not info")

        return info
