from flask import Flask, render_template, request
import random
import time
import messages

app = Flask(__name__)


@app.route('/')
def index():
    return news('Crime', 'Modern Journalism', messages.fake_news_intro())


@app.route('/<string:title>')
def article(title):
    return news('News', title.strip().title())


@app.route('/<string:cat>/<string:title>')
def categorized_article(cat, title):
    return news(cat.strip().title(), title.strip().title())


@app.errorhandler(404)
def couldnt_find_page(e):
    return news(
        'Crime',
        'Friend incapable of pasting URLs correctly, ends up on 404 page')


def news(category, title, content=""):
    # Generate body here.
    if not content:
        content='This is the news body.'
    return render_template('news.html',**locals())


if __name__ == '__main__':
    app.run()
