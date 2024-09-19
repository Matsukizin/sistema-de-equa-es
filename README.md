# README do Projeto: Calculadora de Sistemas de Equações

## O que é?

Esse projeto é uma calculadora que resolve sistemas de equações lineares. Com ele, você pode descobrir os valores de x e y a partir de duas equações. A interface foi feita usando a biblioteca **PySimpleGUI**, que deixa tudo bem simples e fácil de usar.

## Como funciona?

### 1. Importação da Biblioteca

```python
import PySimpleGUI as sg
```
Aqui, estamos importando a biblioteca que nos ajuda a criar a interface gráfica.

### 2. A Classe `SistemaEquacoes`

A classe `SistemaEquacoes` é onde a mágica acontece!

#### 2.1 Método `__init__`

Neste método, configuramos a janela que aparece na tela:

```python
self.layout = [
    sg.theme('Reddit')
    [sg.Text('Primeira Equação:')],
    ...
]
```
Você pode inserir os números que representam as equações da seguinte forma:

Primeira Equação: ax + by = c  
Segunda Equação: dx + ey = f  

#### 2.2 Método `calcular_resultado`

Esse método faz os cálculos. Usamos as fórmulas:

- Para encontrar x:
  
  x = (c vezes e) menos (b vezes f) dividido por (a vezes e) menos (b vezes d)

- Para encontrar y:
  
  y = (c menos (a vezes x)) dividido por b

Se acontecer um erro, como dividir por zero, o programa trata isso para não travar.

#### 2.3 Método `run`

Esse método mantém a aplicação funcionando. Ele escuta o que o usuário faz na tela:

- Quando você clica em "Calcular", ele pega os números, faz os cálculos e mostra o resultado.
- Se você inserir algo errado, uma mensagem de erro aparece.

### 3. Execução do Programa

A aplicação começa aqui:

```python
if __name__ == '__main__':
    app = SistemaEquacoes()
    app.run()
```

## Como usar?

1. Execute o script Python.
2. Preencha os campos com os números das equações.
3. Clique em "Calcular" para ver os resultados de x e y.
4. Se houver algum erro, uma mensagem vai te avisar.

## Considerações Finais

Essa calculadora é um teste, provavelmente não será atualizada e foi feita apenas para aprendizado. Se quiser usá-la, pode usar :].

## Equação usada explicada melhor

### Cálculo de x

Para encontrar x, usamos a fórmula:

1. Primeiro, pegamos o valor de c (8) e multiplicamos pelo valor de e (1). Isso nos dá 8 vezes 1 igual a 8.
2. Depois, pegamos o valor de b (3) e multiplicamos pelo valor de f (5). Isso nos dá 3 vezes 5 igual a 15.
3. Em seguida, subtraímos o segundo resultado do primeiro: 8 menos 15 igual a -7.
4. Agora, para o denominador, pegamos a (2) e multiplicamos por e (1), que resulta em 2 vezes 1 igual a 2.
5. Em seguida, pegamos b (3) e multiplicamos por d (4), que nos dá 3 vezes 4 igual a 12.
6. Agora, subtraímos 12 de 2: 2 menos 12 igual a -10.
7. Finalmente, dividimos o resultado da subtração do numerador pelo resultado do denominador: -7 dividido por -10 é igual a 0,7.

### Cálculo de y

Agora que temos x, vamos calcular y:

1. Usamos a fórmula para y e começamos pegando c (8).
2. Depois, multiplicamos a (2) pelo valor de x que encontramos (0,7). Isso resulta em 2 vezes 0,7 igual a 1,4.
3. Subtraímos esse resultado de 8: 8 menos 1,4 igual a 6,6.
4. Finalmente, dividimos 6,6 pelo valor de b (3): 6,6 dividido por 3 é igual a 2,2.

### Resultados

Assim, os valores encontrados são:
- x é aproximadamente 0,7
- y é aproximadamente 2,2
