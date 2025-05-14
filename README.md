# 🤫 Secret Santa (Amigo Secreto por E-mail)

Este é um script em Python que realiza o sorteio de um **Amigo Secreto** (Secret Santa) entre participantes e envia automaticamente um e-mail informando quem é o amigo secreto de cada um.

## 📋 Requisitos

- Python 3.8 ou superior
- Conta Gmail com autenticação de dois fatores ativada
- Senha de aplicativo gerada no [Google Account](https://myaccount.google.com/apppasswords)
- Acesso à internet para envio dos e-mails

## 📁 Estrutura de Arquivos
````
SecretSanta/
├── src/
│ └── secret_santa.py
├── .env
└── README.md

````

## ⚙️ Configuração

1. **Clone o repositório** ou copie os arquivos para sua máquina.

2. **Crie um arquivo `.env` na raiz do projeto** com o seguinte conteúdo:
````
PASSWORD=sua_senha_de_aplicativo_aqui
````

3. **Instale as dependências** (se necessário):

````
pip install python-dotenv
````

## ✉️ Como funciona
O script secret_santa.py:

Define uma lista de participantes com seus respectivos nomes e e-mails.

Embaralha e sorteia os pares de amigo secreto.

Envia e-mails personalizados para cada participante informando quem é seu amigo secreto.

## ▶️ Executando o projeto
No terminal, navegue até o diretório src/ e execute:
````
python secret_santa.py
````
## 📌 Observações importantes
Certifique-se de que todos os e-mails listados são válidos.

Evite repetir e-mails.

A senha do aplicativo é necessária pois o Google não permite mais login por senha comum em scripts.

## 📧 Exemplo de e-mail enviado

From: seuemail@gmail.com
Subject: Seu Presente de Amigo Secreto

Oi! O seu amigo secreto é: Sofia!
Lembre-se de gastar entre R$ 50 a R$ 100 no presente, mas não se preocupe em encontrar o presente perfeito!


## **Divirta-se com seu Amigo Secreto! 🎁**

---
