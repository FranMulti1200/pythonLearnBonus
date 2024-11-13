from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)
    pdf.line(10, 21, 200, 21)

    #set line in between
    for i in range(31, 277, 10):
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt='',border='B', align="L", ln=1)

    #set page without header
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set line in between
        for i in range(8, 274, 10):
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt='', border='B', align="L", ln=1)


pdf.output("output.pdf")
