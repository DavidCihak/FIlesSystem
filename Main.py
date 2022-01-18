import logging
import pickle
import csv
from D_Projekty.Ukol12 import Json

#vkladani dat/záznamů do binarniho souboru
'''
from Zamestnanci import Zamestnanci
try:
   Zam1 = Zamestnanci("Tomáš", "Krejčík", "krejcik@spsejecna.cz", 333656989, 40_000, "Game designer")
   Zam2 = Zamestnanci("Benjamin", "Rais", "rais@spsejecna.cz", 163543443, 40_000, "Síťový technik")
   Zam3 = Zamestnanci("Michal", "Douša", "dousa@spsejecna.cz", 222656989, 70_000, "Programátor")
   Zam4 = Zamestnanci("David", "Čihák", "cihak@spsejecna.cz", 111656989, 50_000, "Hardware technik")
   Zam5 = Zamestnanci("Maksym", "Kvetsko", "kvetsko@spsejecna.cz", 444656989, 40_000, "Analytik")

   list = []
   list.append(Zam1)
   list.append(Zam2)
   list.append(Zam3)
   list.append(Zam4)
   list.append(Zam5)
   with open(r"C:\\Users\\dwdci\\Desktop\\Dawe\\School\\C4a\\PV - Python\\Ukol12\\SeznamZam.dat", "wb") as f:
      pickle.dump(list, f)
except:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Nastala chyba pri naplneni >.bin< souboru")
'''
#vytvoření souboru, do kterého se budou zapisovat erorry + format datumu a času
logging.basicConfig(filename="error.log", datefmt="%d-%b-%y %H:%M:%S", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

#nacitani dat z binarniho souboru a pridani do listu
list = []
#hlídá jestli soubor existuje
try:
   print("Výpis dat z binárního souboru: ")
   Zam2 = pickle.load(open('SeznamZam.dat', "rb"))
   for x in Zam2:
      list.append(x)
      print(x)
except FileNotFoundError:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Spatna path nebo se nepodarilo nalezt soubor >.dat.< ")
except:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Pri nacitani ze souboru >.dat< nastala chyba")

header = ['jmeno', 'prijmeni', 'email', 'rodne cislo', 'plat', 'pozice']

#hlídá jestli soubor existuje
try:
   # export objektů do csv souboru
   with open(r"/D_Projekty/Ukol12/CSVSeznam.csv", 'w', encoding="utf-8", newline='') as f:
      writer = csv.writer(f)
      writer.writerow(header)
      for x in range(len(list)):
         data = [list[x].jmeno, list[x].prijmeni,list[x].email,list[x].rod_cis,list[x].plat,list[x].prac_pozice]
         writer.writerow(data)
   print("Export dat do CSV souboru proběhl úspěšně")
except FileNotFoundError:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Spatna path nebo se nepodarilo nalezt soubor >.csv< ")

#hlídá jestli jsou data ve správném formátu
try:
   #vstupy pro metodu config, která serializuje do souboru config.json
   jazyk = str(input("Zadej jazyk, který se nastaví do JsonConfig souboru:"))
   kodovani = str(input("Zadej kodovani, ktere bude v JsonConfig souboru:"))
   username = str(input("Zadej username, ktere bude v JsonConfig souboru:"))
   print("Heslo je nastavené na -> 1234")
except ValueError:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Spatny format vstupu pro JAZYK/KODOVANI/USERNAME -> nutno string")
except:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Chyba pri vstupu od uzivatele")
#hlídá jestli je v metodě dostatek argumentů
try:
   #použití metody config
   Json.config(jazyk, kodovani, username)
except TypeError:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Nedostatecny pocet argumentu pri pouziti metody")
except:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Chyba pri pouziti metody, ktera nastavuje configuracni >.json< soubor")

try:
   #vstup pro ověření username
   des = str(input("Pro deserializaci JsonConfig souboru zadej spravny username zde: "))
except ValueError:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Spatny format vstupu")
except:
   print("Popis chyby + kdy se stala najdete v souboru >error.log<")
   logging.error("Nastala chyba pri zadani username pro overeni")

Json.config_des(des)

