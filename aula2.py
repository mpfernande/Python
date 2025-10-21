cont = 0
totalPagar = 0
while cont <=2:
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade comprada: "))
    precoUnitario = float(input("Digite o preço unitário: "))

    total = quantidade*precoUnitario

    print(f' Total do produto {produto} é:{total:.2f}')
    totalPagar = totalPagar + total     
    cont = cont+1

print(f' O Total a pagar é: {totalPagar:.2f}')

