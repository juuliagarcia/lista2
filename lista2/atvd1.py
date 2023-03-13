
num = int(input("Digite um número inteiro: "))

print("Divisores de", num, ":")
for i in range(1, num+1):
    if num % i == 0:
        print(i)
