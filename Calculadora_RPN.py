# LUCCA BORNANCIN PEDRONI SILVA
''' Você deverá desenvolver um programa, na sua linguagem de programação favorita, que leia 
uma string de entrada e execute a operação matemática contida nesta string. Esta string irá 
representar operações matemáticas segundo uma variação da RPN, que inclui obrigatoriamente 
parênteses para limitar as operações, conforme exemplos a seguir: 
a) (2 3 +) = 5 
b) (3 4 *) = 12 
c) (4 2 2 /) = 1 
d) ((4 2 +) 3 *) = 18  
O seu programa deverá ser capaz de realizar as seguintes operações:  
• Adição representada por +; 
• Subtração representada por -; 
• Multiplicação representada por *; 
• Divisão representada por /; 
As operações devem ser realizadas com número reais, mesmo que todos os exemplos aqui 
utilizados sejam com números inteiros. As operações podem ser aninhadas, sem qualquer limite, 
como pode ser visto nos exemplos a seguir:  
• ((3 4 +) (4 2 /) *) = 14 
• ((3 4 +) (4 (1 1 +) /) *) = 14 
Os operandos serão separados de outros operandos e dos operadores por um caractere de 
espaço. Por fim, O sinal de igual e todos os resultados que estão a direita deste símbolo neste 
enunciado não fazem parte da string que deverá ser lida e estão aqui apenas para facilitar o 
entendimento. '''

print("\n============= CALCULADORA RPN =============")
equacao = input("\nDigite a equacao que deseja calcular: ")

if equacao[0] == "(" and equacao[len(equacao)-1] == ")":
    l = list(equacao[1:len(equacao)-1])
    equacao = "".join(l)
    r = equacao.split()
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
