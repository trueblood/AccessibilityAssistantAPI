from flask import Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config['SECRET_KEY']="hard to guess string"

def scrap_web_page_title(webpage):
    # Get the HTML from the page
    resp = requests.get(webpage)
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    question = 'what is the title'
    title = soup.find('title')
    return title.text

@app.route('/')
def hello_world():
    #text = scrap_web_page_title("https://copyleft.org/")
    return "Hello World! "




if __name__ == '__main__':
    app.run(threaded=True, port=5000)