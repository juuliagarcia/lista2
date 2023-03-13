num = int(input("Digite um número inteiro: "))


for i in range(2, num+1):
   
    eh_primo = True
    
    for j in range(2, i//2 + 1):
    
        if i % j == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(i)
