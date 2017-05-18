from unittest import TestCase
from core.webscrapy import DOU
from core.douparser import DouParser
import json


class TestDou(TestCase):
    def setUp(self):
        self.dou = DOU()
        self.term = "universidade federal dos vales do jequitinhonha e mucuri"

    def tearDown(self):
        self.dou.exit()

    def test_search(self):
        res = self.dou.search(term=self.term)
        self.assertIn('itens encontrados', res)

    def test_search_year(self):
        res = self.dou.search(term=self.term, year='2013')
        self.assertIn('itens encontrados', res)

    def test_search_start(self):
        res = self.dou.search(term=self.term, start='01/01')
        self.assertIn('itens encontrados', res)

    def test_search_end(self):
        res = self.dou.search(term=self.term, end='01/04')
        self.assertIn('itens encontrados', res)

    def test_search_start_end_year(self):
        res = self.dou.search(term=self.term, start='01/01', end='12/12', year='2017')
        self.assertIn('itens encontrados', res)

    def test_parser_dou(self):
        res = self.dou.search(term=self.term, start='01/01', end='12/12', year='2017')
        dou = DouParser(source=res)
        dou_parsed = json.loads(dou.parser())
        self.assertIsInstance(dou_parsed, list)
