import smtplib
import random

def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))

def send_email(emai_send, ma_xac_nhan):
    email = 'phuchau.fit@gmail.com'
    password = 'cmjvyzayiwyjbyxk'
    # emai_send = 'phuchau.2005.vlg@gmail.com'

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)

    subject = 'Xac nhan dang nhap'
    body = f'Hay xac nhan dang nhap bang ma sau: {ma_xac_nhan}\nChu y: Khong chia se ma nay cho bat ky ai!'
    content = f'Subject: {subject}\n\n{body}'

    session.sendmail(email, emai_send, content)

