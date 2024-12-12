import requests
from bs4 import BeautifulSoup


response = requests.get('https://dnd.su/bestiary/')

soup = BeautifulSoup(response.text, 'html.parser')


def get_all_bestiary():
    body = soup.find_all(class_="col list-item__beast for_filter")

    all_names_list = []
    for beast in body:
        all_names_list.append(beast.find(class_="list-item-title").text)
    return all_names_list

def get_bestiary_by_first_letter(letter):
    body = soup.find_all(class_="col list-item__beast for_filter")

    all_names_list = []
    for beast in body:
        if beast.find(class_="list-item-title").text[0] == letter:
            all_names_list.append(beast.find(class_="list-item-title").text)
    return all_names_list


def get_beast_description(name):
    response = requests.get(f'https://dnd.su/bestiary/?search={name}')
    soup = BeautifulSoup(response.text, 'html.parser')

    beast_description = soup.find(class_="params card__article-body")

    description_list = beast_description.find_all("li", class_="subsection desc")

    returned_description = []

    for description in description_list:
        returned_description.append(description.text)

    description = ' \n'.join(returned_description)

    return description