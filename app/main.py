
import requests
import app.scrapwebpage as sw
import app.jsonhelper as jh
import app.matcher as m
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
    #sw.ScrapWebPage.scrap_web_page_title("https://copyleft.org/")
    #text = scrap_web_page_title("https://copyleft.org/")
    #value = jh.JsonHelper.read_from_json_data()
    return "status up"

@app.route('/scraptitle/<website>', methods=['GET'])
def scrapTitle(website):
    url = getFormattedURL(website)
    sw.ScrapWebPage.scrap_web_page_title(url)
    value = jh.JsonHelper.read_from_json_data()
    return value


@app.route('/scrapsource/<website>', methods=['GET'])
def scrapSource(website):
    url = getFormattedURL(website)
    value = sw.ScrapWebPage.scrap_web_page_source(url)
    return value

@app.route('/matcher/<question>', methods=['GET'])
def matcher(question):
    value = m.Matcher.getResults(question, m.Matcher.getNaiveAnswer)
    values = value.values.tolist()
    currentValue = values[0]
    text = jh.JsonHelper.get_json_byQuestion(currentValue[0])
    return text


@app.route('/populatejson/<website>', methods=['GET'])
def populateJson(website):
    url = getFormattedURL(website)
    sw.ScrapWebPage.scrap_web_page_title(url)
    sw.ScrapWebPage.scrap_web_page_paragraph(url)
    sw.ScrapWebPage.scrap_web_page_header(url)
    sw.ScrapWebPage.scrap_web_page_link(url)
    return "success"

if __name__ == '__main__':
  #  app.run(threaded=True, port=8001)
    app.run()