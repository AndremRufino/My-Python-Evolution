import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from iqoptionapi.stable_api import IQ_Option

dados = IQ_Option('hybridtraderss@gmail.com','A7Kmx1q2w3e')
dados.connect()
if dados.check_connect():
    print('Conectado com sucesso ! ')
else:
    print('Falha na conexão. Tente novamente! ')

OpenAssets = dados.get_all_open_time() #Pega os dados na corretora de ativos abertos
ativos = ['USD/JPY','USD/CAD','USD/CHF','EUR/USD','EUR/AUD','EUR/NZD','EUR/GBP','EUR/JPY','EUR/CAD','AUD/JPY','AUD/USD','AUD/CAD','GBP/USD','GBP/AUD','GBP/JPY','GBP/CAD','GBP/NZD','CAD/JPY','CAD/CHF']

print('Quantidade de ativos que eu pré determinei : ',len(ativos))

ativosF = ['USDJPY','USDCAD','USDCHF','EURUSD','EURAUD','EURNZD','EURGBP','EURJPY','EURCAD','AUDJPY','AUDUSD','AUDCAD','GBPUSD','GBPAUD','GBPJPY','GBPCAD','GBPNZD','CADJPY','CADCHF']
AtivosAbertos = []

for a in range(19): #Seleciona os ativos abertos de acordo com a lista acima e 
    if OpenAssets['turbo'][ativosF[a]]['open']:
        AtivosAbertos.append(ativos[a])

print('Ativos abertos : ',len(AtivosAbertos) + 1)#Mostra a quantidade de ativos abertos    
print(AtivosAbertos)


driver = webdriver.Chrome('/Users/Richeli/Desktop/iqoption/chromedriver') #Lozaliza os dados do navegador
driver.get('http://br.investing.com/technical/pivot-points') #Site desejado
time.sleep(10) 

def pivot(html): #Faz o filtro de informações do HTML 
    paridade = []
    bloco = (html.find('tbody').findAll('td'))
    i = -1
    for blocos2 in bloco:
        paridade.append([])
        if str(blocos2)[11] == 'f':
            par = str(blocos2)[-17]+str(blocos2)[-16]+str(blocos2)[-15]+str(blocos2)[-14]+str(blocos2)[-13]+str(blocos2)[-12]+str(blocos2)[-11]
            i += 1
            paridade[i].append(par)
        elif str(blocos2)[11] == 'b':
            valor = str(blocos2)[18] + str(blocos2)[19] + str(blocos2)[20] + str(blocos2)[21] + str(blocos2)[22] + str(blocos2)[23] 
            paridade[i].append(valor)
        else:
            valor = str(blocos2)[5] + str(blocos2)[6] + str(blocos2)[7] + str(blocos2)[8] + str(blocos2)[9] + str(blocos2)[10] 
            paridade[i].append(valor)
    
    return paridade


# Recebe os pivot-points de M5
driver.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='300']").click() #Seleciona o timeframe 
time.sleep(10) 
data = driver.find_element_by_xpath("//div[@id='classical']//table")#Tá certo - Não modificar - Apenas ao mudar para fibonacci ou Camarilla
info = data.get_attribute('outerHTML') #Informa que é HTML
texto = BeautifulSoup(info,'html.parser')
classical = pivot(texto)

# Recebe os pivot-points de M15
driver.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='900']").click() #Seleciona o timeframe 
time.sleep(10) 
data2 = driver.find_element_by_xpath("//div[@id='classical']//table")#Tá certo - Não modificar - Apenas ao mudar para fibonacci ou Camarilla
info2 = data2.get_attribute('outerHTML') #Informa que é HTML
texto2 = BeautifulSoup(info2,'html.parser')
classicalM15 = pivot(texto2)

# Recebe os pivot-points de H1
driver.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='3600']").click() #Seleciona o timeframe 
time.sleep(10) 
data3 = driver.find_element_by_xpath("//div[@id='classical']//table")#Não modificar - Apenas ao mudar para fibonacci ou Camarilla - Pode ser que ocorra um erro aqui por conta da internet 
info3 = data3.get_attribute('outerHTML') #Informa que é HTML
texto3 = BeautifulSoup(info3,'html.parser')
classicalH1 = pivot(texto3)

# Recebe os pivot-points de H5
driver.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='18000']").click() #Seleciona o timeframe 
time.sleep(10) 
data4 = driver.find_element_by_xpath("//div[@id='classical']//table")#Não modificar - Apenas ao mudar para fibonacci ou Camarilla - Pode ser que ocorra um erro aqui por conta da internet 
info4 = data4.get_attribute('outerHTML') #Informa que é HTML
texto4 = BeautifulSoup(info4,'html.parser')
classicalH5 = pivot(texto4)
driver.quit() #Finaliza o navegador


#Aqui começa a captura de dados Fibonacci
#Fibonacci Pivot-points M5
driverf = webdriver.Chrome('/Users/Richeli/Desktop/iqoption/chromedriver')  
driverf.get('http://br.investing.com/technical/pivot-points-fibonacci')
time.sleep(10) 
driverf.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='300']").click() #Seleciona o timeframe 
time.sleep(10)
dataf = driverf.find_element_by_xpath("//div[@id='fibonacci']//table[@class='genTbl closedTbl crossRatesTbl']")
infoF = dataf.get_attribute('outerHTML')
textof = BeautifulSoup(infoF,'html.parser')
fibonacci = pivot(textof)

#Fibonacci pivot-points M15
driverf.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='900']").click() #Seleciona o timeframe 
time.sleep(10)
dataf2 = driverf.find_element_by_xpath("//div[@id='fibonacci']//table[@class='genTbl closedTbl crossRatesTbl']")
infoF2 = dataf2.get_attribute('outerHTML')
textof2 = BeautifulSoup(infoF2,'html.parser')
fibonacci2 = pivot(textof2)

#Fibonacci pivot-points H1
driverf.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='3600']").click() #Seleciona o timeframe 
time.sleep(10)
dataf3 = driverf.find_element_by_xpath("//div[@id='fibonacci']//table[@class='genTbl closedTbl crossRatesTbl']")
infoF3 = dataf3.get_attribute('outerHTML')
textof3 = BeautifulSoup(infoF3,'html.parser')
fibonacci3 = pivot(textof3)

#Fibonacci pivot-points H5
driverf.find_element_by_xpath("//div[@class='lightgrayFont float_lang_base_2 timeFrameWrap']//select[@class='selectBox']//option[@value='18000']").click() #Seleciona o timeframe 
time.sleep(10)
dataf4 = driverf.find_element_by_xpath("//div[@id='fibonacci']//table[@class='genTbl closedTbl crossRatesTbl']")
infoF4 = dataf4.get_attribute('outerHTML')
textof4 = BeautifulSoup(infoF4,'html.parser')
fibonacci4 = pivot(textof4)

driverf.quit()

for i in range(38):
    for h in AtivosAbertos:
        if classical[i][0] == h:
            print('\n')
            print('\n')
            print('         ','     PARIDADE ','      S3   ','    S2    ','  S1    ','  PIVOT    ','   R1   ','   R2  ','    R3  ')
            print('M5 classical ',classical[i])
            print('M5 fibonacci ',fibonacci[i])
            print('M15 classical',classicalM15[i])
            print('M15 fibonacci ',fibonacci2[i])
            print('H1 classical',classicalH1[i])
            print('H1 fibonacci ',fibonacci3[i])
            print('H5 classical',classicalH5[i])
            print('H5 fibonacci ',fibonacci4[i])
        else:
            continue


