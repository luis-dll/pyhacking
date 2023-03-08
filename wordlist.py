#Código para criar wordlists simples

import itertools

palavra = input("Digite a palavra base para a wordlist: ")

caracteres = []
for letra in palavra:
    if letra not in caracteres:
        caracteres.append(letra)

combinacoes = []
for i in range(1, len(caracteres)+1):
    for comb in itertools.product(caracteres, repeat=i):
        senha = ''.join(comb)
        combinacoes.append(senha)

with open('wordlist.txt', 'w') as f:
    for comb in combinacoes:
        f.write(comb + '\n')

print(f"Wordlist gerada com {len(combinacoes)} combinações.")
