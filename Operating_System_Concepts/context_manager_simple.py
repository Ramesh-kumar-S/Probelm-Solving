from contextlib import contextmanager


@contextmanager
def DBConnector():
    print(f'Starting to connect to DB on port 80')
    yield
    print(f'Closing the DB Connection')


with DBConnector() as D:
    print("Connection Success")
