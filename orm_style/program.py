import random

import data.base
import data.core
from data.models import Customer, Order


def main():
    data.core.init()
    # insert_data()
    add_test_data()
    find_orders()
    print('done')


def find_orders():
    session = data.base.session_factory()

    p = 419.42528917889865
    order = session.query(Order).filter(Order.total_price == p).one()

    print("The order")
    print(order)
    print()

    pricy_orders = session.query(Order) \
        .filter(Order.total_price > 990) \
        .order_by(Order.total_price.desc())

    # print(pricy_orders)
    # print(type(pricy_orders))

    print("Pricy orders:")
    for o in pricy_orders[:3]:
        print(o)


def add_test_data():
    session = data.base.session_factory()

    if session.query(Order).count():
        print('Data exists, skipping creation')
        return

    for _ in range(0, 1000):
        o = Order(total_price=random.random() * 1000)
        session.add(o)

    session.commit()
    print("Added {} orders to the db".format(session.query(Order).count()))


def insert_data():
    first_customer = Customer()
    first_customer.email = "jeff@jeff.com"
    first_customer.name = "Jeff Rose"

    print("First customer {} with id {} before save".format(
        first_customer.name, first_customer.id
    ))

    uow = data.base.session_factory()

    # make changes
    uow.add(first_customer)

    uow.commit()

    print("First customer {} with id {} before save".format(
        first_customer.name, first_customer.id
    ))


if __name__ == '__main__':
    main()
