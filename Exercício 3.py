""" Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:
    A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
    Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.
    Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:
    Exemplo:
    Digite o nome do cliente: Fulano de Tal
    Digite o dia de vencimento: 9
    Digite o mês de vencimento: Janeiro
    Digite o valor da fatura: 350,00
    A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada."""
    
class Fatura():
    def __init__(self, nome, dia, mes, valor):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.valor = valor
    
    def boleto(self):
        print(f"Sr(a).{self.nome} a sua fatura com vencimento em {self.dia} de {self.mes} no valor de R$ {self.valor} está fechada")

if __name__ == '__main__':
    nome = str(input("Digite o nome do cliente: "))
    dia = str(input("Digite o dia de vencimento: "))
    mes = str(input("Digite o mês de vencimento: "))
    valor = float(input("Digite o valor da fatura:"))
    cliente = Fatura(nome, dia, mes, valor) 
    
    Fatura.boleto(cliente)