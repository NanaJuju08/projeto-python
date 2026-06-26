from dados.listas import profissionais
from utils.validacoes import *
from datetime import datetime
import re #regex - é uma sequência de caracteres que forma um padrão de busca, usada de forma rápida para validar, encontrar, ou substituir textos e dados que seguem regras específicas (como formatos de e-mail, CPF, ou senhas).

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
            '\nDeixe em branco para não filtrar pelo campo.\n'
        )

        codigo = input('Código: ')
        nome = validar_texto(input('Nome: '))
        cpf = input('CPF: ')
        email = input('Email: ').lower().strip()
        especialidade = validar_texto(input('Especialidade: '))

        if cpf:
            cpf_validado = validar_cpf(cpf)
            if not cpf_validado:
                print('CPF inválido, pesquisa cancelada.')
                continue
            cpf = mascarar_cpf(cpf_validado)

        resultados = []

        for profissional in profissionais:

            if codigo and profissional['codigo'] != int(codigo):
                continue

            if nome and nome not in validar_texto(profissional['nome']):
                continue

            if cpf and profissional['cpf'] != cpf:
                continue

            if email and email not in profissional['email'].lower().strip():
                continue

            if especialidade and validar_texto(profissional['especialidade']) != especialidade:
                continue

            resultados.append(profissional)

        if not resultados:
            print('\nNenhum profissional encontrado!')

        else:
            print(f'\n{len(resultados)} profissional(is) encontrado(s):')

            for profissional in resultados:
                print('\n========== DADOS DO PROFISSIONAL ==========')

                for chave, valor in profissional.items():
                    campo = chave.replace('_', ' ').title()
                    print(f'{campo:<20}: {valor}')

                print('=' * 38)

        continuar = input('\nDeseja realizar outra pesquisa? (S/N): ').upper()

        if continuar != 'S':
            break

def deletar_profissional():
    if len(profissionais) == 0:
        print('Não há profissionais cadastrados.')
        return

    print('\n========== PROFISSIONAIS CADASTRADOS ==========')
    for p in profissionais:
        print(f'Código: {p["codigo"]} - Nome: {p["nome"]}')

    codigo = validar_mensagem(
        '\nDigite o código do profissional que deseja excluir: '
    )

    profissional_encontrado = None
    for p in profissionais:
        if p['codigo'] == codigo:
            profissional_encontrado = p
            break

    if profissional_encontrado is None:
        print('Profissional não encontrado!')
        return

    if profissional_tem_agendamento_em_aberto(profissional_encontrado['codigo']):
        print('Profissional possui agendamento em aberto e não pode ser excluido!')
        return

    confirmar = input(
        f'Tem certeza que deseja excluir o profissional '
        f'"{profissional_encontrado["nome"]}"? (S/N): '
    ).upper()

    if confirmar == 'S':
        profissionais.remove(profissional_encontrado)
        print('Profissional excluído com sucesso!')
    else:
        print('Exclusão cancelada.')
