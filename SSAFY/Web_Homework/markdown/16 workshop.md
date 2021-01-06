**해당 테이블을 수정하여, 다음과 같이 컬럼을 추가하고, 데이터를 삽입하라**.

```sqlite
ALTER TABLE bands ADD COLUMN members INT;
UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;
```

**Id 가3인레코드의members를5로수정하라.**

```sqlite
UPDATE bands SET members=5 WHERE id=3;
```



**Id가2인레코드를삭제하라**

```sqlite
DELETE FROM bands WHERE id=2;
```

