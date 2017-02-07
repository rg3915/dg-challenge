# dg-challenge


## Objetivo

Nós somos a primeira plataforma online para aluguel de vestidos de grandes estilistas do país.
Nossos principais produtos são vestidos e acessórios femininos.

Considere que os nossos vestidos têm como principais características seu modelo, estilista, cor, altura e tamanho.

Quando uma cliente faz uma locação precisamos saber seu nome, endereço, cidade, estado, cep, telefone celular, altura, busto, quadril, cintura, salto e tamanho que ela usa.

Baseado nessas informações, seu desafio é estruturar:

* A base de dados
* A interface gráfica para administrar esses dados
* Criar uma API REST para fazermos o CRUD de vestidos e clientes
* Devemos poder atribuir vestidos a clientes tanto pela interface quanto pela API

Plus:

* Gostamos de gráficos
* Gostamos de coisas customizadas, fora do default
* Gostamos de Python e Django


## Versão

* Python 3.5
* Django==1.9.5


## Instalação

* Clone o repositório.
* Crie um virtualenv com Python 3.5
* Ative o virtualenv.
* Instale as dependências.
* Configure a instância com o .env
* Rode a migração
* Crie um usuário username='admin' pass='demodemo'

```
git clone https://github.com/rg3915/dg-challenge.git
cd dg-challenge
python -m venv .venv
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
pip install -r requirements.txt
cp contrib/env-sample .env
./manage.py makemigrations core
./manage.py migrate
./manage.py createsuperuser --username='admin' --email=''
```

## Testes

```
./manage.py test
```

## Shell do Django

Execute os comandos shell a seguir. Eles inserem uma quantidade aleatória de registros variando entre 1 e 20.

```
make shell_customer
make shell_dress
make shell_order
```

## Selenium

Você também pode usar o **Selenium** para preencher os formulários. Para isso você vai precisar de **duas abas do terminal**.

* Em uma você roda a app na porta 8000
* E na outra você roda os comandos a seguir:

```
make selenium_customer
make selenium_dress
```

O **pedido** é feito manualmente a partir de [http://localhost:8000/order/add/][0] .



## Api Rest

A partir do post [Django Rest Framework Quickstart][1] e [Django Rest Framework Serialization][2] eu fiz a Api Rest.

Neste exemplo também você vai precisar de **duas abas do terminal**.

* Em uma você roda a app na porta 8000
* E na outra você roda os comandos a seguir (usando [httpie][3]):

**Obs:** para os exemplos a seguir considere que já exista um cliente e um vestido cadastrados. Os exemplos referem-se apenas aos **pedidos**.

```
http http://127.0.0.1:8000/api/customers/
http http://127.0.0.1:8000/api/customers/1/
http http://127.0.0.1:8000/api/dresses/1/
http http://127.0.0.1:8000/api/orders/1/

# Create
http POST http://127.0.0.1:8000/api/orders/ customer=1 dress=1 price=450.99

# Update
http PUT http://127.0.0.1:8000/api/orders/1/ customer=1 dress=2 price=999.99

# Delete
http DELETE http://127.0.0.1:8000/api/orders/1/
```

Também podemos usar o [cURL][4].

```
curl http://127.0.0.1:8000/api/orders/1/

# Create
curl -X POST http://127.0.0.1:8000/api/orders/ -H 'Content-Type: application/json' -d '{"customer": 1, "dress": 1, "price": "900.05"}'

# Update
curl -X PUT http://127.0.0.1:8000/api/orders/1/ -H 'Content-Type: application/json' -d '{"customer": 1, "dress": 2, "price": "854.92"}'

# Delete
curl -X DELETE http://127.0.0.1:8000/api/orders/1/
```



## Screenshot

![img](img/graphics.png)

*Dress and Go*

[0]: http://localhost:8000/order/add/
[1]: http://pythonclub.com.br/django-rest-framework-quickstart.html
[2]: http://pythonclub.com.br/django-rest-framework-serialization.html
[3]: https://github.com/jkbrzt/httpie#installation
[4]: http://www.diego-garcia.info/2014/12/13/use-o-curl/
