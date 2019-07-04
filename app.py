from flask import Flask, render_template, request, redirect
import random
import time
import messages
import os
from urllib.parse import unquote, quote

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
    while '%20' in title:
        title = unquote(title)
    if not content:
        content=messages.fake_news_intro()

    title_encoded = title.replace(' ','-') 
    date = time.strftime("%B %-d, %Y", time.localtime()) 
    commenter_1, comment_1 = ('Timathon Kazercowitch', 'I find the state of modern journalism highly concerning: we should do everything we can to support the journalists getting fired today!')
    commenter_2, comment_2 = ('Nida Sireone', 'Why bother? Most of them write about vaginas anyway.')
    return render_template('single-post.html',**locals())


if __name__ == '__main__':
    app.run()
