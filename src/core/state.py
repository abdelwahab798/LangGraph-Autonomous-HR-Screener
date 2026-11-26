from typing import TypedDict, List, Annotated
from operator import add

class overallstate(TypedDict):
    job_description: str
    worker_findings: Annotated[List[dict], add]
    cv:list[dict]

class WorkerState(TypedDict):

# Orchstartor Input
    cv:str
    worker_id: int
    job_description: str

# candiate data
    candidate_name:str
    candidate_email:str
    scan_summary:str
    itreations_num : int
    is_accepted:bool

# optimize
    eval_overall_score:int
    strengths:list[str]
    weaknesses:list[str]
# if rejection
    rejection_email:str

# if accepted
    eval_summary:str
    techincal_questions:list[str]
    accepted_email:str


# Bridge back to OverallState
    worker_findings: Annotated[List[dict], add]


