import requests
import time


def News(url):
    title = None
    Author = None
    content = None
    try:
        r = requests.get(url)
        json_data = r.json()
        for result in json_data:
            if 'articles' in result:
                articles = json_data['articles']
                for data in articles:
                    if 'title' in data:
                        title = data['title']
                    if 'author' in data:
                        Author = data['author']
                    if 'content' in data:
                        content = data['content']

                    print(f"Author:{Author}\nTitle:{title}\nContent:{content}")
                    print("\n")
                    time.sleep(2)
    except Exception as e:
        print(f"Error:{e}")


News('https://newsapi.org/v2/top-headlines?'
     'sources=bbc-news&'
     'apiKey=c4671a061762417b9a55abfc536c1e1a')
