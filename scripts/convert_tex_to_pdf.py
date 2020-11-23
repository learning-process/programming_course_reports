from pdflatex import PDFLaTeX
import sys
filename = sys.argv[1]
pdfl = PDFLaTeX.from_texfile(filename)
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)