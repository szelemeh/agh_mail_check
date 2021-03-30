import os
if os.name == "nt":
    from win10toast import ToastNotifier

    def notify(title, message):
        toaster = ToastNotifier()
        toaster.show_toast(title, f"At {username}")
elif os.name == 'posix':
    def notify(title, message):
        os.system(f"""
            osascript -e 'display notification {message} with title {title}'
            """)


from agh_mail import AghMail
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("AGH_MAIL_USERNAME")
password = os.getenv("AGH_MAIL_PASSWORD")

mail = AghMail(uname=username, pwd=password)
emails = mail.get_unread_adresses()

size = len(emails)
if size >= 1:
    title = f"{len(emails)} new email"
    if size > 1:
        title += "s."
    else:
        title += "."
    notify(title, f"At {username}")
    exit()
