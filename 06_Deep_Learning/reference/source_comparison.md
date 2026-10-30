# 원본 비교와 정리 내역

첨부된 노트북 5개와 매뉴얼 1개를 사용했습니다. 기존 저장소 실물은 첨부되지 않아,
이전 대화의 규칙인 루트의 번호 노트북·역할별 하위 폴더·간결한 한국어 설명을 적용했습니다.
원본 노트북의 실행 출력이 아니라 코드와 설명을 비교했습니다.

| 원본 | 정리 결과 | 보존한 고유 내용 |
| --- | --- | --- |
| `00_텐서플로우_GPU사용확인.ipynb` | [00](../00_tensorflow_gpu_check.ipynb) | 장치 확인, 메모리 증가 설정. 반복 출력과 내부 API 제거 |
| `01_Deep_Learning_base.ipynb` | [01](../01_fashion_mnist_basics.ipynb) | 이미지 확인, 정규화, reshape, 단층 분류, 손실함수, summary |
| `01_Deep_Learning_base(2).ipynb` | [02](../02_hidden_layers_optimizers.ipynb) | 모델 구성 3가지, sigmoid/ReLU, Flatten, 옵티마이저·학습률 비교 과제 |
| `01_DeepLearning_base(3).ipynb` | [03](../03_training_regularization_saving.ipynb) | model_fn, History, 곡선 저장, Dropout, 저장·복원, argmax, 정답/오답 계산, 콜백 |
| `01_Create_Image_Data.ipynb` | [04](../04_image_data_augmentation.ipynb) | 이미지 배열·배치 차원, 증강 옵션과 100개 파일 생성 |
| `UV_개발환경_메뉴얼.txt` | [원본](./UV_개발환경_메뉴얼.txt)과 [README](../README.md) | 원문은 바이트 그대로 보존하고 딥러닝 실행 절차를 README에 재구성 |

## 중복 판단
세 기초 파일은 완전 중복이 아니라 단계별 수업 자료입니다. 파일 전체를 중복으로 버린 것은 없습니다.
원래의 비슷한 파일명 3개는 새 번호 노트로 재편했으므로 완성 폴더에 별도 사본을 넣지 않았습니다.
반복된 import·데이터 다운로드·정규화·분할은 `common/data.py`와 `common/runtime.py`로 합쳤습니다.
첫 기초 노트에서만 데이터 확인 설명을 충분히 남기고 후속 노트는 준비 셀 하나로 구성했습니다.

- `01_Deep_Learning_base.ipynb` ↔ `01_Deep_Learning_base(2).ipynb`: 공백 정규화 후 동일한 비어 있지 않은 셀 5개. 전체 셀 내용 동일: False.
- `01_Deep_Learning_base.ipynb` ↔ `01_DeepLearning_base(3).ipynb`: 공백 정규화 후 동일한 비어 있지 않은 셀 2개. 전체 셀 내용 동일: False.
- `01_Deep_Learning_base(2).ipynb` ↔ `01_DeepLearning_base(3).ipynb`: 공백 정규화 후 동일한 비어 있지 않은 셀 2개. 전체 셀 내용 동일: False.

## 수정·생략한 부분
- 빈 셀, 같은 배열의 전체 출력, 반복 summary, 장시간 학습 로그와 오류 출력은 생략.
- 학습 실험마다 새 모델·옵티마이저를 생성. 재컴파일로 학습이 초기화된다는 오해 방지.
- `keras.Input`으로 입력 모양 명시. 독립 `keras`와 `tensorflow.keras` 혼용 해소.
- ANN/DNN 정의, ReLU의 의미, Flatten·Dropout의 영향, 옵티마이저 순위, 학습률 규칙,
  고정 손실 차이로 과적합 판정, 검증 데이터와 콜백 설명을 바로잡음.
- 원본의 30·50·200회 반복 및 콜백 최대 10,000회를 학습용 기본값으로 단축.
  본문에 원래 반복값을 기록했으며 콜백 상한은 50회로 설정.
- 원본의 RMSprop→Adam 중복 곡선은 Adam 검증곡선 실험으로 합침.
  짧은 RMSprop 학습과 옵티마이저 비교는 따로 보존.
- 모델·그림·증강 저장 폴더를 자동 생성. 이미지 경로를 `data/images/dog.jpg`로 통일.
- ImageDataGenerator는 수업 대응을 위해 보존하고 deprecated 상태를 표시.
- pandas/seaborn 등 사용하지 않는 import와 매뉴얼의 머신러닝·웹 도구 설치는 requirements에서 제외.

## 검증 범위
노트북 형식, 코드 문법, 파일 링크, ZIP 내용과 매뉴얼 동일성을 검사했습니다.
제작 환경에는 TensorFlow와 WSL GPU가 없어 실제 학습·GPU 인식·증강 실행은 검증하지 못했습니다.
requirements는 설치 입력이며 실제 설치 환경을 고정한 lock 파일은 아닙니다.
