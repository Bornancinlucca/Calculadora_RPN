
print("\n====== CALCULADORA RPN ======")
equacao = input("\nDigite a equacao que deseja calcular: ")

if equacao[0] == "(" and equacao[len(equacao)-1] == ")":
    l = list(equacao[1:len(equacao)-1])
    equacao = "".join(l)
    r = equacao.split()
    print(r)
    if r[2] == "+":
        equacao = float(r[0]) + float(r[1])
        print("Resultado = ", equacao)
    elif r[2] == "-":
        equacao = float(r[0]) - float(r[1])
        print("Resultado = ", equacao)
    elif r[2] == '*':
        equacao = float(r[0]) * float(r[1])
        print("Resultado = ", equacao)
    elif r[2] == '/':
        equacao = float(r[0]) / float(r[1])
        print("Resultado = ", equacao)