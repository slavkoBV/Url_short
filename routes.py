from flask import Blueprint, render_template, request, redirect

from .app import db
from .models import Url


shortener = Blueprint('shortener', __name__, template_folder='templates')


@shortener.route('/')
def index():
    return render_template('index.html')


@shortener.route('/<short_url>')
def redirect_to(short_url):
    url = Url.query.filter_by(short_url=short_url).first_or_404()
    url.counter += 1
    db.session.commit()
    return redirect(url.origin_url)


@shortener.route('/add_url', methods=['POST'])
def add_url():
    origin_url = request.form['origin_url']
    exist_url = Url.query.filter_by(origin_url=origin_url).first()
    if not exist_url:
        url = Url(origin_url=origin_url)
        db.session.add(url)
        db.session.commit()
    else:
        url = exist_url

    return render_template('short_url.html',
                           new_url=url.short_url,
                           origin_url=url.origin_url)


@shortener.route('/stat')
def statistic():
    urls = Url.query.all()
    return render_template('statistics.html', urls=urls)
