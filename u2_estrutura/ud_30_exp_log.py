#Expressão lógica

# Retorno em boolenao - Verdade ou falso

# operadores relacionais
# == igual != diferente > maior < menor >= maior igual <= menor igual

a = 12
b = 22
c = 12

print(f"a maior que b = {a>b}\na é menor b = {a<b}\na é igual a c ={a==c}\na é diferente de b = {a!=c}")

# not = negação
# and = e 
# or = ou

# tabela verdade meu resumo

# e só é verdade se todos forem verdade
# ou  só é falso se todos falsos
# not inverte -  verdade vira falso, falso vira verdade

# and                 or                 not

# |x|y|x and y|       |x|y|x and y|      |x|y|not |
# |T|T|   T   |       |T|T|   T   |      |T| |  F |
# |T|F|   F   |       |T|F|   T   |      |F| |  T |
# |F|T|   F   |       |F|T|   T   |      | |T|  F |
# |F|F|   F   |       |F|F|   F   |      | |F|  T |

n = 15 > 2 and 12 > 11
m = 15 > 2 and 12 < 11
o = 15 < 2 or 12 < 11
p = 15 < 2 or 12 > 11
q = True
q_not = not(q)

print(f"\n15 é maior que 2 e 12 maior que 11 (n) = {n}")
print(f"\n15 é maior que 2 e 12 menor que 11 (m) = {m}")
print(f"\n15 é menor que 2 ou 12 menor que 11 (o) = {o}")
print(f"\n15 é menor que 2 ou 12 maior que 11 (p) = {p}")
print(f"\nnega q = {q_not}\n")

# prioridade dos operadores:
# da esquarda para direita
    
#     1° dentro do parêntese
#     2° Expoente
#     3° definição de sinais (ex ++ = +, +- = -, --=+)
#     4° multiplicação e as divisões
#     5° soma e subtração
#     6° commparação
#     7° negação
#     8° and/e 
#     9° or/ou

conta =  1+((4/2)*3)+2**4/(-16)
# 1+((2)*3)+2**4/(-16)
# 1+6+2**4/(-16)
# 1+6+16/(-16) -> 2*2=4*2=8*2=16
# 1+6+-1 -> - com + = - -> 16/16 = -1
# 1+6-1 -> + com - = -
# 7 - 1 -> primeiro da esquerda
# 6

print(conta)