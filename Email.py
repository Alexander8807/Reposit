import smtplib
from email.message import EmailMessage

server = smtplib.SMTP_SSL("smtp.zone.eu", 465)  #выбор порта SMTP или SMTP_SSl, создание соединения
server.login("mario329@mail.ru", "000000000")

msg = EmailMessage()
msg["Subject"] = "Sample email sent by python"
msg["From"] = "mario329@mail.ru"
msg["To"] = "aleksandr-petris@mail.ru"
msg.set_content("Sample email sent with python script")  #только текстовое письмо
msg.add_alternative("""     #любое письмо
    <!DOCTYPE>
    <html>
        <body>
            <h1 style="color: red;">Sample email</h1>
        <body>
    <html>    """, subtype="html") #тип эмейла

server.send_message(msg) #отправка