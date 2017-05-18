from unittest import TestCase
from core.webscrapy import ScrapeDOU


class TestDou(TestCase):
    def setUp(self):
        self.dou = ScrapeDOU()

    def tearDown(self):
        self.dou.exit()

    def test_search(self):
        self.dou.search(term="universidade federal dos vales do jequitinhonha e mucuri")