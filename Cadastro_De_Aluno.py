#               ⬐ Nome de exemplo ⬎ 
print("\n Instituto Xavier para Estudos Avançados \n")

lista_alunos = {}

while True:
 print("-----> Inicio <-----")
 print("")
 print(" 1. Adicionar aluno(a)\n 2. Listar todos os alunos(as)\n 3. Buscar aluno(a) pelo nome\n 4. Remover aluno\n 5. Mostrar média dos alunos(as)\n 6. Sair")
 print("")
 escolha = int(input("Digite o número de acordo com as opções dadas: "))
 print("")

 if escolha == 1:
     print("---> Adição de alunos <---")
     print("")
     nome = (input("Digite o nome do aluno(a): ")).title()
     print("")
     idade = int(input("Digite a idade do aluno(a): "))
     print("")
     poder = input("Digite a nota do aluno(a): ").title()
     print("")
     nota = int(input("Digite o nível de perigo de 0 a 10: "))    
     print("") 

     novo = { "Idade": int(idade), "Nota": (poder), "Nível": int(nota) }      

     lista_alunos[nome] = novo

 elif escolha == 2:
     print("---> Lista de todos os alunos <---")
     print("")
     if lista_alunos == {}:
         print("A lista está vazia!")
         print("")
     else:
         print(lista_alunos)
         print("")

 elif escolha == 3:
     print("---> Buscar aluno pelo nome <---")
     print("")
     busca = input("Digite o nome do aluno: ").title()
     print("")
     if lista_alunos == {}:
         print("A lista está vazia!")
         print("")
     elif busca in lista_alunos:
         print(f"O aluno {busca} está na lista!")
         print("")
         print(lista_alunos.get(busca))
         print("")
     else:
         print("Nenhum aluno com este nome encontrado!")
         print("")

 elif escolha == 4:
     print("---> Remoção de alunos <---")
     print("")
     tirar = input("Digite o nome do aluno: ").title()
     print("")
     if lista_alunos == {}:
         print("A lista está vazia!")
         print("")
     elif tirar in lista_alunos:
         lista_alunos.pop(tirar)
         print("Aluno removido da lista!")
         print("")
     else:
         print("Nenhum aluno com este nome encontrado!")
         print("")
         
 elif escolha == 5:
     print("---> Média geral da nota dos alunos(as) <---")
     print("")
     if len(lista_alunos) == 0:
         print("A lista está vazia!")
         print("")  
     else:
        media = 0
        for Nota in lista_alunos.values():
           media += Nota["Nível"]
     soma = media / len(lista_alunos)
     print(f"A média dos alunos(as) é: {soma:.2f}")
     print("")
    
 elif escolha == 6:
     print("=====Saida=====")
     break