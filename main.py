from fpdf import FPDF
import pandas as pd

#create a pdf instance using fpdf
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for ind, row in df.iterrows():
    #add pages to the instance
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24) #mentioned above statements to apply to them
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21) #creates line from (x1,y1) , (x2,y2)

#create and store the pdf
pdf.output("output.pdf")