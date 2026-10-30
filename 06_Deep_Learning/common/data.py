"""반복되는 Fashion-MNIST 준비만 공통화합니다. 모델 코드는 노트북에 둡니다."""
from tensorflow import keras
from sklearn.model_selection import train_test_split

def load_fashion_data():
    """정규화된 (훈련, 검증, 테스트) 쌍을 반환합니다. 이미지 모양은 유지합니다."""
    (images, labels), (test_images, test_labels) = keras.datasets.fashion_mnist.load_data()
    images = images.astype('float32') / 255.0
    test_images = test_images.astype('float32') / 255.0
    train_x, val_x, train_y, val_y = train_test_split(
        images, labels, test_size=0.2, stratify=labels, random_state=42)
    return (train_x, train_y), (val_x, val_y), (test_images, test_labels)
