pordia = int(input('Quantos cigarros você fuma por dia ?'))
anos = int(input('Durante quantos anos vocẽ fuma ?'))
diasano = 365*anos
cigarrosporano = pordia*diasano
cigarro = 10
minutosperdidos = cigarrosporano*cigarro
dia = 1440
diasperdidos = minutosperdidos/dia
print(f'A pessoa fuma {pordia}, cigarro(s) por dia(s), durante {anos} ano(s)')
print(f'A pessoa perdeu {round(diasperdidos,1)} dias de vida')