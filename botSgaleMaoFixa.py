from iqoptionapi.stable_api import IQ_Option
import sys, time
from datetime import datetime #Importa data e tempo 

dados = IQ_Option('hybridtraderss@gmail.com','A7Kmx1q2w3e')
dados.connect()

if dados.check_connect():
    print('Conectado com sucesso!')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()

def carregarsinais():
    arquivo = open('sinais.txt','r')
    lista = arquivo.readlines()

    for i,a in enumerate(lista):      
        if a == '': 
            del lista[i]
        
        return str(lista)

    arquivo.close()
print('\n')
a = carregarsinais()
dad = a.split(', ')
    

def CalculoPayout(par , tipo, timeframe): #Função que pega o valor de Payout 
    if tipo == 'turbo':
        a = dados.get_all_profit()
        return int(100 * a[par]['turbo'])
    
    elif tipo == 'digital':
            while True: 
                d = dados.get_digital_current_profit(par, timeframe)
                if d != False :
                    d = int(d)
                    break
            dados.unsubscribe_strike_list(par, timeframe)
            return d   

def tend(par,timeframe):
    velas = dados.get_candles(par, (int(timeframe) * 60), 20,  time.time())

    ultimo = round(velas[0]['close'], 4)
    primeiro = round(velas[-1]['close'], 4)

    diferenca = abs( round( ( (ultimo - primeiro) / primeiro ) * 100, 3) )
    tendencia = "call" if ultimo > primeiro and diferenca > 0.01 else "put" if ultimo < primeiro and diferenca > 0.01 else "lateralização"
    return tendencia

# - Dado da Primeira entrada - 
tipo = 'turbo' #Se é binária ou Digital, no caso Binária 
dad[0] = 0
entrada = [int(dad[1]), int(dad[6]), int(dad[11]), int(dad[16]), int(dad[21]), int(dad[26])] #Horário dos Sinais
par = [str(dad[2]), str(dad[7]), str(dad[12]), str(dad[17]), str(dad[22]), str(dad[27])] #Pares dos sinais
direcao = [str(dad[3]), str(dad[8]), str(dad[13]), str(dad[18]), str(dad[23]), str(dad[28])] #Direção dos sinais 'CALL' ou 'PUT'
timeframe = [int(dad[4]), int(dad[9]), int(dad[14]), int(dad[19]), int(dad[24]), int(dad[29])] #Timeframe dos sinais 
horario = [str(dad[5]), str(dad[10]), str(dad[15]), str(dad[20]), str(dad[25]), str(dad[30])] #Horário das entradas  

#Dados da terceira entrada
ConfirmAsset = dados.get_all_open_time() #Pega os dados de Todos os ativos abertos para negociação
contador = 0 #Faz a contagem e a passagem de 
payout = CalculoPayout(str(par[contador]), tipo , int(timeframe[contador]))#Calcula o payout
f = '%H:%M:%S' #É o formato em que a string de horario vai se transformar
m = '00:00:15' #É o tempo que será subtraido do horario , no caso 15 segundos

while contador != 6 : 
    moment = (datetime.strptime(horario[contador] , f) - datetime.strptime(m, f)) #Subtrai o tempo
    times = datetime.now().strftime('%H:%M:%S')
    while str(times) != str(timeT): #Espera ate 15 segundos antes da entrada p/ checar se o ativo está aberto
        times = datetime.now().strftime('%H:%M:%S') #Horário atual exato
        a = list(moment) #Transforma o moment em array
        if times[0] == '0' : #Caso o primeiro numero do horario atual == 0 
            a.insert(0,'0')  #Insere o 0 antes da função continuar 
        timeT = ''.join(a) #Junta o array e transforma em string 
        
        internet = dados.check_connect() #Verifica a conexão 
        if internet == False: #Caso a conexão seja perdida ele tenta a reconexão 
            print('A conexão foi perdida ! Tomando medidas cabiveis')
            break
    else: 
        print((contador + 1),'º Entrada!')
        if ConfirmAsset["turbo"][par[contador]]["open"] == True: #Se o ativo estiver aberto no momento ele faz a conexão 
            print('O par ',par[contador], ' está Aberto, continuando com a execução! ')
            if tend(par[contador], timeframe[contador]) != direcao[contador] : #Verifica a tendência !  
                print("1º sinal contra tendência , pulando entrada ! ")
                contador = contador + 1 
                print('\n')
                continue
            elif tend(par[contador], timeframe[contador]) == direcao[contador] or tend(par[contador], timeframe[contador]) != direcao[contador] == "lateralização": 
                print("Sinal a Favor da tendência ! ")
                while datetime.now().strftime('%H:%M:%S') != horario[contador]: #Espera até o horario ser correto
                    time.sleep(0.100)
                    a = dados.check_connect() #Checa a conexão
                    if a == False: #Caso a conexão seja perdida ele tenta a reconexão 
                        dados.connect #Tenta a reconexão
                        print('A conexão foi perdida ! Tomando medidas cabiveis')
                else: #Caso a conexão seja True a entrada será efetuada!
                    id,status = dados.buy(entrada[contador], par[contador], direcao[contador], timeframe[contador]) #Efetua a entrada 
                    print(contador + 1,'º - ','Entrada efetuada -', par[contador] , 'R$',entrada[contador] ,'!' ) #Informa que a entrada foi efetuada
                    if status:
                        res1 , lucro1 = dados.check_win_v3(status) #Checa o resultado da operação 
                        if lucro1 > 0:
                            print('Win R$ +', ((int(entrada[contador]) * payout )/100))
                            contador = contador + 1 
                            print('\n')
                            pass
                        else: 
                            print('Loss R$ -', int(entrada[contador]))
                            print('\n')
                            contador = contador + 1 
                            pass
                    if status == False :  
                        contador = contador + 1
                        pass
        else: 
            print('Ativo Fechado ! ')
            contador = contador + 1 
            continue
        
