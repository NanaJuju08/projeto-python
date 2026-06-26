from dados.listas import procedimentos
from utils.validacoes import *


def cadastrar_procedimento():
    while True:
        procedimento = {}
        procedimento['codigo'] = len(procedimentos) + 1

        print(
            'Tudo pronto para o cadastro do procedimento.\n'
            'Abaixo, insira as informações necessárias para concluir o cadastro!\n'
        )

        procedimento['nome'] = input('Nome: ').capitalize()
        procedimento['descricao'] = input('Descrição: ').capitalize()
        procedimento['valor'] = validar_float('Valor (Ex.: 00.0): ')
        procedimento['duracao'] = input('Duração (colocar em minutos - Ex.: 120min): ')
        procedimento['sessoes'] = validar_mensagem('Sessões: ')
        procedimento['observacoes'] = input('Observações: ').capitalize()


        procedimentos.append(procedimento)

        print(
            '\procedimento cadastrado com sucesso!'
            '\n========== DADOS DO PROCEDIMENTO =========='
        )

        for chave, valor in procedimento.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('=' * 38)

        continuar = input('\nDeseja cadastrar outro procedimento? (S/N): ').upper()

        if continuar != 'S':
            break


def alterar_procedimento():
    while True:
        for p in procedimentos:
            print(f'Código: {p["codigo"]} - Nome: {p["nome"]}')
            
        codigo = validar_mensagem('Digite o código do procedimento: ')

        procedimento_encontrado = None #Não agrega nenhum valor

        #A variável procedimento percorre a lista, se caso o código digitado esteja na lista, retorna o procedimento_encontrado igual ao procedimento
        for procedimento in procedimentos:
            if procedimento['codigo'] == codigo:
                procedimento_encontrado = procedimento
                break

        if procedimento_encontrado == None:
            print('Procedimento não encontrado!')
            return

        print(f'\nDados atuais do procedimento:')
        for chave, valor in procedimento_encontrado.items():
            campo = chave.replace('_', ' ').title()
            print(f'{campo:<20}: {valor}')

        print('\nOBSERVAÇÃO: Deixe em branco para manter o valor atual.')

        nome = input(f'Nome [{procedimento_encontrado["nome"]}]: ').capitalize()
        if nome:
            procedimento_encontrado['nome'] = nome

        descricao = input(f'Descrição [{procedimento_encontrado["descricao"]}]: ').capitalize
        if descricao:
            procedimento_encontrado["descricao"] = descricao
        
        valor = validar_float(f'Sessões [{procedimento_encontrado["valor"]}]: ')
        if valor:
            procedimento_encontrado["valor"] = valor

        duracao = validar_mensagem(f'Duração [{procedimento_encontrado["duracao"]}](colocar em minutos - Ex.: 120min): ')
        if duracao:
            procedimento_encontrado['duracao'] = duracao

        sessoes = validar_mensagem(f'Sessões [{procedimento_encontrado["sessoes"]}]: ')
        if sessoes:
            procedimento_encontrado['sessoes'] = sessoes
        

        print('\nprocedimento alterado com sucesso!')
    
        print(f'\nDados alterado do procedimento do código {procedimento_encontrado}:')

        for chave, valor in procedimento_encontrado.items():
            print(f'{chave}: {valor}')
        
        continuar = input('\nDeseja alterar outro procedimento? (S/N): ').upper()

        if continuar != 'S':
            break


def pesquisar_procedimento():
    print('Pesquisar')


def deletar_procedimento():
    if len(procedimentos) == 0:
        print('Não há procedimentos cadastrados.')
        return

    print('\n========== PROCEDIMENTOS CADASTRADOS ==========')
    for p in procedimentos:
        print(f'Código: {p["codigo"]} - Nome: {p["nome"]}')

    codigo = int(input('\nDigite o código do procedimento que deseja excluir: '))

    procedimento_encontrado = None
    for p in procedimentos:
        if p['codigo'] == codigo:
            procedimento_encontrado = p
            break

    if procedimento_encontrado is None:
        print('Procedimento não encontrado!')
        return

    confirmar = input(
        f'Tem certeza que deseja excluir o procedimento {procedimento_encontrado["nome"]}? (S/N): ').upper()

    if confirmar == 'S':
        procedimentos.remove(procedimento_encontrado)
        print('Procedimento excluído com sucesso!')
    else:
        print('Exclusão cancelada.')