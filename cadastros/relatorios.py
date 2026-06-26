from dados.listas import *

def relatorio_cliente():
    print('\n========== RELATÓRIO DE CLIENTES ==========')
    print('------------------- CLIENTES -------------------')

    if not clientes:
        print('Nenhum cliente cadastrado.')
        return

    for cliente in clientes:
        print(f'\nCliente #{cliente["codigo"]:03}')
        print('-' * 60)
        print(f'Nome.............: {cliente["nome"]}')
        print(f'CPF..............: {cliente["cpf"]}')
        print(f'Idade............: {cliente["idade"]}')
        print(f'Data Nascimento..: {cliente["data_nascimento"]}')
        print(f'Telefone.........: {cliente["telefone"]}')
        print(f'E-mail...........: {cliente["email"]}')
        print(f'Sexo.............: {cliente["sexo"]}')
        print(f'Endereço.........: {cliente["endereco"]}')

        if cliente["observacoes"]:
            print(f'Observações......: {cliente["observacoes"]}')

    print('\n' + '=' * 60)
    print(f'Total de clientes cadastrados: {len(clientes)}')
    print('=' * 60)


def relatorio_profissional():
    print('\n========== RELATÓRIO DE PROFISSIONAIS ==========')
    print('------------------- PROFISSIONAIS -------------------')

    if not profissionais:
        print('Nenhum profissional cadastrado.')
        return

    for profissional in profissionais:
        print(f'\nProfissional #{profissional["codigo"]:03}')
        print('-' * 60)
        print(f'Nome.............: {profissional["nome"]}')
        print(f'CPF..............: {profissional["cpf"]}')
        print(f'Data Nascimento..: {profissional["data_nascimento"]}')
        print(f'Telefone.........: {profissional["telefone"]}')
        print(f'E-mail...........: {profissional["email"]}')
        print(f'Especialidade....: {profissional["especialidade"]}')
        print(f'CRM..............: {profissional["crm"]}')

        if profissional["observacoes"]:
            print(f'Observações......: {profissional["observacoes"]}')

    print('\n' + '=' * 60)
    print(f'Total de profissionais cadastrados: {len(profissionais)}')
    print('=' * 60)


def relatorio_procedimento():
    print('\n========== RELATÓRIO DE PROCEDIMENTOS ==========')
    print('------------------- PROCEDIMENTOS -------------------')

    if not procedimentos:
        print('Nenhum procedimento cadastrado.')
        return

    for procedimento in procedimentos:
        print(f'\nProcedimento #{procedimento["codigo"]:03}')
        print('-' * 60)
        print(f'Nome.............: {procedimento["nome"]}')
        print(f'Valor............: {procedimento["valor"]}')
        print(f'Duração..........: {procedimento["duracao"]}')
        print(f'Sessões..........: {procedimento["sessoes"]}')

        if procedimento["descricao"]:
            print(f'Descrição........: {procedimento["descricao"]}')

    print('\n' + '=' * 60)
    print(f'Total de procedimentos cadastrados: {len(procedimentos)}')
    print('=' * 60)


def relatorio_agendamento():
    print('\n========== RELATÓRIO DE AGENDAMENTOS ==========')
    print('------------------- AGENDAMENTOS -------------------')

    if not agendamentos:
        print('Nenhum agendamento cadastrado.')
        return

    for agendamento in agendamentos:
        print(f'\nAgendamento #{agendamento["codigo"]:03}')
        print('-' * 60)
        print(f'Cliente..........: {agendamento["nome_cliente"]}')
        print(f'Profissional.....: {agendamento["nome_profissional"]}')
        print(f'Procedimento.....: {agendamento["nome_procedimento"]}')
        print(f'Início...........: {agendamento["data_inicio"]} {agendamento["hora_inicio"]}')
        print(f'Fim..............: {agendamento["data_fim"]} {agendamento["hora_fim"]}')
        print(f'Status...........: {agendamento["status"]}')

        if agendamento["observacoes"]:
            print(f'Observações......: {agendamento["observacoes"]}')

    print('\n' + '=' * 60)
    print(f'Total de agendamentos cadastrados: {len(agendamentos)}')
    print('=' * 60)


def relatorio_geral():
    print('\n')
    print('=' * 60)
    print('CLÍNICA ESTÉTICA MARI GLOW -- RELATÓRIO GERAL DO SISTEMA')
    print('=' * 60)

    # CLIENTES
    print('------------------- CLIENTES -------------------')
    if not clientes:
        print('Nenhum cliente cadastrado.')
    else:
        for cliente in clientes:
            print(f'\nCliente #{cliente["codigo"]:03}')
            print('-' * 60)
            print(f'Nome.............: {cliente["nome"]}')
            print(f'CPF..............: {cliente["cpf"]}')
            print(f'Idade............: {cliente["idade"]}')
            print(f'Data Nascimento..: {cliente["data_nascimento"]}')
            print(f'Telefone.........: {cliente["telefone"]}')
            print(f'E-mail...........: {cliente["email"]}')
            print(f'Sexo.............: {cliente["sexo"]}')
            print(f'Endereço.........: {cliente["endereco"]}')

            if cliente["observacoes"]:
                print(f'Observações......: {cliente["observacoes"]}')

        print('\n' + '=' * 60)
        print(f'Total de clientes cadastrados: {len(clientes)}')
        print('=' * 60)

    # PROFISSIONAIS
    print('------------------- PROFISSIONAIS -------------------')
    if not profissionais:
        print('Nenhum profissional cadastrado.')
    else:
        for profissional in profissionais:
            print(f'\nProfissional #{profissional["codigo"]:03}')
            print('-' * 60)
            print(f'Nome.............: {profissional["nome"]}')
            print(f'CPF..............: {profissional["cpf"]}')
            print(f'Data Nascimento..: {profissional["data_nascimento"]}')
            print(f'Telefone.........: {profissional["telefone"]}')
            print(f'E-mail...........: {profissional["email"]}')
            print(f'Especialidade....: {profissional["especialidade"]}')
            print(f'CRM..............: {profissional["crm"]}')

            if profissional["observacoes"]:
                print(f'Observações......: {profissional["observacoes"]}')

        print('\n' + '=' * 60)
        print(f'Total de profissionais cadastrados: {len(profissionais)}')
        print('=' * 60)

    # PROCEDIMENTOS
    print('------------------- PROCEDIMENTOS -------------------')
    if not procedimentos:
        print('Nenhum procedimento cadastrado.')
    else:
        for procedimento in procedimentos:
            print(f'\nProcedimento #{procedimento["codigo"]:03}')
            print('-' * 60)
            print(f'Nome.............: {procedimento["nome"]}')
            print(f'Valor............: {procedimento["valor"]}')
            print(f'Duração..........: {procedimento["duracao"]}')
            print(f'Sessões..........: {procedimento["sessoes"]}')

            if procedimento["descricao"]:
                print(f'Descrição........: {procedimento["descricao"]}')

        print('\n' + '=' * 60)
        print(f'Total de procedimentos cadastrados: {len(procedimentos)}')
        print('=' * 60)

    # AGENDAMENTOS
    print('------------------- AGENDAMENTOS -------------------')
    if not agendamentos:
        print('Nenhum agendamento cadastrado.')
    else:
        for agendamento in agendamentos:
            print(f'\nAgendamento #{agendamento["codigo"]:03}')
            print('-' * 60)
            print(f'Cliente..........: {agendamento["nome_cliente"]}')
            print(f'Profissional.....: {agendamento["nome_profissional"]}')
            print(f'Procedimento.....: {agendamento["nome_procedimento"]}')
            print(f'Início...........: {agendamento["data_inicio"]} {agendamento["hora_inicio"]}')
            print(f'Fim..............: {agendamento["data_fim"]} {agendamento["hora_fim"]}')
            print(f'Status...........: {agendamento["status"]}')

            if agendamento["observacoes"]:
                print(f'Observações......: {agendamento["observacoes"]}')

        print('\n' + '=' * 60)
        print(f'Total de agendamentos cadastrados: {len(agendamentos)}')
        print('=' * 60)
