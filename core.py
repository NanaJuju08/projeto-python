from cadastros.clientes import cadastrar_cliente
from cadastros.profissionais import cadastrar_profissional

nome_secretario = input(
    'Bem-vindo(a) ao sistema da Clínica Mari Glow.\n'
    'Informe seu nome para iniciar o atendimento.\n'
    'Digite "sair" para encerrar: '
)

if nome_secretario.lower() == 'sair':
    print('Saindo do sistema. Tenha um ótimo dia!')

else:
    while True:

        opcao = int(input(
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
                print('\nCadastro de clientes')
                cadastrar_cliente()

            case 2:
                print('\nCadastro de profissionais')
                cadastrar_profissional()

            case 3:
                print('\nCadastro de procedimentos')

            case 4:
                print('\nCadastro de agendamentos')

            case 5:
                print('\nConsulta de agendamentos')

            case 6:
                print('\nRelatórios')

            case 7:
                print('\nEncerrando sistema.'
                      '\nSaindo do sistema. Tenha um ótimo dia!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')
