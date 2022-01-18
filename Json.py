import json
import logging
try:
    default_path = r"/D_Projekty/Ukol12/SeznamZam.dat"
    default_heslo = "1234"
except NameError:
    print("Popis chyby + kdy se stala najdete v souboru >error.log<")
    logging.error("Proměnná default_path nebo defaul_heslo neni nastavena")

try:
    #metoda config, která zapisuje do souboru config.json.
    def config(jazyk, kodovani, username):
        #Format json souboru.
        nastaveni = {
                "jazyk" : jazyk,
                "kodovani" : kodovani,
                "username" : username,
                "password" : default_heslo,
                "cesta k dat" : default_path
        }
        myJSON = json.dumps(nastaveni)
        # zapisovani do souboru json
        with open("config.json", "w") as jsonfile:
            jsonfile.write(myJSON)
            print("Configurace byla uspesne zapsana")
except FileNotFoundError:
    print("Popis chyby + kdy se stala najdete v souboru >error.log<")
    logging.error("Spatna path nebo se nepodarilo nalezt configuracni soubor >.json< ")
except:
    print("Popis chyby + kdy se stala najdete v souboru >error.log<")
    logging.error("Pri zapisovani do configuracniho souboru >.json< nastala chyba")

try:
    #metoda, která načte username z config souboru porovná ji se zadaným username.
    def config_des(des):
        #načítání souboru config
        with open('config.json') as json_file:
            data = json.load(json_file)
        #pokud des odpovídá username zadanému v config souboru, tak metoda vypíše celý config dictionary soubor.
        #neboli ověření username
        try:
            if des == data['username']:
                print("Obsah config souboru:\n", data)
            else:
                raise Exception
        except:
            print("Popis chyby + kdy se stala najdete v souboru >error.log<")
            logging.error("Pri overovani bylo spatne zadane username")
except:
    print("Popis chyby + kdy se stala najdete v souboru >error.log<")
    logging.error("Pri spusteni metody, ktera deserializuje configuracni soubor")



