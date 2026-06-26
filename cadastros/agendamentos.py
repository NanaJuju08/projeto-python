from dados.listas import agendamentos, clientes, status_agendamento
from utils.validacoes import *


def buscar_cliente_por_codigo(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            return cliente

    return None


def cadastrar_agendamento():
    while True:
        agendamento = {}
        agendamento['codigo'] = len(agendamentos) + 1

        print(
            'Tudo pronto para o cadastro do agendamento.\n'
            'Abaixo, insira as informações necessárias para concluir o cadastro!\n'
        )

        while True:
            codigo_cliente = validar_mensagem('Código do cliente: ')
            cliente = buscar_cliente_por_codigo(codigo_cliente)

            if cliente is None:
                print('Cliente não encontrado!')
                continue

            agendamento['codigo_cliente'] = codigo_cliente
            agendamento['nome_cliente'] = cliente['nome']
            break

        agendamento['descricao'] = input('Descrição: ')
        agendamento['data_inicio'] = validar_data('Data de ínicio (Ex.: dd/mm/aaaa): ')
        agendamento['hora_inicio'] = input('Horário de início (Ex.: HH:mm):')
        agendamento['data_fim'] = validar_data('Data de fim (Ex.: dd/mm/aaaa): ')
        agendamento['hora_fim'] = input('Horário de início (Ex.: HH:mm):')


        agendamentos.append(agendamento)

        print(
            '\nAgendamento cadastrado com sucesso!'
            '\n========== DADOS DO AGENDAMENTO =========='
        )

        for chave, valor in agendamento.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro agendamento? (S/N): ').upper()

        if continuar != 'S':
            break


def alterar_agendamento():

    print(
            'Tudo pronto para o cadastro do agendamento.\n'
            'Abaixo, insira as informacoes necessarias para concluir o cadastro!\n'
        )


def pesquisar_agendamento():
    print('Pesquisar')

    
def deletar_agendamento():
    print('Deletar')