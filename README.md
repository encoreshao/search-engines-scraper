# Goooogle

Simple way to view search results from Google search engine

## Installation

```
python3 -m venv search-engines-scraper-venv
source search-engines-scraper-venv/bin/activate

python3 setup.py install
export FLASK_ENV=development
flask run
```

## Technology stack

- UI: [Bulma](https://bulma.io/documentation/utilities/functions/)
- API: [Python Flask](https://flask.palletsprojects.com/)
- Scraper: [Search-Engines-Scraper](https://github.com/tasos-py/Search-Engines-Scraper)

## Screenshots

- Loading

![https://scraper.ranbot.online](https://github.com/encoreshao/search-engines-scraper/blob/main/assets/google-loading.png)

- Search Results

![https://scraper.ranbot.online](https://github.com/encoreshao/search-engines-scraper/blob/main/assets/google-scraper.png)

## Python

- ues common layout (code block)

```python3
{% extends 'layouts/application.html' %}
```

- python script in Flask Template

```python3
  {% if page == 1 %}
  {% set page_text = 'Page' %}
  {% else %}
  {% set page_text =  %}
  {% endif %}
```