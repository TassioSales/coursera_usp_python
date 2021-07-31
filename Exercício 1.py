"""Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados: 
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez"""

class Quadrado():
    def __init__(self, lado):
        self.lado = lado
        
    def area_quadrado(self):
        area = self.lado * self.lado
        print(f"A area do quadrado e {int(area)}")
    
    def parimetro_quadrado(self):
        parimetro = self.lado * 4
        print(f"O parimentro do quadrado e {int(parimetro)}")

if __name__ == '__main__':
    while True:
            try:
                print("Caso o numero digitado seja do tipo floar ele sera arredondado.")
                lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))
                quadrado_1 = Quadrado(lado)
                Quadrado.area_quadrado(quadrado_1)
                Quadrado.parimetro_quadrado(quadrado_1)
            except  Exception as e:
                print(e)
                print(e.__class__)
                break               