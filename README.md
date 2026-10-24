# 2026_Dev_Study

2026년 동안 학습한 개발 기술과 실습 코드를 **주제별로 정리한 개인 학습 아카이브**입니다.

단순히 강의 파일을 모아두기보다, 각 영역에서 **무엇을 배우고 어떤 실습을 했는지 빠르게 확인할 수 있도록** 구성했습니다. Python 학습 자료는 기존 정리 내용을 그대로 보존하고, Database/API·Data Pipeline·React 영역은 중복 예제와 불필요한 설치 문서를 줄여 보기 편하게 재구성했습니다.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Vite-8-646CFF?logo=vite&logoColor=white" />
</p>

## Study Areas

### 01. Python
Python 기본 문법부터 함수·클래스, 자료구조, 예외 처리, 파일 처리와 문제 풀이까지 학습한 내용을 정리했습니다.

기존에 정리해 둔 학습 노트와 문제 풀이 기록을 그대로 보존했습니다.

**Keywords:** `Python` `Data Types` `Functions` `Classes` `File I/O` `Problem Solving`

### 02. Database & API
PostgreSQL을 이용해 SQL의 기본 CRUD부터 관계형 모델, JOIN, 집계, 트랜잭션을 학습했습니다. 이후 FastAPI에서 REST API를 구성하고 PostgreSQL과 연결하는 흐름까지 실습했습니다.

**Keywords:** `PostgreSQL` `SQL` `CRUD` `JOIN` `Transaction` `FastAPI` `Pydantic` `psycopg`

### 03. Data Pipeline
NumPy/Pandas 기초부터 데이터 입출력·전처리·집계·시각화, 웹 스크래핑, Selenium 자동화까지 데이터가 수집되고 활용되는 흐름을 단계적으로 학습했습니다.

**Keywords:** `NumPy` `Pandas` `Data Cleaning` `Visualization` `Selenium` `BeautifulSoup` `Automation`

> 회귀 모델 학습 자료는 추후 별도 실습 파일을 추가해 `06_machine_learning` 영역을 보강할 예정입니다.

### 04. React Web
React에서 컴포넌트와 라우팅을 구성하고, Axios 기반 API 연동, Redux Toolkit 상태관리, 인증 UI, 게시판/상품/채팅 기능 등을 실습했습니다.

**Keywords:** `React` `React Router` `Redux Toolkit` `Axios` `Ant Design` `MQTT`

## Learning Flow

```text
Python
  ↓
Database & API
  ↓
Data Processing / Pipeline
  ↓
React Web
```

각 기술을 하나의 프로젝트로 억지로 연결한 것이 아니라, **2026년 동안 개발 기초부터 데이터 처리와 웹 개발까지 학습 범위를 넓혀 간 과정**을 한 저장소에서 보여주는 것을 목표로 합니다.

## Repository Structure

```text
2026_Dev_Study/
├─ Python/                    
├─ 01_Database_and_API/
│  ├─ sql/
│  └─ fastapi/
├─ 02_Data_Pipeline/
│  ├─ 01_foundations/
│  ├─ 02_data_processing/
│  ├─ 03_visualization/
│  ├─ 04_web_data/
│  ├─ 05_automation/
│  ├─ 06_machine_learning/
│  └─ data/
├─ 03_React/
├─ ENVIRONMENT.md
└─ README.md
```

## About This Repository

이 저장소의 목적은 하나의 완성 서비스를 제공하는 것이 아니라, **2026년에 공부한 개발 영역과 실습 과정을 한 곳에서 확인할 수 있도록 기록하는 것**입니다.

설치 방법이나 실행 가이드를 중심으로 하기보다, 실제 학습 코드와 주제별 내용을 빠르게 살펴볼 수 있도록 정리했습니다.
