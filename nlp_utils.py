# We import tools that help us turn text into numbers and compare them
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# This function will calculate how similar your CV is to a job description
def calculate_match(cv_text, job_text):

    # Step 1: Put both texts into a list
    # Example:
    # ["my CV text", "job description text"]
    texts = [cv_text, job_text]

    # Step 2: Convert text into numbers
    # TF-IDF = a way to find important words in text
    vectorizer = TfidfVectorizer()

    # This turns words into a matrix of numbers
    vectors = vectorizer.fit_transform(texts)

    # Step 3: Compare how similar the two texts are
    # cosine_similarity gives a score between 0 and 1
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Step 4: Convert to percentage (0–100)
    return round(similarity * 100, 2)