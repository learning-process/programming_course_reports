import pdflatex
import sys

filename = sys.argv[1]
pdf_descriptor = pdflatex.PDFLaTeX.from_texfile(filename)
pdf, log, completed_process = pdf_descriptor.create_pdf(keep_pdf_file=True, keep_log_file=True)
