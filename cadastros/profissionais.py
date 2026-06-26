from datetime import datetime
import re #regex - é uma sequência de caracteres que forma um padrão de busca, usada de forma rápida para validar, encontrar, ou substituir textos e dados que seguem regras específicas (como formatos de e-mail, CPF, ou senhas).

medicos = {}

def cadastrar_profissional():
    while True:
        codigo = int(input('Digite o código do novo médico: '))
        if codigo in medicos:
            print('Código já em uso, tente outro.')
            continue
        else: 
            nome = input('Digite o nome do novo médico: ')
            data_nascimento  = input("Digite a data de nascimento do novo médico (DD/MM/AAAA): ")
            data = datetime.strptime(data_nascimento , "%d/%m/%Y")
            cpf_numeros = input('Digite o CPF do novo médico: ')
            cpf = re.sub(r'\D', '', cpf_numeros)
            cpf_duplicado = False

            if len(cpf) != 11:
                print('CPF inválido!')
                continue

            for dados in medicos.values():
                if dados[2] == cpf:
                    cpf_duplicado = True
                    break

            if cpf_duplicado:
                print('CPF já está em uso!')
                continue

            sexo = input('Digite o sexo do novo médico: ').upper()
            telefone= int(input('Digite o número de telefone do novo médico: '))
            email = input('Digite o email do novo médico: ')
            if not re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email):
                print('Email inválido!')
                continue

            medicos[codigo] = (nome, data_nascimento, cpf, sexo, telefone, email)
            break


def pesquisar_profissional():
    while True:
        print(
            '\n========== PESQUISA DE PROFISSIONAL =========='
            '\nPreencha os campos que deseja usar como filtro.'
            '\nDeixe em branco para nao filtrar pelo campo.\n'
        )

        codigo = input('Codigo: ')
        nome = input('Nome: ').lower()
        cpf = input('CPF: ')
        sexo = input('Sexo: ').lower()
        email = input('Email: ').lower()

        # Aqui o CPF NAO usa mascarar_cpf(), porque no cadastro de profissionais o CPF e salvo so com numeros (re.sub remove tudo que nao for digito). Entao limpamos o CPF digitado do mesmo jeito, pra garantir que a comparacao bata certinho.
        if cpf:
            cpf = re.sub(r'\D', '', cpf)

        resultados = []

        # medicos.items() devolve a CHAVE (cod) e o VALOR (dados) de cada item do dicionario ao mesmo tempo. Diferente de "clientes", aqui "dados" e uma TUPLA, nao um dicionario - por isso precisamos desempacotar ela manualmente na linha de baixo.
        for cod, dados in medicos.items():
            # Desempacotamento de tupla: cada posicao da tupla "dados" e atribuida a uma variavel com nome, na MESMA ORDEM em que foi salva no cadastro (nome, data_nascimento, cpf, sexo, telefone, email).
            # Isso evita ficar usando dados[0], dados[1], dados[2]... no resto do codigo.
            nome_medico, data_nascimento, cpf_medico, sexo_medico, telefone, email_medico = dados

            # Validacao de seguranca: se a pessoa digitar algo que nao seja numero no campo codigo, isso evita o ValueError de int(codigo) mais abaixo, e so ignora esse filtro com um aviso.
            if codigo and not codigo.isdigit():
                print('Codigo invalido, ignorando esse filtro.')
                codigo = ''

            if codigo and cod != int(codigo):
                continue

            if nome and nome not in nome_medico.lower():
                continue

            if cpf and cpf_medico != cpf:
                continue

            if sexo and sexo != sexo_medico.lower():
                continue

            if email and email not in email_medico.lower():
                continue

            # Reconstroi uma tupla com TODOS os dados (incluindo o codigo, que normalmente fica de fora pois e a chave do dicionario) para poder exibir tudo junto na hora de mostrar o resultado.
            resultados.append((cod, nome_medico, data_nascimento, cpf_medico, sexo_medico, telefone, email_medico))

        if not resultados:
            print('\nNenhum profissional encontrado!')

        else:
            print(f'\n{len(resultados)} profissional(is) encontrado(s):')

            # Como "resultados" guarda tuplas (e nao dicionarios), precisamos desempacotar de novo aqui pra poder usar cada campo pelo nome na hora de exibir - nao tem ".items()" pra fazer isso automatico.
            for cod, nome_medico, data_nascimento, cpf_medico, sexo_medico, telefone, email_medico in resultados:
                print('\n========== DADOS DO PROFISSIONAL ==========')
                print(f'{"Codigo":<20}: {cod}')
                print(f'{"Nome":<20}: {nome_medico}')
                print(f'{"Data Nascimento":<20}: {data_nascimento}')
                print(f'{"Cpf":<20}: {cpf_medico}')
                print(f'{"Sexo":<20}: {sexo_medico}')
                print(f'{"Telefone":<20}: {telefone}')
                print(f'{"Email":<20}: {email_medico}')
                print('=' * 38)

        continuar = input('\nDeseja realizar outra pesquisa? (S/N): ').upper()

        if continuar != 'S':
            break

def alterar_profissional():
    print('Alterar')

def pesquisar_profissional():
    print('Pesquisar')

def deletar_profissional():
    if len(medicos) == 0:
        print('Não há profissionais cadastrados.')
        return

    print('\n========== PROFISSIONAIS CADASTRADOS ==========')
    for codigo, dados in medicos.items():
        # dados[0] = nome (de acordo com a tupla: nome, data_nascimento, cpf, sexo, telefone, email)
        print(f'Código: {codigo} - Nome: {dados[0]}')

    codigo = int(input('\nDigite o código do profissional que deseja excluir: '))

    if codigo not in medicos:
        print('Profissional não encontrado!')
        return

    nome_profissional = medicos[codigo][0]
    confirmar = input(
        f'Tem certeza que deseja excluir o profissional '
        f'"{nome_profissional}"? (S/N): '
    ).upper()

    if confirmar == 'S':
        del medicos[codigo]
        print('Profissional excluído com sucesso!')
    else:
        print('Exclusão cancelada.')