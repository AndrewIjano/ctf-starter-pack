# Hack The Box: Sick Teacher
**Categoria:** Crypto
**Pontos:** 20
**Descrição:**

>Can you break the cipher?
>
>Please submit the flag in lowercase: HTB{lowercase}


## Write-up
Inicialmente, precisamos descobrir que tipo de encriptação foi usada. Como o texto é relativamente grande, talvez seja algo sensível à análise de frequência.

Por isso, fazemos um teste de [análise de frequência](https://ecee.colorado.edu/~mathys/ecen1200/hwcl11/cryptography/decryptSubst1.html) e vemos que a distribuição dos caracteres está de forma muito parecida com o inglês. Uma **cifra de substituição** talvez seja a resposta.

Através do [quipqiup](https://quipqiup.com/), usamos um algoritmo para tentar inferir os possíveis caracteres do texto.

Uma resposta parcial é essa:
```
HISTORY OF HA??THEBO?
HA??THEBO? ?ENT LIVE SO?E TI?E IN ?AY OF 2017. SIN?E THEN, IT HAS ?RO?N
VERY ?UI??LY TO THOUSANDS OF ?E?BERS FRO? ALL OVER THE ?LOBE. THE HALL OF
FA?E LISTS THE TOP 100 USERS IN ORDER OF POINTS. AT THE TI?E OF ?RITIN?,
THE TOP 3 USERS ARE STEFANO118, FILLIPOS AND AH?ED. THERE ARE SO?E
FORU?S, A SHOUTBO? AND A SLA?? ?HANNEL. SLA?? AND SHOUTBO? ARE A?ESO?E,
BUT THE FORU?S NEED SO?E LOVE! I ?ISH ?ORE PEOPLE USED THE?. HOPEFULLY
THIS IS ENOU?H TE?T TO HELP ?ITH YOUR SUBSTITUTION! ?ET ?RA??IN! PS DON'T
FOR?ET TO SUPPORT HA??THEBO? IF YOU ?AN SPARE SO?E ?ONEY. EVERY PENNY
HELPS!

?O?O - ARRE?EL
FLA? LORE?IPSU?DOLORSITA?ET
```  
Vemos que a flag ainda não foi totalemente decriptada, mas podemos dar algumas dicas para o algoritmo ser mais efetivo. Por exemplo, vemos que `KHLTIKWECD=HACKTHEBOX` e `ZGHF=FLAG`.

Com essas dicas temos um texto mais completo:
```
HISTORY OF HACKTHEBOX
HACKTHEBOX ?ENT LIVE SOME TIME IN MAY OF 2017. SINCE THEN, IT HAS GRO?N
VERY ?UICKLY TO THOUSANDS OF MEMBERS FROM ALL OVER THE GLOBE. THE HALL OF
FAME LISTS THE TOP 100 USERS IN ORDER OF POINTS. AT THE TIME OF ?RITING,
THE TOP 3 USERS ARE STEFANO118, FILLIPOS AND AHMED. THERE ARE SOME
FORUMS, A SHOUTBOX AND A SLACK CHANNEL. SLACK AND SHOUTBOX ARE A?ESOME,
BUT THE FORUMS NEED SOME LOVE! I ?ISH MORE PEOPLE USED THEM. HOPEFULLY
THIS IS ENOUGH TEXT TO HELP ?ITH YOUR SUBSTITUTION! GET CRACKIN! PS DON'T
FORGET TO SUPPORT HACKTHEBOX IF YOU CAN SPARE SOME MONEY. EVERY PENNY
HELPS!

XOXO - ARREXEL
FLAG LOREMIPSUMDOLORSITAMET
```

**Resposta:** HTB{loremipsumdolorsitamet}

## Outros Write-ups e arquivos
* Nada ainda
