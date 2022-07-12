# calculadora_python
<sub>*Trabalho realizado por João Marcelo, em 07/2022, para o laboratório do curso de Python, da datascienceacademy. </sub>
# Objetivo

O objetivo deste pequeno projeto é desenvolver uma calculadora em python, para fins de estudo de aplicação de alguns métodos e estruturas básicos da linguagem. Embora seja um projeto bastante simples, algumas funcionalidades apresentadas são de grande importância, e são utilizadas em códigos mais complexos e robustos.

# Sobre a calculadora
A calculadora apresenta apenas quatro funções (adição, subtração, multiplicação e divisão) que são aplicadas a dois números passados pelo usuário, por parâmetro.

# Métodos e estruturas estudados
* **Estrutura de repetição while** Em nossa calculadora utilizamos a estrutura de repetição while de duas maneiras. Primeiramente, colocamos todo o nosso código dentro de um while True. Dessa forma todo nosso código é executado no loop, até que o usuário informe que não deseja continuar com o programa. Ao informar que não deseja utilizar a calculadora novamente, utilizamos o break para interromper a repetição. Também utilizamos o while para que o usuário escolha apenas as opções disponibilizadas pelo programa. Caso seja inserido um opção inválida, o programa irá comunicar o usuário e solicitar o input novamente.

* **Método sleep()** Importado da biblioteca time, o método sleep permite que seja criado um pequeno intervalo em segundos, a ser definido por parâmetro, simulando um tempo de processamento no nosso programa.

* **Método upper().strip() e slicing** Em Python, upper()  é um método embutido, built in, utilizado para manipulação de strings, que retorna uma cópia da string com as letras minúsculas convertidas em maiúsculas. O método strip() elimina os caracteres vazio no início e no final da string. Esses dois métodos, juntamente com o índice que passamos, permitem que o programa reconheça, apenas a primeira letra da resposta passada pelo usuário por parâmetro.
