from bottle import route, run, template
from requests_html import HTMLSession

TEMPLATE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap');
body {
  max-width: 40rem;
  margin: auto auto;
  font-family: 'Noto Serif', serif;
}
</style>
<h2>{{ title }}</h2>
<article>{{ !article.html }}</article>
"""

@route('/<url:path>')
def index(url: str):
    session = HTMLSession()

    response = session.get(url)
    response.raise_for_status()

    title = response.html.find('h2.article-title', first=True).text
    article = response.html.find('div.article', first=True)

    return template(TEMPLATE, title=title, article=article)

run(host='localhost', port=8000)

