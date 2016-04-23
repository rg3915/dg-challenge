import time
import csv
from random import randint
from selenium import webdriver
from gen_names import gen_female_first_name, gen_male_first_name, gen_last_name
from gen_random_values import gen_number, gen_height

page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/dress/add/')

g = randint(0, 1)

if g:
    dict_ = gen_female_first_name()
else:
    dict_ = gen_male_first_name()

first_name = dict_['first_name']
last_name = gen_last_name()
full_name = ' '.join([first_name, last_name])
print(full_name)

dress_list = []

''' Lendo os dados de dress.csv '''
with open('fix/dress.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        dress_list.append(dct)
    f.close()

INDEX = randint(0, 13)

fields = [
    ['id_dress_model', dress_list[INDEX]['dress']],
    ['id_stylist', full_name],
    ['id_color', dress_list[INDEX]['color']],
    ['id_dress_height', gen_height()],
    ['id_dress_size', gen_number(34, 44)],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])

# button = page.find_element_by_id('id_submit')
button = page.find_element_by_class_name('btn-primary')
button.click()

page.quit()
