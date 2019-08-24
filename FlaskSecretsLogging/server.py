from flask import Flask, request, redirect

app = Flask(__name__)

SECRET_STRING = '<secret-value>'


def log(thing: str):
    print(thing)


@app.route('/')
def index():
    cookie = request.cookies.get('MyCookie')
    if cookie != SECRET_STRING:
        return redirect('/login')
    # Pretend this is a log
    log(cookie)
    return 'You made it!'


@app.route('/login', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    log(password)
    resp = redirect('/')
    if username == 'admin' and password == 'password':
        # One minute long session
        resp.headers['Set-Cookie'] = f'MyCookie={SECRET_STRING}; Max-Age=60'
    return resp


if __name__ == '__main__':
    app.run()
