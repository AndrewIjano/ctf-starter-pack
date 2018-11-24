# picoCTF - 2018: Crypto Warmup 1

**Categoria:** Crypto
**Pontos:** 75
**Descrição:**

> Crpyto can often be done by hand, here's a message you got from a friend, llkjmlmpadkkc with the key of thisisalilkey. Can you use this table to solve it?
>
> Hints:
>
> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
>
> Please use all caps for the message.

## Write-up

Vemos que a tabela usada é exatamente a tabela de substituição da cifra de Vigenère. Com um decifrador como [dcode](https://www.dcode.fr/vigenere-cipher) usando a chave dada, encontramos a flag.

**Resposta:** `picoCTF{SECRETMESSAGE}`.
## Outros Write-ups e arquivos

* Nada ainda
