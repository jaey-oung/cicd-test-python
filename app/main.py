from fastapi import FastAPI
from app.routes import test

# FastAPI 애플리케이션 생성
app = FastAPI()

# /test 엔드포인트 라우터 등록
app.include_router(test.router)

# fastapi 서버 실행 명령어:
# uvicorn app.main:app