# ide  = editor de texto, ambiente de programação
# tipos primitivos int - inteiros - ex 10

inteiro = 11
print(type(inteiro))
print("¨"*20)
print(inteiro)
print("¨"*20)
# recurso para visualizar melhor o número

# numero = 1000000 == 1_000_000

add_um = 12
print(add_um)
print("¨"*20)

add_um += 1
print(add_um)
print("¨"*20)

add_um = add_um +1
print(add_um)
print("¨"*20)

print("O comando dir()mostra as funções que se pode fazer com o tipo primitivo\n")
print(dir(add_um))
#\n para pular linha
print("__"*40)

# float - numero decimais

float_num = 11.0
print(f"O número {float_num} é do tipo {type(float_num)}")
print(".."*20)

int_n = 12
converte = float(int_n)
convert_str = str(converte)
print("para converter -> variálvel = tipoParaConvevrter(o que será convertido)")
print(f"O número {int_n} é do tipo {type(int_n)}")
print(f"O número {converte} ficou do tipo {type(converte)}")
print(f"Agora o {convert_str} é do tipo {type(convert_str)}")

# o float tem um n° limitado ´máximo é 2.45**792 bits

# 1000000.0 = 1_000_000.0

# numeros complexos -  terminam com j ou i

num_complexo= 5j
print(type(num_complexo))
print("\n__"*40)

# booleano - verdadeiro e falso
# é em letras miúscula o nome do valor
# flag = sinalizador

bool_v = True
bool_f = False

# string sequência de caracteres
# vem aspas simples e duplas

char = "a "
str_letras = 'letra'
concatenizacao = char + str_letras


print(char)
print(str_letras)
print(concatenizacao)
print("~~"*20)
# pegar caractere específico, lista

print(f"\nposição 0 = 1° tem {concatenizacao[0]}\nO espaço conta como caracteres {concatenizacao[1]}\nPode pegar a última posição usando menos, que inica no -1 {concatenizacao[-2]}")
print("~~"*20)

# Slice = fatiamento
# ex: frase[parametro inicio:parametro limite(pega uma casa antes):tamanho do passo (se pula)]

frase = "\nAbacate e cavlos não são azuis"
print(frase[10:17])

print(f"\nEste Slice pula de 2 em dois\nTem no total 29 caracteres, mas coloquei 3 para pegar o último\n ficou: {frase[0:30:2]}")

print(f"\n: : deixa a frase toda, o n° negativo vem de trás para frente\n{frase[::-1]}")

# strip limpa espaços em branco das pontas
# é uma bult in -> coloca ponto e depois a chama

com_espaco = "      Tudo bem?      "
print(f"|{com_espaco}|")
print("com strip")
print(f"|{com_espaco.strip()}|\n")

# up - função, tudo maiúsculo

maiu = "abcder"
print(maiu.upper())

minu = "AGHTCFHY"
print(maiu.lower())

#split
#referencia espaçço em branco caso não passe referência
# se não me engano forma uma lista, como novos índices

divisao = "Frase corta com base em espaço em branco"
print('')
print(divisao.split())

com_caracteres = "separa com base no: dois ponto: a frase, email, nome, etc"
print('')
print(com_caracteres.split(":"))

# escopo
# hall de atuação da varável
# global - vista do começo ao fim
# local - conhece quando chama a função, por exemplo

# DECLARAÇÃO LOCAL É A MAIS PRÓXIMA E É QUE SUPERIOR/PRIORITÁRIA

# caso não tenha a variável na função/bloco, será a global

print("\n__"*40)

global_1 = 1
glo_loc = 2

print(f"Globais\nglobal_1 = {global_1}\nglobal_local = {glo_loc}")

def funcao():
    
    glo_loc = 4
    print(f"Globais\nglobal_local da funçao ={glo_loc}")

#chamando a função
funcao()
print(f"Globais\nglobal_1 ={global_1}\nglobal_local final = {glo_loc}")

# cconverões:

# int -> float = x = float(y)
# float -> int = x = int(y)
# float -> int = x = round(y)- arredonda, joga valor para cima
# str -> int = x = int(y)
# float -> str = x = str(y)

float_num_1 = 10.3
float_num_2 = 10.5
float_num_3 = 10.59

convert_1 = int(float_num_1)
convert_1_r = round(float_num_1)
convert_2_r = round(float_num_2)
convert_3_r = round(float_num_3)

print(convert_1)
print(convert_1_r)
print(convert_2_r)
print(convert_3_r)

# _________________________ desafio _______________________

#receber valor positivo, receber frase, converter numero para decinal, caracteres maiúsculas e depois print

numero = int(input("valor maior que o, inteiro: "))
texto = input("Digite uma frase: ")

x = float(numero)
texto = texto.upper()

print(x)
print(texto)