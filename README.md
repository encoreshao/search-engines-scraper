# Goooogle

A simple way to view search results from the search engines (Google, Bing, AOL, etc.)

## Installation

```
python3 -m venv search-engines-scraper-venv
source search-engines-scraper-venv/bin/activate

python3 setup.py install
export FLASK_ENV=development
flask run
```

## Technology Stack

- UI: [Bulma](https://bulma.io/documentation/utilities/functions/)
- Icons: [Fontawesome](https://fontawesome.com/v5/docs/web/setup/host-font-awesome-yourself)
- Backend API: [Flask](https://flask.palletsprojects.com/)
- Scraper: [Search-Engines-Scraper](https://github.com/tasos-py/Search-Engines-Scraper)
- Random Image: [Unsplash](https://unsplash.it/1200/900?random)

## Screenshots

- Loading

![https://scraper.ranbot.online](https://github.com/encoreshao/search-engines-scraper/blob/main/assets/google-loading.png)

- Search Results

![https://scraper.ranbot.online](https://github.com/encoreshao/search-engines-scraper/blob/main/assets/google-scraper.png)

## Python

- used common layout [code block]

```python3
{% extends 'layouts/application.html' %}
```

- Python script in flask template

```python3
  {% if page == 1 %}
  {% set page_text = 'Value 1' %}
  {% else %}
  {% set page_text = 'Value 2' %}
  {% endif %}
```
