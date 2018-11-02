# O que é criptografia?

Criptografia vem do grego _kryptós_ e _graphein_, que significam "secreta" e "escrita", respectivamente. Até a era moderna, ela era sinônimo de _encriptação_, que é a conversão de uma mensagem legível para algo aparentemente sem sentido, e é esse o conceito usado em CTFs.

Para entender melhor essa ideia, digamos que _Alice_ quer mandar uma mensagem para _Bob_ sem que uma terceira pessoa, digamos _Eve_, descubra seu counteúdo.

Para isso, _Alice_ usa um certo algoritmo para tornar a mensagem ilegível de forma que só _Bob_ saberá reverter a mensagem encriptada.

![](crypto-introduction.png)

Assim, quando _Eve_ interceptar a mensagem por meio do canal inseguro, se ela não possui o algoritmo criptográfico usado por _Alice_ e _Bob_, ela não será capaz de entender a mensagem.

Ao longo da história, várias técnicas de ocultar mensagens foram desenvolvidas. Antes da criptografia pré-computacional, a __criptografia clássica__ era formada por um conjunto de métodos de _substituição_ e _transpoisção_ de caracteres. E com o advento da computação, a __criptografia moderna__ se tornou amplamente embasada em teorias matemáticas e práticas de ciência da computação.

Para esse guia, começaremos com os métodos da criptografia clássica.
