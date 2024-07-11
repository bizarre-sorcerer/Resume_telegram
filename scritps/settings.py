import pdfkit
import os

BASE_DB_FOLDER = 'db'

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

options = {
    'dpi': 365,
    'page-size': 'A4',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    'encoding': "UTF-8",
    'custom-header' : [
    ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None,
}

SERVICE_NAME = 'guitvcer_resume_bot'

BASE_DB_FOLDER = 'db'

WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

BASE_PATH = os.path.dirname(__file__)

MEDIA_URL = os.path.join(BASE_PATH, 'media')

BIRTH_DATE_FORMAT = 'dd-mm-yyyy'

TOKEN = "5967331395:AAHAUexUYWfnRTG5953gPtlaPamh5c4aIbg"