from flask import Flask , render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
    result = json.loads(requests.get('https://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year=2022&sort_by=popularity.desc').text)
    print(result['results'][1])
    return render_template('index.html', data=result)

if __name__ =='__main__':
    app.run(port=5000, debug=True)