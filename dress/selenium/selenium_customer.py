import time
import csv
from random import randint
from selenium import webdriver
from gen_names import gen_female_first_name, gen_last_name
from gen_random_values import gen_number, gen_phone, gen_height

page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/customer/add/')

dict_ = gen_female_first_name()
first_name = dict_['first_name']
last_name = gen_last_name()
print(first_name, last_name)

email = '{}.{}@example.com'.format(first_name[0].lower(), last_name.lower())

address_list = []

''' Lendo os dados de address.csv '''
with open('fix/address.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        address_list.append(dct)
    f.close()

INDEX = randint(0, 9)

fields = [
    ['id_first_name', first_name],
    ['id_last_name', last_name],
    ['id_email', email],
    ['id_phone', gen_phone()],
    ['id_address', address_list[INDEX]['address']],
    ['id_complement', address_list[INDEX]['complement']],
    ['id_district', address_list[INDEX]['district']],
    ['id_city', address_list[INDEX]['city']],
    ['id_uf', address_list[INDEX]['city']],
    ['id_cep', address_list[INDEX]['cep']],
    ['id_person_height', gen_height()],
    ['id_bust', gen_number(34, 42)],
    ['id_hip', gen_number(34, 42)],
    ['id_waist', gen_number(34, 44)],
    ['id_heel', gen_number(34, 44)],
    ['id_person_size', gen_number(34, 44)],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])

# button = page.find_element_by_id('id_submit')
button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
