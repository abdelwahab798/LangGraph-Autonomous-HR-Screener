from pydantic import BaseModel, Field
from typing import List

class ScannerSchema(BaseModel):
    candidate_name: str = Field(description="Full name of the candidate extracted from the CV")
    candidate_email: str = Field(description="Email address of the candidate extracted from the CV")
    scan_summary: str = Field(description="Summary of candidate's projects, education, experience, and skills (or flaws if rejected)")
    is_accepted: bool = Field(description="True if candidate matches job description requirements, else False")

class GeneratorSchema(BaseModel):
    technical_questions: List[str] = Field(
        description="Tailored technical interview questions combining job requirements with the candidate's specific projects and skills")

class EvaluatorSchema(BaseModel):
    overall_score: int = Field(description="Overall quality score from 1 to 10", ge=1, le=10)
    eval_summary: str = Field(description="Constructive feedback summarizing why questions passed or how to improve them")
    strengths: List[str] = Field(description="Questions that are strong, deep, and well-tailored")
    weaknesses: List[str] = Field(description="Questions that are generic or need improvement")