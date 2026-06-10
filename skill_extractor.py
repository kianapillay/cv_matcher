# This is a simple AI-style "skill finder"
# It checks which known skills appear in text

def extract_skills(text):

    text = text.lower()  # Convert to lowercase for easier matching

    found_skills = []

    # A basic list of skills we want to detect
    skill_aliases = {
    "python": ["python"],
    "machine learning": ["machine learning", "ml"],
    "data analysis": ["data analysis", "analytics"],
    "software development": ["software development", "application development"],
    "web development": ["web development", "frontend", "backend"],
    "azure": ["azure", "cloud"]
}
    for skill, aliases in skill_aliases.items():

        for alias in aliases:
            if alias in text:
                found_skills.append(skill)
                break

    return found_skills