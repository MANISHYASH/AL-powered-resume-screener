# Resume Classifier: Identify Your Ideal Role

 Project Overview
 ---------------

The Resume Classifier is an intelligent system designed to analyze resumes and match them with the most suitable job roles. This application uses Natural Language Processing (NLP) and Machine Learning techniques to extract key skills, compare them against predefined job profiles, and predict the best job category for the candidate.

 Objective
------------

The primary goal of this project is to assist job seekers in identifying their ideal career path by analyzing their resumes. This tool also provides insights into skill gaps, allowing users to understand what skills they need to develop to increase their job prospects.

Key Features
------------

- Resume Parsing: Supports PDF and DOCX resume formats for automatic text extraction.
- Job Role Matching: Compares extracted skills with predefined job roles and calculates a match percentage.
- ML-Based Prediction: Uses a trained machine learning model to predict the most suitable job category.
- Skill Insights: Identifies matched and missing skills for each role.
- Word Cloud Visualization: Displays a word cloud to highlight the most common terms in the resume.
- Resume Summary: Provides a structured summary of education, skills, and experience.
- Downloadable Report: Users can download a PDF report of their job fit analysis.
- Skill Suggestions: Offers personalized recommendations for improving missing skills.

Technology Stack
----------------

- Python: Core programming language
- Streamlit: Interactive web-based user interface
- SpaCy: Natural Language Processing (NLP) for skill extraction
- scikit-learn: Machine learning model training and prediction
- PyPDF2 & Mammoth: PDF and DOCX file parsing
- WordCloud & Matplotlib: Data visualization                                        

How It Works
------------

- Resume Upload: Users upload their resumes in PDF or DOCX format.
- Skill Extraction: Relevant skills are extracted using NLP techniques.
- Role Matching: Each job role is compared against the resume to calculate match percentages.
- Prediction: The ML model predicts the most suitable job category.
- Insights & Report: Users receive a comprehensive report, including skill suggestions and improvement areas.

📦 Installation

1. Clone the repository:
  git clone https://github.com/MANISHYASH/ResumeInsight-AI-Powered-Resume-Classifier.git
  cd resume-classifier

2. Set up a virtual environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
  pip install -r requirements.txt

4. Download the spaCy language model:
  python -m spacy download en_core_web_sm

5. Run the application:
  streamlit run app.py

Usage
------

- Upload your resume (PDF or DOCX format).
- Review the extracted content and skill match percentages.
- Predict the best-fitting job role using the ML model.
- Download a comprehensive job-fit report.
- Follow skill improvement suggestions for better alignment with your desired role.

Future Improvements
------------------

- Enhance the ML model with more job categories.
- Add support for multiple languages.
- Integrate real-time job market analysis for dynamic skill recommendations.

Contribution
----------

Contributions are welcome! Feel free to fork this repository, open issues, or submit pull requests.

Contact
-------

For any queries or suggestions, contact yashwantmanish@gmail.com
