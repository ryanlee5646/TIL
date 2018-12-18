# f = open('ssafy.txt','w')     #w: write, r: read, a: append
# f.write('This is SSAFY')
# f.close()

with open('ssafy.txt','w',encoding='utf8') as f:
    #for i in range(10):  
    f.writelines(['1\n' '2\n' '3\n'])
        # \t: tab, \\: 
        # '\\:' 문자 그대로 의미
        # \' or \" : 따옴표, 쌍따옴표 문자

