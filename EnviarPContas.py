#!/usr/bin/env python
# coding: utf-8

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os
import base64
import pandas as pd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def EnviarPContas(path):
    
    # Importa o arquivo com os contatos e transforma em dataframe
    lista_envio = pd.read_excel(path)
    
    for index in lista_envio.index:
        
        # Busca os dados do contato no dataframe
        nome_completo = str(lista_envio["Nome Completo"][index])
        ano = str(lista_envio["Qual o ano de recebimento do Bolsa Atleta?"][index])
        email = str(lista_envio["E-Mail"][index])
        
        # Gera o path e nome do arquivo para ser anexado
        arquivo = ano + " " + nome_completo + ".pdf"
        arquivo_path = "Z:/Documentos/Ministério do Esporte/Bolsa Atleta/Prestação de Contas/Prestação de Contas " + ano + "/" + arquivo

        message = Mail(
            from_email="inscricoes@remobrasil.com",
            to_emails=email
        )
        
        # Variaveis do Template SendGrid
        message.dynamic_template_data = {
            "nome-completo": nome_completo
        }
        
        # ID do Template
        message.template_id = "d-05b5c69596134834b49cf68702d97396"
        
        # Anexando o arquivo
        with open(arquivo_path, "rb") as f:
            data = f.read()
            f.close()

        encoded_file = base64.b64encode(data).decode()

        attachedFile = Attachment(
            FileContent(encoded_file),
            FileName(arquivo),
            FileType("application/pdf"),
            Disposition("attachment")
        )

        message.attachment = attachedFile
        
        # Envio do email
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("Enviado para {}" .format(email))
        except Exception as e:
            print(e.message)

if __name__ == "__main__":
    EnviarPContas(path=input("Qual o caminho do arquivo com as solicitações? "))