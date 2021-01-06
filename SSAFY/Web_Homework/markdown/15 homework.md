1. 우리가 사용하는 **SQLite**는 **RDBMS**에 속한다. RDBMS의 특징을 2가지 만작성하세요.

  ```
  1. 모든 데이터를 2차원 테이블로 표현
  2. 테이블은 row(record, tuple)과 column(field, item)으로 이루어진 기본 데이터 저장 단위
  3. 만들거나 이용하기도 비교적 쉽지만, 무엇보다도 확장이 용이하다는 장점을 가짐
  4. 상호 관련성을 가진 테이블의 집합
  ```

  

2. **True False**
     2.1. RDBMS를 조작하기 위해서는 SQL문을 사용한다. **[ T ]**

     2.2. SQL에서 명령어는 대문자로 써야만 동작한다. **[ F ]**

     * 소문자도 가능하나, 대문자를 권장

     2.3. 일반적인 SQL문에서 명령어는 세미콜론(;) 으로 끝난다. **[ T ]**

     * 세미콜론(;)단위로 명령어(Query)로 간주함

     2.4. SQLite에서 dot(.)으로 시작하는 명령어는 SQL이 아니다. **[ T ]**

     * .은 sqlite3 프로그램의 기능을 실행하는 것.

     2.5. 한 개의 DB에는 한개의 테이블만 존재한다. **[ F ]**

     

3. **다음코드의 실행결과로 나타나는 값을 작성하세요.**

  ```sqlite
  sqlite> .nullvalue “NULL”
  sqlite> CREATE TABLE ssafy (
  …> id INTEGER,
  …> location TEXT,
  …> class INTEGER
  …> );
  sqlite> INSERT INTO ssafy (id, location)
  …> VALUES (1, ‘JEJU’);
  sqlite> SELECT class FROM ssafy WHERE id=1;
  ```

  ```
  ------
  "NULL"
  ```

  