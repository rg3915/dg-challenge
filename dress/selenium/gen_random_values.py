import string
from random import randint, choice


def gen_string(max_length):
    return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
gen_string.required = ['max_length']


def gen_number(min_number=1, max_number=99):
    # gera numeros inteiros entre 1 e 99
    return randint(min_number, max_number)


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_phone():
    # gera um telefone no formato xx xxxxx-xxxx
    digits_ = gen_digits(11)
    return '{} 9{}-{}'.format(digits_[:2], digits_[3:7], digits_[7:])


def gen_height():
    a = randint(50, 99)
    return "1.%s" % a
