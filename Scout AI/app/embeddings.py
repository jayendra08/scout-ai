from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

# Singleton model instance
_model = None

def get_model() -> SentenceTransformer:
    """
    Lazy load and return the SentenceTransformer model instance.
    """
    global _model
    if _model is None:
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def generate_embeddings(texts: List[str]) -> np.ndarray:
    """
    Generate dense vector embeddings for a list of text strings using SentenceTransformer.
    """
    if not texts:
        return np.array([])

    model = get_model()
    embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    return embeddings


def compute_job_embeddings(job_texts: List[str]) -> np.ndarray:
    """
    Compute vector embeddings for all job description texts.
    """
    return generate_embeddings(job_texts)
