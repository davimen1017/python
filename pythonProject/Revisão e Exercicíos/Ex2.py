def mediaCalculo(formativa1, formativa2, provabi):
    return ((formativa1 + formativa2 )*0.3)+((provabi)*0.7)        
def display(mediaBimentral):
    print(f'Sua média bimestral é: {mediaBimentral}')

formativa1 = int(input('Digite a nota da formativa 1: '))
formativa2 = int(input('Digite a nota da formativa 2: '))
provabi = int(input('Digite a nota da prova bimestral: '))
mediaBimestral = mediaCalculo(formativa1, formativa2, provabi)
display(mediaBimestral)