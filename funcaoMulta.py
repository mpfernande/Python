velocidadeCarro = int(input("Digite a velocidade do carro: "))
def multaTransito(velocidade):
    if velocidade >80:
        multa = (velocidade - 80) * 5.00
        print(f'Você foi multado e o valor da multa é {multa}')
    else:
        print("Você está dentro dos limites de velocidade")

multaTransito(velocidadeCarro)