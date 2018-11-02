# Código ASCII

Nessa seção, vamos apresentar uma das codificações mas famosas para representar texto em um computador: o ASCII.

> O nome ASCII vem do inglês _American Standard Code for Information Interchange_ que significa "Código Padrão Americano para o Intercâmbio de Informação"

O ASCII, originalmente baseado no inglês, codifica 128 caracteres específicos com __7 bits__. Como um computador normalmente trabalha na escala de bytes (8 bits), o ASCII é mais frequentemente encontrado numa representação de __8 bits__.


A tabela abaixo mostra todos os caracteres do código ASCII.

![](ascii-table.png)

Você pode usar essa tabela para decodificar uma sequência de números em binário, decimal ou hexadecimal para ASCII.

## ASCII em Python
Uma maneira mais fácil de manipular a codificação ASCII, em vez de usar manualmente uma tabela, é por meio de códigos. Em Python, usamos as funções `ord()` e `chr()` para isso.

A função `ord()` recebe uma string de tamanho 1 e retorna um inteiro que representa o código da letra, se ela for ASCII, devolverá seu código ASCII. Por exemplo, `ord('a')` devolverá `97`.

Já a função `chr()` é o inverso da anterior. Ela recebe um inteiro e devolve o caractere com o respectivo código ASCII. Por exemplo, `chr(97)` devolverá `'a'`.
## Exercícios

https://www.wechall.net/challenge/training/encodings/ascii/index.php

https://www.wechall.net/challenge/training/encodings/url/index.php

## Referências
[ASCII table](http://www.asciitable.com/)

[Python Built-in Functions](https://docs.python.org/2/library/functions.html)
