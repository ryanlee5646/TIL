import simplejson as json
# import json
# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website': 'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Park',
    'website': 'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Lee',
    'website': 'daum.com',
    'from':'Daegu'
})

# print(data)
# Dict(Json) -> Str
e = json.dumps(data,indent=2) # 한줄로 나오는 json을 들여쓰기 해주는 indent
# print(type(e))
# print(e)

# Str -> Dict(json)
d = json.loads(e)
# print(type(d))
# print(d)

with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
    outfile.write(e)

with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    # print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
