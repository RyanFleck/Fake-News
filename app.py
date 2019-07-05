from flask import Flask, render_template, request, redirect
import random
import time
import os
from urllib.parse import unquote, quote

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


@app.route('/g/<string:ncat>/<string:ntitle>')
def global_article_redirect(ncat, ntitle):
    '''After rewriting the URL, returns the formatted HTML template.'''

    if ' ' in ntitle or ' ' in ncat:
        return news(ncat.strip().title(), ntitle.strip().title())

    category = decode(ncat)
    content = messages.fake_news_intro()
    title = decode(ntitle)
    date = time.strftime("%B %-d, %Y", time.localtime())
    commenter_1, comment_1 = (
        'Timathon Kazercowitch', 'I find the state of modern journalism highly concerning: we should do everything we can to support the journalists getting fired today!')
    commenter_2, comment_2 = (
        'Nida Sireone', 'Why bother? Most of them write about vaginas anyway.')
    return render_template('single-post.html', **locals())


@app.errorhandler(404)
def couldnt_find_page(e):
    return news(
        'Crime',
        'Friend incapable of pasting URLs correctly, ends up on 404 page')


def news(category, title, content=""):

    while '%20' in title:
        title = decode(title)

    while ' ' in title:
        title = encode(title)

    title_encoded = encode(title) 

    if(category):
        return redirect('/g/' + encode(category) + '/' + title_encoded)
    else:
        return redirect('/g/news/' + title_encoded)


def encode(string):
    return quote(unquote(string.replace(' ', '-').title()))


def decode(string):
    return unquote(unquote(string.replace('-', ' ').title()))


if __name__ == '__main__':
    app.run()
