class Zamestnanci:
    #konstruktor
    def __init__(self, jmeno, prijmeni, email, rod_cis, plat, prac_pozice):
            self.jmeno = jmeno
            self.prijmeni = prijmeni
            self.email = email
            self.rod_cis = rod_cis
            self.plat = plat
            self.prac_pozice = prac_pozice
    #toString
    def __str__(self):
        return str("Zaměstnanec: " + self.jmeno +" "+ self.prijmeni + ", " +self.email +", "+str(self.rod_cis) + ", "+ str(self.plat) + ", " + self.prac_pozice)