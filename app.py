from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask import Flask,render_template,request 
app = Flask(__name__)

def get_ArticleFirstParagraph(searchTerm):
    searchTerm = request.form['searchInput']
    fullURL = baseURL+searchTerm
    html = urlopen(fullURL).read()
    content = BeautifulSoup(html, "html.parser")
    paragraphs = content.find_all("p")
    for para in paragraphs:
        if(searchTerm.lower() in para.text.lower()):
            return para.text

baseURL = 'https://en.wikipedia.org/wiki/'
@app.route('/',methods=['POST','GET'])
def index():   
    if request.method == 'POST':
        searchTerm = request.form['searchInput']
        # fullURL = baseURL+searchTerm
        # html = urlopen(fullURL).read()
        # content = BeautifulSoup(html, "html.parser")
        # paragraphs = content.find_all("p")
        # for para in paragraphs:
        #     if(searchTerm.lower() in para.text.lower()):
        #         return para.text
        return get_ArticleFirstParagraph(searchTerm)
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
