import requests
import app.jsonhelper as jh
from bs4 import BeautifulSoup
import uuid

class ScrapWebPage():
    
    def scrap_web_page_paragraph(webpage):
        # Get the HTML from the page
        resp = requests.get(webpage)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        rows = soup.find_all('p')
        id = 0
        for row in rows:
            question = 'read paragraph ' + str(id)
            jh.JsonHelper.write_to_json(str(uuid.uuid4()), row, row.text, 'paragraph', question)
            id += 1 

    def scrap_web_page_title(webpage):
        # Get the HTML from the page
        resp = requests.get(webpage)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        question = 'what is the title'
        title = soup.find('title')
        jh.JsonHelper.write_to_json(str(uuid.uuid4()), title, title.text, 'title', question)

    def scrap_web_page_header(webpage):
               # Get the HTML from the page
        resp = requests.get(webpage)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        rows = soup.find_all('h2')
        id = 0
        for row in rows:
            question = 'read header ' + str(id)
            jh.JsonHelper.write_to_json(str(uuid.uuid4()), row, row.text, 'header', question)
            id += 1 

    def scrap_web_page_link(webpage):
               # Get the HTML from the page
        resp = requests.get(webpage)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        rows = soup.find_all('a')
        id = 0
        for row in rows:
            question = 'read link ' + str(id)
            jh.JsonHelper.write_to_json(str(uuid.uuid4()), row, row.text, 'link', question)
            id += 1 

    def scrap_web_page_source(webpage):
        # Get the HTML from the page
        resp = requests.get(webpage)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')
        text = soup.find_all(text=True)
        question = 'what is the source'
        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            # there may be more elements you don't want, such as "style", etc.
        ]

        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        formatted = output.replace('"', '')
        formattedagain = formatted.replace("\n", "")
        return formattedagain


