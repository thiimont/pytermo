import random
import re
import unicodedata

import requests

modo_online = False

try:
    r = requests.get("https://api.dicionario-aberto.net/wotd")
    r.raise_for_status()
    modo_online = True
    print(
        "AVISO: O modo online está ativado. Isso significa que as palavras digitadas serão verificadas. Pode conter algumas falhas."
    )
    print(
        "As palavras digitadas no modo online precisam de acentuação, caso contrário serão dadas como inválidas."
    )
except (requests.exceptions.RequestException, requests.exceptions.ConnectionError) as e:
    print(f"{e}")
    print(f"ERRO: Erro ao ativar o modo online.")


def verificar_palavra(palavra):
    global modo_online
    if modo_online:
        try:
            v = requests.get(f"https://api.dicionario-aberto.net/word/{palavra}")
            v.raise_for_status()
            if "word" in v.json()[0]:
                return True
            else:
                return False

        except IndexError:
            return False

        except (
            requests.exceptions.RequestException,
            requests.exceptions.ConnectionError,
        ) as e:
            modo_online = False
            print(f"{e}")
            print(
                f"ERRO: Erro ao verificar a palavra. A palavra será considerada como correta e o jogo continuará sem verificação online."
            )
            return True
    else:
        return True


try:
    with open("palavras.txt", "r") as file:
        palavras = file.read().split()
except IOError as e:
    print(f"ERRO: Erro na leitura da lista de palavras: {e}")
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
    palavra_input_string = palavra_input
    palavra_input = list(re.sub(r"[^a-zA-Záàãâéèêíìóòõôúüç]", "", palavra_input))

    if len(palavra_input) != 5:
        print(
            "A palavra deve ter 5 letras (não são permitidos símbolos e números). Tente novamente."
        )
        continue
    else:
        print(f"Você escreveu: {palavra_input}")

    if verificar_palavra(palavra_input_string):
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
                print(f"Letra incorreta: {palavra_input[i]} ({i+1})")

        contador_tentativas -= 1

    else:
        print("Palavra inválida!")
        continue

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

    if contador_tentativas == 0:
        print("Infelizmente você zerou o número de tentativas :(")
        print(f"Resultado final: {palavra_estado_atual}")
        print(f"A palavra correta era: {palavra_sorteada}")
        break
