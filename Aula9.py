

preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))
if preco1 < preco2 and preco1 < preco3:
    menor = preco1
    if preco2 < menor:
        menor = preco2
print(menor)