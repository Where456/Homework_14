from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/movie/<title>")
def main_page(title):
    text = get_by_title(title)
    return text


@app.route("/movie/<int:year>/to/<int:year2>")
def search_by_years(year, year2):
    text = search_with_lim(year, year2)
    return text


@app.route("/rating/children")
def type_child():
    text = type_search('children')
    return text


@app.route("/rating/family")
def type_family():
    text = type_search('family')
    return text


@app.route("/rating/adult")
def type_adult():
    text = type_search("adult")
    return text


@app.route("/genre/<genre>")
def search_by_genre_page(genre):
    text = search_by_genre(genre)
    return text


app.run()
