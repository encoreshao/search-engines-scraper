# Goooogle

A modern, SaaS-style web search aggregator that scrapes results from multiple search engines including Bing, AOL, Google, DuckDuckGo, and more.

Built by [RanBOT Labs](https://ranbot.online)

## Features

- **Multi-Engine Search** - Aggregate results from 9 search engines
- **Modern SaaS UI** - Clean, professional design with Tailwind CSS
- **Skeleton Loading** - Beautiful shimmer animation during search
- **Video Gallery** - Curated videos on AI, technology, and entertainment
- **Responsive Design** - Works on desktop and mobile devices

### Supported Search Engines

| Engine | Status |
|--------|--------|
| Bing | Working |
| AOL | Working |
| Google | Limited (bot protection) |
| DuckDuckGo | Limited |
| Ask | Limited |
| Qwant | Limited |
| Mojeek | Limited |
| Dogpile | Limited |
| Torch | Limited |

> **Note:** Bing and AOL are recommended for reliable results. Other engines may be blocked due to anti-bot protection.

## Installation

```bash
# Create virtual environment
python3 -m venv search-engines-scraper-venv
source search-engines-scraper-venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
flask run --port 5001
```

Then visit [http://localhost:5001](http://localhost:5001)

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | [Tailwind CSS](https://tailwindcss.com/) |
| **Typography** | [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) + [DM Sans](https://fonts.google.com/specimen/DM+Sans) |
| **Icons** | Custom SVG (Heroicons style) |
| **Backend** | [Flask](https://flask.palletsprojects.com/) |
| **Scraper** | [Search-Engines-Scraper](https://github.com/tasos-py/Search-Engines-Scraper) |

## UI Features

### Home Page
- Centered search interface with inline controls
- Engine selector dropdown
- Results count selector
- Keyboard shortcut support (Enter to search)
- Engine status indicators

### Loading Experience
- Skeleton shimmer animation
- Placeholder cards matching result layout
- Status header with live indicator
- Smooth CSS gradient animation

### Search Results
- Card-based results with hover effects
- Domain badges
- External link indicators
- Graceful "No Results" state

### Video Gallery
- Tab-based navigation (Featured, Music, Videos, Docs, AI Agents)
- Curated YouTube video embeds
- Responsive grid layout

## Project Structure

```
search-engines-scraper/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── search_engines/        # Scraper modules
│   ├── engines/           # Individual engine scrapers
│   └── ...
├── templates/
│   ├── layouts/
│   │   └── application.html   # Base layout
│   ├── components/
│   │   ├── _search_results.html
│   │   └── _search_results_v2.html
│   ├── index.html         # Home page
│   └── video.html         # Video gallery
└── static/
    └── styles/
        └── index.css      # Custom styles
```

## Development

### Running in Development Mode

```bash
source search-engines-scraper-venv/bin/activate
export FLASK_DEBUG=1
flask run --port 5001
```

### Template Syntax

Using Jinja2 templates with Flask:

```python
{% extends 'layouts/application.html' %}

{% block content %}
  <!-- Page content -->
{% endblock %}
```

Conditional logic in templates:

```python
{% if request.endpoint == 'index' %}
  <!-- Active state -->
{% endif %}
```

## License

MIT License - See [LICENSE](LICENSE) file

## Author

- **RanBOT Labs** - [ranbot.online](https://ranbot.online)
- **Blog** - [icmoc.com](https://icmoc.com)
- **GitHub** - [@encoreshao](https://github.com/encoreshao)
