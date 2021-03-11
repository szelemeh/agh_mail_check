import os
from agh_mail import AghMail
from win10toast import ToastNotifier
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("AGH_MAIL_USERNAME")
password = os.getenv("AGH_MAIL_PASSWORD")

mail = AghMail(uname=username, pwd=password)
emails = mail.get_unread_adresses()

size = len(emails)
if size >= 1:
    toaster = ToastNotifier()
    title = f"{len(emails)} new email"
    if size > 1:
        title += "s."
    else:
        title += "."
    toaster.show_toast(title, "At shelest@student.agh.edu.pl")
    exit()
