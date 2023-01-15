
import requests
import app.scrapwebpage as sw
import app.databasehelper as db
from bs4 import BeautifulSoup
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY']="hard to guess string"

def getFormattedURL(website):
    inputArray = website.split()
    url = "https://"
    for i in range(len(inputArray)):
        url += inputArray[i]
    return url.lower()

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
    #value = jh.JsonHelper.read_from_json_data()
    return "success"


@app.route('/scrapsource/<website>', methods=['GET'])
def getSource(website):
    url = getFormattedURL(website)
    value = sw.ScrapWebPage.scrap_web_page_source(url)
    return value



@app.route('/populatedatabase/<website>', methods=['GET'])
def populatedatabase(website):
    url = getFormattedURL(website)
    #sw.ScrapWebPage.scrap_web_page_title(url)
    #sw.ScrapWebPage.scrap_web_page_paragraph(url)
    #sw.ScrapWebPage.scrap_web_page_header(url)
    #sw.ScrapWebPage.scrap_web_page_link(url)
    #sw.ScrapWebPage.scrap_web_page_source(url)
    return "success"


@app.route('/getdatabyquestioncleaned/<website>/<question>', methods=['GET'])
def getDataByQuestionCleaned(website, question):
    url = getFormattedURL(website)
    value = db.DatabaseHelper.findDataByQuestion_Cleaned(question, url)
    return value

@app.route('/getdatabyquestionjson/<website>/<question>', methods=['GET'])
def getDataByQuestionJson(website, question):
    url = getFormattedURL(website)
    value = db.DatabaseHelper.findDataByQuestion_Json(question, url)
    return value


if __name__ == '__main__':
  #  app.run(threaded=True, port=8001)
    app.run()