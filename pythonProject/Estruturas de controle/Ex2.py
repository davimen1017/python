def calculoQuadrado(n):
    return n**2
def display(quadrado,n):
    if n < 0:
        print('O número que você digitou é negativo')
    else:
        print(f'O quadrado do número {n} é {quadrado}')

n = float(input('Digite um número qualquer que seja positivo: '))
quadrado = calculoQuadrado(n)
display(quadrado,n)