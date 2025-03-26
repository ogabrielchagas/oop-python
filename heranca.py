class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print('Acelerando...')
    
    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')

class Uno(Carro):
    marca = 'Fiat'
    modelo = 'Uno'
    ano = 1992
    

carro = Carro()
carro.acelerar()

uno = Uno()
print(uno.marca)
uno.frear()
print(uno.quantidade_passageiros)
