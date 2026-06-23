
from dados.listas import clientes
from utils.validacoes import validar_mensagem

def cadastrar_cliente():

    while True:
        cliente = {}
        cliente['codigo'] = len(clientes) + 1 #Incrementa +1 toda vez que cadastra um novo cliente - CONFERIR ACENTO!!

        print(
            'Tudo pronto para o cadastro do cliente.\n'
            'Abaixo, insira as informações necessárias para concluir o cadastro!\n'
            'Caso deseja sair do sistema, digite "sair" ou clique em qualquer tecla para prosseguir:\n'
        )

        cliente['nome'] = input('Nome completo: ')
        cliente['cpf'] = input('CPF (Ex.: 000.000.000-00): ')
        cliente['idade'] = validar_mensagem(int(input('Idade: ')))
        cliente['data_nascimento'] = input('Data de nascimento (Ex.: dd/mm/aaaa): ')
        cliente['telefone'] = input('Telefone móvel (Ex.: 00000-0000): ')
        cliente['email'] = input('E-mail: ')
        cliente['sexo'] = input('Sexo: ')
        cliente['endereco'] = input('Endereço: ')
        cliente['observacoes'] = input('Observações sobre o cliente: ')


        clientes.append(cliente)

        print('\nCliente cadastrado com sucesso!'
            '\n========== DADOS DO CLIENTE ==========')

        for chave, valor in cliente.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro cliente? (S/N): ').upper()
        
        if continuar != 'S':
            break