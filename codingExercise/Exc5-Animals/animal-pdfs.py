#import pandas as pd
from click import style
from fpdf import FPDF
import glob
from pathlib import Path


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

files = glob.glob("animals-txt/*.txt")

for file in files:
    pdf.add_page()
    filename = Path(file).stem
    animal_name = filename.title()
    pdf.set_font(family="helvetica", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name)

pdf.output("animals.pdf")
