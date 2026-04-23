operation = input("Digite a operação (+, -, *, /): ")

match operation:
    case "+":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    case "-":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    case "*":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        result = n1 * n2
        print(f"O resultado da multiplicação é: {resultado}")