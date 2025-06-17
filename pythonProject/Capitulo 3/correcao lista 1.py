def soma (numero1,numero2):
    return numero1+numero2

def subtracao(numero1,numero2):
    return numero1-numero2

def multiplicacao(numero1,numero2):
    return numero1*numero2

def divisao(numero1,numero2):
    return numero1//numero2
#main
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite outro número: '))
resultadoSoma = soma(numero1,numero2)
resultadoSub = subtracao(numero1,numero2)
resultadoMulti = multiplicacao(numero1,numero2)
resultadoDivi = divisao(numero1,numero2)
print(f'O resultado da soma entre os número é {resultadoSoma}, o resultado da subtração é '
      f'{resultadoSub}, o resultado da multiplicação é {resultadoMulti}, o resultado da divisão é {resultadoDivi}')