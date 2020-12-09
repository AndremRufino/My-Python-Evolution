

def ValorSalario(nome,qtdFilhos,salario):
    print(salario)
    print(qtdFilhos)
    if qtdFilhos == 0:
        salarioF = salario + ((salario * 5)/100)    
    elif qtdFilhos == 1:
        salarioF = salario + ((salario * 10)/100)
    elif qtdFilhos >= 2:
        salarioF = salario + ((salario * 15)/100)

    print('O funcionário ',nome,'\nPossui : ',qtdFilhos,'Filhos \nTem o salário de :',salario,'\nTerá um aumento, sendo o salário final : ',salarioF )
    

 

name = input('Digite o nome do funcionário : ')
qtdFilhos = int(input("Digite a quantidade de filhos que o funcionário tem : "))
salario = int(input("Digite o valor do salário do funcionário : "))

if qtdFilhos < 0:
    qtdFilhos = 0

if salario < 0:
    while salario < 0:
        print("Valor inválido. Tente novamente!")
        salario = int(input("Digite o valor do salário do funcionário : "))



ValorSalario(name,qtdFilhos,salario)
