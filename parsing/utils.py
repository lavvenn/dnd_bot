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


def get_beast_small_description(name):
    response = requests.get(f'https://dnd.su/bestiary/?search={name}')
    soup = BeautifulSoup(response.text, 'html.parser')

    beast_description = soup.find(class_="params card__article-body")

    description_list_li = beast_description.find_all("li")

    description_list = []

    for description in description_list_li:
        description_list.append(description.text)

    return [description_list[0], description_list[1], description_list[2], description_list[3]]


def get_beast_abilities(name):
    response = requests.get(f'https://dnd.su/bestiary/?search={name}')
    soup = BeautifulSoup(response.text, 'html.parser')

    beast_abilities = soup.find(class_="params card__article-body")

    abilities_list_div = beast_abilities.find_all("div", class_="stat")

    abilities_list = []

    for ability in abilities_list_div:
        abilities_list.append(ability.text[3:])


    return abilities_list


def get_beast_description(name):
    response = requests.get(f'https://dnd.su/bestiary/?search={name}')
    soup = BeautifulSoup(response.text, 'html.parser')

    beast_description = soup.find(class_="params card__article-body")

    description_list = beast_description.find_all("li", class_="subsection desc")

    returned_list = []

    for description in description_list:
        returned_list.append(description.text)
    return returned_list