import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pokemon = await response.json()
            print(pokemon.get('name'))


async def main():
    urls = ["https://pokeapi.co/api/v2/pokemon/200", "https://pokeapi.co/api/v2/pokemon/201"]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)  # wait for a collection of tasks to complete and retrieve all return values
    return results


asyncio.run(main())
