from sentence_transformers import SentenceTransformer
import logging

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed(sentences):
    # encode default convert to numpy
    sentence_embeddings = model.encode(sentences)
    for sentence, embedding in zip(sentences, sentence_embeddings):
        logging.info("Sentence:", sentence)
        logging.info("Embedding:", embedding)
        logging.info("")

    return sentence_embeddings