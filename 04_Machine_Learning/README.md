# Machine Learning

[← 루트로 이동](../README.md)

날짜별 복습본보다는 **한 번에 다시 보기 좋은 대표 노트** 중심으로 정리했습니다. 중복 내용은 제거하고, 짧게 나뉘어 있던 회귀 노트는 합쳤습니다.

## 실행 환경 설정

머신러닝 실습은 라이브러리 충돌을 줄이기 위해 `04_Machine_Learning` 폴더 안에 `.venv` 가상환경을 만들어 사용하는 것을 권장합니다.

```bash
cd 04_Machine_Learning
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

가상환경 활성화 후 필요한 라이브러리를 한 번에 설치합니다.

```bash
pip install -r requirements.txt
```

VS Code에서 `.ipynb` 파일을 열었다면 우측 상단 **Select Kernel**에서 `.venv` 환경을 선택합니다.

> `.venv`는 PC별 실행 환경이므로 GitHub에는 올리지 않습니다.

## 공통 라이브러리

노트북마다 같은 `import` 구문을 반복하지 않도록 [`common/libraries.py`](./common/libraries.py)에 머신러닝 학습에서 사용하는 라이브러리를 모아두었습니다.

각 학습 노트북에서는 첫 부분에서 다음과 같이 불러옵니다.

```python
%run ../common/libraries.py
```

그리고 해당 노트북에서 실제 사용하는 라이브러리의 역할만 간단한 주석으로 표시합니다. 공통 파일에는 **import와 matplotlib 기본 설정만** 두고, 전처리·훈련·평가 코드는 각 노트북에 그대로 남겨 학습 흐름을 확인할 수 있도록 했습니다.

## 학습 순서

| 순서 | 주제 | 대표 노트 |
| ---: | --- | --- |
| 01 | Data Preparation | [01_Data_Preparation README](./01_Data_Preparation/README.md) |
| 02 | Regression | [02_Regression README](./02_Regression/README.md) |
| 03 | Regression Project | [03_Regression_Project README](./03_Regression_Project/README.md) |
| 04 | Classification | [04_Classification README](./04_Classification/README.md) |
| 05 | Ensemble Project | [05_Ensemble_Project README](./05_Ensemble_Project/README.md) |

## 중복 정리 내용

- `3day_Feature_Enginnering`은 후속 `4day` 노트와 대부분 겹쳐 후속본만 유지했습니다.
- 짧은 `wines.ipynb`, `asd` 형태의 복습/초안 중 대표 노트와 겹치는 것은 제외했습니다.
- 선형회귀와 다중회귀는 한 노트북으로 합쳤습니다.
- 주택가격 관련 여러 버전은 가장 완성도가 높은 전체 모델·튜닝 노트 하나로 정리했습니다.
- 앙상블의 짧은 실습본은 전체 실습본과 겹쳐 제거하고, 최종 와인 분류 과제는 종합 학습 노트로 유지했습니다.
- Python/Pandas 기초 복습은 `01_Python`, `03_Data_Pipeline`과 중복되어 ML 폴더에서는 제외했습니다.

## 공용 파일

- [data](./data/README.md) : 머신러닝 학습 데이터셋
- [models](./models/README.md) : 저장한 모델 파일
- [requirements.txt](./requirements.txt) : 머신러닝 패키지

이전: [← Data Pipeline](../03_Data_Pipeline/README.md) · 다음: [React →](../05_React/README.md)
