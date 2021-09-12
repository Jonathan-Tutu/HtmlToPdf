import pdfkit
from datetime import datetime, timedelta

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time #sleep

date = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d") #On récupère le jour précédent et on le convertit en string
final_date = date.replace("-", "")
Chemin = "C:/Users/Jonathan/Desktop/RapportJournalier_" + final_date + "/" #Chemin a modifier
kitoptions = {"enable-local-file-access": None, "encoding":"UTF-8"}
NomFichier = "RapportJournalier_" + final_date
pdfkit.from_file(Chemin + NomFichier + ".htm", Chemin + NomFichier + ".pdf", options=kitoptions)

time.sleep(30)

#Gestion mail
try:
    fromaddr = "TestSMTPAPITSE@gmail.com" #TOCHANGE
    toaddr = "TestSMTPAPITSE@gmail.com" #TOCHANGE
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Rapport Journalier " + final_date
    body = "Rapport Journalier TITAN du " + final_date
    msg.attach(MIMEText(body, 'plain'))
    filename = NomFichier + ".pdf"
    attachment = open(Chemin + NomFichier + ".pdf", "rb") #Chemin a modifier

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()
    s.login(fromaddr, "rnjxmzjznkqqbsvv") #TOCHANGE
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

        