from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Welcome!! this is Moustafa Esayed and this is my final capstone"
    }
