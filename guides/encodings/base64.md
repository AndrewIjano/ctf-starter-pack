# Base64

Agora que você já teve contato com o código ASCII, vamos conhecer o __Base64__, um método para codificar e decodificar dados binários em caracteres ASCII.

Esse método é utilizado frequentemente para transferir dados em meios que só suportam formatos ASCII, por exemplo, enviar anexos por e-mail (que usa o [MIME](https://pt.wikipedia.org/wiki/MIME)).

O nome base64 origina-se do fato de que esse sistema é constituido de 64 caracteres, representando exatamente 6 bits de dados. Com isso, três bytes de 8 bits podem ser representados por 4 digitos de 6 bits em Base64.

A tabela abaixo mostra a equivalência entre os valores de um conjunto de 6 bits e os caracteres usados para codificação.

<img src="base64-table.png" width="480">

Quando os bits da mensagem original não são multiplos de 6, são adicionados zeros como _padding_. Assim, na mensagem codificada é colocado um `=` para cada dois zeros de _padding_. Aliás, esse `=` é uma forma bem comum de reconhecer um texto codificado em Base64.

Abaixo está um exemplo de um texto codificado em Base64:

```
texto:          M        |        a        |        n
8 bits:  0 1 0 0 1 1 0 1 | 0 1 1 0 0 0 0 1 | 0 1 1 0 1 1 1 0
6 bits:  0 1 0 0 1 1 | 0 1 0 1 1 0 | 0 0 0 1 0 1 | 1 0 1 1 1 0       
Valor:        19     |      22     |      5      |      46
texto:        T      |      W      |      F      |      u
(Base64)
```
E se tirarmos o `n`, a codificação vai necessitar de um _padding_:
```
texto:          M        |        a        |  
8 bits:  0 1 0 0 1 1 0 1 | 0 1 1 0 0 0 0 1 |  
6 bits:  0 1 0 0 1 1 | 0 1 0 1 1 0 | 0 0 0 1 0 0 | 0 0 0 0 0 0      
Valor:        19     |      22     |      5      |  (padding)
texto:        T      |      W      |      E      |      =
(Base64)
```

## Ferramentas

Para manipular textos em Base64, pode-se usar o comando Unix `base64`.

Por exemplo, se tivermos uma arquivo `sagan.txt` com o texto `The Cosmos is all that is or ever was or ever will be`. Podemos convertê-lo para um arquivo `sagan64.txt` com o comando

```bash
base64 sagan.txt > sagan64.txt
```

O resultado será o arquivo `sagan64.txt` com o texto `VGhlIENvc21vcyBpcyBhbGwgdGhhdCBpcyBvciBldmVyIHdhcyBvciBldmVyIHdpbGwgYmUK`.

Agora, para decodificar o arquivo `sagan64.txt`, usamos o mesmo comando com a flag `-d`:

```bash
base64 -d sagan64.txt
```
## Exercícios
[OverTheWire: Krypton 0](http://overthewire.org/wargames/krypton/krypton0.html)

[Decodifique essa mensagem](../../challenges/training/encodings/base64.md)
