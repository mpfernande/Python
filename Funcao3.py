# Criar uma função chamada areaTerreno que vai receber como parâmetro a largura e comprimento de um terreno e vai retornar a área do terreno

def areaTerreno(Largura, Comprimento):
    area = largura * Comprimento
    
    return area

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
print (f"A área total do terreno é {areaTerreno(largura,comprimento)} metros quadrados")
