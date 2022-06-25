import subprocess
from flask import Flask, render_template, jsonify, request
import threading
import requests
from search_engines import Google, Bing, Aol, Duckduckgo

host_name = '0.0.0.0'
port = 5000
app = Flask(__name__)

# https: // bulma.io/documentation/overview/start/


@app.route("/")
def get_beer():
    r = requests.get("http://api.punkapi.com/v2/beers/random")
    beerJson = r.json()

    beer = {
        'name': beerJson[0]['name'],
        'abv': beerJson[0]['abv'],
        'desc': beerJson[0]['description'],
        'foodPair': beerJson[0]['food_pairing'][0]
    }
    return render_template('index.html', beer=beer)


@app.route("/google")
def google():
    keyword = request.args.get('q')
    pages = int(request.args.get('pages', 1))
    engine = Google()
    results = engine.search(keyword, pages)

    return jsonify(results.results())


@app.route("/bing")
def bing():
    keyword = request.args.get('q')
    pages = int(request.args.get('pages', 1))
    engine = Bing()
    results = engine.search(keyword, pages)

    return jsonify(results.results())


@app.route("/aol")
def aol():
    keyword = request.args.get('q')
    pages = int(request.args.get('pages', 1))
    engine = Aol()
    results = engine.search(keyword, pages)

    return jsonify(results.results())


@app.route("/duckduckgo")
def duckduckgo():
    keyword = request.args.get('q')
    pages = int(request.args.get('pages', 1))
    engine = Duckduckgo()
    results = engine.search(keyword, pages)

    return jsonify(results.results())


if __name__ == '__main__':
    threading.Thread(
        target=lambda: app.run(host=host_name, port=port,
                               debug=True, use_reloader=False)
    ).start()
