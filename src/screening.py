from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

with open("src/prompt_template.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template=prompt_text
)

llm = ChatGroq(api_key=GROQ_API_KEY, model='llama3-70b-8192')  
parser = StrOutputParser()

chain = prompt | llm | parser

def screen_candidate(resume_text: str, job_description: str) -> str:
    return chain.invoke({
        "resume_text": resume_text,
        "job_description": job_description
    })
if __name__ == "__main__":
    test_resume = """
    John Doe is a software engineer with 5 years of experience in backend development.
    Skilled in Python, FastAPI, AWS, and Docker. Holds a B.Tech in Computer Science.
    """

    test_job_description = """
    We are hiring a backend developer with strong knowledge of Python, APIs,
    and experience in deploying on cloud (AWS preferred).
    """

    result = screen_candidate(test_resume, test_job_description)
    print("===== SCREENING RESULT =====")
    print(result)
