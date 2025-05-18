from fastapi import APIRouter

router = APIRouter()

# SpringBoot에서 호출할 테스트용 API 엔드포인트
@router.get("/test")
async def test():
    return "성공!"