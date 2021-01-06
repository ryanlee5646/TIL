import requests
import json

result = []

res = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=fbba0ab051a2676aeb15855cbf738aed&language=ko-KR")  # 페이지 번호를 기준으로 데이터를 받아옴 
data = res.json()

for r in data['genres']:
    genre_data = {}
    genre_data['pk'] = r["id"]
    genre_data['model'] = "movies.genre"
    genre_data['fields'] = {
        'name' : r['name'],
    }
    result.append(genre_data)
    
with open('genre.json','w',encoding='utf-8') as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\n")    