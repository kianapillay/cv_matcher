from semantic_matcher import calculate_semantic_match

cv = """
Software developer with Python, SQL, Azure and web development experience.
"""

job = """
Looking for a software engineer with Python and cloud computing experience.
"""

score = calculate_semantic_match(cv, job)

print("Semantic Score:", score)