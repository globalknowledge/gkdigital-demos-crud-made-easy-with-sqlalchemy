import data.base
import data.tables


def main():
    data.base.create_db()
    # insert_data()
    add_test_data()
    find_data()


def find_data():
    custs = data.tables.customers
    conn = data.base.created_conn()

    cust221 = conn.execute(custs.select().where(custs.c.email == 'cust221@aol.com')).first()
    print("Single customer")
    print(cust221.id, cust221.email, cust221.created)
    print()

    latest_customers = conn.execute(custs
            .select().where(custs.c.email.like('cust99%@aol.com'))
            .order_by(custs.c.created.desc()))

    print("Latest")
    for c in latest_customers:
        print(c)


def insert_data():
    statement = data.tables.customers.insert().values(
        name='mkennedy', email='michael@aol.com'
    )

    # print(statement)

    conn = data.base.created_conn()
    result = conn.execute(statement)

    print("New record: {}".format(result.inserted_primary_key))


def add_test_data():
    conn = data.base.created_conn()
    if conn.execute(data.tables.customers.count()).scalar() > 1:
        print("Skipping insert")
        return

    to_insert = []
    for i in range(0, 1000):
        to_insert.append({
            'name': 'cust_{}'.format(i + 1),
            'email': 'cust{}@aol.com'.format(i + 1)
        })

    conn.execute(data.tables.customers.insert(), to_insert)
    conn.close()

    print("Added {} customers to the db".format(len(to_insert)))


if __name__ == '__main__':
    main()
