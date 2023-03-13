numero = int(input("Digite um número inteiro: "))

while True:
    limite = int(input("Digite o limite da tabuada: "))
    for i in range(1, limite+1):
        print(numero, "x", i, "=", numero*i)    
    break