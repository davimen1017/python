precoCapaLivro = 24.95
precoCapaLivroDesconto = precoCapaLivro - (precoCapaLivro * 0.40)
custoFretePrimeiroExemplar = precoCapaLivroDesconto + 3.00
custoFreteRestante = precoCapaLivroDesconto+0.75
custoTotalAtacado = custoFretePrimeiroExemplar + (custoFreteRestante * 59)

print(f'O preço total de atacado para 60 exemplares é de {custoTotalAtacado}')
