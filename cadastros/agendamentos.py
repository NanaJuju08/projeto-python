from dados.listas import agendamentos
from utils.validacoes import *


def cadastrar_agendamento():
    while True:
        agendamento = {}
        agendamento['codigo'] = len(agendamentos) + 1

        print(
            'Tudo pronto para o cadastro do agendamento.\n'
            'Abaixo, insira as informacoes necessarias para concluir o cadastro!\n'
        )

        print(
            '\Agendamento cadastrado com sucesso!'
            '\n========== DADOS DO AGENDAMENTO =========='
        )

        for chave, valor in agendamento.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro agendamento? (S/N): ').upper()

        if continuar != 'S':
            break
