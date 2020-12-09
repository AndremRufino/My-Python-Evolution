def media(altura,idade):  
    media = sum(altura)/5
    totalAlunos = 0
    for i in range(0,5):
        if idade[i] >= 18 and altura[i] < media:
            totalAlunos += 1

    return print("\nA média de altura é : ",media,"\nA quantidade de alunos que tem mais de 18 anos e são menores que a média é : ",totalAlunos)

altura =[]
idade = []
for i in range(0,5):
    alt = float(input("Digite a altura do aluno : "))
    ida = int(input("Digite a idade do aluno : ")) 
    print('\n')
    altura.append(alt)
    idade.append(ida)

media(altura,idad