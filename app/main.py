
import requests
import app.scrapwebpage as sw
import app.jsonhelper as jh
from bs4 import BeautifulSoup
from flask import Flask

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



def getFormattedURL(website):
    inputArray = website.split()
    url = "https://"
    for i in range(len(inputArray)):
        url += inputArray[i]
    return url

@app.route('/')
def hello_world():
    sw.ScrapWebPage.scrap_web_page_title("https://copyleft.org/")
    #text = scrap_web_page_title("https://copyleft.org/")
    value = jh.JsonHelper.read_from_json_data()
    return value

@app.route('/scraptitle/<website>', methods=['GET'])
def scrapTitle(website):
    inputArray = website.split()
    url = "https://"
    for i in range(len(inputArray)):
        url += inputArray[i]
    website = url
    sw.ScrapWebPage.scrap_web_page_title(url)
    value = jh.JsonHelper.read_from_json_data()
    return value


@app.route('/scrapsource/<website>', methods=['GET'])
def scrapSource(website):
    url = getFormattedURL(website)
    value = sw.ScrapWebPage.scrap_web_page_source(url)
    return value


if __name__ == '__main__':
  #  app.run(threaded=True, port=8001)
    app.run()