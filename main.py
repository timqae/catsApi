"""
Your API key:
4c76b502-8817-45e6-982e-6bb19f225342

Use it as the 'x-api-key' header when making any request to the API,
or by adding as a query string paramter e.g. 'api_key=4c76b502-8817-45e6-982e-6bb19f225342'
"""
import requests
import queue

tasks = queue.Queue()

SEARCH_IMG = 'https://api.thecatapi.com/v1/images/search'

data = list()

session = requests.session()
session.headers.update({
    'x-api-key': '4c76b502-8817-45e6-982e-6bb19f225342'
})


def load_imgs(session, tasks):
    while not tasks.empty():
        with session.get(tasks.get()) as resp:
            print('status', resp.status_code)
            resp.close()


if __name__ == '__main__':
    for i in range(3):
        with session.get(SEARCH_IMG, params={'limit': 5}) as resp:
            print('get response with', resp.status_code)
            resp.raise_for_status()
            data.extend(resp.json())

    for item in data:
        url = item['url']
        tasks.put(url)
        print('PUT', url)
