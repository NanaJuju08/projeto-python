from dados.listas import profissionais
from utils.validacoes import *
from datetime import datetime
import re #regex - é uma sequência de caracteres que forma um padrão de busca, usada de forma rápida para validar, encontrar, ou substituir textos e dados que seguem regras específicas (como formatos de e-mail, CPF, ou senhas).

profissional = {}

def cadastrar_profissional():
    while True:
        profissional = {}
        profissional['codigo'] = len(profissionais) + 1

        print(
            'Tudo pronto para o cadastro do profissional.\n'
            'Abaixo, insira as informações necessárias para concluir o cadastro!\n'
        )

        profissional['nome'] = input('Nome completo: ').capitalize()

        while True:
            cpf = validar_cpf(input('CPF: '))

            if cpf:
                if cpf_duplicado(cpf, profissionais):
                    print('CPF já cadastrado!')
                    continue

                profissional['cpf'] = mascarar_cpf(cpf)
                break

        while True:
            data = validar_data_numeros(
                input('Data de nascimento (ddmmaaaa): ')
            )

            if data:
                profissional['data_nascimento'] = mascarar_data(data)
                break
        
        while True:
            telefone = validar_telefone(
                'Telefone móvel: '
            )

            if telefone_duplicado(telefone, profissionais):
                print('Telefone já cadastrado!')
                continue

            profissional['telefone'] = telefone
            break


        while True:
            email = validar_email(
                'E-mail (Ex.: user@gmail.com): '
            )

            if email_duplicado(email, profissionais):
                print('E-mail já cadastrado!')
                continue

            profissional['email'] = email
            break

        profissional['especialidade'] = input('Especialidade: ').capitalize()
        profissional['crm'] = input('CRM: ').capitalize()
        profissional['observacoes'] = input('Observações sobre o profissional: ').capitalize()

        profissionais.append(profissional)

        print(
            '\nProfissional cadastrado com sucesso!'
            '\n========== DADOS DO PROFISSIONAL =========='
        )

        for chave, valor in profissional.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro profissional? (S/N): ').upper()

        if continuar != 'S':
            break


def alterar_profissional():
     while True:
        print('\n')
        for p in profissionais:
            print(f'Código: {p["codigo"]} - Nome: {p["nome"]}')

        codigo = validar_mensagem('Digite o código do profissional: ')

        profissional_encontrado = None #Não agrega nenhum valor

        #A variável profissional percorre a lista, se caso o código digitado esteja na lista, retorna o profissional_encontrado igual ao profissional
        for profissional in profissionais:
            if profissional['codigo'] == codigo:
                profissional_encontrado = profissional
                break

        if profissional_encontrado == None:
            print('\nprofissional não encontrado!')
            return

        print(f'\nDados atuais do profissional:')
        for chave, valor in profissional_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('\nOBSERVAÇÃO: Deixe em branco para manter o valor atual.\n')

        nome = input(f'Nome [{profissional_encontrado["nome"]}]: ')
        if nome:
            profissional_encontrado['nome'] = nome

        while True:
            telefone = validar_telefone(
                f'Telefone [{profissional_encontrado["telefone"]}]: ',
                permitir_vazio=True
            )

            if not telefone:
                break

            if telefone != profissional_encontrado['telefone'] and telefone_duplicado(telefone, profissionais):
                print('Telefone já cadastrado!')
                continue

            profissional_encontrado['telefone'] = telefone
            break


        while True:
            email = validar_email(
                f'E-mail [{profissional_encontrado["email"]}]: ',
                permitir_vazio=True
            )

            if not email:
                break

            if email.lower() != profissional_encontrado['email'].lower() and email_duplicado(email, profissionais):
                print('E-mail já cadastrado!')
                continue

            profissional_encontrado['email'] = email
            break


        endereco = input(
            f'Endereco [{profissional_encontrado["endereco"]}]: '
        )
        if endereco:
            profissional_encontrado['endereco'] = endereco

        print('\nprofissional alterado com sucesso!')
    
        print(f'\nDados alterados do profissional:')

        for chave, valor in profissional_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')
        
        continuar = input('\nDeseja alterar outro profissional? (S/N): ').upper()

        if continuar != 'S':
            break


def pesquisar_profissional():
    while True:
        print(
            '\nPreencha os campos que deseja usar como filtro.'
            '\nDeixe em branco para nao filtrar pelo campo.\n'
        )

               # Cada input vira um "filtro opcional". Se a pessoa deixar em branco, a variável fica como string vazia (''), que é "falsy" em Python - isso e o que faz o filtro ser ignorado mais embaixo.
        codigo = input('Código: ')
        nome = validar_texto(input('Nome: '))
        cpf = input('CPF: ')
        email = input('Email: ').lower().strip()
        especialidade = validar_texto(input('Especialidade: '))

        # Só tenta validar/mascarar o CPF se a pessoa realmente digitou algo.
        # Se o CPF for invalido, validar_cpf() retorna None, e o "if cpf_validado" evita que a gente tente mascarar um valor inválido.
        if cpf:
            cpf_validado = validar_cpf(cpf)
            cpf = mascarar_cpf(cpf_validado) if cpf_validado else None

        resultados = []  # lista temporaria, criada do zero em cada pesquisa


        for profissional in profissionais:
            
            # Cada "if campo and condicao: continue" e um filtro.
            # - Se o campo estiver vazio (''), o "and" ja para ali e o filtro e ignorado (o profissional passa direto, sem ser bloqueado).
            # - Se o campo estiver preenchido, testa a condicao: se o profissional NÃO bate com o filtro, "continue" pula pro proximo profissional sem adicionar ele em resultados.
            if codigo and profissional['codigo'] != int(codigo):
                continue

            if nome and nome not in validar_texto(profissional['nome']):
                continue

            if cpf and profissional['cpf'] != cpf:
                continue

            if email and email not in profissional['email'].lower():
                continue

            if especialidade and especialidade not in validar_texto(profissional['especialidade']):
                continue

            # Se o profissional passou por TODOS os filtros sem cair em nenhum "continue", ele bate com a pesquisa e entra no resultado.
            resultados.append(profissional)

        if not resultados:
            print('\nNenhum profissional encontrado!')

        else:
            print(f'\n{len(resultados)} profissional(is) encontrado(s):')

            for profissional in resultados:
                print('\n========== DADOS DO PROFISSIONAL ==========')

                # Mesmo padrao de exibicao usado no cadastro: percorre o dicionario inteiro automaticamente, sem precisar listar campo por campo no print.
                for chave, valor in profissional.items():
                    campo = chave.replace('_', ' ').title()
                    print(f'{campo:<20}: {valor}')

                print('=' * 38)

        continuar = input('\nDeseja realizar outra pesquisa? (S/N): ').upper()

        # Como esse "if" e a ultima linha do while, nao precisa de "else: continue" - se a condicao for falsa, o loop ja volta pro topo naturalmente.
        if continuar != 'S':
            break


def deletar_profissional():
    if len(profissional) == 0:
        print('Não há profissionais cadastrados.')
        return

    print('\n========== PROFISSIONAIS CADASTRADOS ==========')
    for codigo, dados in profissional.items():
        # dados[0] = nome (de acordo com a tupla: nome, data_nascimento, cpf, sexo, telefone, email)
        print(f'Código: {codigo} - Nome: {dados[0]}')

    codigo = int(input('\nDigite o código do profissional que deseja excluir: '))

    if codigo not in profissional:
        print('Profissional não encontrado!')
        return

    nome_profissional = profissional[codigo][0]
    confirmar = input(
        f'Tem certeza que deseja excluir o profissional '
        f'"{nome_profissional}"? (S/N): '
    ).upper()

    if confirmar == 'S':
        del profissional[codigo]
        print('Profissional excluído com sucesso!')
    else:
        print('Exclusão cancelada.')