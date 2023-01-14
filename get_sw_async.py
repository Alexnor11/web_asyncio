import asyncio
import time

from more_itertools import chunked

from db import engine, Session, People, Base

import aiohttp

URL = 'https://swapi.dev/api'

CHUNK_SIZE = 10


async def get_person(person_id: int) -> dict:
    session = aiohttp.ClientSession()
    response = await session.get(f'{URL}/people/{person_id}')
    response_json = await response.json()
    await session.close()
    return response_json


async def get_people(start, end):
    for id_chunk in chunked(range(start, end), CHUNK_SIZE):
        coroutines = [get_person(i) for i in id_chunk]
        result = await asyncio.gather(*coroutines)
        for person in result:
            yield person


async def main():
    async for person in get_people(1, 17):
        print(person['name'])
        print(person['mass'])

start = time.time()
asyncio.run(main())
print('Время работы ', time.time() - start)
