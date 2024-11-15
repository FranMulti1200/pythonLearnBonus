from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
files = glob.glob("animals-txt/*.txt")

# Create a one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")
#pdf.set_auto_page_break(auto=False, margin=0)

# Go through each text file
for file in files:
    # Add a page to the PDF document for each text file
    pdf.add_page()
    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(file).stem
    animal_name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="helvetica", size=16, style="B")
    pdf.cell(w=50, h=8, txt=animal_name, ln=1)

    # Get the content of each text file
    with open(file, "r") as file_animal:
        content = file_animal.read()
    # Add the text file content to the PDF
    pdf.set_font(family="helvetica", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Produce the PDF
pdf.output("animals.pdf")
