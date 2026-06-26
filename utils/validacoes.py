from dados.listas import *
from datetime import datetime
import unicodedata
import re

#OBSERVAÇÃO: O Try e o Except são utilizados para retorna o erro ao usuário sem quebrar o código

#Função para validar se o campo recebe apenas valor, o ValueError serve para mostrar o erro do dado inválido para o tipo dele, mas sem quebrar o sistema
def validar_mensagem(mensagem):
    while True:
        try:
            numero = int(input(mensagem))

            if numero < 0:
                print('O valor não pode ser negativo!')
                continue

            return numero

        except ValueError:
            print('Apenas números são válidos!')


def validar_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))

            if numero < 0:
                print('O valor não pode ser negativo!')
                continue

            return numero

        except ValueError:
            print('Apenas números são válidos!')


def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, str(cpf))) #Ela serve para remover tudo que não for número de uma variável cpf.


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        print('O campo CPF precisa ter 11 números.')
        return None

    return cpf


def cpf_duplicado(cpf, clientes):
    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente['cpf']) == cpf:
            return True #Retorna true se encontrou

    return False #Retorna false se não encontrou


def mascarar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return None #Retorna None se não tem nada

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    #cpf[:3]      # 123
    #cpf[3:6]     # 456
    #cpf[6:9]     # 789
    #cpf[9:]      # 00


#Limpar o campo da data
def limpar_data(data):
    return ''.join(filter(str.isdigit, str(data)))


def validar_data_numeros(data):
    data = limpar_data(data)

    if len(data) != 8:
        print('A data deve possuir 8 números.')
        return None

    return data


#Mascarar as datas
def mascarar_data(data):
    data = limpar_data(data)

    if len(data) != 8:
        return None

    return f'{data[:2]}/{data[2:4]}/{data[4:]}'


#Validar a mascarar o número de telefone em tipo móvel (00000-0000)
def validar_telefone(mensagem, permitir_vazio=False):
    while True:
        entrada = input(mensagem)

        if permitir_vazio and entrada == '':
            return ''

        telefone = ''.join(filter(str.isdigit, entrada))

        if len(telefone) == 9:
            return f'{telefone[:5]}-{telefone[5:]}'

        print('O telefone deve possui 9 números')


def telefone_duplicado(telefone, clientes):
    telefone = ''.join(filter(str.isdigit, telefone))

    for cliente in clientes:
        telefone_cliente = ''.join(
            filter(str.isdigit, cliente['telefone'])
        )

        if telefone_cliente == telefone:
            return True

    return False


#Validar o e-mail
def validar_email(mensagem, permitir_vazio=False):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #Expressão para validar o e-mail

    while True:
        email = input(mensagem).strip()

        if permitir_vazio and email == '':
            return ''

        if re.match(padrao, email):
            return email

        print('E-mail inválido!')


def email_duplicado(email, clientes):
    email = email.lower().strip()

    for cliente in clientes:
        if cliente['email'].lower().strip() == email:
            return True

    return False


#Busca o cliente por código, se retornar resposta, ele mostra o dicionário do cliente
def buscar_cliente_por_codigo(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            return cliente
        
    return None


#Busca o profissional por código, se retornar resposta, ele mostra o dicionário do profissional
def buscar_profissional_por_codigo(codigo):
    for profissional in profissionais:
        if profissional['codigo'] == codigo:
            return profissional
        
    return None


#Busca o procedimento por código, se retornar resposta, ele mostra o dicionário do procedimento
def buscar_procedimento_por_codigo(codigo):
    for procedimento in procedimentos:
        if procedimento['codigo'] == codigo:
            return procedimento
        
    return None

def validar_texto(texto):
    texto = texto.lower().strip()

    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(
        letra for letra in texto
        if unicodedata.category(letra) != 'Mn'
    )

    texto = texto.replace(' ', '')

    return texto


def validar_hora(mensagem):
    while True:
        hora = input(mensagem)

        try:
            datetime.strptime(hora, '%H:%M')
            return hora

        except ValueError:
            print('Hora inválida! Use HH:MM.')


def validar_periodo(data_inicio, hora_inicio, data_fim, hora_fim):

    inicio = datetime.strptime(
        f'{data_inicio} {hora_inicio}',
        '%d/%m/%Y %H:%M'
    )

    fim = datetime.strptime(
        f'{data_fim} {hora_fim}',
        '%d/%m/%Y %H:%M'
    )

    if fim <= inicio:
        return False

    return True

def cliente_ocupado(codigo_cliente, inicio_novo, fim_novo, agendamentos):
    for agendamento in agendamentos:

        if agendamento['codigo_cliente'] != codigo_cliente:
            continue

        inicio = datetime.strptime(
            f"{agendamento['data_inicio']} "
            f"{agendamento['hora_inicio']}",
            '%d/%m/%Y %H:%M'
        )

        fim = datetime.strptime(
            f"{agendamento['data_fim']} "
            f"{agendamento['hora_fim']}",
            '%d/%m/%Y %H:%M'
        )

        if inicio_novo < fim and fim_novo > inicio:
            return True

    return False

def profissional_ocupado(codigo_profissional, inicio_novo, fim_novo, agendamentos):
    for agendamento in agendamentos:

        if agendamento['codigo_profissional'] != codigo_profissional):
            continue

        inicio = datetime.strptime(
            f"{agendamento['data_inicio']} "
            f"{agendamento['hora_inicio']}",
            '%d/%m/%Y %H:%M'
        )

        fim = datetime.strptime(
            f"{agendamento['data_fim']} "
            f"{agendamento['hora_fim']}",
            '%d/%m/%Y %H:%M'
        )

        if inicio_novo < fim and fim_novo > inicio:
            return True

    return False

