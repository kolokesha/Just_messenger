import time

import flask


app = flask.Flask(__name__)
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


@app.route("/")
def hello():
    return "Hello, Skillbox! <a href='/status'>Статус</a>"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Skillbox Messenger',
        'time': time.asctime(),
    }


@app.route("/send", methods=['POST'])
def send_message():
    data = flask.request.json

    if not isinstance(data, dict):

        return flask.abort(400)
    if 'name' not in data or 'text' not in data:
        return flask.abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return flask.abort(400)
    if not (0 < len(name) <= 128):
        return flask.abort(400)
    if not (0 < len(text) < 1000):
        return flask.abort(400)


    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    database.append(message)

    # if '/help' == text:
    #     database.append({
    #         'name': 'Bot',
    #         'text': 'Привет я бот. Работаю так-то',
    #         'time': time.time()
    #     })

    return {'ok': True}


@app.route("/messages")
def get_messages():
    try:
        after = float(flask.request.args['after'])
    except:
        return flask.abort(400)

    messages = []
    for message in database:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:50]}


app.run()
