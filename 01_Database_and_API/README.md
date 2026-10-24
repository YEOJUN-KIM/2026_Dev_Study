# Database & API

PostgreSQL을 이용한 관계형 데이터베이스 학습과 FastAPI 기반 API 실습을 한 영역으로 정리했습니다.
강의 순서보다 **데이터를 저장하고 조회한 뒤 API에서 활용하는 흐름**이 보이도록 재구성했습니다.

## 학습 내용

- PostgreSQL 기본 구조와 SQL CRUD
- 조건 조회, 정렬, 패턴 검색, NULL 처리
- PK/FK를 이용한 관계형 테이블 설계
- JOIN, 집계 함수, GROUP BY / HAVING
- COMMIT / ROLLBACK 트랜잭션
- FastAPI 라우팅과 Pydantic 데이터 검증
- 메모리 기반 REST CRUD
- `psycopg`를 이용한 PostgreSQL 조회/등록
- 환경변수를 이용한 DB 연결정보 분리

## 구성

```text
sql/
├─ 01_schema_and_crud.sql
├─ 02_filter_sort_query.sql
├─ 03_product_crud_practice.sql
├─ 04_relational_model.sql
└─ 05_joins_aggregation_transactions.sql

fastapi/
├─ 01_memory_crud.py
└─ postgresql/
   ├─ database.py
   └─ main.py
```

> FastAPI는 별도 대형 프로젝트가 아니라, DB 학습 과정에서 API와 DB 연동 흐름을 익힌 실습으로 정리했습니다.
