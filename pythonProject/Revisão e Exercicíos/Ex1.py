def formula(altura):
    return (62.1*altura)-44.7
def displaypesoIdeal(pesoIdeal,altura):
    print(f'A sua altura {altura} e o seu peso ideal é: {formula}')
altura = float(input('Digite sua altura: '))
pesoIdeal = formula(altura)
displaypesoIdeal(pesoIdeal,altura)