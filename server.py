from bottle import route, run, template
from requests_html import HTMLSession

@route('/<url:path>')
def index(url: str):
    session = HTMLSession()

    response = session.get(url)
    response.raise_for_status()

    article = response.html.find('div.article', first=True)
    return template('<article>{{ !article.html }}</article>', article=article)

run(host='localhost', port=8000)

