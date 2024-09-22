import spacy
from pdfminer.high_level import extract_text
from pyresparser import ResumeParser

# Download spaCy model if not already downloaded
# Uncomment the line below if you haven't downloaded the model yet
spacy.cli.download("en_core_web_sm")

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_skills(text):
    # Process the text using spaCy
    doc = nlp(text)
    
    # Extract skills using spaCy's named entity recognition (NER)
    skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
    
    return skills

def read_pdf(file_path):
    # Extract text from PDF using pdfminer
    text = extract_text(file_path)
    return text

def extract_skills_from_resume(file_path):
    # Read the PDF file
    resume_text = read_pdf(file_path)
    
    # Use pyresparser to get additional skills
    resume_data = ResumeParser(file_path).get_extracted_data()
    additional_skills = resume_data.get('skills', [])
    
    # Extract skills using spaCy
    spaCy_skills = extract_skills(resume_text)
    
    # Combine and return all extracted skills
    all_skills = list(set(additional_skills + spaCy_skills))
    return all_skills

# Replace 'your_resume.pdf' with the actual file path to your PDF resume
pdf_file_path = r'C:\Users\Ayman\Desktop\parser\test\55.pdf'

try:
    extracted_skills = extract_skills_from_resume(pdf_file_path)
    if extracted_skills:
        print("Skills extracted from the resume:")
        for skill in extracted_skills:
            print(skill)
    else:
        print("No skills extracted from the resume.")
except Exception as e:
    print(f"An error occurred: {e}")
