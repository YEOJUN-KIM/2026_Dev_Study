# Machine Learning

머신러닝 수업 내용을 **처음부터 다시 읽어도 흐름을 이해할 수 있는 학습노트 형태**로 정리한 폴더입니다.

기준은 다음과 같습니다.

- 처음 배우는 개념은 **설명 → 예제 → 결과 확인** 순서로 정리
- 이미 배운 `read_csv`, `train_test_split`, 스케일링 등의 준비 과정은 한 셀로 묶기
- 단순 변수 출력, 같은 결과 반복 확인 등은 제거
- 잘못된 코드나 데이터 누수 가능성이 있는 흐름은 수정
- 학습 단계는 폴더를 계속 열지 않도록 `.ipynb` 파일 번호로 구분
- `data`, `common`, `models`, `reference`처럼 역할이 다른 파일만 폴더로 유지

## 학습 순서

| 순서 | 학습 내용 | 노트 |
| ---: | --- | --- |
| 01 | 결측치·이상치·자료형·문자열 정리 | [데이터 전처리](./01_data_preprocessing.ipynb) |
| 02 | 상관관계·인코딩·스케일링·파생변수·SMOTE | [특성 엔지니어링](./02_feature_engineering.ipynb) |
| 03 | KNN 회귀·R²·오차·하이퍼파라미터·한계 | [KNN 회귀](./03_knn_regression.ipynb) |
| 04 | 선형·다중·다항 회귀·PolynomialFeatures·규제 | [선형·다중·다항 회귀](./04_linear_multiple_polynomial_regression.ipynb) |
| 05 | 여러 회귀모델 비교·GridSearchCV·모델 저장 | [회귀 모델 비교와 튜닝](./05_regression_model_comparison_and_tuning.ipynb) |
| 06 | KNN·LogisticRegression·DecisionTree·분류 평가 | [분류 기초](./06_classification_basics.ipynb) |
| 07 | RandomForest·ExtraTrees·Boosting·XGBoost·튜닝 | [앙상블과 성능 평가](./07_ensemble_and_model_evaluation.ipynb) |
| 08 | KMeans, PCA, DBSCAN, Silhouette Score, Adjusted Rand Score | [군집 분석](./08_kmeans_dbscan.ipynb) |

## 폴더 구조

```text
04_Machine_Learning/
├─ common/
│  └─ libraries.py
├─ data/
├─ models/
├─ reference/
├─ 01_data_preprocessing.ipynb
├─ 02_feature_engineering.ipynb
├─ 03_knn_regression.ipynb
├─ 04_linear_multiple_polynomial_regression.ipynb
├─ 05_regression_model_comparison_and_tuning.ipynb
├─ 06_classification_basics.ipynb
├─ 07_ensemble_and_model_evaluation.ipynb
├─ 08_kmeans_dbscan.ipynb
├─ requirements.txt
└─ README.md
```

## 처음 실행할 때

`04_Machine_Learning` 폴더에서 가상환경을 생성합니다.

```powershell
python -m venv .venv
```

PowerShell에서 스크립트 실행이 막히는 경우 현재 PowerShell 창에만 임시 허용합니다.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

가상환경 활성화:

```powershell
.\.venv\Scripts\Activate.ps1
```

필요한 라이브러리 설치:

```powershell
pip install -r .\requirements.txt
```

VS Code의 노트북 커널은 다음 환경을 선택합니다.

```text
04_Machine_Learning\.venv\Scripts\python.exe
```

각 노트북에서는 공통 import를 다음 한 줄로 불러옵니다.

```python
from common.libraries import *
```

> `.venv`는 PC마다 경로와 환경이 달라지므로 GitHub에 업로드하지 않습니다.
