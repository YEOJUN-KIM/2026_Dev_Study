# common

머신러닝 노트북에서 반복되는 import를 `libraries.py` 한 곳에서 관리합니다.

각 노트북에서는 다음 한 줄로 불러옵니다.

```python
from common.libraries import *
```

`libraries.py`에는 **import와 그래프 기본 설정만** 두고, 실제 전처리·학습·평가 코드는 각 노트북에 남겨 학습 흐름이 보이도록 구성합니다.
