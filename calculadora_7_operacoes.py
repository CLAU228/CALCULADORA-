def calculadora():

    print("Bem-vindo à Calculadora 7 Operações!")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponenciação")
    print("6 - Divisão Exata")
    print("7 - Resto da Divisão")

    escolha = int(input("Digite o número da operação desejada: "))
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == 1:
        print("Resultado:", a + b)
    elif escolha == 2:
        print("Resultado:", a - b)
    elif escolha == 3:
        print("Resultado:", a * b)
    elif escolha == 4:
        print("Resultado:", a / b)
    elif escolha == 5:
        print("Resultado:", a ** b)
    elif escolha == 6:
        print("Resultado:", a // b)
    elif escolha == 7:
        print("Resultado:", a % b)
    else:
        print("Operação inválida!")

calculadora()

