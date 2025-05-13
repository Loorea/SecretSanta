from dotenv import load_dotenv
import random
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def send_email(sender, receiver_email, recipient):
    password = "suasenhaaqui"
    subject = "Seu Presente de Amigo Secreto"
    body_msg = f'''\
Oi! O seu amigo secreto é: {recipient}!
Lembre-se de gastar entre R$ 50 a R$ 100 no presente, mas não se preocupe em encontrar o presente perfeito!
'''

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body_msg, 'plain', 'utf-8'))

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            print("Login bem-sucedido!")
            server.sendmail(sender, receiver_email, msg.as_string())
            print(f"E-mail enviado para {recipient}")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar o e-mail para {recipient}: {e}")

names_and_emails = [
    ['Eduardo', 'eduardo@gmail.com'],
    ['Sofia', 'sofia@gmail.com'],
    ['Henrique', 'henrique@gmail.com'],
    ['Bruno', 'bruno@gmail.com'],
    ['Larissa', 'larissa@gmail.com'],
]

def generate_pairs(names):
    while True:
        shuffled = names[:]
        random.shuffle(shuffled)
        pairs = list(zip(names, shuffled))
        if all(giver[0] != receiver[0] for giver, receiver in pairs):
            return pairs

pairs = generate_pairs(names_and_emails)

for giver, receiver in pairs:
    send_email("seuemail@gmail.com", giver[1], receiver[0])
    print(f"Email enviado para {giver[0]} sobre seu amigo secreto {receiver[0]}")
