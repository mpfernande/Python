def CalcularAumento(Salario,percentualAumento):
    #Esta função calcula o aumento de salário do mês
    Aumento = Salario * percentualAumento
    salarioCorrigido = Salario + Aumento
    return(Aumento, salarioCorrigido)

salario = float(input("Digite o salário do funcionário: "))
perAumento = float(input("Digite o percentual de aumento: "))
perAumento = (perAumento/100)

print(CalcularAumento(salario,perAumento))

