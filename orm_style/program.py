import data.base
import data.core
from data.models import Customer


def main():
    data.core.init()
    insert_data()
    print('done')


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
