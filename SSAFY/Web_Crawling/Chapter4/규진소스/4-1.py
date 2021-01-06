import pickle # (객체, 텍스트) 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = "C:/Users/student/Desktop/section4/test.bin"
tfilename = "C:/Users/student/Desktop/section4/test.txt"

data1 = 77
data2 = 'Hello, world'
data3 = ["car", "apple", "house"]

# 바이너리 쓰기
with open(bfilename, "wb") as f: # wright binary
    # dump (객체를 바이너리로 쓸 때)
    # dumps(문자열 직렬화)
    pickle.dump(data1,f)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

# 텍스트 쓰기
with open(tfilename, 'wt') as f: # write text
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3)) # data3은 리스트형태라서 write로 받지 못함

# 바이너리 읽기
# 받은 데이터를 바이너리로 직렬화 시켜 보낸뒤 그거를 다시 역직렬화 시켜주는 모듈 pickle
# 텍스트는 관계없이 string형태로 받음
with open(bfilename, 'rb') as f: # read binary
    b = pickle.load(f) # loads(문자열 역직렬화)
    print(type(b), 'Binary Read1 |', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read2 |', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3 |', b)
# <class 'int'> Binary Read1 | 77
# <class 'str'> Binary Read2 | Hello, world
# <class 'list'> Binary Read3 | ['car', 'apple', 'house']
# pickle를 통해 역직렬화 해서 출력한 건 자료형 형태를 유지

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + ' | ', line, end='')
# <class 'str'> Text Read1 |  77
# <class 'str'> Text Read2 |  Hello, world
# <class 'str'> Text Read3 |  car
# <class 'str'> Text Read4 |  apple
# <class 'str'> Text Read5 |  house

# 한번 text file로 쓴거는 text로 저장되어 읽어와도 자료형이 string이 됨
