import subprocess
from urllib import response
from flask import Flask, render_template, jsonify, request
import threading
import requests
from search_engines import Google, Bing, Aol, Duckduckgo

host_name = '0.0.0.0'
port = 5000
app = Flask(__name__)

# https: // bulma.io/documentation/overview/start/


@app.route("/")
def index():
    # r = requests.get("http://api.punkapi.com/v2/beers/random")
    # beerJson = r.json()

    # beer = {
    #     'name': beerJson[0]['name'],
    #     'abv': beerJson[0]['abv'],
    #     'desc': beerJson[0]['description'],
    #     'foodPair': beerJson[0]['food_pairing'][0]
    # }
    return render_template('index.html')


@app.route("/video")
def video():
    return render_template('video.html')


@app.route("/google", methods=['POST'])
def google():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        keyword = request.json['q']
        pages = int(request.json['pages'])
        engine = Google()
        response = engine.search(keyword, pages)

        return render_template('components/_search_results.html',
                               keyword=keyword,
                               results=response.results())
        # return jsonify(response.results())
    else:
        return 'Content-Type not supported!'


@app.route("/bing", methods=['POST'])
def bing():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        keyword = request.json['q']
        pages = int(request.json['pages'] | 1)
        engine = Bing()
        response = engine.search(keyword, pages)

        return jsonify(response.results())
    else:
        return 'Content-Type not supported!'


@app.route("/aol", methods=['POST'])
def aol():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        keyword = request.json['q']
        pages = int(request.json['pages'] | 1)
        engine = Aol()
        response = engine.search(keyword, pages)

        return jsonify(response.results())
    else:
        return 'Content-Type not supported!'


@app.route("/duckduckgo", methods=['POST'])
def duckduckgo():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        keyword = request.json['q']
        pages = int(request.json['pages'] | 1)
        engine = Duckduckgo()
        response = engine.search(keyword, pages)

        return jsonify(response.results())
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
    threading.Thread(
        target=lambda: app.run(host=host_name, port=port,
                               debug=True, use_reloader=False)
    ).start()
