import random
import csv
from dress.core.models import Customer
from dress.selenium.gen_names import gen_female_first_name, gen_last_name
from dress.selenium.gen_random_values import gen_number, gen_phone, gen_height

address_list = []

''' Lendo os dados de address.csv '''
with open('fix/address.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

REPEAT = random.randint(1, 20)

''' Insert Customers '''
for i in range(REPEAT):
    dict_ = gen_female_first_name()
    first_name = dict_['first_name']
    last_name = gen_last_name()
    print(first_name, last_name)
    email = '{}.{}@example.com'.format(
        first_name[0].lower(), last_name.lower())
    INDEX = random.randint(0, 9)
    obj = Customer(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=gen_phone(),
        address=address_list[INDEX]['address'],
        complement=address_list[INDEX]['complement'],
        district=address_list[INDEX]['district'],
        city=address_list[INDEX]['city'],
        uf=address_list[INDEX]['city'],
        cep=address_list[INDEX]['cep'],
        person_height=gen_height(),
        bust=gen_number(34, 42),
        hip=gen_number(34, 42),
        waist=gen_number(34, 44),
        heel=gen_number(34, 44),
        person_size=gen_number(34, 44),
    )
    obj.save()


# Done
