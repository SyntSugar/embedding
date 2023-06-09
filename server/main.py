import argparse
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from server.config import parse_config_file
from server.embedding import embed

app = FastAPI()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Embedding server start with environment-based configuration")
    parser.add_argument("-e", choices=["local", "online"], default="local", help="which environment to use")
    args = parser.parse_args()
    return args

@app.middleware("http")
async def ip_whitelist_middleware(request: Request, call_next):
    client_ip = request.client.host
    ip_whitelist = parse_config_file(args.environment)

    if client_ip not in ip_whitelist:
        return JSONResponse(status_code=403, content="Access denied")

    response = await call_next(request)
    return response

@app.get("/embedding/{semantics}")
def embedding(semantics):
    sentence_embeddings = embed(semantics)
    return JSONResponse(status_code=200, content=sentence_embeddings)

if __name__ == "__main__":
    args = parse_arguments()

    ip_writelist = parse_config_file(args.environment)

    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)