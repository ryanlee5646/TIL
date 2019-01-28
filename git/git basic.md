# Git & GitHub

## Git repository를 clone한 경우

#### *새로운* 자리에 깃 동기화 하는 방법

#### 1. 복사하고자 하는 폴더를 Github에서 가져 오기.

```
git clone <깃헙 복사된 주소> [폴더명]
```

예) `git clone https://github.com/ryanlee5646/TIL.git`

개인 설정을 하지 않은 상태에서 내려 받을 수 있는 이유?

- TIL repository 는 public으로 공개 설정되어있기 때문에, 누구나 다운로드는 사용 가능.

- but 업로드 및 수정은 권한이 있는 사람만 가능.

- git clone으로 내려 받은 파일/폴더는 git init/git remote add origin 등을 할 필요 없음

  (이미 git으로 관리 되고 있기 때문임)

#### 2. Git bash에 입력된 기존의 계정 정보 삭제하기

#### (그대로입력)

```
git credential reject
protocol=https
host=github.com
```

#### 3. 새로운 계정 정보 입력하기

`git push` 후 계정 로그인 하기

#### 4. Git내 정보 설정

`git config --global --list` : git에 저장된 정보 설정 확인

`git config --global user.name 'Gyujin Lee' `: 이름 설정

`git config --global user.email 'ryanlee5646@gmail.com'` : 이메일 주소설정

커밋을 작성할 때, 깃이라는프로그램에 커밋한 사람에 대한 정보를 알려주기 위한 용도.

`git log` : git에서 commit 시 저장된 user name 과 user email의 정보 확인 가능.

*public으로 공개된 타인의 폴더를 clone으로 내려 받은 후, push가 가능한가?*

*commit은 누구나 할 수있음 (git log시, commit된 정보가 update된 것을 알 수 있 음)*

*그러나 git push 시, 권한이 없어 git push가 deny 됨. (하위 deny message참조요망)*

> remote: Permission to sgmpy/materials.git denied to harrylee0810. fatal: unable to access '<https://github.com/sgmpy/materials.git/>': The requested URL returned error: 403

```
#Git이름, 이메일 재설정
git config --global user.name 'Gyujin Lee'
git config --global user.email 'ryanlee5646@gmail.com'

#GitHub 로그인 정보 초기화
git credential reject
protocol=https
host=github.com
```

## Git repository를 처음 생성한 경우

`git init` : git 초기화. 지금 폴더를 git으로 관리하겠다!

(관리하려는 폴더 내에서 입력 할 것)

`git remote add origin 주소 `: 원격 저장소 (remote repository) 주소 등록

`git remote set-url origin 주소` : 원격 저장소 수정

(ex. 기존 폴더를 github에서 gitlab으로 옮기고 싶을때)

`git remote -v`: 이 폴더를 푸쉬할수있는 주소들이 보임

`git remote add (설정할 별칭) 주소`: 별칭을 설정하지 않으면 origin값으로 설정됨. 

ex )`git remote add github https://github.com/ryanlee5646/homeworkshop.git`        

origin 기본주소가 아닌 다른 주소로 push 하고 싶을때는

`git push 별칭(github) master`





## Git Commit & Push

- `git status` : 현재 폴더의 git 의 상태 확인

- `git add .` : 현재 폴더의 변경사항들을 commit하기 위하여 준비

  ​	`.` 대신에 특정 파일 이름도 가능

- `git commit -m 'D04 | 190107 AM | Git & CLI'` : commit, 변경사항 저장. `''`안에 있는 메세지는 자유롭게 작성 가능.

- `git push -u origin master` : remote로 등록된 원격 저장소에 commit한 것들 올리기

  - 이후에는 git push만 입력해도 동작함. (`git clone`을 한경우에도 해당됨)
  - 이 컴퓨터에서 최초 push인 경우, 로그인 창이 뜨며 로그인을해줍니다.

## Git pull

- `git pull` : GitHub에 올라가 있는 내용들, 즉 commit들을 내려받는 것.
- 아침에 오자마자 `git pull` 한번 하고 시작합시다!