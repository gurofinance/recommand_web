from flask import Flask , render_template , request
import requests
import json
from datetime import date
from fetch import movie, movie_collection
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
    if request.method == 'GET':
        year = date.today().year
        year_url = f'http://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year={year}&sort_by=popularity.desc'
        result = json.loads(requests.get('https://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&primary_release_year=2022&sort_by=popularity.desc').text)
        # print(result['results'][1])
        top_year = movie_collection()
        top_year.fetch(year_url)
        genre_url =f'https://api.themoviedb.org/3/genre/movie/list?api_key=da396cb4a1c47c5b912fda20fd3a3336&language=en-US'
        genres = json.loads(requests.get(genre_url).text)
        # print(genres)
        top_genre_collection = []
        for data in genres['genres']:
            # print(data['id'])
            genre_id = f'https://api.themoviedb.org/3/discover/movie?api_key=da396cb4a1c47c5b912fda20fd3a3336&with_genres={data["id"]}&sort_by=popularity.desc'
            # print(genre_id)
            top_genre = movie_collection()
            top_genre.fetch(genre_id)
            # for result in top_genre.results:
            #     print(result.title)
            top_genre_id = [top_genre.results , data['name']]
            top_genre_collection.append(top_genre_id)
        # print(top_genre_collection)
        return render_template('index.html',top_year = top_year.results, year= year, top_genre=top_genre_collection)

if __name__ =='__main__':
    app.run(port=5000, debug=True)