from dados.listas import *

def relatorio_cliente():
    print('\n========== RELATÓRIO DE CLIENTES ==========')

def relatorio_profissional():
    print('\n========== RELATÓRIO DE PROFISSIONAIS ==========')

def relatorio_procedimento():
    print('\n========== RELATÓRIO DE PROCEDIMENTOS ==========')

def relatorio_agendamento():
    print('\n========== RELATÓRIO DE AGENDAMENTOS ==========')

def relatorio_geral():
    print('\n')

    print('=' * 60)
    print('CLÍNICA ESTÉTICA MARI GLOW -- RELATÓRIO GERAL DO SISTEMA')
    print('=' * 60)

    #SAÍDA DE CLIENTES
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

    #SAÍDA DE PROFISSIONAIS
    print('------------------- PROFISSIONAIS -------------------')
    if not profissionais:
        print('Nenhum profissional cadastrado.')
        return
    
    for profissional in profissionais:
        print(f'\nprofissional #{profissional["codigo"]:03}')
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

    print('------------------- PROCEDIMENTOS -------------------')
    """ if not clientes:
        print('Nenhum cliente cadastrado.')
        return
    
    for cliente in clientes:
        print(f'\nCliente #{cliente['codigo']:03}')
        print('-' * 60)
        print(f'Nome.............: {cliente['nome']}')
        print(f'CPF..............: {cliente['cpf']}')
        print(f'Telefone.........: {cliente['telefone']}')
        print(f'E-mail...........: {cliente['email']}')
        print(f'Data Nascimento..: {cliente['data_nascimento']}')
        print(f'Sexo.............: {cliente['sexo']}')
        print(f'Endereço.........: {cliente['endereco']}')

        if cliente['observacoes']:
            print(f'Observações......: {cliente['observacoes']}')

    print('\n' + '=' * 60)
    print(f'Total de clientes: {len(clientes)}')
    print('=' * 60) """

    print('------------------- AGENDAMENTOS -------------------')
    """ if not clientes:
        print('Nenhum cliente cadastrado.')
        return
    
    for cliente in clientes:
        print(f'\nCliente #{cliente['codigo']:03}')
        print('-' * 60)
        print(f'Nome.............: {cliente['nome']}')
        print(f'CPF..............: {cliente['cpf']}')
        print(f'Telefone.........: {cliente['telefone']}')
        print(f'E-mail...........: {cliente['email']}')
        print(f'Data Nascimento..: {cliente['data_nascimento']}')
        print(f'Sexo.............: {cliente['sexo']}')
        print(f'Endereço.........: {cliente['endereco']}')

        if cliente['observacoes']:
            print(f'Observações......: {cliente['observacoes']}')

    print('\n' + '=' * 60)
    print(f'Total de clientes: {len(clientes)}')
    print('=' * 60) """