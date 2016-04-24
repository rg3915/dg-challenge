import random
from dress.core.models import Customer, Dress, Order

REPEAT = random.randint(1, 20)
customer = Customer.objects.all()
dress = Dress.objects.all()

for i in range(REPEAT):
    INDEX_CUSTOMER = random.randint(0, customer.count() - 1)
    INDEX_DRESS = random.randint(0, dress.count() - 1)
    Order.objects.create(
        customer=customer[INDEX_CUSTOMER],
        dress=dress[INDEX_DRESS],
        price=random.random() * random.randint(100, 1500)
    )


# done
