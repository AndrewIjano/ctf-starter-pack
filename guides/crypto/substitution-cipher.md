# Cifras de Substituição Simples

Agora que você está familiarizado com a [Cifra de César](caeser-cipher.md), vamos apresentar uma generalização desse conceito: as __cifras de substituição simples__.

Em uma cifra de substituição simples, cada letra é substituida individualmente de acordo com um __alfabeto de substituição__. Esse alfabeto pode ser uma rotação fixa do alfabeto normal (como a cifra de César) ou algum embaralhamento mais complexo.

Alguns exemplos notáveis de cifra de substituição simples são:

## Cifra de Atbash
> Seu nome tem origem da primeira, última, segunda e penúltima letra Hebraica (Aleph-Taw-Bet-Shin)

Nessa cifra, cada letra é mapeada para o alfabeto invertido, ou seja, a primeira vira a última, a segunda vira a penúltima e assim por diante.

```
original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
cifra:    Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
```
Assim, se usarmos essa cifra em `may the force be with you`, obteremos:

```
original: M A Y  T H E  F O R C E  B E  W I T H  Y O U
cifrado:  N Z B  G S V  U L I X V  Y V  D R G S  B L F
```

A Cifra de Atbash pode ser interpretada como um caso particular da [Cifra de Affine](https://en.wikipedia.org/wiki/Affine_cipher), uma cifra que usa aritimética modular para encriptar.

## Cifra da Palavra-Chave

A Cifra da Palavra-Chave ou _keyword cipher_ consiste em escolher uma __chave__ e usá-la para decidir como as letras serão susbtituidas.

As palavras repetidas dessa chave serão removidas e a própria chave será o começo do alfabeto a ser mapeado. O resto das letras continuarão em ordem alfabética, tirando as letras já usadas.

Por exemplo, escolhendo a chave `Marvin`, o novo alfabeto terá esse formato

```
original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
cifra:    M A R V I N B C D E F G H J K L O P Q S T U W X Y Z
```
Assim, ao encriptar a mensagem `Arthur Dent`, obteremos:

```
original: A R T H U R  D E N T
cifrado:  M P S C T P  V I J S
```

## Detectando
Como mencionado no guia de [Cifra de César](caesar-cipher.md), uma mensagem encriptada por uma cifra de substituição simples terá uma ditribuição de frequência das letras semelhante ao da língua usada, mas com as letras trocadas.

Essa distribuição de frequência de um texto pode ser identificada através de uma __análise de frequência__.

Nas línguas naturais, algumas letras aparecem mais frequentemente que outras, como uma espécie de digital do idioma. Por exemplo, a letra mais comum na lígua inglesa é o __"e"__, em português é o __"a"__.

Essa análise de frequência pode ser feita simplesmente contando as letras do texto. Existem ferramentas online para isso como o site [dcode](https://www.dcode.fr/frequency-analysis) ou pode ser feito rapidamente com um biblioteca em Python, onde `text` é o texto a ser analisado:

```python
from collections import Counter
Counter(text.upper()).most_common()
```

## Solucionando

O ponto fraco de cifras de substituição simples é que elas são muito suscetíveis à __análises de frequência__.


Assim, se você tiver um texto de tamanho razoável, por volta de 50 caracteres, é possível analisar a frequência com que as letras aparecem e deduzir qual foi o alfabeto de substituição usado.

O site [guaballa](https://www.guballa.de/substitution-solver) é um excelente decodificador de cifras de substituição simples.

## Exercícios
[OverTheWire: Krypton 3](http://overthewire.org/wargames/krypton/krypton3.html)

## Referências
[Cifra de Atbash: Jeremiah's Game](https://publications.mi.byu.edu/fullscreen/?pub=1367&index=3)

[Cifra da Palavra-Chave: GeeksforGeeks](https://www.geeksforgeeks.org/keyword-cipher/)

[Learn Cryptography ](https://learncryptography.com/attack-vectors/frequency-analysis)
