cont = 1
qtd = int(input("Quantas notas deseja adicionar"))
lista_notas = []
while qtd >= cont:
    notas = float(input(f"Digite a {cont}º nota: "))
    lista_notas.append(notas)
    cont += 1    
print(f"A media do aluno e {sum(lista_notas) / len(lista_notas)}")
            
                                  
    
    