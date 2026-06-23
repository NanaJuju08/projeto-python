def validar_mensagem(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Apenas números são válidos!")