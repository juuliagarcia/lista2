num = int(input("Digite um número inteiro: "))

a, b = 0, 1

print("Sequência de Fibonacci até o", num, "º termo:")
for i in range(num):
    print(a, end=" ")
    a, b = b, a+b
