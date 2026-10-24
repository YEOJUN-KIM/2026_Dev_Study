"""PostgreSQL 연결 설정 예제.

공개 저장소에 비밀번호를 직접 기록하지 않고 환경변수에서 읽도록 구성했습니다.
"""
import os
import psycopg


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "ai_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
    )
