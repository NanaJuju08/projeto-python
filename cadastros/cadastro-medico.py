from datetime import datetime
import re #regex - é uma sequência de caracteres que forma um padrão de busca, usada de forma rápida para validar, encontrar, ou substituir textos e dados que seguem regras específicas (como formatos de e-mail, CPF, ou senhas).

medicos = {}

def cadastro_medico():
    while True:
        codigo = int(input('Digite o código do novo médico: '))
        if codigo in medicos:
            print('Código já em uso, tente outro.')
            continue
        else: 
            nome = input('Digite o nome do novo médico: ')
            data_nascimento  = input("Digite a data de nascimento do novo médico (DD/MM/AAAA): ")
            data = datetime.strptime(data_nascimento , "%d/%m/%Y")
            cpf_numeros = input('Digite o CPF do novo médico: ')
            cpf = re.sub(r'\D', '', cpf_numeros)
            cpf_duplicado = False

            if len(cpf) != 11:
                print('CPF inválido!')
                continue

            for dados in medicos.values():
                if dados[2] == cpf:
                    cpf_duplicado = True
                    break

            if cpf_duplicado:
                print('CPF já está em uso!')
                continue

            sexo = input('Digite o sexo do novo médico: ').upper()
            telefone= int(input('Digite o número de telefone do novo médico: '))
            email = input('Digite o email do novo médico: ')
            if not re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
                print('Email inválido!')
                continue

            medicos[codigo] = (nome, data_nascimento, cpf, sexo, telefone, email)
            break

cadastro_medico()

print(medicos)