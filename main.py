from flask import Flask,jsonify,request
import csv
from demographicflitering import output 
from contentbasedfiltering import get_recomdations

all_movies=[]
with open('final.csv',encoding='utf-8')as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

# print(all_movies)
liked_movies=[]
not_liked_movies=[]
did_not_watched=[]

app=Flask(__name__)
@app.route('/get-movie')
def get_movie():
    movie_data = { 
        "title": all_movies[1][6], 
        "poster_link": all_movies[1][22],
        "release_date": all_movies[1][11] or "N/A", 
        "duration": all_movies[1][13], 
        "rating": all_movies[1][16], 
        "overview": all_movies[1][7]
     } 
    return jsonify({ "data": movie_data, 
    "status": "success" 
    })
    #    return jsonify({
    #     "data": all_movies[1][0],
    #     "status": "success"
    # })

@app.route('/liked_movies',methods=['POST'])   
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movie.append(movie)
    return jsonify({
        'status':'success'
    },201)

@app.route('/not_liked_movies',methods=['POST'])
def not_liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        'status':'success'
    },201)

@app.route('/did_not_watched',methods=['POST'])
def did_not_watched():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watched.append(movie)
    return jsonify({
        'status':'success'
    },201)

@app.route('/popular_movies')
def popular_movies():
    movie_data=[]
    for movie in output:
        data={
            'title':movie[0],
            'imdb_link':movie[1],
            'release_date':movie[2] or 'n/a',
            'vote_average':movie[3],
            'overview':movie[4]

        }
        movie_data.append(data)
        print(movie_data)
    return jsonify({
        'status':'success',
        'data':movie_data
    },201)

@app.route('/recomended_movies')
def recomended_movies():
    movie_data=[]
    for movie in liked_movies:
        output=get_recomdations(liked_movies[6])
        for data in output:
            movie_data.append(data)
    
    import itertools
    movie_data.sort()
    movie_data=list(movie for movie,_ in itertools.groupby(movie_data))
    all_recomended=[]
    for movie in movie_data:
        data={
            'title':movie[0],
            'imdb_link':movie[1],
            'release_date':movie[2] or 'n/a',
            'vote_average':movie[3],
            'overview':movie[4]

        }
        all_recomended.append(data)
    return jsonify({
        'status':'success',
        'data':'all_recomended'
    },201)

if __name__=='__main__':
    app.run(debug=True)
