#ALGORITMO QUE SERÁ CRIADO DEVERÁ SER USADO O IF E WHILE PARA DIGITAR 3 FUNCIONÁRIOS

#Uma empresa decide dar um reajuste a seus funcionários de acordo com os 
#critérios: 
#50% para aqueles que ganham menos de 3000. 
#20% para aqueles que ganham entre 3000 e 5000 (inclusive);
#15% para aquele que ganham entre 5001 a 7000 
#10% para os demais.

# 1 - Criar as variáveis do programa
cont = 0
# 2 - Criar os inputs que o usuário vai ter que digitar

while cont <=2:
    salario = float(input("Digite o salário atual do funcionário: "))

# 3 - Criar os cálculos do reajuste dos salários
    if salario <=3000:
        reajuste = salario * 0.50
    elif salario >3000 and salario <=5000:
        reajuste = salario * 0.20
    elif salario >=5001 and salario <=7000:
        reajuste = salario*0.15

    else:
        reajuste = salario * 0.10

    salarioReajustado = salario + reajuste
    
# 4 - Criar os PRINTS: O Valor do reajuste e o Salário com o reajuste
    print(reajuste)
    print (salarioReajustado)
    cont = cont+1