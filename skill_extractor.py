# This is a simple AI-style "skill finder"
# It checks which known skills appear in text
import re

def extract_skills(text):

    text = text.lower()  # Convert to lowercase for easier matching

    found_skills = []

    # A basic list of skills we want to detect
    skill_aliases = {
    "python": ["python"],
    "java": ["java"],
    "kotlin": ["kotlin"],
    "c#": ["c#", "csharp"],
    "react": ["react", "reactjs"],
    "javascript": ["javascript", "js"],
    "html": ["html"],
    "css": ["css"],
    "sql": ["sql", "mysql", "postgresql"],
    "azure": ["azure"],
    "aws": ["aws", "amazon web services"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "git": ["git", "github"],
    "rest api": ["rest api", "restful api"],
    "machine learning": ["machine learning", "ml"]
}
    for skill, aliases in skill_aliases.items():

        for alias in aliases:
            if re.search(rf"\b{re.escape(alias)}\b", text):
                found_skills.append(skill)
                break

    return found_skills