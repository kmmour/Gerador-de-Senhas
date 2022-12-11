#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import choice
import string
from time import sleep
from datetime import datetime
import os

# Salvando o último acesso 

def salvar_data():
    with open('txt.txt', 'w') as my_file:
        my_file.write(str(datetime.date(datetime.now())))

def ler_data():
    if os.path.isfile('./txt.txt'):
        with open('txt.txt', 'r') as my_file:
            resposta = my_file.read()
        return resposta
    else:
        return 'Esse é o seu primeiro acesso! :)'

# Inicio

def gerador_senha():
    senha_tipo_1 = string.digits
    senha_tipo_2 = string.digits + string.punctuation + string.ascii_letters
    senha_tipo_3 = string.digits + string.ascii_letters
    senha_gerada = ''

# Contato inicial com o usuário

    print('-'*45)
    print('\033[1mGerador de senhas\033[m'.center(50))
    print(f'Seu último acesso: {ler_data()}'.center(50)) 
    print('-'*45)
    print('Bem-vindo ao gerador de senhas automático!')
    sleep(1)
    print('Tipos de senhas \033[1;32mdisponíveis:\033[m'.center(50))
    print('\033[1;32m\n[1]:\033[m Números\n\033[1;32m[2]:\033[m Números + Símbolos + Letras')
    print('\033[1;32m[3]:\033[m Números + Letras')
    sleep(1)

# Perguntas para gerar a senha e tratamento de erros

    try:
        tipo_de_senha = int(input('\nDigite o tipo de senha que deseja: '))

        if tipo_de_senha >3 or tipo_de_senha <1:
            while tipo_de_senha >3 or tipo_de_senha <1:
                print('\033[1;31mErro ao gerar a senha! Informe um número de 1 a 3:\033[m ')
                tipo_de_senha = int(input('\nDigite o tipo de senha que deseja: '))
        if tipo_de_senha <=4 or tipo_de_senha >=1:
            tamanho = int(input('\nDigite quantos digitos você quer na sua senha: '))
            if tipo_de_senha == 1:
                for i in range (tamanho):
                    senha_gerada += choice(senha_tipo_1)
            elif tipo_de_senha == 2:
                for i in range (tamanho):
                    senha_gerada += choice(senha_tipo_2)
            elif tipo_de_senha == 3:
                for i in range (tamanho):
                    senha_gerada += choice(senha_tipo_3)
        print(f'\n\033[1mEssa foi a senha gerada:\033[m \033[1;32m{senha_gerada}\033[m')
        if tamanho <=7:
            print('\033[1;33mPara uma senha mais segura, informe um digito maior ou igual a 8!\033[m')

    except ValueError:
            print(f'\033[1;31m\nErro ao gerar senha!\033[m')
            print('Para que a sua senha seja gerada:\033[m\n\033[1;31m[1]:\033[m Não digite símbolos\n\033[1;31m[2]:\033[m Não digite o número por extenso')

    finally:
        print('\nDeseja tentar novamente?')
        repeticao = input('Digite (1) para \033[1;32mSIM\033[m e (2) para \033[1;31mNÃO\033[m: ')
        if repeticao == '1':
            gerador_senha()
        elif repeticao == '2':
            salvar_data()
            print('\nVolte sempre!')
        
gerador_senha()

