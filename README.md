## Sistema de gerenciamento de alunos em Python

O código apresenta um sistema de gerenciamento de alunos desenvolvido em **Python**. Ele permite adicionar, listar, buscar e remover alunos, além de calcular a média das notas cadastradas. As informações são armazenadas em um dicionário chamado `lista_alunos`.

A função `print()` é utilizada para exibir o nome da instituição, as opções do menu, os dados cadastrados e as mensagens do sistema. Já a função `input()` recebe as informações digitadas pelo usuário, como nome, idade e nota do aluno.

As funções `int()` e `len()` também são utilizadas. A função `int()` converte os valores digitados para números inteiros, enquanto `len()` retorna a quantidade de alunos cadastrados no dicionário.

O método `title()` formata os nomes digitados, deixando a primeira letra de cada palavra em maiúscula. Isso facilita a busca dos alunos e mantém os nomes armazenados de forma padronizada.

O método `get()` é usado para consultar e apresentar os dados de um aluno específico:

`lista_alunos.get(busca)`

O método `pop()` é utilizado para remover um aluno do dicionário por meio do nome informado:

`lista_alunos.pop(tirar)`

O método `values()` retorna somente os valores armazenados no dicionário. No código, ele é utilizado para percorrer os dados dos alunos e somar suas notas:

`lista_alunos.values()`

O sistema utiliza um laço `while True` para manter o menu funcionando continuamente. O programa permanece em execução até que o usuário escolha a opção de saída. Quando isso acontece, o comando `break` encerra o laço.

As estruturas condicionais `if`, `elif` e `else` verificam qual opção foi escolhida e controlam as operações do sistema. Elas também verificam se o dicionário está vazio, se o aluno pesquisado existe ou se ele pode ser removido.

O laço `for` percorre os valores armazenados no dicionário para realizar o cálculo da média. A nota de cada aluno é adicionada à variável `media` e, depois, o resultado é dividido pela quantidade de alunos cadastrados.

Também são utilizadas f-strings para inserir variáveis dentro das mensagens. Na apresentação da média, a formatação `.2f` mostra o resultado com duas casas decimais:

`print(f"A média dos alunos(as) é: {soma:.2f}")`

Portanto, os principais métodos e funções utilizados no código foram:

- `print()`: exibe informações na tela;
- `input()`: recebe informações digitadas pelo usuário;
- `int()`: converte valores para números inteiros;
- `len()`: retorna a quantidade de elementos do dicionário;
- `title()`: padroniza os nomes com iniciais maiúsculas;
- `get()`: consulta os dados de um aluno;
- `pop()`: remove um aluno do dicionário;
- `values()`: retorna os valores armazenados no dicionário;
- `break`: encerra o laço principal do programa.

Além desses recursos, o código utiliza dicionários, laços de repetição, estruturas condicionais, operadores de soma e divisão e formatação de números decimais. Com isso, o sistema consegue cadastrar e gerenciar informações dos alunos de maneira simples.
