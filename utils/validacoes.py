def validar_mensagem(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Apenas numeros sao validos!')


def validar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        print('O campo CPF precisa ter 11 numeros.')
        return None

    return cpf


def limpar_cpf(cpf):
    return ''.join(filter(str.isdigit, str(cpf)))


def cpf_duplicado(cpf, clientes):
    cpf = limpar_cpf(cpf)

    for cliente in clientes:
        if limpar_cpf(cliente['cpf']) == cpf:
            return True

    return False


def mascarar_cpf(cpf):
    cpf = limpar_cpf(cpf)

    if len(cpf) != 11:
        return None

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
