# 스타일쉐어 미션
### Uses: Python3.7, Flask, SQLAlchemy, Alembic, Docker, Jinja2

## 환경 설정
1. virtualenv 환경 설정 (virtualenv venv --python=python3.7)
2. venv 상태로 전환 (venv/bin/activate)
3. pip install -r requirements.txt
4. docker-compose up -d local_db
5. alembic 셋팅 ./scripts/alembic.sh upgrade head
6. db 값 초기화 python ./scripts/init.py
7. 서버 실행 ./scripts/local_server.sh
8. [접속](http://127.0.0.1:5000)
