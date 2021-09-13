import pdfkit 

kitoptions = {"enable-local-file-access": None, "encoding":"UTF-8", "load-media-error-handling": "Skip"} #Dernier tuple du dictionnaire permet normalement de skip s'il arrive pas a lire le media 
pdfkit.from_file("C:/Users/Jonathan/Desktop/HTML_THOMAS/test.html", "Out.pdf", options=kitoptions)
