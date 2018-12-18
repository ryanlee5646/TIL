import os

os.chdir(r'C:\Users\student\gyujin\day02\dummy')
#print(os.getcwd()) ##현재 어떤 폴더에 위치해 있는지 comman word directory

for filename in os.listdir('.'): #os.listdir안에 있는 .은 현재 폴더를 의미함
    file_name = filename.replace('합격자_344', '지원자_344')
    os.rename(filename, file_name)
