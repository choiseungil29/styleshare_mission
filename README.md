1. virtualenv 환경 설정 (python3.7)
2. venv 상태로 전환
3. pip install -r requirements.txt
4. docker-compose up -d local_db
5. alembic 셋팅 ./scripts/alembic upgrade head
6. db 값 초기화 ./scripts/init.py
7. 서버 실행 ./scripts/local_server.sh
