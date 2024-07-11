import io
from collections import defaultdict
import pdfkit
from jinja2 import Environment, select_autoescape, FileSystemLoader
import scritps.settings as settings
from scritps.db import *; 


file_loader = FileSystemLoader('templates')
env = Environment(
    loader=file_loader,
    autoescape=select_autoescape(),
)

def get(filepath: str, context: dict) -> str:
    template = env.get_template(filepath)
    return template.render(context)

def convert_pdf(resume: dict):
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

    return pdfkit.from_string(
        input=resume,
        configuration=settings.config,
        options=options,
    )

def generate_resume_file(resume: dict) -> io.BytesIO:
    create_resume(**resume)

    resume = defaultdict(lambda: None, resume)
    print(resume)

    context = {'resume': resume}
    template = get('resume.html', context)
    pdf = convert_pdf(template)

    pdf = io.BytesIO(pdf)
    pdf.name = f'{resume["FIO"]}.pdf'

    return pdf
