from fastapi import FastAPI


app = FastAPI()


# home page
@app.get("/home")
def root():
    return 'welcom to ESG Data et IA FastAPI Workshop'