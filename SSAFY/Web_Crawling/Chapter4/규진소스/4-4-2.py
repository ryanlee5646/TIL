import simplejson as json
# import json

# Dict(Json) 선언

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website': 'naver.com',
    'from':'Seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'Park',
    'website': 'google.com',
    'from':'Busan',
    'grade':[85,67,100,93]
})
data['people'].append({
    'name':'Lee',
    'website': 'daum.com',
    'from':'Daegu',
    'grade':[77,98,97,44]
})

# print(data)

# sjon 파일쓰기(dump)
with open('C:/Users/student/Desktop/section4/member.json','w') as outfile:
    json.dump(data, outfile)

with open('C:/Users/student/Desktop/section4/member.json','r') as infile:
    r = json.load(infile)
    # print(type(r))
    # print(r)
    print("===============")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' + str(g)
        print('Grade:',grade.lstrip()) # lstrip 줄바끔
        print(' ')
