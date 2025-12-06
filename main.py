from fpdf import FPDF
import pandas as pd

#create a pdf instance using fpdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #sets auto page break to false

df = pd.read_csv("topics.csv")

for ind, row in df.iterrows():
    #add pages to the instance
    pdf.add_page()

    #set the header
    pdf.set_font(family="Times", style="B", size=24) #mentioned above statements to apply to them
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    #pdf.line(x1=10, y1=20, x2=200, y2=20)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    pdf.ln(265) #adds breakline, pagebreak

    #set the footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for _ in range(row["Pages"] - 1):
        pdf.add_page()

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(276) #adds breakline, pagebreak
        #set the footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

#create and store the pdf
pdf.output("output.pdf")