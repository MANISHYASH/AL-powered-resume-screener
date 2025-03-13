import streamlit as st
import pickle
import PyPDF2
import mammoth
import spacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load trained model and vectorizer
with open("resume_classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Error loading spaCy model. Ensure 'en_core_web_sm' is installed using 'python -m spacy download en_core_web_sm'.")
    st.stop()

# Job roles and corresponding skills
job_roles = {
    "Data Scientist": {"Python", "Machine Learning", "SQL", "TensorFlow", "Data Analysis"},
    "Software Engineer": {"Java", "C++", "Python", "Git", "Algorithms"},
    "Web Developer": {"HTML", "CSS", "JavaScript", "React", "Node.js"},
    "Data Analyst": {"SQL", "Excel", "Python", "Statistics", "Data Visualization"},
    "Cybersecurity Specialist": {"Network Security", "Encryption", "Penetration Testing", "Firewall", "Incident Response"},
    "Project Manager": {"Agile", "Scrum", "Budgeting", "Stakeholder Management", "Scheduling"},
    "UI/UX Designer": {"Wireframing", "Prototyping", "Figma", "Adobe XD", "User Research"},
    "Cloud Engineer": {"AWS", "Azure", "Docker", "Kubernetes", "CI/CD"}
}

# Flatten all job skills for matching
all_skills = {skill.lower() for skills in job_roles.values() for skill in skills}

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    return "".join(page.extract_text() or "" for page in pdf_reader.pages)

def extract_text_from_docx(docx_file):
    """Extracts text from a DOCX file."""
    result = mammoth.extract_raw_text(docx_file)
    return result.value or ""

def extract_skills(text):
    """Extracts recognized skills from the text using keyword matching."""
    text_lower = text.lower()
    return {skill for skill in all_skills if skill in text_lower}

def calculate_match_percentage(resume_text):
    """Calculates skill match percentage for each job role."""
    resume_skills = extract_skills(resume_text)
    match_results = {}

    for role, skills in job_roles.items():
        matched_skills = {skill for skill in skills if skill.lower() in resume_skills}
        match_percentage = (len(matched_skills) / len(skills)) * 100 if skills else 0
        missing_skills = skills - matched_skills
        match_results[role] = (match_percentage, matched_skills, missing_skills)

    best_match = max(match_results.items(), key=lambda x: x[1][0])
    return best_match, match_results

def plot_wordcloud(text):
    """Generates and displays a word cloud from the provided text."""
    if not text.strip():
        st.warning("⚠️ Not enough content to generate a word cloud.")
        return

    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Streamlit Custom Styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #2E4053;
    }
    .stButton>button {
        color: white;
        background-color: #1F618D;
        border-radius: 10px;
    }
    .stTabs div[role="tab"]:nth-child(1) {
        color: #2471A3;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App Interface
st.title("📄 Resume Classifier: Identify Your Ideal Role")

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_extension == "docx":
        resume_text = extract_text_from_docx(uploaded_file)

    best_match, match_results = calculate_match_percentage(resume_text)

    tab1, tab2, tab3 = st.tabs(["🔍 Match Analysis", "📊 Word Cloud", "📈 Prediction"])

    with tab1:
        st.info(f"💼 Best Match: {best_match[0]} ({best_match[1][0]:.2f}%)")

        st.subheader("📌 Detailed Match for Each Role")
        for role, (match_percentage, matched_skills, missing_skills) in match_results.items():
            st.write(f"**{role}:** {match_percentage:.2f}%")
            st.write(f"✔️ Matched Skills: {', '.join(matched_skills) or 'None'}")
            st.write(f"❌ Missing Skills: {', '.join(missing_skills) or 'None'}")

    with tab2:
        st.subheader("🌟 Resume Word Cloud")
        plot_wordcloud(resume_text)

    with tab3:
        if st.button("Predict Job Role"):
            resume_tfidf = vectorizer.transform([resume_text])
            predicted_roles = model.predict(resume_tfidf)

            if isinstance(predicted_roles[0], list):
                st.success(f"✅ Predicted Job Categories: {', '.join(predicted_roles[0])}")
            else:
                st.success(f"✅ Predicted Job Category: {predicted_roles[0]}")