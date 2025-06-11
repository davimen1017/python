def soma(n1, n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

resultadoSoma = soma(n1,n2)
resultadoSubtracao = subtracao(n1,n2)
resultadoMultiplicacao = multiplicacao(n1,n2)
resultadoDivisao = divisao(n1,n2)
print(f'resltado da soma é {resultadoSoma} o resultado da subtração é {resultadoSubtracao}  o resultado da multiplicação é {resultadoMultiplicacao} o resultado da divisao é {resultadoDivisao}')