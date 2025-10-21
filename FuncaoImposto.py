   
def Imposto(receita,txImposto):
    impostoDevido = receita * txImposto

    return impostoDevido
#print(f'Imposto devido é {Imposto(90000,0.15)}')

faturamento = float(input("Digite o faturamento do mes: "))
print(f'Imposto devido é {Imposto(faturamento,0.15)}')

