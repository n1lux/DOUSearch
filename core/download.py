import requests
from main import config
from urllib.parse import urlparse
from urllib.parse import parse_qs
from core.utils import source_soup


class PDFResource:
    def __init__(self):
        try:
            self.temp_dir = config.TEMP_DIR
        except AttributeError:
            raise Exception("TEMP_DIR not defined in config.py")

        try:
            self.user_agent = config.USER_AGENT
        except AttributeError:
            raise Exception("USER_AGENT not defined in config.py")

        self._chunk_size = 1024
        self._pdf_url = None
        self._stored_pdf_file_uri = None
        self._pdf_file_content = None

    def _request(self, url):
        headers = {'User-Agent': self.user_agent}

        try:
            return requests.get(url=url, stream=True, headers=headers)
        except:
            return None

    @staticmethod
    def _parse_file_name(url):
        name = ''
        url_parsed = urlparse(url=url)
        args = parse_qs(url_parsed.query)
        for k, v in args.items():
            name += "{}_{}".format(k, str(v[0]).replace('/', ''))

        return name

    def download(self, url):
        self._pdf_url = url
        res = self._request(url=url)
        pdf_url, pdf_content = None, None
        content_soup = source_soup(res.content)

        for c in content_soup.find_all('frame'):
            if c.get('name') == 'visualizador':
                pdf_url = c.get('src')

        if pdf_url:
            url = '{}/{}'.format('http://pesquisa.in.gov.br/imprensa', pdf_url.replace("../../", ''))
            pdf_content = self._request(url=url)

        self._pdf_file_content = pdf_content

        return pdf_content

    def save(self, file_name=None, dir_name=None):
        name = self._parse_file_name(url=self._pdf_url)

        if file_name and dir_name:
            _file = "{}{}/{}.pdf".format(self.temp_dir, dir_name, file_name)
        else:
            _file = "{}{}.pdf".format(self.temp_dir, name)

        try:
            with open(_file, 'wb') as fd:
                for chunk in self._pdf_file_content.iter_content(self._chunk_size):
                    fd.write(chunk)
        except FileNotFoundError:
            raise Exception("Dir not found...")

        self._stored_pdf_file_uri = _file
        return True

    def to_text(self):
        pass
