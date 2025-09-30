def verificaIdade(idade):
    if idade >= 18:
        return True
    else:
        return False
def display(idade, deMaior):
    if deMaior == True:
        print('Você é de maior')
    else:
        print('Você é de menor')

idade = int(input('Digite a sua idade:'))
deMaior = verificaIdade(idade)
display(idade, deMaior)
