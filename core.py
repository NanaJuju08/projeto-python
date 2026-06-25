from cadastros.clientes import *
from cadastros.profissionais import *
from cadastros.procedimentos import *
from cadastros.agendamentos import *

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
            '1 - Clientes\n'
            '2 - Profissionais\n'
            '3 - procedimentos\n'
            '4 - Agendamentos\n'
            '5 - Emissão de relatórios\n'
            '6 - Sair\n'
            'Digite a opção: '
        ))

        match opcao:
            case 1:
                print('\n========== CLIENTES ==========')
                op = input('O que deseja fazer?\n'
                           'C - Cadastro\n'
                           'A - Alteração\n'
                           'E - Exclusão\n'
                           'P - Pesquisa\n'
                           'Escolha a opção que deseja: ').upper()
                
                if op == 'C':
                    cadastrar_cliente()
                
                if op == 'A':
                    alterar_cliente()
                
                if op == 'E':
                    excluir_cliente()
                
                if op == 'P':
                    pesquisar_cliente()
                
                else:
                    print('Opção inválida. Tente novamente.')

            case 2:
                print('\n========== PROFISSIONAIS ==========')
                cadastrar_profissional()

            case 3:
                print('\n========== PROCEDIMENTOS ==========')
                cadastrar_procedimento()

            case 4:
                print('\n========== AGENDAMENTOS ==========')
                cadastrar_agendamento()

            case 5:
                print('\n========== RELATÓRIOS ==========')

            case 6:
                print('\nEncerrando sistema.'
                      '\nSaindo do sistema. Tenha um ótimo dia!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')
