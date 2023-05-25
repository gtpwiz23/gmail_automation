import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

smtp_instance = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)

smtp_instance.ehlo()
smtp_instance.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
smtp_instance.sendmail('pythonsmtp777@gmail.com', ['nzarzycki@gmail.com','akojichubiyojo1997@gmail.com'], 
                    'Subject: Our first project.\nDear Alice, so long and thanks for all the fish. Sincerely, Boyo')
smtp_instance.quit()

