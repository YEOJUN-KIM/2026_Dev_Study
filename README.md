# 2026_Dev_Study

2026년 동안 진행한 개발 공부를 **학습 순서와 주제 기준**으로 정리한 저장소입니다.  
날짜별 복습 파일을 그대로 쌓기보다, 같은 내용을 반복한 자료는 합치고 대표 학습 노트 중심으로 정리했습니다.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black" />
</p>

## 🚀 Quick Navigation

| 순서 | 영역 | 주요 내용 | 바로가기 |
| ---: | --- | --- | --- |
| 01 | Python | 문법, 자료구조, 문제 풀이, 알고리즘 | [01_Python README](./01_Python/README.md) |
| 02 | Database & API | SQL, PostgreSQL, FastAPI | [02_Database_and_API README](./02_Database_and_API/README.md) |
| 03 | Data Pipeline | NumPy/Pandas, 전처리, 시각화, 수집, 자동화 | [03_Data_Pipeline README](./03_Data_Pipeline/README.md) |
| 04 | Machine Learning | 전처리·특성공학, 회귀, 분류, 앙상블, 튜닝 | [04_Machine_Learning README](./04_Machine_Learning/README.md) |
| 05 | React | React, Router, Redux, Axios | [05_React README](./05_React/README.md) |

## 🤖 Machine Learning 빠른 이동

| 순서 | 주제 | 핵심 내용 | 이동 |
| ---: | --- | --- | --- |
| 01 | Data Preparation | 결측치·이상치·EDA·특성공학 | [바로가기](./04_Machine_Learning/01_Data_Preparation/README.md) |
| 02 | Regression | KNN, 선형·다중·다항 회귀 | [바로가기](./04_Machine_Learning/02_Regression/README.md) |
| 03 | Regression Project | 주택가격 예측, 모델 비교, GridSearchCV, 저장·예측 | [바로가기](./04_Machine_Learning/03_Regression_Project/README.md) |
| 04 | Classification | 로지스틱/의사결정트리 기반 분류 학습 | [바로가기](./04_Machine_Learning/04_Classification/README.md) |
| 05 | Ensemble Project | 랜덤포레스트·부스팅·성능평가 | [바로가기](./04_Machine_Learning/05_Ensemble_Project/README.md) |

## 📚 Learning Flow

```text
01 Python
   ↓
02 Database & API
   ↓
03 Data Pipeline
   ↓
04 Machine Learning
   ↓
05 React
```

## 📁 Repository Structure

```text
2026_Dev_Study/
├─ 01_Python/
│  ├─ 01_학습노트/
│  ├─ 02_문제풀이/
│  └─ 03_실수목록/
├─ 02_Database_and_API/
│  ├─ 01_SQL/
│  └─ 02_FastAPI/
├─ 03_Data_Pipeline/
│  ├─ 01_foundations/
│  ├─ 02_data_processing/
│  ├─ 03_visualization/
│  ├─ 04_web_data/
│  └─ 05_automation/
├─ 04_Machine_Learning/
│  ├─ 01_Data_Preparation/
│  ├─ 02_Regression/
│  ├─ 03_Regression_Project/
│  ├─ 04_Classification/
│  ├─ 05_Ensemble_Project/
│  ├─ data/
│  └─ models/
├─ 05_React/
├─ ENVIRONMENT.md
└─ README.md
```

## 정리 원칙

- 같은 개념을 반복한 날짜별 노트는 더 완성도 높은 버전만 남겼습니다.
- 내용이 짧고 연속되는 회귀 노트는 하나의 노트북으로 합쳤습니다.
- 머신러닝의 Python/Pandas 복습은 상위 Python·Data Pipeline과 중복되어 제거했습니다.
- 머신러닝 데이터셋은 `04_Machine_Learning/data/`, 저장 모델은 `04_Machine_Learning/models/`에서 공용으로 관리합니다.
- 테스트 데이터는 최종 모델 평가용이라는 흐름을 유지하고, 모델 선택 과정은 검증 데이터 중심으로 정리합니다.

전체 사용 환경은 [ENVIRONMENT.md](./ENVIRONMENT.md)에서 확인할 수 있습니다.
