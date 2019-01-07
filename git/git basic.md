# Git & GitHub

## Git에 내 정보 설정

* `git config --global user.name 'Gyujin Lee'`:  이름 설정
* `git config --global user.email 'ryanlee5646@gmail.com'`: 이메일 설정
* `git config --global --list` : 정보 설정 확인

## Git repo를 처음 생성한 경우

* `git init` :  git 초기화, 지금 폴더를 git으로 관리하겠다. (관리하려는 폴더 안에서 입력)
* `git remote add origin  주소`: 원격 저장소(remote repository) 주소 등록
  * `git remote set-url origin 주소`: 원격 저장소 수정



## Git repo clone한 경우

* `git clone 주소`: 이 주소로 부터 내용 내려받기
  * 이 경우에는 `git init, git remote add origin` 주소를 하지 않아도 이미 다 되어있다.

## Git Commit & Push

* `git status`: 현재 폴더의 git의 상태 확인
* `git add .`: 현재 폴더의 변경사항들을 commit하기 위하여 준비
  * `.`은 현재 파일의 모든 사항을 추가하는 것이며, `.`이 아닌 특정 **파일 이름**도 가능.
* `git commit -m 'D04 | 190107 AM | Git & CLI'`: commit, 변경 사항 저장. `''`안에 있는 메세지는 자유롭게 작성 가능.
* `git push -u origin master`:  remote로 등록된 원격 저장소에 commit한 것들 올리기
  * 이 후에는 `git push`만 입력해도 동작. `git clone` 을 한경우에도 해당함.
  * 이 컴퓨터에서 최초 push인 경우, 로그인 창이 뜨며 로그인을 해줍니다. 

## Git Pull

* git pull: Github에 올라가 있는 내용들, 즉 commit들을 내려받는 것.
* 아침에 오자마자 git pull 한번 하고 시작합시다!



## Git & GitHub 재설정

```bash
# Git 이름, 이메일 재설정
git config --global user.name 'Gyujin Lee'
git config --global user.email
'ryanlee5646@gmail.com'

# GitHub 로그인 정보 초기화
git credential rejct (#아래명령어는 다 붙여서 써야함)
protocol=https
host=github.com
```

