num = int(input("Digite dois número inteiro: "))

soma = 0

while num != 0:
    ultimo_digito = num % 10
    soma += ultimo_digito
    num = num // 10

print("A soma dos dígitos é:", soma)
