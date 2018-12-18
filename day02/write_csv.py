home = {
    '서민수':'진평동',
    '강대현':'진평동',
    '권민재':'인의동'
}

import csv

with open('home.csv','w',encoding='utf8',newline='') as f:
    csv_writer = csv.writer(f)
    for item in home.items():      #List의 형태로 [(key, value), ...]
        csv_writer.writerow(item) ##csv함수를 쓰게되면 아랫줄에 개행을 놔눠주는 입력을 하지않아도 알아서 다해줌
        # f.write(f'{item[0]},{item[1]}\n')