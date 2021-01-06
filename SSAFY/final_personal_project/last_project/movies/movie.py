import requests
import json


page = 4
result = []
num = 1
for i in range(1,page):
    res = requests.get("https://api.themoviedb.org/3/movie/now_playing?api_key=fbba0ab051a2676aeb15855cbf738aed&language=ko-KR&page="+str(i))  # 페이지 번호를 기준으로 데이터를 받아옴 
    data = res.json()
    for mv in data['results']:
        movie_data = {}
        movie_data['pk'] = num
        movie_data['model'] = "movies.movie"
        movie_data['fields'] = {
            'movie_id' : mv['id'],
            'title_kr' : mv['title'], # 한국어 제목
            'title_en' : mv['original_title'], # 영문 제목
            'poster_path' : mv['poster_path'] if mv['poster_path'] else "", # 포스터 
            'overview' : mv['overview'], # 개요
            'genres' : mv['genre_ids'], # 장르가 배열형태로 들어감
            'release_date': mv['release_date'],
            'vote_count' : mv['vote_count'],
            'vote_average': mv['vote_average'],
            
        }
        num+=1
        result.append(movie_data)
        
with open('movie.json','w',encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\n")    