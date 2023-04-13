# scrap de la page https://www.classicnumber.com/annuaire-pros.php

from bs4 import BeautifulSoup
import requests
import csv
import re

with open('contacts_classic_number.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'phone', 'street', 'city','country', 'website', 'description'])

    root = 'https://www.classicnumber.com'

    professionnals = f'{root}/annuaire-pros.php'

    result = requests.get(professionnals)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')


    # atteindre la div qui contient la carte + la card professionnel
        # toucher tous les liens de la carte (pointeur sur la carte)
            # scrapper la card professionnel à gauche de la carte