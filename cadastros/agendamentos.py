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


            if not validar_periodo(agendamento['data_inicio'], agendamento['hora_inicio'], agendamento['data_fim'], agendamento['hora_fim']):
                print('A data/hora final deve ser maior que a data/hora inicial.')
                continue
        
        agendamento['hora_fim'] = validar_hora('Horário de fim:')

        inicio_novo = datetime.strptime(
            f"{agendamento['data_inicio']} {agendamento['hora_inicio']}",
            '%d/%m/%Y %H:%M'
        )

        fim_novo = datetime.strptime(
            f"{agendamento['data_fim']} {agendamento['hora_fim']}",
            '%d/%m/%Y %H:%M'
        )

        if cliente_ocupado(agendamento['codigo_cliente'], inicio_novo, fim_novo, agendamentos):
            print('Cliente já possui agendamento nesse horário.')
            continue

        if profissional_ocupado(agendamento['codigo_profissional'], inicio_novo, fim_novo, agendamentos):
            print('Profissional já possui agendamento nesse horário.')
            continue

        #REGRAS IMPLEMENTADAS
        #Validação de cliente, profissional e procedimento.
        #Controle de datas e horários.
        #Impedimento de agendamentos em datas passadas.
        #Validação do período do atendimento.
        #Controle de conflito de horários para clientes.
        #Controle de conflito de horários para profissionais.
        #Controle de status do agendamento.

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
    while True:
        print('\n')
        for a in agendamentos:
            print(
                f'Código: {a["codigo"]} - '
                f'Cliente: {a["nome_cliente"]} - '
                f'Profissional: {a["nome_profissional"]} - '
                f'Status: {a["status"]}'
            )

        codigo = validar_mensagem('Digite o código do agendamento: ')

        agendamento_encontrado = None

        for agendamento in agendamentos:
            if agendamento['codigo'] == codigo:
                agendamento_encontrado = agendamento
                break

        if agendamento_encontrado is None:
            print('Agendamento não encontrado!')
            return

        print('\nDados atuais do agendamento:\n')

        for chave, valor in agendamento_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('\nOBSERVAÇÃO:Deixe em branco para manter o valor atual.\n')

        descricao = input(
            f'Descrição [{agendamento_encontrado["descricao"]}]: ')

        if descricao:
            agendamento_encontrado['descricao'] = descricao

        data_inicio = input(f'Data início [{agendamento_encontrado["data_inicio"]}] (ddmmaaaa): ')

        if data_inicio:
            data_inicio = mascarar_data(
                validar_data_numeros(data_inicio)
            )

        else:
            data_inicio = agendamento_encontrado['data_inicio']

        hora_inicio = input(f'Hora início [{agendamento_encontrado["hora_inicio"]}]: ')

        if not hora_inicio:
            hora_inicio = agendamento_encontrado['hora_inicio']

        data_fim = input(f'Data fim [{agendamento_encontrado["data_fim"]}] (ddmmaaaa): ')

        if data_fim:
            data_fim = mascarar_data(
                validar_data_numeros(data_fim)
            )

        else:
            data_fim = agendamento_encontrado['data_fim']

        hora_fim = input(f'Hora fim [{agendamento_encontrado["hora_fim"]}]: ')

        if not hora_fim:
            hora_fim = agendamento_encontrado['hora_fim']

        if not validar_periodo(data_inicio, hora_inicio, data_fim, hora_fim):
            print('Período inválido!')
            continue

        inicio_novo = datetime.strptime(
            f'{data_inicio} {hora_inicio}',
            '%d/%m/%Y %H:%M'
        )

        fim_novo = datetime.strptime(
            f'{data_fim} {hora_fim}',
            '%d/%m/%Y %H:%M'
        )

        if cliente_ocupado(agendamento_encontrado['codigo_cliente'], inicio_novo, fim_novo, agendamentos, agendamento_encontrado['codigo']):
            print('Cliente já possui agendamento nesse horário!')
            continue

        if profissional_ocupado(agendamento_encontrado['codigo_profissional'], inicio_novo, fim_novo, agendamentos, agendamento_encontrado['codigo']):
            print('Profissional já possui agendamento nesse horário!')
            continue

        agendamento_encontrado['data_inicio'] = data_inicio
        agendamento_encontrado['hora_inicio'] = hora_inicio
        agendamento_encontrado['data_fim'] = data_fim
        agendamento_encontrado['hora_fim'] = hora_fim

        print('\nStatus do agendamento:')

        for i, status in enumerate(status_agendamento, start=1):
            print(f'{i} - {status}')

        opcao = input(
            f'Status '
            f'[{agendamento_encontrado["status"]}]: '
        )

        if opcao:
            opcao = int(opcao)

            if 1 <= opcao <= len(status_agendamento):
                agendamento_encontrado['status'] = (
                    status_agendamento[opcao - 1]
                )

        observacoes = input(
            f'Observações [{agendamento_encontrado["observacoes"]}]: ').capitalize()

        if observacoes:
            agendamento_encontrado['observacoes'] = observacoes

        print('\nAgendamento alterado com sucesso!\n')

        print(f'\nDados alterados do cliente:')
        for chave, valor in agendamento_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        continuar = input(
            '\nDeseja alterar outro agendamento? (S/N): '
        ).upper()

        if continuar != 'S':
            break

def pesquisar_agendamento():
    while True:
        print(
            '\n========== PESQUISA DE AGENDAMENTO =========='
            '\nPreencha os campos que deseja usar como filtro.'
            '\nDeixe em branco para não filtrar pelo campo.\n'
        )

        codigo = input('Codigo do agendamento: ')
        codigo_cliente = input('Codigo do cliente: ')
        codigo_profissional = input('Codigo do profissional: ')
        codigo_procedimento = input('Codigo do procedimento: ')
        nome_cliente = validar_texto(input('Nome do cliente: '))
        nome_profissional = validar_texto(input('Nome do profissional: '))
        data_inicio = input('Data de inicio (ddmmaaaa): ')
        status = validar_texto(input('Status (Ex.: Agendado, Confirmado...): '))

        if data_inicio:
            data_validada = validar_data_numeros(data_inicio)
            if not data_validada:
                print('Data inválida, pesquisa cancelada.')
                continue
            data_inicio = mascarar_data(data_validada)

        if codigo:
            try:
                codigo = int(codigo)
            except ValueError:
                print('Código inválido, pesquisa cancelada.')
                continue

        if codigo_cliente:
            try:
                codigo_cliente = int(codigo_cliente)
            except ValueError:
                print('Código do cliente inválido, pesquisa cancelada.')
                continue

        if codigo_profissional:
            try:
                codigo_profissional = int(codigo_profissional)
            except ValueError:
                print('Código do profissional inválido, pesquisa cancelada.')
                continue

        if codigo_procedimento:
            try:
                codigo_procedimento = int(codigo_procedimento)
            except ValueError:
                print('Código do procedimento inválido, pesquisa cancelada.')
                continue

        resultados = []

        for agendamento in agendamentos:

            if codigo and agendamento['codigo'] != codigo:
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

            if status and validar_texto(agendamento['status']) != status:
                continue

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
    agendamentos_excluiveis = []

    for agendamento in agendamentos:
        if not agendamento_em_aberto(agendamento):
            agendamentos_excluiveis.append(agendamento)

    if len(agendamentos_excluiveis) == 0:
        print(
            'Não há agendamentos disponíveis para exclusão.'
        )
        return

    print('\n========== AGENDAMENTOS EXCLUÍVEIS ==========')

    for a in agendamentos_excluiveis:
        print(
            f'Código: {a["codigo"]} - '
            f'Cliente: {a["nome_cliente"]} - '
            f'Status: {a["status"]}'
        )

    codigo = validar_mensagem(
        '\nDigite o código do agendamento que deseja excluir: '
    )

    agendamento_encontrado = None

    for a in agendamentos_excluiveis:
        if a['codigo'] == codigo:
            agendamento_encontrado = a
            break

    if agendamento_encontrado is None:
        print('Agendamento não encontrado ou não pode ser excluído!')
        return

    confirmar = input(
        f'Tem certeza que deseja excluir o agendamento do cliente {agendamento_encontrado["nome_cliente"]}? (S/N): ').upper()

    if confirmar == 'S':
        agendamentos.remove(agendamento_encontrado)
        print('Agendamento excluído com sucesso!')
    else:
        print('Exclusão cancelada.')
