# Streamlit is what lets us build a simple web app
import streamlit as st

# We import our function from the other file
from nlp_utils import calculate_match
from skill_extractor import extract_skills
from file_reader import extract_text_from_pdf

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

        # Compare skills
        missing_skills = []

        for skill in job_skills:
            if skill not in cv_skills:
                missing_skills.append(skill)

        st.write("### DEBUG CV TEXT")
        st.write(cv_text)

        if missing_skills:
            st.write("### Skills You Should Improve:")
            for skill in missing_skills:
                st.write(f"- {skill}")
        else:
            st.success("You match all required skills")
        
        # Calculate skill-based score (more realistic than TF-IDF alone)
        total_required = len(job_skills)

        if total_required == 0:
            skill_score = 0
        else:
            matched = len([skill for skill in job_skills if skill in cv_skills])
            skill_score = (matched / total_required) * 100

        st.write("### AI Insight:")
        if skill_score > 70:
            st.write("You are a strong candidate for this role based on skill overlap.")
        elif skill_score > 40:
            st.write("You partially match this role. Focus on missing skills to improve your chances.")
        else:
            st.write("You are currently not a strong match, but this shows clear skill gaps to work on.")

        # DISPLAY RESULTS

        st.subheader(f"Skill Match Score: {round(skill_score, 2)}%")

        st.write("### CV Skills Found:")
        st.write(cv_skills)

        st.write("### Job Skills Required:")
        st.write(job_skills)

        st.write("### Missing Skills:")
        st.write(missing_skills)
        

        # Feedback
        if skill_score > 70:
            st.success("Strong match ")
        elif skill_score > 40:
            st.warning("Medium match — improve your CV")
        else:
            st.error("Low match — needs improvement")

            