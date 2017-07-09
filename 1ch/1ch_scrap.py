import smtplib

def smtp():
    smtplib.SMTP('127.0.0.1', port=66000)


if __name__ == '__main__':
    smtp()
    