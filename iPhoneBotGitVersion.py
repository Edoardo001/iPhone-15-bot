# iPhone 15 project
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
import time
import requests
import sys

def iphone_bot_core():
    # lista degli iphone da cercare
    login_page = 'https://www.amazon.it/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.it%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=itflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0'
    product_pages = ["https://www.amazon.it/Apple-iPhone-Pro-Max-256/dp/B0CHX1DDJM?ref_=ast_sto_dp&th=1&psc=1",
                     "https://www.amazon.it/dp/B0CHX4FBSK",
                     "https://www.amazon.it/gp/product/B0CHWZ6YV6",
                     "https://www.amazon.it/gp/product/B0CHXB8FGP"
                     ]


    # settaggio di options per evitare di aprire il browser in modalità grafica
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument("timeout=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # inizializzazione del driver di Chrome
    driver = webdriver.Chrome(options=options)
    # per ogni sito nella lista fai cose, mi creo inoltre un attributo booleano per capire se è il primo avvio del ciclo

        # apre il sito, però alla prima apertura ho bisogno di un delay maggiore per farmi fare il login
    driver.get(login_page)
    loginMail = driver.find_element(By.ID,"ap_email")
    email = "Inserisci qui la tua mail"
    loginMail.send_keys(email)
    print("Effettuo il login con email: ",email,  "e password: **********")
    loginMail.submit()
    time.sleep(2)
    loginPass = driver.find_element(By.ID, "ap_password")
    loginPass.send_keys("Inserisci qui la tua password")
    time.sleep(10)
    loginPass.submit()


    # ottiene il codice html della pagina
    html = driver.page_source
    # crea un oggetto BeautifulSoup con il codice html
    soup = BeautifulSoup(html, 'html.parser')
    # estrae il contenuto
    content = soup.find_all()

    until_close = True
    while until_close:
            for x in product_pages:
                driver.get(x)
                prodotto = driver.find_element(By.ID, "productTitle").text

                try:
                   disponibilita = driver.find_element(By.ID, "addToCart_feature_div")
                   print(prodotto," Dispositivo TROVATO!!!")
                   manda_alert("Ho trovato il dispositivo -> " + prodotto)
                   break
                except:
                    print(prodotto," non disponibile, continuo la mia ricerca strunz!")
                    #driver.refresh()
                    #time.sleep(50)
                    for i in range(10, 0, -1):
                        print(f"Cooldown, riprovo tra {i} secondi ", end="\r", flush=True)
                        time.sleep(1)


    # chiude il driver
    driver.quit()

#telegram notifier
def manda_alert(message):

    apiToken = '6301682380:AAEAj47JVDR5jBGJYQcwqujg_Q0b_28ZQbY'
    chatID = '79141739'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)








# Esecuzione metodo principale
print("**** Tranquillo fratello, troviamo l'iphone, non temere *****************")
print("*** Ci ripigliam tutt chill che è u nuostr!, STRUUUUUNZ! ")
iphone_bot_core()


