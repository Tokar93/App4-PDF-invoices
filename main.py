from fpdf import FPDF
from pathlib import Path
import glob

animals = glob.glob('animals/*.txt')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for animal in animals:
    with open(animal, 'r') as file:
        description = file.read()
    animal_name = Path(animal).stem.title()
    pdf.add_page()
    pdf.set_font(size=16, style='B', family='Times')
    pdf.cell(w=0, h=12, txt=animal_name, align='L',
             ln=1, border=0)
    pdf.set_font(size=10, family='Times' )
    pdf.multi_cell(w=0, h=5, txt=description)
    #pdf.cell(w=0, h=12, txt=description, align='L',
             #ln=1, border=0)

pdf.output('output.pdf')

