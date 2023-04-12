import requests
import time


def get_questions(tag: str):
    to_date = int(time.time())
    from_date = to_date - 172800000
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={from_date}&todate={to_date}&order=desc&sort' \
          f'=activity&tagged={tag.lower()}&site=stackoverflow'
    response = requests.get(url)

    if response.status_code == 200:
        all_questions = response.json()['items']
        for question in all_questions:
            print('- ', question['title'])
    else:
        print('Error', response.status_code)

if __name__ == '__main__':
    get_questions('Python')
