numero = int(input("Digite um número inteiro: "))
fator = 2

while numero > 1:
    if numero % fator == 0:
        print(fator)
        numero = numero / fator
    else:
        fator += 1