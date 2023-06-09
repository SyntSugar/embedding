import argparse
from fastapi import FastAPI
from server.config import parse_config_file
from server.embedding import embed

app = FastAPI()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Embedding server start with environment-based configuration")
    parser.add_argument("-e", choices=["local", "online"], default="local", help="which environment to use")
    args = parser.parse_args()
    return args

@app.get("/embedding/{semantics}")
def embedding(semantics):
    sentence_embeddings = embed(semantics)
    return {"sentence_embeddings": sentence_embeddings}

if __name__ == "__main__":
    args = parse_arguments()

    config_file = "/conf/{}/config.toml".format(args.environment)
    config_path = parse_config_file(args.environment)

    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)