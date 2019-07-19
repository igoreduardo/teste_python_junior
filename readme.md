# Teste de Programação (Júnior)

Esse é um teste para avaliar conceitos básicos de programação.

Realize um fork desse repositório, resolva os três testes abaixo e depois nos encaminhe o link do respositório com as respostas.

Os exercícios devem ser resolvidos utilizando-se python 3.7

Pedimos que o nome dos scripts obedeça ao seguinte padrão: teste_{id_problema}.py

https://www.urionlinejudge.com.br/judge/pt/problems/view/1015  
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020  
https://www.urionlinejudge.com.br/judge/pt/problems/view/1016  


É possível passar uma entrada para um programa usando o sinal de '<' (menor que). Então o seu script deve ser capaz de ler linhas de um arquivo de entrada utilizando o comando input.

Ex:

`a = input()`

A saída de se programa deve concidir com aquilo que está disposto no exercício. Para produzir uma saída utilize o comando print.

Ex:

`print('a={}'.format(a))`


## Exemplo de resolução

Tomamos como exemplo o exercício que está descrito abaixo.

O Mesmo pode ser melhor visualizado no seguinte link:
[1002 - Área do Círculo - URI Online Judge](https://www.urionlinejudge.com.br/judge/pt/problems/view/1002)

---
### Área do Círculo

A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

#### Entrada

A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

#### Saída
Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

|Exemplos de Entrada   |Exemplos de Saída   |
|---|---|
|2.00|A=12.5664|
| 100.64|A=31819.3103|
| 150.00|A=70685.7750|
---

### Resolução
<code> #!/usr/bin/env python </code>  
<code>  # -*- coding: utf-8 -*- </code>  
<code>
a = float(input())  
r = (a**2) * 3.14159  
print('A={0:.4f}'.format(r))  
</code>

Tendo em vista o padrão de nomenclatura que deve ser usado para nomear os arquivos, iremos testar os scripts da seguintes maneira:

`python teste_1002.py < arquivo_entrada > arquivo_saida`

o seu programa deve produzir um arquivo de saída identico ao esperado no problema
