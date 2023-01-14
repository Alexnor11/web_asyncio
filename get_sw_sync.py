import time

import requests

URL = 'https://swapi.dev/api'


def get_person(person_id) -> dict:
    return requests.get(f'{URL}/people/{person_id}').json()


def main():
    for person_id in range(1, 11):
        print(get_person(person_id))


start = time.time()
main()
print('Время работы', time.time() - start)
