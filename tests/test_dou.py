from unittest import TestCase
from core.webscrapy import ScrapeDOU
from core.douparser import DouParser


class TestDou(TestCase):
    def setUp(self):
        self.dou = ScrapeDOU()

    def tearDown(self):
        self.dou.exit()

    def test_search(self):
        res = self.dou.search(term="universidade federal dos vales do jequitinhonha e mucuri")
        self.assertIn('itens encontrados', res)

    def test_parser_dou(self):
        res = self.dou.search(term="universidade federal dos vales do jequitinhonha e mucuri")
        dou = DouParser(source=res)
        dou_parsed = dou.parser()
