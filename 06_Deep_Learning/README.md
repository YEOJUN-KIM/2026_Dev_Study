# 05. Deep Learning

TensorFlow/Keras로 이미지 분류의 기본 흐름과 모델 학습·저장, 이미지 증강을 정리합니다.
학습노트는 루트에 번호 순서로 두고, 데이터·공통 함수·참고 자료만 하위 폴더로 구분합니다.

## 학습 순서

| 순서 | 학습노트 | 주요 내용 |
| ---: | --- | --- |
| 00 | [TensorFlow GPU 확인](./00_tensorflow_gpu_check.ipynb) | 장치 목록, 메모리 설정, 연산 장치 |
| 01 | [이미지 분류 기초](./01_fashion_mnist_basics.ipynb) | Fashion-MNIST, 정규화, Dense, 손실함수 |
| 02 | [은닉층과 옵티마이저](./02_hidden_layers_optimizers.ipynb) | Sequential 구성, Flatten, ReLU, 학습률 |
| 03 | [학습곡선·규제·모델 저장](./03_training_regularization_saving.ipynb) | History, Dropout, 콜백, 저장·복원, 예측 |
| 04 | [이미지 데이터 증강](./04_image_data_augmentation.ipynb) | 이미지 배열, 배치 차원, 변형·저장 |

모든 노트북은 **이 폴더를 작업 위치로 선택하고 새 커널에서 위에서 아래로** 실행합니다.
01~03은 각각 독립 실행하며 Fashion-MNIST를 처음 사용할 때 다운로드합니다.
04의 `dog.jpg`는 미첨부이므로 직접 준비합니다. 없으면 안내 후 증강을 건너뜁니다.
학습 횟수는 복습하기 편하게 줄였으며 수업의 원래 횟수는 각 노트에 표시했습니다.

## 폴더와 참고 자료

```text
05_Deep_Learning/
├── README.md
├── 00_tensorflow_gpu_check.ipynb
├── 01_fashion_mnist_basics.ipynb
├── 02_hidden_layers_optimizers.ipynb
├── 03_training_regularization_saving.ipynb
├── 04_image_data_augmentation.ipynb
├── requirements.txt
├── requirements-gpu.txt
├── common/
│   ├── __init__.py
│   ├── data.py
│   └── runtime.py
├── data/
│   ├── README.md
│   └── images/
└── reference/
    ├── UV_개발환경_메뉴얼.txt
    └── source_comparison.md
```

- [데이터 위치와 실행 결과](./data/README.md)
- [데이터 준비 함수](./common/data.py) · [장치·난수 설정](./common/runtime.py)
- [Linux/uv 개발환경 매뉴얼 원문](./reference/UV_개발환경_메뉴얼.txt)
- [원본별 병합·중복 정리 내역](./reference/source_comparison.md)
- [공통·CPU 의존성](./requirements.txt) · [Linux/WSL2 GPU 의존성](./requirements-gpu.txt)

`common/libraries.py`의 일괄 import는 만들지 않았습니다. 모델과 새 API는 노트북에서 직접 확인하고,
실제로 반복되는 데이터 준비·장치 설정만 공통화했습니다. 기존 다른 학습 폴더의 common 파일을 수정할 필요는 없습니다.
저장소 최상위 README의 학습 목록에는 아래 링크 한 줄을 추가하면 됩니다.

```markdown
| 05 | [Deep Learning](./05_Deep_Learning/README.md) | TensorFlow · 이미지 분류 · 모델 저장 · 데이터 증강 |
```

## Ubuntu/WSL + uv + TensorFlow GPU 설정

업로드한 매뉴얼의 WSL → Ubuntu → uv → 가상환경 → CUDA 경로 → GPU 확인 순서를 따릅니다.
아래 명령은 Windows PowerShell과 Ubuntu Bash를 구분해서 실행합니다.
기준은 Python 3.10, TensorFlow 2.20.0입니다. 실제 GPU 학습은 제작 환경에서 실행하지 못했습니다.

### 1. Windows에서 WSL2와 Ubuntu 준비

NVIDIA GPU와 WSL을 지원하는 **Windows용 NVIDIA 드라이버**를 준비합니다.
현대 TensorFlow의 Windows GPU 실행은 WSL2 경로를 사용합니다.
[TensorFlow 설치 안내](https://www.tensorflow.org/install/pip)와
[Microsoft WSL 설치 안내](https://learn.microsoft.com/en-us/windows/wsl/install)를 기준으로 확인합니다.

관리자 PowerShell에서 초기 설치를 진행합니다.

```powershell
wsl --version
wsl --update
wsl --list --online
wsl --install -d Ubuntu
```

설치 화면에 따라 재부팅하고 Linux 사용자명·비밀번호를 만듭니다.
매뉴얼은 `Ubuntu-26.04`와 별칭 `pknu_ubuntu`를 예로 들지만, 설치 가능한 이름을 먼저 확인합니다.
이미 설치한 배포판은 다시 만들지 않습니다. 이후에는 일반 PowerShell을 사용합니다.

```powershell
wsl -l -v
wsl -d Ubuntu
```

`wsl -l -v`의 VERSION이 2인지 확인합니다. 배포판 이름이 다르면 위의 `Ubuntu`를 실제 이름으로 바꿉니다.
VERSION이 1이면 PowerShell에서 `wsl --set-version Ubuntu 2`로 전환합니다.

### 2. Ubuntu 기본 도구와 uv 설치

이후 명령은 Ubuntu 터미널에서 실행합니다. Windows에 설치한 uv와 Linux의 uv·가상환경은 별개입니다.

```bash
sudo apt update
sudo apt install -y build-essential git curl wget htop tree
nvidia-smi
curl -LsSf https://astral.sh/uv/install.sh | sh
```

터미널을 다시 열고 아래를 확인합니다. `nvidia-smi`가 실패하면 먼저 드라이버·WSL 문제를 해결합니다.
uv 설치와 사용자 가상환경 생성에는 관리자 권한이 필요하지 않습니다.
[uv 환경 안내](https://docs.astral.sh/uv/pip/environments/) 참고.

```bash
uv --version
mkdir -p ~/workspace
cd ~/workspace
```

저장소를 이 위치에 복사하거나 clone하고 그 안의 `05_Deep_Learning`으로 이동합니다.
예를 들어 독립 폴더로 복사했다면 `cd ~/workspace/05_Deep_Learning`입니다.
Windows의 `.venv`를 복사해서 사용하지 않고 Linux 안에서 새로 만듭니다.

### 3. 가상환경과 패키지 설치

현재 위치에 README와 requirements 파일이 보이는지 확인한 뒤 실행합니다.

```bash
uv venv .venv --python 3.10
source .venv/bin/activate
python --version
uv pip install -r requirements-gpu.txt
```

GPU가 없는 CPU 환경에서는 마지막 명령을 `uv pip install -r requirements.txt`로 바꿉니다.
GPU용 파일은 공통 의존성을 포함하고 `tensorflow[and-cuda]` 추가 의존성을 설치합니다.
두 파일을 순서대로 설치할 필요는 없습니다. Python 버전은 매뉴얼의 3.10을 유지했습니다.
TensorFlow만 버전을 고정하고 나머지는 호환 범위를 지정했으므로 완전한 환경 잠금 파일은 아닙니다.

### 4. CUDA 경로 설정과 GPU 확인

먼저 기본 설치만으로 확인합니다.

```bash
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

GPU가 인식되면 별도 경로 설정을 생략합니다. `nvidia-smi`는 정상인데 TensorFlow에서 CUDA 라이브러리
경로 누락이 발생하면 매뉴얼의 `LD_LIBRARY_PATH`와 `XLA_FLAGS` 설정을 적용할 수 있습니다.
원문의 `python3.10` 고정 경로 대신 현재 가상환경의 실제 패키지 경로를 사용합니다.
Ubuntu Bash에서 다음 블록을 한 번 실행한 뒤 가상환경을 다시 활성화합니다.

```bash
if ! grep -q '# Study TensorFlow CUDA paths' .venv/bin/activate; then
cat <<'EOF' >> .venv/bin/activate

# Study TensorFlow CUDA paths
_STUDY_OLD_LD_LIBRARY_PATH="${LD_LIBRARY_PATH-}"
_STUDY_OLD_XLA_FLAGS="${XLA_FLAGS-}"
_study_site="$("$VIRTUAL_ENV/bin/python" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
if [ -d "$_study_site/nvidia" ]; then
    _study_nv_libs="$(find "$_study_site/nvidia" -type d -name lib | paste -sd ':' -)"
    export LD_LIBRARY_PATH="$_study_nv_libs${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
    if [ -d "$_study_site/nvidia/cuda_nvcc/nvvm/libdevice" ] && [[ "${XLA_FLAGS-}" != *--xla_gpu_cuda_data_dir* ]]; then
        export XLA_FLAGS="${XLA_FLAGS:+$XLA_FLAGS }--xla_gpu_cuda_data_dir=$_study_site/nvidia/cuda_nvcc"
    fi
fi
unset _study_site _study_nv_libs
EOF
fi
deactivate
source .venv/bin/activate
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

이 추가 설정은 Bash용입니다. `deactivate`는 추가 환경변수를 자동 복원하지 않습니다.
다른 가상환경으로 전환할 때는 새 터미널을 열거나 아래처럼 복원합니다.

```bash
export LD_LIBRARY_PATH="${_STUDY_OLD_LD_LIBRARY_PATH-}"
export XLA_FLAGS="${_STUDY_OLD_XLA_FLAGS-}"
deactivate
```

`cuda_nvcc/nvvm/libdevice`가 없으면 XLA_FLAGS를 설정하지 않습니다.
XLA 경고가 계속되면 설치된 TensorFlow와 CUDA 패키지 조합을
[공식 설치 절차](https://www.tensorflow.org/install/pip)에서 확인합니다.

### 5. Notebook 실행

CUDA 환경변수를 적용한 Ubuntu 터미널에서 실행하면 Jupyter에도 같은 환경이 전달됩니다.

```bash
python -m ipykernel install --user --name deep-learning --display-name "Python (05 Deep Learning)"
python -m jupyterlab
```

표시된 주소를 브라우저에서 열고 **Python (05 Deep Learning)** 커널로 00부터 실행합니다.
VS Code를 쓰면 WSL 확장으로 Ubuntu 폴더를 열고 해당 `.venv/bin/python`을 커널로 선택합니다.
`sys.executable`이 Windows 경로라면 Linux 가상환경 커널로 바꿉니다.
경로 설정 후에도 이미 실행 중인 Jupyter·커널에는 반영되지 않으므로 종료 후 다시 실행합니다.

### 6. GPU가 인식되지 않을 때

1. PowerShell의 `wsl -l -v`에서 WSL2인지 확인합니다.
2. Ubuntu의 `nvidia-smi`로 Windows 드라이버와 GPU 연결을 확인합니다.
3. `which python`이 현재 폴더의 `.venv/bin/python`인지 확인합니다.
4. `uv pip show tensorflow`로 설치 여부를 확인하고 GPU용 requirements를 적용합니다.
5. 위 CUDA 경로 설정을 적용한 터미널에서 Jupyter를 다시 실행합니다.
6. 00의 실제 행렬 연산 장치까지 확인합니다. GPU가 없어도 나머지는 CPU로 실행할 수 있습니다.

### 매뉴얼의 선택 설정

원문의 `.wslconfig` 네트워크 미러링, `/etc/wsl.conf`의 systemd, SSH·FileZilla는
별도 Linux 서버 관리에 관한 참고 내용입니다. 이 노트북의 로컬 Jupyter 실행에 필수는 아닙니다.
원문의 `/home/server`, 드라이브 경로와 계정 값은 본인 환경에 맞게 바꿉니다.

### 설치 환경 기록

실제 설치·실행을 확인한 뒤 다음으로 환경을 기록할 수 있습니다.

```bash
uv pip freeze > requirements-lock.txt
# 같은 OS·Python 환경에서 기록한 버전을 설치할 때
uv pip install -r requirements-lock.txt
```

이 폴더의 검증 범위와 원본별 변경 내역은 [정리 기록](./reference/source_comparison.md)에 있습니다.
