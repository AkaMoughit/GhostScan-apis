# main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from scan import router as scan_router
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI()


app.include_router(scan_router)
# CORS middleware
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redirect the root URL to the documentation
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/health_check")
async def health_check():
    return {"status":"ok"}