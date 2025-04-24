# 🐍📚 Pytermo - Uma pequena e simples recriação em Python do famoso jogo de navegador "Termo"

Esse é o meu **primeríssimo projeto (de muitos!) em Python**, mas tentei ao máximo seguir boas práticas e deixar a experiência agradável. Talvez eu aprimore esse projeto no futuro.

Existem dois arquivos (duas versões) do jogo, o **pytermo** e o **pytermo-online**.

Jogo original (que é uma adaptação brasileira do Wordle): <a href="https://term.ooo/">Termo</a>

---

## Lógica do jogo
- Assim como no jogo original, você deve tentar adivinhar a palavra de 5 letras, com apenas 5 tentativas;
- A cada tentativa, o jogo te dará feedback de quais letras estão corretas, parcialmente corretas *(estão na palavra, mas na posição errada)* ou incorretas *(não estão na palavra)*;
- Você vence o jogo quando adivinhar a palavra antes das tentativas se esgotarem.

## Como adicionar palavras ao jogo
- É só adicionar palavras com 5 caracteres ao arquivo "palavras.txt" *(separadas por quebra de linha, para evitar problemas)*.
- Caso o arquivo "palavras.txt" esteja completamente vazio ou não exista, o programa irá retornar um erro.
- O arquivo já vem com algumas palavras, caso queira testar sem se preocupar em adicionar palavras.

## Diferença do pytermo para o pytermo-online
- No pytermo, **as palavras não são checadas para ver se elas existem de fato.** No pytermo-online, é utilizada a API do <a href="https://api.dicionario-aberto.net/index.html">Dicionário Aberto</a> para a verificação das palavras.
- O pytermo-online detecta automaticamente se o usuário possui conexão a internet (ou se a API está online) ao abrir o jogo. Caso não possua, o modo online é desativado e o jogo vai agir igualzinho ao pytermo padrão.
- Caso a internet caia no meio do jogo, o modo online também será desativado e prosseguirá sem nenhuma verificação (nem mesmo se a internet voltar).

## Bibliotecas utilizadas
- random *(sortear uma palavra da lista)*
- re *(tratar dos inputs, impedindo o uso de símbolos, números que fogem do padrão)*
- unicodedata *(usada para remover a acentuação da palavra sorteada, garantindo que não haja diferenças na hora de comparar inputs com ou sem acentuação)*
- requests **(somente usada no pytermo-online)** *(para verificar se a palavra digitada é válida por meio de uma API)*

