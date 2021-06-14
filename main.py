import datetime
import time

print('https://replit.com/@Levashov/messenger')

# print(time.time())
# dt = datetime.datetime.fromtimestamp(time.time())
# print(dt)

# dt = datetime.datetime.now()
# print(dt)
# print(dt.year)

# 100
# 100.5
# 'Привет'
# [100, 200, 300, 'четыреста', [0, 1, 2]]
# {
#     'name': 'Jack',
#     'text': 'Привет всем!',
#     'time': '2021-06-07 21:00:00'
# }

database = [
    {
        'name': 'Jack',
        'text': 'Привет всем!',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Привет, Jack!',
        'time': time.time()
    },
]


def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)


send_message('admin', 'Я щас вас заблочу')
send_message('Jack', 'Не надо не блочь')


def print_messages(messages):
    for message in messages:
        dt = datetime.datetime.fromtimestamp(message['time'])
        # print(f'{dt.hour}:{dt.minute}', message['name'])
        print(dt, message['name'])
        print(message['text'])
        print()


def get_messages(after):
    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)

    return messages


print_messages(get_messages(0))
