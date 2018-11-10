# Hack The Box: You Can Do It!
**Categoria:** Crypto
**Pontos:** 10
**Descrição:**

> The flag is in the format HTB{plaintext}

## Write-up
Inicialmente, não temos muita informação sobre a cifra usada. A primeira tentativa foi um brute-force de cifra de césar, mas não ouve resultado. Como o texto dado é muito pequeno, qualquer cifra de substituição que exija uma análise de frequência já pode ser descartada.

Em seguida, o próximo chute foi alguma **cifra de tranposição**. Assim, temos que induzir um tipo de tranposição usada.

Analisando o texto, podemos enxergar a palavra `YOU`:

```
YhaOanUtdsYoeOieUttc!
```

E essas letras aparecem num mesmo padrão: um conjunto de 3 caracteres. Assim, podemos dividir o texto nesse conjunto:

```
YHA
OAN
UTD
SYO
EOI
EUT
TC!
```
Lendo as colunas, obtemos `YOUSEETHATYOUCANDOIT!`.


**Resposta:** HTB{YOUSEETHATYOUCANDOIT!}

## Outros Write-ups e arquivos
* Nada ainda
