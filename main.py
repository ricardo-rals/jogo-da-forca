import random

palavras = []
quantidade_palavras = 5

while True:
    print('========================================================================\n')
    print('----------Seja bem vindo ao Jogo da Forca. ----------')
    print('\n========================================================================\n')
    tema = input('Informe um tema para o jogo: ')

    for indice in range(quantidade_palavras):
        if quantidade_palavras > 1:
            print(f'----------Você pode inserir {quantidade_palavras} palavras.----------')
        else:
            print(f'----------Você pode inserir {quantidade_palavras} palavra.-----------')  
        palavra = input(f'Informe uma palavra: ')
        palavras.append(palavra)
        quantidade_palavras -= 1

    break
 
palavra_sorteada = random.choice(palavras)
palavra_escondida = '-' * len(palavra_sorteada)
letras_adivinhadas = []
max_tentativas = 6

while True:
    print('========================================================================\n')
    print(f'Dica: O tema escolhido foi {tema} e tem {len(palavra_sorteada)} letras.')
    print('\n========================================================================\n')
    print('Palavra')
    print(palavra_escondida)

    letra = input('Digite uma letra: ')

    if letra in letras_adivinhadas:
        print('Você já digitou essa letra. Tente outra por favor')
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_sorteada:
        lista = []

        for indice in range(len(palavra_sorteada)):
            if letra == palavra_sorteada[indice]:
                lista.append(letra)
            else:
                lista.append(palavra_escondida[indice])
        
        palavra_escondida = ''.join(lista)
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas')

    if palavra_escondida == palavra_sorteada:
        print('Parabéns, você ganhou!!')
        break
    elif max_tentativas == 0:
        print(f'Você perdeu. A palavra era {palavra_sorteada}.')
        break
