import asyncio
import aiohttp
import time

async def request_site(session, url):
    async with session.get(url) as response:
        print(f'contents len: {response.content_length}, from {url}')

async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 3

    start_time = time.time()

    asyncio.run(request_all_sites(urls))

    duration = time.time() - start_time

    print(f"Download {len(urls)} sites in {duration} seconds")

if __name__ == "__main__":
    main()


"""
contents len: 3721, from https://www.jython.org
contents len: 3721, from https://www.jython.org
contents len: 3721, from https://www.jython.org
contents len: None, from https://realpython.com
contents len: None, from https://realpython.com
contents len: None, from https://realpython.com
contents len: 274, from http://olympus.realpython.org/dice
contents len: 274, from http://olympus.realpython.org/dice
contents len: 274, from http://olympus.realpython.org/dice
Download 9 sites in 2.630709648132324 seconds
"""