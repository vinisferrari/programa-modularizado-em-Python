def entrada_carro():
    global carros 
    carros = []
    for i in range(0,4):
        carros.append(input())
        
def entrada_consumo():
    global consumo 
    consumo = []
    for i in range(0,4):
        consumo.append(int(input()))

def economico():
    menor_consumo = consumo.index(min(consumo))
    return carros[menor_consumo]

def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
    
main()