from bs4 import BeautifulSoup as bs
import re
import json


class DouParser:
    def __init__(self, source):
        self.source = source

    def _soup(self):
        return bs(self.source, 'html.parser')

    @staticmethod
    def _clean_text(text):
        return re.sub('\s+', ' ', text)

    @staticmethod
    def _has_data(elem):
        for c in elem.findChildren():
            try:
                return 'data' in c.get('class')
            except TypeError:
                return False

    @staticmethod
    def _to_json(data):
        return json.dumps(data, sort_keys=True, indent=4)

    def _get_data(self, elem):
        info = {}

        try:
            th = elem.find('th')
            info['preview'] = self._clean_text(th.a.get_text(strip=True))
            info['pdf_dou_url'] = th.a.get('href')
        except AttributeError:
            print("Tag has not info")

        try:
            td = elem.find('td')
            info['resume'] = self._clean_text(td.get_text(strip=True))
        except AttributeError:
            print("Tag has not info")

        return info

    def parser(self):
        soup = self._soup()
        data = []

        tb_info = soup.find(name='table', attrs={'id': 'ResultadoConsulta'})

        if tb_info:
            tr_iter = iter(tb_info.find_all('tr'))
            for tr in tr_iter:
                dou_info = {}
                if self._has_data(elem=tr):
                    dou_info.update(self._get_data(elem=tr))
                    dou_info.update(self._get_data(elem=next(tr_iter)))
                    data.append(dou_info)

        return self._to_json(data)
