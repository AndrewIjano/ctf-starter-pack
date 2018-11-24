# picoCTF - 2018: hertz

**Categoria:** Crypto
**Pontos:** 150
**Descrição:**

> Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell2.picoctf.com 14928
>
> Hints:
> NOTE: Flag is not in the usual flag format



## Write-up

Conectando com o endereço do enunciado, recebemos um texto cifrado por cifra de substituição. Usando o site [guballa](https://www.guballa.de/substitution-solver) para decifrar, obtemos o trecho incial do texto na forma:

```
-------------------------------------------------------------------------------
congrats here is your flag - substitution_ciphers_are_solvable_gatmlnvhri
-------------------------------------------------------------------------------
in a village of la mancha, the name of which i have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. an olla of rather more beef than mutton, a salad on most
...
```
**Resposta:** `picoCTF{substitution_ciphers_are_solvable_gatmlnvhri}`.
## Outros Write-ups e arquivos

* Nada ainda
