import asyncio
import requests
import time


async def get_url(task_id, url, sleep_time):
    print(f"started at {time.strftime('%X')}")
    r = requests.get(url)
    print(r.status_code)
    content = r.content
    await asyncio.sleep(sleep_time)
    print(task_id, len(content))
    print(f"finished at {time.strftime('%X')}")


loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(get_url(1, "http://www.oa.com", 5)),
    loop.create_task(get_url(2, "http://tiyan.oa.com", 10)),
    loop.create_task(get_url(3, "http://hr.oa.com", 20))

]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
