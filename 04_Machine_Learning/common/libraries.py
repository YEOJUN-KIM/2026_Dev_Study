# Machine Learning Common Libraries
# 각 학습 노트북에서 반복되는 import를 한 곳에서 관리합니다.

# =========================================================
# 기본 데이터 처리 및 시각화
# =========================================================

# pandas : DataFrame 처리, CSV/Excel 등의 데이터 입출력
import pandas as pd

# numpy : 배열 및 수치 계산
import numpy as np

# matplotlib : 기본 그래프 시각화
import matplotlib.pyplot as plt

# seaborn : 통계 그래프, 히트맵 등 시각화
import seaborn as sns

# joblib / pickle : 학습한 모델이나 Python 객체 저장 및 불러오기
import joblib
import pickle

# 그래프 기본 설정
plt.rcParams["figure.figsize"] = (12, 5)
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False


# =========================================================
# 통계 분석
# =========================================================

# stats : 다양한 통계 분석 및 검정
from scipy import stats

# pearsonr : 선형 상관관계 검정
# spearmanr : 순위 기반 상관관계 검정
from scipy.stats import pearsonr, spearmanr


# =========================================================
# 데이터 분리 및 하이퍼파라미터 튜닝
# =========================================================

# train_test_split : 훈련/검증/테스트 데이터 분리
# GridSearchCV : 교차검증을 이용한 하이퍼파라미터 탐색
from sklearn.model_selection import train_test_split, GridSearchCV


# =========================================================
# 데이터 전처리 및 특성 변환
# =========================================================

# LabelEncoder : 범주형 값을 숫자로 변환
# StandardScaler : 평균 0, 표준편차 1 기준 표준화
# MinMaxScaler : 데이터를 일정 범위(기본 0~1)로 변환
# RobustScaler : 중앙값과 IQR을 이용해 이상치 영향을 줄여 스케일링
# MaxAbsScaler : 최대 절댓값을 기준으로 스케일링
# PolynomialFeatures : 제곱항·교차항 등 새로운 특성 생성
from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    MaxAbsScaler,
    PolynomialFeatures,
)

# SMOTE : 소수 클래스 데이터를 생성해 클래스 불균형 완화
from imblearn.over_sampling import SMOTE


# =========================================================
# K-최근접 이웃 모델
# =========================================================

# KNeighborsRegressor : 가까운 K개의 이웃을 이용한 회귀
# KNeighborsClassifier : 가까운 K개의 이웃을 이용한 분류
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier


# =========================================================
# 선형 모델
# =========================================================

# LinearRegression : 선형회귀
# Ridge : L2 규제를 사용하는 선형회귀
# Lasso : L1 규제를 사용하는 선형회귀
# LogisticRegression : 확률을 이용한 선형 분류
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression


# =========================================================
# 결정트리 모델
# =========================================================

# DecisionTreeRegressor : 결정트리 회귀
# DecisionTreeClassifier : 결정트리 분류
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier


# =========================================================
# 앙상블 모델
# =========================================================

# RandomForest : 여러 결정트리를 이용하는 배깅 계열 모델
# ExtraTrees : 분할 과정의 랜덤성을 더 높인 트리 앙상블
# GradientBoosting : 이전 모델의 오차를 순차적으로 보완하는 부스팅
# HistGradientBoosting : 히스토그램 기반으로 학습 효율을 높인 부스팅
from sklearn.ensemble import (
    RandomForestRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    HistGradientBoostingClassifier,
)

# XGBRegressor / XGBClassifier : XGBoost 기반 회귀·분류 모델
from xgboost import XGBRegressor, XGBClassifier


# =========================================================
# 모델 성능 평가
# =========================================================

# mean_absolute_error : 회귀 MAE
# mean_squared_error : 회귀 MSE
# r2_score : 회귀 R²(결정계수)
# confusion_matrix : 분류 오차행렬
# ConfusionMatrixDisplay : 오차행렬 시각화
# accuracy_score : 정확도
# precision_score : 정밀도
# recall_score : 재현율
# f1_score : F1-Score
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
