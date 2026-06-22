from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load AI model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_match(cv_text, job_text):

    # Convert text into AI embeddings
    cv_embedding = model.encode(cv_text)

    job_embedding = model.encode(job_text)

    # Compare meaning
    similarity = cos_sim(cv_embedding, job_embedding)

    score = float(similarity[0][0]) * 100

    return round(score, 2)