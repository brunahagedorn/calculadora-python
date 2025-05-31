# calculadora.py

def menu():
    print("\n===== CALCULADORA EM PYTHON =====")
    print("[1] Somar")
    print("[2] Subtrair")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Sair")
    print("==================================")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '5':
        print("Encerrando a calculadora... Até mais!")
        break

    if opcao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro! Por favor, digite números válidos.")
            continue

        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} x {num2} = {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} ÷ {num2} = {resultado}")
            else:
                print("Erro! Não é possível dividir por zero.")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
