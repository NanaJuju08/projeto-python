from dados.listas import *
from utils.validacoes import *

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

        while True:
            codigo_profissional = validar_mensagem('Código do profissional: ')
            profissional = buscar_profissional_por_codigo(codigo_profissional)

            if profissional is None:
                print('Profissional não encontrado!')
                continue

            agendamento['codigo_profissional'] = codigo_profissional
            agendamento['nome_profissional'] = profissional['nome']
            break

        
        while True:
            codigo_procedimento = validar_mensagem('Código do procedimento: ')
            procedimento = buscar_procedimento_por_codigo(codigo_procedimento)

            if procedimento is None:
                print('Procedimento não encontrado!')
                continue

            agendamento['codigo_procedimento'] = codigo_procedimento
            agendamento['nome_procedimento'] = procedimento['nome']
            break

        agendamento['descricao'] = input('Descrição: ')

        while True:
            data_inicio = validar_data_numeros(
                input('Data de início (ddmmaaaa): ')
            )

            if data_inicio:
                agendamento['data_inicio'] = mascarar_data(data_inicio)
                break

        agendamento['hora_inicio'] = validar_hora('Horário de início:')

        while True:
            data_fim = validar_data_numeros(
                input('Data de fim (ddmmaaaa): ')
            )

            if data_fim:
                agendamento['data_fim'] = mascarar_data(data_fim)
                break

        agendamento['hora_fim'] = validar_hora('Horário de início:')

        if not validar_periodo(agendamento['data_inicio'], agendamento['hora_inicio'], agendamento['data_fim'], agendamento['hora_fim']):
            print('A data/hora final deve ser maior que a data/hora inicial.')
            continue

        #As tuplas sempre começam pelo index 0, então, enumeramos começando pelo 1 para mostrar ao usuário
        #Porém o python ainda usa a index começada pelo 0, então, fazemo a opção do usuário(1,2,3..) -1 para o python(0,1,2..)
        #O -1 converte:

        #Usuário:
        #1 - Agendado
        #2 - Confirmado
        #3 - Em andamento
        #4 - Concluído

        #Tupla:
        #0 - Agendado
        #1 - Confirmado
        #2 - Em andamento
        #3 - Concluído

        print('\nStatus do agendamento:')

        for i, status in enumerate(status_agendamento, start=1):
            print(f'{i} - {status}')

        while True:
            opcao = validar_mensagem('Escolha o status: ')

            if 1 <= opcao <= len(status_agendamento):
                agendamento['status'] = status_agendamento[opcao - 1]
                break

            print('Status inválido!')

        agendamento['observacoes'] = input('Observações: ').capitalize()
            
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
    while True:
        print(
            '\n========== PESQUISA DE AGENDAMENTO =========='
            '\nPreencha os campos que deseja usar como filtro.'
            '\nDeixe em branco para nao filtrar pelo campo.\n'
        )

        # Mesma logica das outras pesquisas: campo vazio = filtro ignorado.
        codigo = input('Codigo do agendamento: ')
        codigo_cliente = input('Codigo do cliente: ')
        codigo_profissional = input('Codigo do profissional: ')
        codigo_procedimento = input('Codigo do procedimento: ')
        nome_cliente = validar_texto(input('Nome do cliente: '))
        nome_profissional = validar_texto(input('Nome do profissional: '))
        data_inicio = input('Data de inicio (ddmmaaaa): ')
        status = validar_texto(input('Status (Ex.: Agendado, Confirmado...): '))

        # As datas no agendamento sao guardadas ja mascaradas (ex.: 26/06/2026).
        # Se a pessoa digitar so numeros (ddmmaaaa), passamos pela mesma mascara usada no cadastro, pra comparacao bater certinho.
        if data_inicio:
            data_validada = validar_data_numeros(data_inicio)
            data_inicio = mascarar_data(data_validada) if data_validada else None

        resultados = []  # lista temporaria, criada do zero em cada pesquisa

        for agendamento in agendamentos:

            if codigo and agendamento['codigo'] != int(codigo):
                continue

            if codigo_cliente and agendamento['codigo_cliente'] != codigo_cliente:
                continue

            if codigo_profissional and agendamento['codigo_profissional'] != codigo_profissional:
                continue

            if codigo_procedimento and agendamento['codigo_procedimento'] != codigo_procedimento:
                continue

            if nome_cliente and nome_cliente not in validar_texto(agendamento['nome_cliente']):
                continue

            if nome_profissional and nome_profissional not in validar_texto(agendamento['nome_profissional']):
                continue

            if data_inicio and agendamento['data_inicio'] != data_inicio:
                continue

            if status and status not in validar_texto(agendamento['status']):
                continue

            # Se o agendamento passou por TODOS os filtros, entra no resultado.
            resultados.append(agendamento)

        if not resultados:
            print('\nNenhum agendamento encontrado!')

        else:
            print(f'\n{len(resultados)} agendamento(s) encontrado(s):')

            for agendamento in resultados:
                print('\n========== DADOS DO AGENDAMENTO ==========')

                for chave, valor in agendamento.items():
                    campo = chave.replace('_', ' ').title()
                    print(f'{campo:<20}: {valor}')

                print('=' * 38)

        continuar = input('\nDeseja realizar outra pesquisa? (S/N): ').upper()

        if continuar != 'S':
            break
    
def deletar_agendamento():
    print('Deletar')