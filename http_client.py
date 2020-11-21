import httpx

if __name__ == '__main__':
    client = httpx.Client()

    response = client.get('http://0.0.0.0:3000/articles')

    items = response.json()

    for item in items:
        print(item)

        print(item['title'])

        print()
