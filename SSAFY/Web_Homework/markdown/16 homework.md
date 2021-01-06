* **다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.**

  ```sqlite
  CREATE TABLE friends(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name  TEXT NOT NULL,
  location TEXT NOT NULL
  );
  ```

* **해당 테이블에 다음과 같이 데이터를 입력한다.**

```sqlite
INSERT INTO friends (name, location) VALUES ('Justin', 'Seoul');
INSERT INTO friends (name, location) VALUES ('Simon', 'New York');
INSERT INTO friends (name, location) VALUES ('Chang', 'Las Vegas');
INSERT INTO friends (name, location) VALUES ('John', 'Sydney');

```

* 스키마를 다음과 같이 변경한다.

```sqlite
ALTER TABLE friends ADD married INT;
```

* 데이터를 다음과 같이 추가한다.

```sqlite
UPDATE friends SET married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
```



* 

```sqlite
DELETE FROM friends WHERE married=0;
```

