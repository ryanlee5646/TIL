# #1 한번에 처리
with open('ssafy.txt','r',encoding='utf8')  as f:
    lines = reversed(f.readlines())
    with open('ssafy_reverse.txt', 'w', encoding='utf8') as p:
        p.writelines(lines)

# #2 read / write 구분해서
# with open('ssafy.txt', 'r',encoding='utf8') as f: #이미 생성되있는  ssafy.txt를 가져와서
#     lines = f.readlines() #ssafy.txt 호출

#     # for line in lines: #ssafy.txt 출력
#     #     print(line.strip())

# with open('ssafy_reverse.txt','w',encoding = 'utf8') as p: # ssafy_reverse.txt를 새로 만듬
#     p.writelines(reversed(lines)) #뒤집어서 출력
