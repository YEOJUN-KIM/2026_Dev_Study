# Machine Learning

[← 루트로 이동](../README.md)

날짜별 복습본보다는 **한 번에 다시 보기 좋은 대표 노트** 중심으로 정리했습니다. 중복 내용은 제거하고, 짧게 나뉘어 있던 회귀 노트는 합쳤습니다.

## 학습 순서

| 순서 | 주제 | 대표 노트 |
| ---: | --- | --- |
| 01 | Data Preparation | [전처리](./01_Data_Preparation/01_data_preprocessing.ipynb) · [특성공학](./01_Data_Preparation/02_feature_engineering.ipynb) |
| 02 | Regression | [KNN 회귀](./02_Regression/01_knn_regression_basics.ipynb) · [선형/다중 회귀](./02_Regression/02_linear_multiple_regression.ipynb) · [다항 특성](./02_Regression/03_polynomial_features.ipynb) |
| 03 | Regression Project | [주택가격 예측 + 모델비교 + GridSearchCV](./03_Regression_Project/01_housing_price_modeling_and_tuning.ipynb) |
| 04 | Classification | [분류 기초](./04_Classification/01_classification_basics.ipynb) |
| 05 | Ensemble Project | [앙상블 분류](./05_Ensemble_Project/01_ensemble_classification.ipynb) · [와인 분류 프로젝트](./05_Ensemble_Project/02_wine_classification_project.ipynb) |

## 중복 정리 내용

- `3day_Feature_Enginnering`은 후속 `4day` 노트와 대부분 겹쳐 후속본만 유지했습니다.
- 짧은 `wines.ipynb`, `asd` 형태의 복습/초안 중 대표 노트와 겹치는 것은 제외했습니다.
- 선형회귀와 다중회귀는 한 노트북으로 합쳤습니다.
- 주택가격 관련 여러 버전은 가장 완성도가 높은 전체 모델·튜닝 노트 하나로 정리했습니다.
- 앙상블의 짧은 실습본은 전체 실습본과 겹쳐 제거하고, 최종 와인 분류 과제는 프로젝트 노트로 유지했습니다.
- Python/Pandas 기초 복습은 `01_Python`, `03_Data_Pipeline`과 중복되어 ML 폴더에서는 제외했습니다.

## 공용 파일

- [data](./data/) : 머신러닝 학습 데이터셋
- [models](./models/) : 저장한 모델 파일
- [requirements.txt](./requirements.txt) : 머신러닝 패키지

이전: [← Data Pipeline](../03_Data_Pipeline/) · 다음: [React →](../05_React/)
