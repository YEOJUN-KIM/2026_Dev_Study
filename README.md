# 2026_Dev_Study

2026년 동안 **데이터를 다루고, 저장하고, API로 연결하고, 웹에서 활용하는 전체 개발 흐름을 이해하고 직접 구현할 수 있는 기반을 만들기 위해** 학습한 내용을 정리한 저장소입니다.

Python을 시작으로 Database와 API, Data Processing / Pipeline, React Web까지 학습 범위를 단계적으로 확장하며  
각 기술을 개별적으로 익히는 데서 끝나지 않고, **하나의 서비스가 만들어지는 과정에서 각 기술이 어떤 역할을 하는지 이해하는 것**을 목표로 공부하고 있습니다.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Vite-8-646CFF?logo=vite&logoColor=white" />
</p>

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

- **Python**으로 프로그래밍 기초와 데이터 처리 기반을 익히고
- **Database & API**를 통해 데이터를 저장하고 외부와 연결하는 방법을 학습하며
- **Data Processing / Pipeline**에서 데이터를 수집·가공·분석하는 흐름을 확장하고
- **React Web**으로 데이터를 실제 사용자 화면에서 활용하는 과정을 학습하고 있습니다.

향후에는 이 흐름 위에 데이터 분석과 머신러닝 모델 학습까지 연결해,  
**데이터 수집 → 처리 → 저장 → API → 웹 서비스 → 모델 활용**로 이어지는 개발 과정을 직접 구현할 수 있는 역량을 갖추는 것을 목표로 합니다.

## Study Areas

### [01. Python](./Python/)
Python 기본 문법부터 함수·클래스, 자료구조, 예외 처리, 파일 처리와 문제 풀이까지 학습한 내용을 정리했습니다.

기존에 정리해 둔 학습 노트와 문제 풀이 기록을 그대로 보존하고 있습니다.

**Keywords:** `Python` `Data Types` `Functions` `Classes` `File I/O` `Problem Solving`

---

### [02. Database & API](./01_Database_and_API/)
PostgreSQL을 이용해 SQL의 기본 CRUD부터 관계형 데이터 모델, JOIN, 집계, 트랜잭션을 학습했습니다.

이후 FastAPI를 활용해 REST API를 구성하고 PostgreSQL과 연결하며,  
**데이터베이스의 데이터를 애플리케이션에서 사용할 수 있도록 연결하는 백엔드 흐름**을 실습했습니다.

**Keywords:** `PostgreSQL` `SQL` `CRUD` `JOIN` `Transaction` `FastAPI` `Pydantic` `psycopg`

---

### [03. Data Processing / Pipeline](./02_Data_Pipeline/)
NumPy와 Pandas를 기반으로 데이터 입출력, 전처리, 집계, 시각화부터 웹 스크래핑과 Selenium 자동화까지 학습했습니다.

단순한 데이터 분석을 넘어 **데이터가 수집되고, 정리되고, 다음 단계에서 사용할 수 있는 형태로 가공되는 과정**을 이해하는 데 초점을 두고 있습니다.

**Keywords:** `NumPy` `Pandas` `Data Cleaning` `Visualization` `Selenium` `BeautifulSoup` `Automation`

> 회귀 모델 학습 자료는 추후 추가하여 데이터 전처리 → 스케일링 → 모델 학습 → 평가 → 저장 → 예측 흐름까지 확장할 예정입니다.

---

### [04. React Web](./03_React/)
React에서 컴포넌트와 라우팅을 구성하고, Axios 기반 API 연동, Redux Toolkit 상태 관리, 인증 UI, 게시판·상품·채팅 기능 등을 실습했습니다.

백엔드와 데이터 처리 영역에서 만들어진 데이터를 **사용자가 실제로 확인하고 상호작용할 수 있는 웹 화면으로 연결하는 과정**을 학습했습니다.

**Keywords:** `React` `React Router` `Redux Toolkit` `Axios` `Ant Design` `MQTT`

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

## Development Environment

사용한 주요 언어와 도구의 간단한 환경 정보는 [ENVIRONMENT.md](./ENVIRONMENT.md)에서 확인할 수 있습니다.
