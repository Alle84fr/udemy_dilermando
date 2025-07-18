num = int(input("Numero: "))

if num <= 0: 
    print("Numero inteiro maior que zero")
else:
    resto = num % 2
    if resto == 0: print(f"{num} é par")
    else: print(f"{num} é impar")

#______________________________________________

h = float(input("Altura: "))
s = input("mulher ou hômem: ")

if s == "mulher":
    print(f"Seu peso ideal é {(62.1*h)-44.7:.2f}")
else:
    print(f"Seu peso ideal é {(72.7*h)-58:.2f}")