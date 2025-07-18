# estrutura Sequencial - comando executado em sequencia

# esrutura com devio de fluxo

# CONDICIONAL  -> se for verdade vai para um lado e executa o cód ou vai para outro bloco e sai da condição
# se -if- (condição verdadeira), se não -else - (falso) 
print(f" ")
alistar = int(input("sua idade: "))

if alistar == 18: print ("Vode deve se alistar\nClique em seguir")

print ("Você não tem 18, a idade para se alistar")

# TEM BLOCO DE CÓD TANTO NO IF QUANTO NO ELSE
print(" ")
nota_1 = float(input("nota 1: "))
nota_2 = float(input("nota 2: "))

media = (nota_1 + nota_2)/2

if media >= 5 : print(f"\nSua média foi {media:.2f}\nVocê está aprovado")
# :.2f = quero apenas 2 casas decimais, o f é de float

else: print(f"Sua média foi {media}\nVocê está reprovado\n")

# multiplas condições

#elif = else + if

if media >= 6 : print(f"\nSua média foi {media:.2f}\nVocê está aprovado")
elif media >=5 : print(f"sua nota foi {media}\nVocê está de recuperação")
else: print(f"Sua média foi {media}\nVocê está reprovado\n")


# aninhamento 

fruta = input("\nFruta que quer comprar: ")
banana = 10
manga = 5
goiaba = 3
laranja = 15

#aqui deve ser and e não or, por se for or, banana não é banana = v, porém banha é diferente de manga, então é verdade, e entra no if. porém com and, tem que ser todas vedades,todas são de fatos comparadas (a forma escrita, digamos assim)
if fruta != "banana" and fruta != "manga" and fruta != "goiaba" and fruta != "laranja":print(f"Não temos a fruta {fruta}")
else:
    print(f"Temos {banana} bananas")
    print(f"Temos {manga} mangas")
    print(f"Temos {goiaba} goiabas")
    print(f"Temos {laranja} laranjas")
    qtd = int(input("Quantidade desejada: "))
    if fruta == "banana":
        if qtd > banana:
            print("Quantidade froda de estoque")
        else:
            print(f"O kilo da banana é R$ 5.00, total R$ {5*qtd:.2f}")
            banana -= qtd
    elif fruta == "manga":
        if qtd > manga:
            print("Quantidade froda de estoque")
        else:
            print(f"o Kilo da manga é R$8.50, total R$ {8.5*qtd:.2f}")
            manga -= qtd
    elif fruta == "goiaba":
        if qtd>goiaba:
            print("Quantidade froda de estoque")
        else:
            print(f"o Kilo da goiaba é R$3.20, total R$ {3.2*qtd:.2f}")
            goiaba -= qtd
    else:
        if qtd>laranja:
            print("Quantidade froda de estoque")
        else:
            print(f"o Kilo da laranja é R$11.00, total R$ {11*qtd:.2f}")
            laranja -= qtd

    
    print(f"\nTemos {manga} mangas")
    print(f"Temos {goiaba} goiabas")
    print(f"Temos {laranja} laranjas")