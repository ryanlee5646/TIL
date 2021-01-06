* **bands 테이블에서 모든 데이터 레코드의 id와 name만 조회하는 Query를 작성하라.**

  ​                                  **Table Name : bands**

  | id(INTEGER) | name(TEXT) | debut(INTEGER) |
  | ----------- | ---------- | -------------- |
  | 1           | Queen      | 1973           |
  | 2           | Coldplay   | 1998           |
  | 3           | MCR        | 2001           |

  

```sqlite
CREATE TABLE bands (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
debut INT NOT NULL
);
INSERT INTO bands (name, debut) VALUES ('Queen', 1973);
INSERT INTO bands (name, debut) VALUES ('Coldplay',1998);
INSERT INTO bands (name, debut) VALUES ('MCR', 2001);  

```



```sqlite
SELECT id, name FROM bands 
```



* **bands 테이블에서 debut가 2000보다 작은 밴드들의 이름만을 조회하는 Query를 작성하라.**

```sqlite
SELECT name FROM bands WHERE debut<2000;
```







