# Streamlit is what lets us build a simple web app
import streamlit as st

# We import our function from the other file
from skill_extractor import extract_skills
from file_reader import extract_text_from_pdf
from semantic_matcher import calculate_semantic_match

# This creates the title of your app
st.title("AI CV + Job Match Analyzer")

# This creates a text box where user pastes CV
cv_file = st.file_uploader("Upload your CV (PDF)", type=["pdf"])

# This creates a text box for job description
job_text = st.text_area("Paste job description here")

# This creates a button
if st.button("Analyze Match"):

    if cv_file and job_text:

        cv_text = extract_text_from_pdf(cv_file)

        # NEW SYSTEM (skill extraction)
        cv_skills = extract_skills(cv_text)
        job_skills = extract_skills(job_text)

        matched_skills = [skill for skill in job_skills if skill in cv_skills]
        missing_skills = [skill for skill in job_skills if skill not in cv_skills]
        skill_match_details = [] 

        skill_score = (len(set(matched_skills)) / len(set(job_skills))) * 100 if job_skills else 0
        semantic_score = calculate_semantic_match(cv_text, job_text)
        final_score = (skill_score * 0.8) + (semantic_score * 0.2)

        role_profiles = {
        "Backend Developer": ["python", "sql", "rest api", "docker"],
        "Frontend Developer": ["javascript", "react", "html", "css"],
        "Data Analyst": ["sql", "python", "data analysis"],
        "Cloud Engineer": ["azure", "aws", "docker", "kubernetes"],
        "ML Engineer": ["python", "machine learning", "sql"]
        }

        role_scores = {}

        for role, skills in role_profiles.items():
            match_count = len([s for s in skills if s in cv_skills])
            role_scores[role] = match_count / len(skills)

        best_role = max(role_scores, key=role_scores.get)
        best_score = role_scores[best_role]

        st.subheader("Best Fit Role Explanation")

        role_explanation = f"""
        You match best with **{best_role}** because your CV contains:
        - {', '.join([s for s in role_profiles[best_role] if s in cv_skills])}

        Missing key skills:
        - {', '.join([s for s in role_profiles[best_role] if s not in cv_skills])}
        """

        st.success(role_explanation)

        # UI Section #

        st.subheader("Match Overview")
        st.progress(min(final_score / 100, 1.0))
        st.caption("Overall match between your CV and the job description")
        st.subheader(f"Final Score: {round(final_score, 2)}%")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Skill Score", f"{round(skill_score, 2)}%")

        with col2:
            st.metric("Semantic Score", f"{semantic_score}%")

        with col3:
            st.metric("Final Score", f"{round(final_score, 2)}%")

        st.subheader("Why this match?")

        for skill in matched_skills:
            confidence = "High" if skill in cv_skills else "Medium"

            skill_match_details.append({
                "skill": skill,
                "status": "matched",
                "confidence": confidence
            })

            st.write(f" {skill} → Strong match in your CV")

        for skill in missing_skills:
            skill_match_details.append({
                "skill": skill,
                "status": "missing",
                "confidence": "High importance (required by job)"
            })
            
            st.write(f" {skill} → Not found in CV (important for role)")

        st.subheader("Skill Strength Breakdown")

        for skill in matched_skills:
            strength = min(100, len(skill) * 10 + 60)
            st.write(f"{skill}: {strength}% confidence match")

        st.subheader("AI Insight")
        if final_score > 75:
            st.success("Your CV strongly matches the meaning of the job description.")
        elif final_score > 50:
            st.warning("Your CV is somewhat aligned with this role")
        else:
            st.error("Your CV does not strongly match this job description.")
        
        with st.expander("View Extracted CV Text"):
            st.write(cv_text)

        st.subheader("Skills Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### Matched Skills")
            st.write(matched_skills if matched_skills else "None")
            
        with col2:
            st.write("### Missing Skills")
            st.write(missing_skills if missing_skills else "None")
        
        skill_recommendations = {
        "python": "Build small automation scripts or API projects.",
        "sql": "Practice joins, aggregations, and database design.",
        "docker": "Learn how to containerize a Flask or Node app.",
        "aws": "Try deploying a simple app using AWS EC2 or S3.",
        "kubernetes": "Start with deploying containers using Minikube.",
        "react": "Build a simple dashboard or portfolio website."
        }

        st.subheader("Skill Improvement Suggestions")

        for skill in missing_skills:
            if skill in skill_recommendations:
                st.write(f" {skill}: {skill_recommendations[skill]}")

        if missing_skills:
            st.write("### Skills You Should Improve:")
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.success("You match all required skills")