# Common

머신러닝 노트에서 공통으로 사용하는 import와 기본 시각화 설정을 관리합니다.

- [libraries.py](./libraries.py)

각 머신러닝 노트북에서는 다음 한 줄로 불러옵니다.

```python
%run ./common/libraries.py
```

전처리 함수나 모델 학습 함수는 공통 파일에 숨기지 않고 각 학습 노트북에 직접 작성합니다.
