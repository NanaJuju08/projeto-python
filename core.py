from cadastros.clientes import *
from cadastros.profissionais import *
from cadastros.procedimentos import *
from cadastros.agendamentos import *
from cadastros.relatorios import *
from utils.validacoes import *

nome_secretario = input(
    '\nBem-vindo(a) ao sistema da Clínica Mari Glow.\n'
    'Informe seu nome para iniciar o atendimento.\n'
    'Digite "sair" para encerrar: '
).capitalize()

if nome_secretario.lower() == 'sair':
    print('Saindo do sistema. Tenha um ótimo dia!')

else:
    while True:

        opcao = validar_mensagem(
            '\n========================================'
            f'\nOlá, {nome_secretario}. O que deseja realizar hoje?\n'
            '1 - Clientes\n'
            '2 - Profissionais\n'
            '3 - Procedimentos\n'
            '4 - Agendamentos\n'
            '5 - Relatórios\n'
            '6 - Sair\n'
            'Digite a opção: '
        )

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
                
                elif op == 'A':
                    alterar_cliente()
                
                elif op == 'E':
                    deletar_cliente()
                
                elif op == 'P':
                    pesquisar_cliente()
                
                else:
                    print('\nOpção inválida. Tente novamente.')

            case 2:
                print('\n========== PROFISSIONAIS ==========')
                
                op = input('O que deseja fazer?\n'
                           'C - Cadastro\n'
                           'A - Alteração\n'
                           'E - Exclusão\n'
                           'P - Pesquisa\n'
                           'Escolha a opção que deseja: ').upper()
                
                if op == 'C':
                    cadastrar_profissional()
                
                elif op == 'A':
                    alterar_profissional()
                
                elif op == 'E':
                    deletar_profissional()
                
                elif op == 'P':
                    pesquisar_profissional()
                
                else:
                    print('\nOpção inválida. Tente novamente.')

            case 3:
                print('\n========== PROCEDIMENTOS ==========')
                
                
                op = input('O que deseja fazer?\n'
                           'C - Cadastro\n'
                           'A - Alteração\n'
                           'E - Exclusão\n'
                           'P - Pesquisa\n'
                           'Escolha a opção que deseja: ').upper()
                
                if op == 'C':
                    cadastrar_procedimento()
                
                elif op == 'A':
                    alterar_procedimento()
                
                elif op == 'E':
                    deletar_procedimento()
                
                elif op == 'P':
                    pesquisar_procedimento()
                
                else:
                    print('\nOpção inválida. Tente novamente.')

            case 4:
                print('\n========== AGENDAMENTOS ==========')

                op = input('O que deseja fazer?\n'
                           'C - Cadastro\n'
                           'A - Alteração\n'
                           'E - Exclusão\n'
                           'P - Pesquisa\n'
                           'Escolha a opção que deseja: ').upper()
                
                if op == 'C':
                    cadastrar_agendamento()
                
                elif op == 'A':
                    alterar_agendamento()
                
                elif op == 'E':
                    deletar_agendamento()
                
                elif op == 'P':
                    pesquisar_agendamento()
                
                else:
                    print('\nOpção inválida. Tente novamente.')

            case 5:
                print('\n========== RELATÓRIOS ==========')

                
                op = validar_mensagem('Qual relatório deseja imprimir?\n'
                           '1 - Clientes\n'
                           '2 - Profissionais\n'
                           '3 - Procedimentos\n'
                           '4 - Agendamentos\n'
                           '5 - Geral\n'
                           'Escolha a opção que deseja: ')
                
                if op == 1:
                    relatorio_cliente()
                
                elif op == 2:
                    relatorio_profissional()
                
                elif op == 3:
                    relatorio_procedimento()
                
                elif op == 4:
                    relatorio_agendamento()
                
                elif op == 5:
                    relatorio_geral()
                
                else:
                    print('\nOpção inválida. Tente novamente.')

            case 6:
                print('\nEncerrando sistema.'
                      '\nSaindo do sistema. Tenha um ótimo dia!')
                break

            case _:
                print('\nOpção inválida. Tente novamente.')
