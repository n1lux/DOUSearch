from unittest import TestCase
from core.webscrapy import DOU
from core.douparser import DouParser
import json


class TestDouSearch(TestCase):
    def setUp(self):
        self.dou = DOU()
        self.term = "term to search"

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


class TestPDFResouce(TestCase):

    def setUp(self):
        self._url = "http://pesquisa.in.gov.br/imprensa/jsp/visualiza/index.jsp?jornal=2&pagina=33&data=16/05/2017"

    def test_download_pdf_dou_withou_tempdir(self):
        from core.download import PDFResource
        with self.assertRaises(Exception) as context:
            pdf = PDFResource()

        self.assertIn("TEMP_DIR not defined", str(context.exception))

    def test_download_pdf_dou_withou_useragent(self):
        from core.download import PDFResource
        with self.assertRaises(Exception) as context:
            pdf = PDFResource()

        self.assertIn("USER_AGENT not defined", str(context.exception))

    def test_download_pdf_dou(self):
        from core.download import PDFResource
        pdf = PDFResource()
        file = pdf.download(url=self._url)
        self.assertTrue(isinstance(file, bytes))

    def test_download_pdf_save(self):
        from core.download import PDFResource
        pdf = PDFResource()
        pdf.download(url=self._url)
        pdf.save()
