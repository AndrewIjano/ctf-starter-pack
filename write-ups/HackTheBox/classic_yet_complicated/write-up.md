# Hack The Box: Classic, yet complicated!
**Categoria:** Crypto
**Pontos:** 10
**Descrição:**

> Find the plaintext, the key is your flag!
>
> Flag format : HTB{key in lowercase}
>

## Write-up
Pelo título, podemos inferir que a criptografia usada seja algo simples e bem conhecida.

Através de uma [análise de frequência](https://ecee.colorado.edu/~mathys/ecen1200/hwcl11/cryptography/decryptSubst1.html), vemos que não foi usada uma cifra de substituição mono-alfabética (pois as letras não possuem distribuições parecidas com o inglês). Um possível chute foi a **cifra de vigenere**.

Através do [dcode](https://www.dcode.fr/vigenere-cipher), testei se ele conseguia induzir uma possível _key_. Usando a opção de análise estatística, recebemos como melhor resposta o texto:

```
THEVIVENRRECIPHTRWNSINVENIEDOYAFRENRHMNNBLAISTDEIIGENERTINGHETHCECTUEYITIS
AEOLLALPHABTTIPCIPHERQECNUSEITUHESGWOORMOGECVPHERALEHAOETSTOECCRLPTTHEDPTA
VNOTHERLORQSTHELEITEESINTHEKIGRNERECIEHEEARESHIUTEQBYDIFFTREATAMOUNISNBRMA
LLYSONRUSINGALORQORPHRAHEAFT
```  

Com a _key_ `HELLOHORYD`.

Como o texto e a _key_ estão bem próximos de algo legível e conhecido, podemos inferir uma _key_ `HELLOWORLD`. Assim, decriptando no mesmo site usando essa nove _key_ obtemos

```
the vigenere cipher, was invented by a frenchman, blaise de vigenere in
 the 16th century. it is a polyalphabetic cipher because it uses two or
 more cipher alphabets to encrypt the data. in other words, the letters
 in the vigenere cipher are shifted by different amounts, normally done
 using a word or phrase as the encryption key . unlike the monoalphabetic
 ciphers, polyalphabetic ciphers are not susceptible to frequency
 analysis, as more than one letter in the plaintext can be represented by
 a single letter in the encryption. the key is the flag.
```

Logo, a _key_ é a resposta.

**Resposta:** HTB{helloworld}

## Outros Write-ups e arquivos
* Nada ainda
