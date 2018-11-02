# Guia para CTFs
Este guia destina-se a entusiastas de segurança da informação e que desejam participar de CTFs.

## O que são CTFs?
CTF significa Capture the Flag. No contexto de segurança da informação, são competições que envolvem diversas áreas como descoberta de vulnerabilidades, técnicas de [espionagem](https://en.wikipedia.org/wiki/Tradecraft) e criação de <a href="https://pt.wikipedia.org/wiki/Exploit_(seguran%C3%A7a_de_computadores)"> exploits </a> e ferramentas.

De maneira geral, nessas competições os jogadores são apresentados a problemas, programas com falhas de segurança ou sistemas para serem invadidos. E em cada problema, programa ou sistema, há uma chave secreta ou "flag". Encontrar essa flag é a prova que você resolveu o desafio e enviando no campo especificado faz seu time ganhar pontos.

## Tipos de CTFs

Os CTFs são divididos em dois tipos:

### Attack-defense
Todos os times recebem uma Máquina Virtual com algumas falhas de segurança. O objetivo é capturar as flags através das vulnerabilidades dos outros times e protegendo seu próprio time de invasões corrigindo suas falhas de segurança.

### Jeopardy-sytle
Todos são apresentados a questões de diversas categorias, níveis de dificuldades e pontuações, também chamadas de _challenges_. As categorias variam de competição para competição, as principais são

* __Crypto:__ Envolvem problemas relacionados a [criptografia](https://en.wikipedia.org/wiki/Outline_of_cryptography).

* __Stegano:__ [Esteganografia](https://en.wikipedia.org/wiki/Steganography) é a arte de esconder em plena vista e que envolve basicamente mensagens escondidas em outras mensagens.

* __Forensics:__ É uma área ampla que pode incluir análise de formato de arquivos, [memory dumps](https://pt.wikipedia.org/wiki/Core_dump) e  [pacotes](https://en.wikipedia.org/wiki/Packet_analyzer) e até esteganografia.

* __Reversing:__ São desafios de engenharia reversa. Envolvem encontrar vulnerabilidades de algum programa que você não possui o código.

* __Web Hacking:__  Envolvem atacar vulnerabilidades comuns no ramo de tecnologia web.

* __Programming:__ Testam sua habilidade de criar scripts.

* __Miscellaneous:__ Problemas variados e normalmente com baixa pontuação.

## Quando ocorrem os CTFs?
Esses eventos ocorrem em vários perídos e lugares, sendo organizados por pessoas diferentes. Alguns podem acontecer remotamente (on-line) ou presencialmente (on-site).

Uma ótima plataforma para acompanhar as datas das principais competições é o [CTFtime](https://ctftime.org/event/list/upcoming).

## Como se preparar para CTFs?
O melhor jeito de se preparar para essas competições é praticando.

Abaixo está uma lista de alguns sites com ótimo conteúdo para treinar.

Para auxiliar esse processo, este guia pretende abordar alguns conceitos básicos para resolver esses desafios de forma didática e rápida.

E ainda, uma ótima forma de treinar é observar resoluções (ou _write-ups_) de desafios que você não conseguiu ou quer ver outra resolução dele.  

## Onde treinar?
Alguns dos sites abaixo serão usados como exercício para este guia.

### [WeChall](https://www.wechall.net/)
Plataforma com desafios de diversas áreas e dificuldades.

### [OverTheWire](http://overthewire.org/wargames/)
Site com diversos _wargames_ onde é necessário conectar no respectivo servidor por meio do terminal. O desafio __Bandit__ é muito recomendado para aprender comandos de Linux.

### [picoCTF 2018](https://2018game.picoctf.com/)
A edição 2018 de uma competição muito famosa e voltada para estudantes. Apresenta ótimos desafios introdutórios e de diversas áreas.   

### [Hack The Box](https://www.hackthebox.eu/login)
Plataforma voltada para invasão de máquinas, simula cenários reais de _pentest_. Possui também alguns desafios de várias áreas, como os outros, e é preciso "_hackear_" o site para conseguir o login.
## Referências
[CTF-BR](https://ctf-br.org/)


[OpenCTF](http://openctf.com/faq/)

[Trail of Bits](https://trailofbits.github.io/ctf)

[CTFtime](https://ctftime.org/)
