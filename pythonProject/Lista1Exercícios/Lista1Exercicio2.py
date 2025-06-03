senha = str(input('Digite sua senha com 5 dígitos: '))
qtdDigitos = len(senha)
for digitos in senha:
    if qtdDigitos!=5:
        print('Sua senha deve ter 5 dígitos')
    else:
        print(digitos)