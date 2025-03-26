quantidade = 3
soma = 0

for i in range(quantidade):
    nota = float(input("Digite sua nota:"))
    soma += nota
    media = soma / 3
      
    if media > 7:
        print("Aluno aprovado.")
    elif media < 6 and media > 5:
        print("Recuperação")
    else:
        print("Reprovado")

    print(media)
