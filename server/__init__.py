"""Embedding server, one-stop HTTP service for sentence semantic embedding, based on the advanced Sentence Transformers model."""

__version__ = "0.1.0"

from embedding import embed
from config import parse_config_file