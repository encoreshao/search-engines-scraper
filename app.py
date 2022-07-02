import subprocess
from urllib import response
from flask import Flask, render_template, jsonify, request
import threading
import requests
from search_engines import Google, Bing, Aol, Duckduckgo, Ask, Torch, Qwant, Mojeek, Dogpile

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


@app.route("/scraper", methods=['POST', 'GET'])
def scraper():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        keyword = request.json['q']
        browser = request.json['browser']
        pages = int(request.json['pages'])
        if browser == 'google':
            response = Google().search(keyword, pages)
        elif browser == 'bing':
            response = Bing().search(keyword, pages)
        elif browser == 'aol':
            response = Aol().search(keyword, pages)
        elif browser == 'ask':
            response = Ask().search(keyword, pages)
        elif browser == 'torch':
            response = Torch().search(keyword, pages)
        elif browser == 'qwant':
            response = Qwant().search(keyword, pages)
        elif browser == 'mojeek':
            response = Mojeek().search(keyword, pages)
        elif browser == 'dogpile':
            response = Dogpile().search(keyword, pages)
        elif browser == 'duckduckgo':
            response = Duckduckgo().search(keyword, pages)
        else:
            raise ValueError('Unknown browser: %s' % browser)

        return render_template('components/_search_results.html',
                               keyword=keyword,
                               results=response.results())
    else:
        keyword = request.args.get('q')
        pages = int(request.args.get('pages', 1))
        browser = request.args.get('browser')

        if browser == 'google':
            response = Google().search(keyword, pages)
        elif browser == 'bing':
            response = Bing().search(keyword, pages)
        elif browser == 'aol':
            response = Aol().search(keyword, pages)
        elif browser == 'ask':
            response = Ask().search(keyword, pages)
        elif browser == 'torch':
            response = Torch().search(keyword, pages)
        elif browser == 'qwant':
            response = Qwant().search(keyword, pages)
        elif browser == 'mojeek':
            response = Mojeek().search(keyword, pages)
        elif browser == 'dogpile':
            response = Dogpile().search(keyword, pages)
        elif browser == 'duckduckgo':
            response = Duckduckgo().search(keyword, pages)
        else:
            raise ValueError('Unknown browser: %s' % browser)

        return jsonify(response.results()), 201


if __name__ == '__main__':
    threading.Thread(
        target=lambda: app.run(host=host_name, port=port,
                               debug=True, use_reloader=False)
    ).start()
