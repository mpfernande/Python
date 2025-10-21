# Criar uma função chamada Soma que vai receber como parâmetro dois valores e vai retornar a soma dos 2 números

def soma(x,y):
    total = x + y
    
    return total

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: ")) 

print (f" A soma é {soma(x,y)}")