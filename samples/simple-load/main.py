import asyncio
import sys

import aiohttp


async def payload():
    method = "get"
    url = "http://service:8080/simple-api"
    repeat_delay = 1

    counter = 0
    while True:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            req = getattr(session, method)
            try:
                async with req(url, timeout=2) as resp:
                    await resp.read()
                    counter += 1
                    print(counter, resp.status, file=sys.stdout)

            except Exception as error:
                print(error, file=sys.stdout)

        await asyncio.sleep(repeat_delay)

print("try start",__name__ , file=sys.stdout)
if __name__ == '__main__':
    print("start", file=sys.stdout)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(payload())
    loop.close()