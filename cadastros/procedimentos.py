from dados.listas import procedimentos
from utils.validacoes import *


def cadastrar_procedimento():
    while True:
        procedimento = {}
        procedimento['codigo'] = len(procedimentos) + 1

        print(
            'Tudo pronto para o cadastro do procedimento.\n'
            'Abaixo, insira as informacoes necessarias para concluir o cadastro!\n'
        )

        print(
            '\procedimento cadastrado com sucesso!'
            '\n========== DADOS DO PROCEDIMENTO =========='
        )

        for chave, valor in procedimento.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro procedimento? (S/N): ').upper()

        if continuar != 'S':
            break
