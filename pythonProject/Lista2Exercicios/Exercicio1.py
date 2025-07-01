salario = float(input('Digite o valor do salário: '))
porcentagem = float(input('Digite a porcentagem do aumento: '))
aumento = (porcentagem/100)*salario
novosalario = aumento+salario
print(f'Seu salário de {salario}, recebeu um aumento de {porcentagem}%')
print(f'Seu novo salário é {novosalario}')