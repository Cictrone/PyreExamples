from flask import Flask, render_template_string, make_response, request
from html import escape

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': '<h1>Hello!</h1>', 'body': '<p>No Body here :(</p>'}
    if request.args.get('body'):
        context['body'] = escape(request.args.get('body'))
    template = f'''<!DOCTYPE html><html>{context['title']}{context['body']}</html>'''
    print(template)
    resp = make_response(render_template_string(template))
    resp.headers['X-XSS-Protection'] = 0  # for demo purposes >:)
    return resp


if __name__ == '__main__':
    app.run()
