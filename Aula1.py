txDolar = 1.8
produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
precoUnitario = float(input("Digite o preço unitário: "))

total = quantidade*precoUnitario
totalDolar = total/txDolar
print(produto)
print(total)
print(totalDolar)