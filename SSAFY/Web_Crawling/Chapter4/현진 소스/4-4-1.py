import simplejson as simplejson
import json

# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})
data['people'].append({
    'name':'Kim',
    'website':'google.com',
    'from':'Busan'
})
data['people'].append({
    'name':'Kim',
    'website':'daum.net',
    'from':'Incheon'
})

# print(data)

# {'people': [{'name': 'Kim', 'from': 'Seoul', 'website': 'naver.com'}, {'name': 'Kim', 'from': 'Busan', 'website': 'google.com'}, {'name': 'Kim', 'from': 'Incheon', 'website': 'daum.net'}]}

# Dict(Json) -> Str
e = json.dumps(data, indent=4)
# print(type(e))
# print(e)

# Str -> Dict(Json)
d = json.dumps(e)
# print(type(d))
# print(d)

with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
    outfile.write(e)


with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('Name:' + p['name'])
        print('website:' + p['website'])
        print('From:' + p['from'])
        print('')
