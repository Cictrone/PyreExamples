from flask import Flask, request

from os import system
app = Flask(__name__)


def system_exec(cmd: str) -> int:
    return system(cmd)


@app.route('/')
def index():
    cmd = request.args.get('cmd', None)
    if cmd is not None:
        return f'Congrats! You returned: {system_exec(cmd)}.center()'
    return f'Congrats!'


if __name__ == '__main__':
    app.run()
