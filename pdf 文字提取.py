import pdfplumber
path=r'C:\Users\lenovo\Desktop\研究报告\《水果生鲜研究报告》.pdf'

with pdfplumber.open(path) as pdf:
    page=pdf.pages[3]
    print(page.extract_text())
