from fastapi import FastAPI


app = FastAPI()


# import debugpy
# debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

@app.get("/")
def read_root():
    return {"Hello": "World12"}

@app.get("/hits")
def read_root():
    r.incr("hits")
    return {"Number of hits" : r.get("hits")}