# Hack The Box: Hackerman
**Categoria:** Stegano
**Pontos:** 20
**Descrição:**

>There should be something hidden inside this photo... Can you find out?

## Write-up
Inicialmente, fizemos testes com os programas `foremost` e `steganabara`. Nenhum deles acusou algo escondido.

Uma segunda tentativa foi usar o comando

```
strings hackerman.jpg
```

Com isso, encontramos dois trechos suspeitos:
```
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
	#3R
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
```
```
5634275d694f8665957746c9619132f0
```
Ao pesquisar o segundo trecho no Google, vemos que se trata do Hash MD5. Que nos dá a palavra `almost`.

Pesquisando sobre o primeiro trecho, vemos que se trata de um header de um arquivo escondido pelo `steghide`.

Assim, usando esse programa para encontrar o arquivo escondido, colocamos a senha `almost` e conseguimos extrair o arquivo `hackerman.txt`.

Dentro do arquivo, encontramos o texto `SFRCezN2MWxfYzBycH0=`, que está codificado em **base64**. Assim, com o comando

```
base64 -d hackerman.txt
```

obtemos a flag.

**Resposta:** HTB{3v1l_c0rp}

## Outros Write-ups e arquivos
* Nada ainda
