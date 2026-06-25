from dados.listas import clientes
from utils.validacoes import *


def cadastrar_cliente():
    while True:
        cliente = {}
        cliente['codigo'] = len(clientes) + 1

        print(
            'Tudo pronto para o cadastro do cliente.\n'
            'Abaixo, insira as informacoes necessarias para concluir o cadastro!\n'
        )

        cliente['nome'] = input('Nome completo: ')

        while True:
            cpf = validar_cpf(input('CPF: '))

            if cpf:
                if cpf_duplicado(cpf, clientes):
                    print('CPF ja cadastrado!')
                    continue

                cliente['cpf'] = mascarar_cpf(cpf)
                break

        cliente['idade'] = validar_mensagem('Idade: ')
        cliente['data_nascimento'] = validar_data('Data de nascimento (Ex.: dd/mm/aaaa): ')
        cliente['telefone'] = validar_telefone('Telefone movel (Ex.: 00000-0000): ')
        cliente['email'] = validar_email('E-mail: ')
        cliente['sexo'] = input('Sexo: ').capitalize()
        cliente['endereco'] = input('Endereço: ').capitalize()
        cliente['observacoes'] = input('Observaçoes sobre o cliente: ').capitalize()

        clientes.append(cliente)

        print(
            '\nCliente cadastrado com sucesso!'
            '\n========== DADOS DO CLIENTE =========='
        )

        for chave, valor in cliente.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro cliente? (S/N): ').upper()

        if continuar != 'S':
            break

def alterar_cliente():
        codigo = validar_mensagem('Digite o codigo do cliente: ')

        cliente_encontrado = None

        for cliente in clientes:
            if cliente['codigo'] == codigo:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print('Cliente nao encontrado!')
            return

        print('\nDados atuais:')
        for chave, valor in cliente_encontrado.items():
            print(f'{chave}: {valor}')

        print('\nDeixe em branco para manter o valor atual.')

        nome = input(f'Nome [{cliente_encontrado["nome"]}]: ')
        if nome:
            cliente_encontrado['nome'] = nome

        telefone = input(
            f'Telefone [{cliente_encontrado["telefone"]}]: '
        )
        if telefone:
            cliente_encontrado['telefone'] = telefone

        email = input(
            f'E-mail [{cliente_encontrado["email"]}]: '
        )
        if email:
            cliente_encontrado['email'] = email

        endereco = input(
            f'Endereco [{cliente_encontrado["endereco"]}]: '
        )
        if endereco:
            cliente_encontrado['endereco'] = endereco

        print('\nCliente alterado com sucesso!')