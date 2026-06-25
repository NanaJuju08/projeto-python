from cadastros.clientes import cadastrar_cliente
from cadastros.profissionais import cadastrar_profissional
from cadastros.procedimentos import cadastrar_procedimento
from cadastros.agendamentos import cadastrar_agendamento

nome_secretario = input(
    '\nBem-vindo(a) ao sistema da Clínica Mari Glow.\n'
    'Informe seu nome para iniciar o atendimento.\n'
    'Digite "sair" para encerrar: '
)

if nome_secretario.lower() == 'sair':
    print('Saindo do sistema. Tenha um ótimo dia!')

else:
    while True:

        opcao = int(input(
            '\n========================================'
            f'\nOlá, {nome_secretario}. O que deseja realizar hoje?\n'
            '1 - Cadastro de clientes\n'
            '2 - Cadastro de profissionais\n'
            '3 - Cadastro de procedimentos\n'
            '4 - Cadastro de agendamentos\n'
            '5 - Consulta de agendamentos\n'
            '6 - Emissão de relatórios\n'
            '7 - Sair\n'
            'Digite a opção: '
        ))

        match opcao:
            case 1:
                print('\n========== CADASTRO DE CLIENTES ==========')
                cadastrar_cliente()

            case 2:
                print('\n========== CADASTRO DE PROFISSIONAIS ==========')
                cadastrar_profissional()

            case 3:
                print('\n========== CADASTRO DE PROCEDIMENTOS ==========')
                cadastrar_procedimento()

            case 4:
                print('\n========== CADASTRO DE AGENDAMENTOS ==========')
                cadastrar_agendamento()

            case 5:
                print('\n========== CONSULTA DE AGENDAMENTOS ==========')

            case 6:
                print('\n========== RELATÓRIOS ==========')

            case 7:
                print('\nEncerrando sistema.'
                      '\nSaindo do sistema. Tenha um ótimo dia!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')
