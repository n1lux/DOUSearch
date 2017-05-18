from pathlib import Path
import os

ROOT_DIR = Path(os.path.abspath(os.path.join(__file__, os.pardir))).parent

SEARCH_ROOT = "http://portal.imprensanacional.gov.br/pesquisa"
WEBDRIVER_PATH = os.path.join(ROOT_DIR, 'webdrivers/')
TEMP_DIR = "/tmp/dousearch/data/"
DEFAULT_WEBDRIVER = 1