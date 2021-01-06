## Oracle(오라클)



#### 설치방법

**링크**: https://stophyun.tistory.com/190

**MacOS 환경**

맥os 환경에서는 오라클을 직접 설치 할 수가 없다.

그래서 Docker를 통해서 설치해야한다.

**Docker 설치 순서**

1. Docker 회원가입
2. Docker 다운로드 및 설치
3. 응용프로그램 등록

**Oracle 설치 및 실행**

1. `docker login` : Docker(도커) 계정에 로그인

2. `docker pull jaspeen/oracle-xe-11g` : Oracle 설치(Oracle-11g)
3. `docker run --name oracle11g -d -p 8080:8080 -p 1521:1521 jaspeen/oracle-xe-11g` : 이미지 실행

4. `docker exec -it oracle11g sqlplus`: 오라클 실행
   * User-name : `system`
   * password : `oracle`

**Oracle SQL Developer(GUI)를 설치 및 실행**



`docker images`: 현재 가상환경보기

`docker ps -al`: 현재 프로세서 보기

`docker start c33f5b34d7ad`: 가상환경 ID로 시작

`docker stop c33f5b34d7ad` : 가상환경 ID로 끝