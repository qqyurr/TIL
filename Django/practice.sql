-- 보기 쉽게 만들기
.headers on
.mode column

INSERT INTO classmates(name,age,address)
VALUES('홍길동',30,'서울');
-- 데이터 삽입 시 'INSERT INTO'를 사용합니다
-- 모든 열에 데이터를 넣을 때는 column을 명시할 필요가 없습니다.

-- SQLite는 따로 primarykey를 정의하지 않으면, rowid가 자동생성된다.
-- primary key는 integer만 사용가능합니다
SELECT rowid, *
FROM classmates;

-- not null을 써서 공백이면 데이터 입력이 불가하게 설정
CREATE TABLE classmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL);

-- 테이블의 구조를 알 수 있습니다.
.schema classmates

CREATE TABLE classmates(
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL);

INSERT INTO classmates
   ...> VALUES('김규연',20,'대한민국'),('규김발',20,'대한민국'),('몰라',20,'대한민국');


SELECT rowid,age
   ...> FROM classmates;


-- LIMIT 갯수제한 OFFSET 위치제한(n번째 가져오고 싶으면 n-1을 적으면 된다.)
SELECT rowid, name
FROM classmates
LIMIT 1 
OFFSET 2;


SELECT rowid, name
FROM classmates
WHERE address='대한민국';

-- column의 값을 중복없이 가져올 때 'DISTINCT'
SELECT DISTINCT age FROM classmates;

-- DELETE
-- SELECT로 내가 지울 값을 가져와본다.
-- 정확히 가져오는지 확인 후 지운다.
DELETE FROM classmates
WHERE rowid=2;

-- autoincrement
CREATE TABLE tests(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);
INSERT INTO tests (name) VALUES('홍길동');
INSERT INTO tests (name) VALUES('김규연');


DELETE FROM tests WHERE id=2;
INSERT INTO tests (name) VALUES('오수완');

-- .shell clear (터미널 clear)

-- DATA 수정
UPDATE classmates
SET name='홍길동', address='제주도'
WHERE rowid=1;

-- csv파일
.mode csv
.import users.csv users


SELECT *
FROM users
WHERE age>=30;

SELECT last_name, age
FROM users
WHERE age>=30 and last_name='김';

SELECT COUNT(*)
FROM users;

SELECT AVG(age)
FROM users
WHERE age>=30;

--  계좌 잔액이 가장 많은 사람과 그 사람 이름
SELECT first_name, MAX(balance)
FROM users;

-- 20대인 사람
SELECT *
FROM users
WHERE age LIKE '2_';

SELECT *
FROM users
WHERE phone LIKE '02-%';

SELECT *
FROM users
WHERE first_name LIKE '%준';

SELECT *
FROM users
WHERE phone LIKE '%-5114-%';


SELECT *
FROM users
ORDER BY age ASC
LIMIT 10;

-- 나이를 기준으로 한 번 정렬하고, 그 뒤 last_name을 기준으로 정렬을 한 번 더
SELECT * 
FROM users
ORDER BY age, last_name ASC
LIMIT 10;

SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;

CREATE TABLE articles(
title TEXT NOT NULL,
content TEXT NOT NULL);

INSERT INTO articles
VALUES('1번제목','1번내용');

-- 테이블명 변경
ALTER TABLE articles 
RENAME TO news;

-- 새로운 컬럼 추가(not null로 추가할 때 (1) not null을 뺴서 넣는다. (2) default값을 넣어서 추가한다.)
ALTER TABLE news
ADD COLUMN created_at TEXT;