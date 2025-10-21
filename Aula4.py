txinss = 0.10
nomeFuncionario = input("Digite o nome do funcionário: ")
salarioBruto = float(input("Digite o salário bruto do funcionário: "))
txgratificacao = float(input("Digite a porcentagem de grafificação: "))

gratificacao = salarioBruto * txgratificacao
inss = salarioBruto * txinss
salarioLiquido = salarioBruto-inss+gratificacao
print(f'O nome do funcionário é: {nomeFuncionario}')
print(f'O salário bruto é: {salarioBruto}')
print(f'O valor do INSS é: {inss}')
print(f'O valor do salário líquido é: {salarioLiquido}')
