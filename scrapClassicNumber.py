# scrap de la page https://www.classicnumber.com/les-professionnels.php

from bs4 import BeautifulSoup
import requests
import csv
import re

with open('contacts_classic_number.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'phone', 'street', 'city','country', 'website', 'description'])

    root = 'https://www.classicnumber.com'

    professionnals = f'{root}/les-professionnels.php'

    result = requests.get(professionnals)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')


    contacts = soup.find('div', class_= 'liste-pros-pays')

    links = []
    for link in contacts.find_all('a', href = True):
        links.append(link['href'])

    for link in links:
        result = requests.get(f'{root}/{link}')
        content = result.text
        soup = BeautifulSoup(content, 'html.parser')

        # récupération de chaque page de contact
        contact = soup.find('div', class_= 'advert-header')
        # titre h3 = nom de l'entreprise
        contact_name = contact.find('h3').get_text()
        # récupération du tel 
        if contact.find('a', href= re.compile(r'^tel:')):
            contact_phone = contact.find('a', href= re.compile(r'^tel:')).get_text()
        # récupération de l'adresse
        if contact.find('a', adresse= True):
            contact_address = contact.find('a', adresse= True)['adresse']
            address_lines = contact_address.split(',')
            contact_street = address_lines[0]
            contact_city = address_lines[1]
            contact_country = address_lines[2]

        # récupération du site web caché (href du a)
        if contact.find('a', href= re.compile(r'^http')):
            contact_website = contact.find('a', href= re.compile(r'^http'))['href']
        # récupération du descriptif du contact
        paragraphs = contact.find_all('p')
        if paragraphs:
            contact_description = paragraphs[-1].get_text()



        row = [contact_name]

        if contact_phone:
            row.append(contact_phone)
        else:
            row.append('')
            
        if contact_street:
            row.append(contact_street)
        else:
            row.append('')

        if contact_city:
            row.append(contact_city)
        else:
            row.append('')

        if contact_country:
            row.append(contact_country)
        else:
            row.append('')
        
        if contact_website:
            row.append(contact_website)
        else:
            row.append('')

        if contact_description:
            row.append(contact_description)
        else:
            row.append('')
        

        writer.writerow(row)