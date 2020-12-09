from iqoptionapi.stable_api import IQ_Option #API 
import sys, time #Bibliotecas para encerrar caso necessário e para pegar o tempo 
from datetime import datetime , date #Importa data e tempo 
from math import floor #Permite arrededondar os números 

dados = IQ_Option('hybridtraderss@gmail.com', 'A7Kmx1q2w3e') #Digite o Login e a Senha da plataforma IQ.Option - Respectivamente
dados.connect() #Realiza conexão com a plataforma 
    
timez = int(time.time()) #Recebe o TEMPO ATUAL em segundos inteiros
datad = datetime.now() #Dados da data atual : Só é usado para usar o ano atual já que só é pedido o dia e o mês 
data = str(datetime.fromtimestamp(timez).strftime('%Y-%m-%d %H:%M:%S')) #Transforma o time.time() em datetime, só é usado lá em baixo p\ subtrair os dias
dataInp = str(input('Digite a data : (dia-mês), respectivamente : ')) #Pega os dados da DATA DO TESTE 
dia = str(dataInp[0] + dataInp[1]) #Recebe os valores do DIA 
mes = str(dataInp[3] + dataInp[4]) #Recebe os valores de MES 

#Provavelmente nao fará diferença de tirar pois o isoweekday nao suporta dias 
if int(dia) > 31:#: #Confere se o valor DIA é valido 
    while int(dia) > 31: #Caso o valor seja inválido :
        print('\n','Valor inválido. Digite novamente :')
        dataInp = str(input(' Digite a data : (dia-mês), respectivamente : ')) #Pede novamente o valor até que o mesmo seja válido
        dia = str(dataInp[0] + dataInp[1]) #Pega os valores do DIA 
        dataFinal = str(dataInp[0]+dataInp[1]+'-'+dataInp[3]+dataInp[4]) #Organiza a data 
if int(mes) > 12 :# Confere se o valor MÊS é válido
    while int(mes) > 12:
        print('\n','Valor invalido. Digite novamente :')
        dataInp = str(input(' Digite a data : (dia-mês), respectivamente : ')) #Pede novamente o valor até que o mesmo seja válido
        mes = str(dataInp[3] + dataInp[4])
        dataFinal = str(dataInp[0]+dataInp[1]+'-'+dataInp[3]+dataInp[4])
if len(dataInp) > 5 or len(dataInp) < 5: #Confere que o tamanho do vetor(string) é correto
    while len(dataInp) > 5 or len(dataInp) < 5:
        print('\n'+'Valores inválidos. Digite novamente :')
        dataInp = str(input(' Digite a data : (dia-mês), respectivamente : '))

dateIn = date(year = int(str(datad.year)) , month = int(str(dataInp[3] + dataInp[4])), day = int(str(dataInp[0] + dataInp[1]))) #Esse formato eu vou usar para retornar o dia da semana que é 
diaweek = dateIn.isoweekday()
diaescrito = 'Sabado' if diaweek == 6 else 'domingo'
print('O DIA DA SEMANA É : ', diaweek)
if diaweek == 6 or diaweek == 7: #Não deixa catalogar fim de semana
    while diaweek == 6 or diaweek == 7: 
        print('\n'+'Valores inválidos. Digite novamente :')
        dataInp = str(input('Digite a data : (dia-mês), respectivamente : ')) #Pega os dados da DATA DO TESTE 
        dateIn = date(year = int(str(datad.year)) , month = int(str(dataInp[3] + dataInp[4])), day = int(str(dataInp[0] + dataInp[1]))) #Esse formato eu vou usar para retornar o dia da semana que é 
        diaweek = dateIn.isoweekday()
        diaescrito = 'Sabado' if diaweek == 6 else 'Domingo'
        print('O DIA DA SEMANA É : ', diaweek,'',diaescrito)


dataFinal = str(str(datad.year)+'-'+(dataInp[3]+dataInp[4])+'-'+str(dataInp[0]+dataInp[1])) #Organiza o Dia desejado no formato y-m-d
dateF = datetime.strptime(dataFinal, '%Y-%m-%d') # Deixa no formato datetime especificado 
date1 = datetime.strptime(data ,'%Y-%m-%d %H:%M:%S') # Deixa no formato datetime especificado
dias = str((date1 - dateF)) #Realiza a subtração dos dias
tot = int(dias[0] + dias[1]) #Transforma a quantidade de dias em INT e positivo
print('Diferença de dias = ', tot)
times = int(time.time()) - (tot * 86400) #Encontra o dia certo ao subtrair o tempo em time()
Dtime = floor(times / 300) #Divide o número por 300 e pega arredonda para a vela mais próxima 
Ftime = (Dtime * 300) #Calcula o TEMPO ARREDONDADO para a vela mais próxima
print('tempo de depois',times)
timezz = datetime.fromtimestamp(Ftime).strftime('%Y-%m-%d %H:%M:%S') #FORMATA O TEMPO ARREDONDADO 
subTatual = str(timezz) #Recebe o time no formato de minutos p\ subtrair novamente o tempo e deixar como 00:00 do dia que precisa do resultado
subT = subTatual[11]+subTatual[12]+subTatual[13]+subTatual[14]+subTatual[15]+subTatual[16]+subTatual[17]+subTatual[18]#Recebe somente o resultado do tempo em string 
print('subtatual = ',subTatual[11]+subTatual[12]+subTatual[13]+subTatual[14]+subTatual[15]+subTatual[16]+subTatual[17]+subTatual[18])
h = str(subTatual[11]+subTatual[12])
m = str(subTatual[14]+subTatual[15])
s = str(subTatual[17]+subTatual[18])
tempoF = (((int(h) * 3600)) + (int(m) * 60) + int(s)) #Transforma em segundos a quantidade de tempo que já passou hj, para a catalogação começar 00:00
Ftime = Ftime - tempoF
timezz = datetime.fromtimestamp(Ftime).strftime('%Y-%m-%d %H:%M:%S')
print('HORARIO DO DIA JÁ ARREDONDADO : ',timezz)

print('\n')


qtdDias = int(input('Quantos dias você deseja análisar ? : ')) #Pega a quantidade de dias para serem análisados 
if qtdDias < 1:
    while qtdDias < 1:
        qtdDias = int(input('Quantos dias você deseja análisar ? : ')) #Pega a quantidade de dias para serem análisados
minpct = int(input('Digite a porcentagem minima de acerto : '))
if minpct < 60:
    while minpct < 60:
        print('Porcentagem muito pequena , tente novamente : ')
        minpct = int(input('Digite a porcentagem minima de acerto : '))

inicio = int(input('Digite o Horário de inicio (EM HORAS SOMENTE): '))
Final = int(input('Digite o horário de finálização (EM HORAS SOMENTE) : '))
if (inicio < 0) or inicio > (23):
    print('Dados inválidos, tente novamente :')
    Inicio = int(input('Digite o Horário de inicio (EM HORAS SOMENTE): '))
    Final = int(input('Digite o horário de finálização (EM HORAS SOMENTE) : '))
if (Final < 0) or Final > (23):
    print('Dados inválidos, tente novamente :')
    Inicio = int(input('Digite o Horário de inicio (EM HORAS SOMENTE): '))
    Final = int(input('Digite o horário de finálização (EM HORAS SOMENTE) : '))

horario = Ftime #É tempo 
DiasT = [] #Vetor onde serão armazenadas as informações de HORARIO, ou seja todos os horarios de velas desejadas
ContCall = [[],[],[],[],[],[],[],[],[],[],[]] #Matriz que vai contar quantas velas foram CALL de todos os ativos
ContPut = [[],[],[],[],[],[],[],[],[],[],[]]  #Matriz que vai contar quantas velas foram PUT
ContDoji = [[],[],[],[],[],[],[],[],[],[],[]] #Matriz que vai contar quantas velas foram DOJI
resultado = [[],[],[],[],[],[],[],[],[],[],[]] # Vai ser usado para registrar as entradas e verificar o resultado  
contador_ = 0
for i in range() 288: #Dá tamanho aos Arrays 
    DiasT.append(0)
    for z in range(10):
        ContCall[z].append(0) #Adiciona elementos na matriz Call
        ContPut[z].append(0) #Adiciona elementos na matriz Put
        ContDoji[z].append(0) #Adiciona elementos na matriz Doji
   

def tendencia(paridade , time__, timeframe):
    candles = dados.get_candles(paridade, (timeframe * 60), 20, time__)
    ultimo = round(candles[0]['close'], 4)
    primeiro = round(candles[-1]['open'], 4)
    
    diferenca = abs( round( ( (ultimo - primeiro) / primeiro ) * 100, 3) )
    tendencia = "CALL" if ultimo < primeiro and diferenca > 0.01 else "PUT" if ultimo > primeiro and diferenca > 0.01 else "DOJI"
    return tendencia


print('\n')
contator = 0
cont = 0
Contpar = 0
parity = ['AUDCAD','GBPJPY','EURJPY','GBPNZD','EURNZD','EURUSD','CADJPY','EURAUD','EURCAD','GBPAUD','USDJPY']
while Contpar != int(len(parity)):
    print('Catalogando : ',parity[Contpar],'...')
    while cont != qtdDias:
        velas = dados.get_candles(parity[Contpar] , (60*5) , 288 , horario)
        velas.reverse()
        for a in velas :

            res = datetime.fromtimestamp(horario).strftime('%Y-%m-%d %H:%M:%S')
            YearIn = date(year = int(str(res[0] + res[1] + res[2] + res[3])) , month = int(str(res[5] + res[6])), day = int(str(res[8] + res[9])) ) #Esse formato eu vou usar para retornar o dia da semana que é 
            dateX = date(year = int(str(timezz[0] + timezz[1] + timezz[2] + timezz[3])) , month = int(str(timezz[5] + timezz[6])), day = int(str(timezz[8] + timezz[9])) )         
            moment = str(res[10] + res[11] + res[12] + res[13] + res[14] + res[15] + res[16] + res[17])
            DiasT[contator] = moment
            diaSemana = YearIn.isoweekday() # Classifica a data em dias da semana de (1 - 7)

            if diaSemana == 7 or diaSemana == 6 : # Não contabiliza fim de semana 
                horario = horario - 300 
            else:      
                if a['open'] < a['close']:
                    ContCall[Contpar][contator] = ContCall[Contpar][contator] + 1 
                    #print(res, ' || Abertura : ',a['open'], '   Fechamento : ',a['close'], ' || ', contator , '|| PARIDADE = ', parity[Contpar])
                    contator = contator + 1
                    horario = horario - 300 


                elif a['open'] > a['close']:
                    ContPut[Contpar][contator] = ContPut[Contpar][contator] + 1
                    #print(res, ' || Abertura : ',a['open'], '   Fechamento : ',a['close'], ' || ', contator, '|| PARIDADE = ', parity[Contpar])
                    contator = contator + 1 
                    horario = horario - 300
                    

                elif a['open'] == a['close']:
                    ContDoji[Contpar][contator] = ContDoji[Contpar][contator] + 1           
                    #print(res, ' || Abertura : ',a['open'], '   Fechamento : ',a['close'], ' || ', contator, '|| PARIDADE = ', parity[Contpar])
                    contator = contator + 1 
                    horario = horario - 300
                #print('CONTPAR = ||||||',Contpar)

        contator = 0    
        cont = cont + 1
    cont = 0
    horario = Ftime
    Contpar = Contpar + 1 
         

contador = 0
pctgCALL = 0
pctgPUT = 0

print('\n')

timeK = Ftime
Contpair = 0
y = 0
while Contpair != int(len(parity)): #Vai catalogar os sinais de acordo com a porcentagem de acerto
    for s in ContCall[Contpair]:
        pctgCALL = ( ( ( s  )*100) / ( s + ContDoji[Contpair][contador] + ContPut[Contpair][contador] ) )
        pctgPUT = ( ( ( ContPut[Contpair][contador] )*100) / ( s + ContDoji[Contpair][contador] + ContPut[Contpair][contador] ) )
        TimeV_ = str(DiasT[contador])        

        if (int(str(TimeV_[1]) + str(TimeV_[2])) > inicio) and ((int(str(TimeV_[1]) + str(TimeV_[2]))) < Final):
            if pctgCALL > pctgPUT:
                if pctgCALL > minpct: #Se a entrada for de CALL ele vai executar isso :
                    print('|| HORÁRIO :', DiasT[contador],'|| DIRECAO : CALL','|| PORCENTAGEM CALL = ', int(pctgCALL) ,'  || PORCENTAGEM PUT', int(pctgPUT), '|| QTD PUT : ', ContPut[Contpair][contador] , '|| QTD CALL : ',ContCall[Contpair][contador],'||PARIDADE = ', parity[Contpair] )
                    sentido = 'CALL' #Direção da entrada
                    final = DiasT[contador] #Pega o horário da entrada
                    resultado[Contpair].append(str(final) + str(sentido) + str(parity[Contpair])) #Salva a entrada em uma Matriz para resultados
                    y = y + 1 #Ajusta a posição da Matriz 
            else:
                if pctgPUT > minpct: #Se a entrada for de PUT ele vai executar isso :
                    print('|| HORÁRIO :', DiasT[contador] ,'|| DIRECAO : PUT',' || PORCENTAGEM CALL = ', int(pctgCALL) ,'  || PORCENTAGEM PUT', int(pctgPUT), '|| QTD PUT : ', ContPut[Contpair][contador] , '|| QTD CALL : ',ContCall[Contpair][contador],'||PARIDADE = ', parity[Contpair] )
                    sentido = 'PUT' #Direção da entrada
                    final = DiasT[contador] #Pega o horário da entrada
                    resultado[Contpair].append(str(final) + str(sentido) +':'+ str(parity[Contpair])) #Salva a entrada em uma Matriz para resultados
                    y = y + 1 #Ajusta a posição da Matriz
        contador = contador + 1 
    y = 0
    contador = 0
    Contpair = Contpair + 1 #Muda a paridade de acordo com o vetor lá em cima 

print('\n')
print('\n')

resultado[0].reverse()
resultado[1].reverse()
resultado[2].reverse()
resultado[3].reverse()

for a in range(10)
    for x in resultado[a]:
        print(x)



