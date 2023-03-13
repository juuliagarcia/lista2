num = int(input("Digite um número inteiro: "))

print("Múltiplos de", num, "menores que 100:")

for i in range(1, 100):
    if num * i >= 100:
        break
    print(num * i)
