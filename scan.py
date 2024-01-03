from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/scan", tags=["Scan"])

@router.post("/")
async def scan(file: UploadFile = File(...)):
    return {"filename": file.filename,
            "size":file.size,
            "headers":file.headers,
            "content type":file.content_type}