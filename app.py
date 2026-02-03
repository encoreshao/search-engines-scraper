from flask import Flask, render_template, jsonify, request
import threading
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


def get_search_engine(browser):
    '''Returns the appropriate search engine instance.'''
    engines = {
        'google': Google,
        'bing': Bing,
        'aol': Aol,
        'ask': Ask,
        'torch': Torch,
        'qwant': Qwant,
        'mojeek': Mojeek,
        'dogpile': Dogpile,
        'duckduckgo': Duckduckgo,
    }
    if browser not in engines:
        raise ValueError('Unknown browser: %s' % browser)
    return engines[browser]()


@app.route("/scraper", methods=['POST', 'GET'])
def scraper():
    content_type = request.headers.get('Content-Type')

    try:
        if (content_type == 'application/json'):
            keyword = request.json['q']
            browser = request.json['browser']
            pages = int(request.json['pages'])

            engine = get_search_engine(browser)
            response = engine.search(keyword, pages)

            return render_template('components/_search_results.html',
                                   keyword=keyword,
                                   results=response.results())
        else:
            keyword = request.args.get('q')
            pages = int(request.args.get('pages', 1))
            browser = request.args.get('browser')

            engine = get_search_engine(browser)
            response = engine.search(keyword, pages)

            return jsonify(response.results()), 201
    except Exception as e:
        # Log the error but return empty results instead of 500
        print(f"Search error ({browser}): {type(e).__name__}: {e}")
        if content_type == 'application/json':
            return render_template('components/_search_results.html',
                                   keyword=keyword if 'keyword' in dir() else '',
                                   results=[])
        return jsonify([]), 200


if __name__ == '__main__':
    threading.Thread(
        target=lambda: app.run(host=host_name, port=port,
                               debug=True, use_reloader=False)
    ).start()
