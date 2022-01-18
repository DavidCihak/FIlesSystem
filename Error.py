import xml.etree.cElementTree as ET
#není zcela hotové, ze zadání jsem uplně nepochopil, jestli soubor ma byt .log nebo .xml
#zapisovani chyb do souboru .log by mělo perfektne fungovat
chyby = {
            "Nacitani" : "Pri nacitani ze souboru nastala chyba",
            "Nastaveni" : "Proměnná default_path nebo defaul_heslo neni nastavena",
            "Path" : "Spatna path nebo se nepodarilo nalezt soubor",
            "Uzivatel" : "Chyba pri vstupu od uzivatele",
            "PocetArgu" : "Nedostatecny pocet argumentu pri pouziti metody",
            "Overeni" : "Pri overovani bylo spatne zadane username"
}


def err_to_xml():
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")

    ET.SubElement(doc, "field1", name="Chyba1").text = chyby['Nacitani']
    ET.SubElement(doc, "field2", name="Chyba2").text = chyby['Nastaveni']
    ET.SubElement(doc, "field1", name="Chyba3").text = chyby['Path']
    ET.SubElement(doc, "field2", name="Chyba4").text = chyby['Uzivatel']
    ET.SubElement(doc, "field1", name="Chyba5").text = chyby['PocetArgu']
    ET.SubElement(doc, "field2", name="Chyba6").text = chyby['Overeni']

    tree = ET.ElementTree(root)
    tree.write("Errors.xml")
