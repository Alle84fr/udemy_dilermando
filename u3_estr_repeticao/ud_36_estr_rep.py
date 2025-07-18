# Estruturas de repetição = conjunto de comandos que dão mais "movimentos" aos programas/Scripts
# uma ação pode ser executada várias vezes sem darmos um comando

#%%

# ........................................for

#for variavelDeInteração in sequência :
# comando/s

#função RANGE - restonar lista de valores
# apenas o fim é obrigatório no interável/sequência/lista
# range(inicio, fim, passos)

for i in range(2):
    print(i)
for e in range (2,8): 
    #lembrando que fica no 7, um a menos
    # pula de um em um
    print(f" outro {e}")
for i in range(0,24,4):
    print(f"{i}")
    
    
# %%

# fiz diferente
# f = format

soma = 0
for i in range(1,6):
    nota = int(input(f"notas {i}: "))
    soma += nota
    print(f"Você digitou {nota}\nsoma {soma}")
media = soma/5
print(f"A média é {media}")     


#%%

for char in "Passaros":
    # desta froma o final não é \n, mas espaço entre os caracteres e -
    print(char, end= " - ")
    
    
# %%

# fatorial -> número que é resultado da multiplicação dos n anteriores incluindo o próprio n°

n = int(input("n° a fatorar: "))

fatorial = 1
p = 1

if n < 0: print("não existe  fatorias de {n}")
elif n == 0: print("Fatorial de {n} é 1")
else:
    #deve-se por mais um em n porquê se por só n termina um n° antes
    for i in range(1,n+1):
        print(f"{i}° valor é {fatorial*p}")
        fatorial = fatorial*p
        p += 1
        
        
    print(f"Fatorial de {n} é {fatorial}")
# %%
