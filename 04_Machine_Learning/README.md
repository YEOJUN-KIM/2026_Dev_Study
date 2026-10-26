# Machine Learning

[← 루트로 이동](../README.md)

머신러닝 학습 순서를 파일 번호로 바로 확인할 수 있도록 노트북을 한 폴더에 정리했습니다.  
이미 배운 데이터 준비 과정은 한 셀로 묶고, 새로 배우는 개념과 모델은 단계별로 나누어 기록합니다.

## 실행 환경

```bash
cd 04_Machine_Learning
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

필요한 패키지 설치:

```bash
pip install -r requirements.txt
```

VS Code에서는 `.ipynb`의 Kernel을 `.venv` Python으로 선택합니다.

## 학습 순서

| 순서 | 내용 | 이동 |
| ---: | --- | --- |
| 01 | 결측치·이상치·중복값 등 데이터 전처리 | [01_data_preprocessing.ipynb](./01_data_preprocessing.ipynb) |
| 02 | 분포·상관관계·인코딩·스케일링 등 특성 엔지니어링 | [02_feature_engineering.ipynb](./02_feature_engineering.ipynb) |
| 03 | KNN 회귀와 이웃 수에 따른 변화 | [03_knn_regression.ipynb](./03_knn_regression.ipynb) |
| 04 | 선형·다중·다항 회귀와 특성 확장 | [04_linear_multiple_polynomial_regression.ipynb](./04_linear_multiple_polynomial_regression.ipynb) |
| 05 | 여러 회귀 모델 비교와 GridSearchCV 튜닝 | [05_regression_model_comparison_and_tuning.ipynb](./05_regression_model_comparison_and_tuning.ipynb) |
| 06 | KNN·로지스틱 회귀·결정트리 분류와 평가 | [06_classification_basics.ipynb](./06_classification_basics.ipynb) |
| 07 | 앙상블 모델 비교·튜닝·분류 성능평가 | [07_ensemble_and_model_evaluation.ipynb](./07_ensemble_and_model_evaluation.ipynb) |

## 보조 폴더

- [common](./common/) — 공통 import 및 시각화 설정
- [data](./data/) — 학습 데이터
- [models](./models/) — 저장한 모델
- [reference](./reference/) — 참고 자료

## 정리 기준

- 새로 배우는 개념은 셀을 나누어 설명과 결과를 확인합니다.
- 이미 반복해서 사용한 `read_csv → X/y → train_test_split → scaler` 같은 준비 과정은 한 셀에 묶습니다.
- 테스트 데이터는 가능한 한 최종 일반화 성능 확인용으로 사용하고, 모델 비교는 검증 데이터 중심으로 진행합니다.
- 모델별로 지원하는 하이퍼파라미터가 다르므로 공통 반복문에서 무리하게 같은 속성을 넣지 않습니다.
