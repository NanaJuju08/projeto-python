from dados.listas import clientes
from utils.validacoes import *


def cadastrar_cliente():
    while True:
        cliente = {}
        cliente['codigo'] = len(clientes) + 1

        print(
            'Tudo pronto para o cadastro do cliente.\n'
            'Abaixo, insira as informações necessárias para concluir o cadastro!\n'
        )

        cliente['nome'] = input('Nome completo: ').capitalize()

        while True:
            cpf = validar_cpf(input('CPF: '))

            if cpf:
                if cpf_duplicado(cpf, clientes):
                    print('CPF já cadastrado!')
                    continue

                cliente['cpf'] = mascarar_cpf(cpf)
                break

        cliente['idade'] = validar_mensagem('Idade: ')


        while True:
            data = validar_data_numeros(
                input('Data de nascimento (ddmmaaaa): ')
            )

            if data:
                cliente['data_nascimento'] = mascarar_data(data)
                break

        while True:
            telefone = validar_telefone(
                'Telefone móvel: '
            )

            if telefone_duplicado(telefone, clientes):
                print('Telefone já cadastrado!')
                continue

            cliente['telefone'] = telefone
            break


        while True:
            email = validar_email(
                'E-mail (Ex.: user@gmail.com): '
            )

            if email_duplicado(email, clientes):
                print('E-mail já cadastrado!')
                continue

            cliente['email'] = email
            break

        cliente['sexo'] = input('Sexo: ').capitalize()
        cliente['endereco'] = input('Endereço: ').capitalize()
        cliente['observacoes'] = input('Observações sobre o cliente: ').capitalize()

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
    while True:
        print('\n')
        for c in clientes:
            print(f'Código: {c["codigo"]} - Nome: {c["nome"]}')

        codigo = validar_mensagem('Digite o código do cliente: ')

        cliente_encontrado = None #Não agrega nenhum valor

        #A variável cliente percorre a lista, se caso o código digitado esteja na lista, retorna o cliente_encontrado igual ao cliente
        for cliente in clientes:
            if cliente['codigo'] == codigo:
                cliente_encontrado = cliente
                break

        if cliente_encontrado == None:
            print('\nCliente não encontrado!')
            return

        print(f'\nDados atuais do cliente:')
        for chave, valor in cliente_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('\nOBSERVAÇÃO: Deixe em branco para manter o valor atual.\n')

        nome = input(f'Nome [{cliente_encontrado["nome"]}]: ').capitalize()
        if nome:
            cliente_encontrado['nome'] = nome


        while True:
            telefone = validar_telefone(
                f'Telefone [{cliente_encontrado["telefone"]}]: ',
                permitir_vazio=True
            )

            if not telefone:
                break

            if telefone != cliente_encontrado['telefone'] and telefone_duplicado(telefone, clientes):
                print('Telefone já cadastrado!')
                continue

            cliente_encontrado['telefone'] = telefone
            break


        while True:
            email = validar_email(
                f'E-mail [{cliente_encontrado["email"]}]: ',
                permitir_vazio=True
            )

            if not email:
                break

            if email.lower() != cliente_encontrado['email'].lower() and email_duplicado(email, clientes):
                print('E-mail já cadastrado!')
                continue

            cliente_encontrado['email'] = email
            break


        endereco = input(
            f'Endereco [{cliente_encontrado["endereco"]}]: '
        )
        if endereco:
            cliente_encontrado['endereco'] = endereco

        print('\nCliente alterado com sucesso!')
    
        print(f'\nDados alterados do cliente:')

        for chave, valor in cliente_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')
        
        continuar = input('\nDeseja alterar outro cliente? (S/N): ').upper()

        if continuar != 'S':
            break


def pesquisar_cliente():
    while True:
        print(
            '\nPreencha os campos que deseja usar como filtro.'
            '\nDeixe em branco para não filtrar pelo campo.\n'
        )

        # Cada input vira um "filtro opcional". Se a pessoa deixar em branco, a variável fica como string vazia (''), que é "falsy" em Python - isso e o que faz o filtro ser ignorado mais embaixo.
        codigo = input('Código: ')
        nome = validar_texto(input('Nome: '))
        cpf = input('CPF: ')
        email = input('Email: ').lower().strip()

        # Só tenta validar/mascarar o CPF se a pessoa realmente digitou algo.
        # Se o CPF for invalido, validar_cpf() retorna None, e o "if cpf_validado" evita que a gente tente mascarar um valor inválido.
        if cpf:
            cpf_validado = validar_cpf(cpf)
            cpf = mascarar_cpf(cpf_validado) if cpf_validado else None

        resultados = []  # lista temporaria, criada do zero em cada pesquisa


        for cliente in clientes:

            # Cada "if campo and condicao: continue" e um filtro.
            # - Se o campo estiver vazio (''), o "and" ja para ali e o filtro e ignorado (o cliente passa direto, sem ser bloqueado).
            # - Se o campo estiver preenchido, testa a condicao: se o cliente NÃO bate com o filtro, "continue" pula pro proximo cliente sem adicionar ele em resultados.
            if codigo and cliente['codigo'] != int(codigo):
                continue

            if nome and nome not in validar_texto(cliente['nome']):
                continue

            if cpf and cliente['cpf'] != cpf:
                continue

            if email and email not in cliente['email'].lower():
                continue

            # Se o cliente passou por TODOS os filtros sem cair em nenhum "continue", ele bate com a pesquisa e entra no resultado.
            resultados.append(cliente)

        if not resultados:
            print('\nNenhum cliente encontrado!')

        else:
            print(f'\n{len(resultados)} cliente(s) encontrado(s):')

            for cliente in resultados:
                print('\n========== DADOS DO CLIENTE ==========')

                # Mesmo padrao de exibicao usado no cadastro: percorre o dicionario inteiro automaticamente, sem precisar listar campo por campo no print.
                for chave, valor in cliente.items():
                    campo = chave.replace('_', ' ').title()
                    print(f'{campo:<20}: {valor}')

                print('=' * 38)

        continuar = input('\nDeseja realizar outra pesquisa? (S/N): ').upper()

        # Como esse "if" e a ultima linha do while, nao precisa de "else: continue" - se a condicao for falsa, o loop ja volta pro topo naturalmente.
        if continuar != 'S':
            break

    
def deletar_cliente():
    if len(clientes) == 0:
        print('Não há clientes cadastrados.')
        return

    print('\n========== CLIENTES CADASTRADOS ==========')
    for c in clientes:
        print(f'Código: {c["codigo"]} - Nome: {c["nome"]}')

    codigo = int(input('\nDigite o código do cliente que deseja excluir: '))

    # procura o cliente pelo código
    cliente_encontrado = None
    for c in clientes:
        if c['codigo'] == codigo:
            cliente_encontrado = c
            break

    if cliente_encontrado is None:
        print('Cliente nao encontrado!')
        return

    confirmar = input(
        f'Tem certeza que deseja excluir o cliente '
        f'"{cliente_encontrado["nome"]}"? (S/N): '
    ).upper()

    if confirmar == 'S':
        clientes.remove(cliente_encontrado)
        print('\nCliente excluido com sucesso!\n')
    else:
        print('\nExclusão cancelada.\n')
