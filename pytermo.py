import random
import re
import unicodedata

try:
    with open("palavras.txt", "r") as file:
        palavras = file.read().split()
except IOError as e:
    print(f"Erro na leitura da lista de palavras: {e}")
    exit()

palavra_estado_atual = list("_____")
contador_tentativas = 5

palavra_sorteada = random.choice(palavras)

# Remoção dos acentos da palavra sorteada
palavra_sorteada_sem_acento = "".join(
    [
        c
        for c in unicodedata.normalize("NFKD", palavra_sorteada)
        if not unicodedata.combining(c)
    ]
)

palavra_sorteada = list(palavra_sorteada)
palavra_sorteada_sem_acento = list(palavra_sorteada_sem_acento)

print(
    "Bem-vindo ao Pytermo! Você deve adivinhar a palavra de 5 letras em no máximo 5 tentativas.\nDesenvolvido com ♥ por thiimont"
)
while True:
    print("------------------------------")
    # Tire o comentário da linha abaixo para ter a palavra correta logo de início
    # print(f"A palavra da vez é: {palavra_sorteada}")
    print(palavra_estado_atual)
    print(f"Tentativas restantes: {contador_tentativas}")
    palavra_input = input("Digite uma palavra: ").lower()
    palavra_input = list(re.sub(r"[^a-zA-Záàãâéèêíìóòõôúüç]", "", palavra_input))

    if len(palavra_input) != 5:
        print(
            "A palavra deve ter 5 letras (não são permitidos símbolos e números). Tente novamente."
        )
        continue
    else:
        print(f"Você escreveu: {palavra_input}")

    for i in range(len(palavra_input)):
        if (
            palavra_input[i] == palavra_sorteada[i]
            or palavra_input[i] == palavra_sorteada_sem_acento[i]
        ):
            print(f"Letra e posição corretas: {palavra_input[i]} ({i+1})")
            palavra_estado_atual[i] = palavra_input[i]

        elif (
            palavra_input[i] in palavra_sorteada
            or palavra_input[i] in palavra_sorteada_sem_acento
        ):
            print(f"Letra correta, mas posição errada: {palavra_input[i]} ({i+1})")

        else:
            print(f"Essa letra não está na palavra: {palavra_input[i]} ({i+1})")

    if (
        palavra_estado_atual == palavra_sorteada
        or palavra_estado_atual == palavra_sorteada_sem_acento
    ):
        print(f"Parabéns, você adivinhou a palavra: {palavra_sorteada}!")
        if (5 - contador_tentativas) >= 0:
            print(
                f"Você adivinhou a palavra em {5 - contador_tentativas} tentativa(s)!"
            )
        break

    contador_tentativas -= 1

    if contador_tentativas == 0:
        print("Infelizmente você zerou o número de tentativas :(")
        print(f"Resultado final: {palavra_estado_atual}")
        print(f"A palavra correta era: {palavra_sorteada}")
        break
