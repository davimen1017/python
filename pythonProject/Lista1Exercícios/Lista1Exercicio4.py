popMundial = 8.200000000
taxCrescimento = 0.0085
ano = 0
for c in range(1,6):
    ano +=1
    estimativa = popMundial * ((1 + taxCrescimento) ** ano)
    print(f'A população daqui {ano} vai ser de {estimativa}')