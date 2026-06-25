from datetime import datetime
import re

def validar_mensagem(mensagem):
    while True:
        try:
            numero = int(input(mensagem))

            if numero < 0:
                print('O valor nao pode ser negativo!')
                continue

            return numero

        except ValueError:
            print('Apenas numeros sao validos!')


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        print('O campo CPF precisa ter 11 numeros.')
        return None

    return cpf


def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, str(cpf)))


def cpf_duplicado(cpf, clientes):
    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente['cpf']) == cpf:
            return True

    return False


def mascarar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return None

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def validar_data(mensagem):
    while True:
        data = input(mensagem)

        try:
            datetime.strptime(data, '%d/%m/%Y')
            return data
        except ValueError:
            print('Data invalida! Use o formato dd/mm/aaaa.')

def validar_telefone(mensagem):
    while True:
        telefone = ''.join(filter(str.isdigit, input(mensagem)))

        if len(telefone) == 9:
            return f'{telefone[:5]}-{telefone[5:]}'

        print('Telefone invalido! Use o formato 00000-0000.')

def validar_email(mensagem):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input(mensagem).strip()

        if re.match(padrao, email):
            return email

        print('E-mail invalido!')