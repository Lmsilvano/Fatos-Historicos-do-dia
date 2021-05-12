from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time




#                                                         Functions                                                   #


def logar_click(logar, pas):
    # Adeque os seletores das variaveis campo_log e campo_password a nomeclatura utilizada na pagina de login da rede social escolhida. Em geral, a sugestão de seletor já escrita funciona.
    campo_log = driver.find_element_by_xpath('//input[contains(@id, "index_email")]')
    time.sleep(1)
    campo_log.click()
    campo_log.send_keys(logar)
    time.sleep(2)
    campo_password = driver.find_element_by_xpath('//input[contains(@id, "index_pass")]')
    time.sleep(1)
    campo_password.click()
    campo_password.send_keys(pas)
    time.sleep(1)
    campo_password.send_keys(Keys.ENTER)


def send_msg(msg):
    # Você deve adequar o seletor da variavel campo_msg a nomeclatura empregada na pagina, o seletor referese ao campo em branco onde se digita a mensagem. Deixei preenchido com um exemplo
    campo_msg = driver.find_element_by_xpath('//div[contains(@class, "reply_field submit_post_field")]')
    time.sleep(2)
    campo_msg.click()
    for value in msg:
        campo_msg.send_keys(value)
        # o envio das teclar shift + enter serve para separar os fatos em linhas separadas, mantendo tudo em uma unica postagem. Você deve verificar se a caixa de mensagem da rede social escolhida para saída do bot, utiliza shift+enter para quebra de linha.
        campo_msg.send_keys(Keys.SHIFT + Keys.ENTER)
    time.sleep(1)
    campo_msg.send_keys(Keys.ENTER)
    time.sleep(3)


#                                                       Program                                                       #


driver = webdriver.Chrome(ChromeDriverManager().install())

# este é o site de onde o script retira os fatos históricos, alterando o site devese adequar o seletor da variavel content a nomeclatura empregada na pagina também
driver.get('https://www.educabras.com/hoje_na_historia')
time.sleep(5)
content = driver.find_elements_by_css_selector(".accordian-inner .nascido_neste_dia")

# para não ficar muito massante limitei a 5 fatos, começando dos mais recentes [-1]
conte = content[-1]
conte1 = content[-2]
conte2 = content[-3]
conte3 = content[-4]
conte4 = content[-5]
conteF = [conte.text.replace('\n', ' '), conte1.text.replace('\n', ' '), conte2.text.replace('\n', ' '),
          conte3.text.replace('\n', ' '), conte4.text.replace('\n', ' ')]
time.sleep(2)

# você deve inserir o endereço da página de login, exemplo https://vk.com/
driver.get('endereço da pagina de login da rede social')
time.sleep(4)
# insira o log e a senha do perfil na rede social
log = ['nome da conta']
password = ['senha']
logar_click(log, password)
time.sleep(6)
driver.get('endereço onde deve ser postados os fatos')
send_msg(conteF)
driver.close()

# Leia as observações feitas no readme antes de tentar rodar o script