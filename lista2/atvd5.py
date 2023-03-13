num = int(input("Digite um número inteiro: "))

fat = 1
for i in range(2, num+1):
    fat *= i

print("O fatorial de", num, "é", fat)
