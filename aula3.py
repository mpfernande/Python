
# ALGORITMO QUE SERÁ CRIADO VAI SER EM UMA LISTA E USAR O WHILE
# O WHILE DEVERÁ TER A OPÇÃO PARA DIGITAR TRÊS MESES DE FATURAMENTO

# 1 - CRIAR 3 LISTAS VAZIA: Mes, Faturamento
mes = []
faturamento = []
txImposto = 0.18
cont = 0

while cont <2:
# 2 - CRIAR UM INPUT PARA O USUÁRIO DIGITAR O MÊS e o FATURAMENTO  
    mesDigitado = (input("Digite o mês do faturamento: "))
    faturamentoDigitado = float(input("Digite o faturamento: "))

# 3 - ARMAZENAR O MÊS DO FATURAMENTO E O VALOR DO FATURAMENTO NA LISTA CRIADA
    mes.append(mesDigitado)
    faturamento.append(faturamentoDigitado)

    cont = cont+1
# 4 - CALCULAR O IMPOSTO DEVIDO
ImpostoDevido = sum(faturamento)*txImposto

# 5 - NO FINAL PEDE-SE: PRINTAR O TOTAL DO FATURAMENTO E IMPOSTO 

print (sum(faturamento))
print (ImpostoDevido)

print("----Algorítmo SOMAR NÚMEROS----")


