from fastapi import FastAPI


from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/ping")
async def ping():
    return {"pong": "42"}


run = Mangum(app)