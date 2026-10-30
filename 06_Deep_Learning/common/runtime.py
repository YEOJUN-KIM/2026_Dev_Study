"""장치 초기화 전에 실행하는 메모리 설정과 난수 설정."""
import tensorflow as tf

def configure_runtime(seed=42, deterministic=False):
    gpus = tf.config.list_physical_devices('GPU')
    for gpu in gpus:
        try:
            tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as error:
            raise RuntimeError('커널을 재시작하고 첫 셀부터 실행하세요.') from error
    tf.keras.utils.set_random_seed(seed)
    if deterministic:
        tf.config.experimental.enable_op_determinism()
    return gpus
