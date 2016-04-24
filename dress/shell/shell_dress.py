import random
import csv
from dress.core.models import Dress
from dress.selenium.gen_names import gen_female_first_name, gen_male_first_name, gen_last_name
from dress.selenium.gen_random_values import gen_number, gen_height

dress_list = []

''' Lendo os dados de dress.csv '''
with open('fix/dress.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        dress_list.append(dct)
    f.close()


REPEAT = random.randint(1, 20)

''' Insert Dress '''
for i in range(REPEAT):
    g = random.randint(0, 1)
    dict_ = gen_female_first_name() if g else gen_male_first_name()
    first_name = dict_['first_name']
    last_name = gen_last_name()
    full_name = ' '.join([first_name, last_name])
    print(full_name)
    INDEX = random.randint(0, 13)
    obj = Dress(
        dress_model=dress_list[INDEX]['dress'],
        stylist=full_name,
        color=dress_list[INDEX]['color'],
        dress_height=gen_height(),
        dress_size=gen_number(34, 44),
    )
    obj.save()


# Done
