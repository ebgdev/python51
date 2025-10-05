# simple mail transfer protocol

import smtplib
from email.message import EmailMessage
from datetime import datetime

customers = [
    {'name':'customer1','surname':'surname1','email':'xxxxxxx@gmail.com','birthdate':'10-02'},
    {'name':'customer2','surname':'surname2','email':'xxxxxxx@gmail.com','birthdate':'10-02'},
    {'name':'customer3','surname':'surname3','email':'xxxxxxx@gmail.com','birthdate':'10-02'},
]

today = datetime.now().strftime('%m-%d')

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_personal_gmail@gmail.com'
EMAIL_PASSWORD = 'app password from google account'


for customer in customers:
    if customer['birthdate'] == today:
        msg = EmailMessage()

        msg['Subject'] = f'Happy Birthday {customer['name']}'
        msg['To'] = customer['email']
        msg['From'] = EMAIL_ADDRESS
        name_concat = customer['name'] + ' ' + customer['surname']

        msg.set_content(f"""Happy Birthday {name_concat}.
                        Wishing you a fantastic birthday filled with joy, success, and happiness! 🥳
                        Thank you for being a valued customer.
                        Best regards,  
                        FastAlgoPy Team
                        """)
        

        try:
            with smtplib.SMTP(SMTP_SERVER,SMTP_PORT) as smtp:
                # start transfer layer security
                smtp.starttls()
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
                print('Mail sent successfully.')
        except Exception as e:
            print('failure. Mail does not send.')
            print(e)