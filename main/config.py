from pathlib import Path
import os

ROOT_DIR = Path(os.path.abspath(os.path.join(__file__, os.pardir))).parent

VERSION = '1.0'
#SEARCH_ROOT = "http://portal.imprensanacional.gov.br/pesquisa"
SEARCH_ROOT = "https://pesquisa.in.gov.br/imprensa/core/start.action"
WEBDRIVER_PATH = os.path.join(ROOT_DIR, 'webdrivers/')
TEMP_DIR = "/tmp/dousearch/data/"
DEFAULT_WEBDRIVER = 1
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
