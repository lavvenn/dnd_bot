from utils import get_all_bestiary, get_bestiary_by_first_letter, get_beast_description

all_items = get_all_bestiary()

item_by_first_letter = get_bestiary_by_first_letter('А')

print(all_items[0])
print(item_by_first_letter)

print(get_beast_description('Арук Громовержец Туунлакалага'))