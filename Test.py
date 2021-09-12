import pdfkit 

kitoptions = {"enable-local-file-access": None, "encoding":"UTF-8"}
pdfkit.from_file("C:/Users/Jonathan/Desktop/HTML_THOMAS/test.html", "Out.pdf", options=kitoptions)
