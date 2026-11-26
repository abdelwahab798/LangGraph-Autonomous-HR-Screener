from core.schema import ScannerSchema
from core.state import overallstate,WorkerState
from ulits.llms import get_structred_llm
from core.logger import get_logger


logger=get_logger("Scanner")

structred_llm=get_structred_llm("gemini-2.5-flash",ScannerSchema)
logger.info("Structred_llm is iniliaze")

def scanner_node(state:WorkerState)->WorkerState:
    try:
        worker_id=state["worker_id"]
        cv=state["cv"]
        job_description=state["job_description"]
        logger.info(f"Woker_Id:{worker_id},Initialized is done")

        prompt=f"""
        You are an expert Technical HR Recruiter.
        Evaluate the following CV against the Job Description.
        Extract the candidate's full name and email, provide a concise summary of their projects, education, experience, and skills (or highlight key gaps if they don't match), and decide whether they are accepted.
        Job Description:
        {job_description}
        Candidate CV:
        {cv}
        """
        response=structred_llm.invoke(prompt)
        logger.info(f"[Worker {worker_id}] Candidate: {response.candidate_name} | Accepted: {response.is_accepted}")

        finiding={
            "candidate_name":response.candidate_name,
            "candidate_email":response.candidate_email,
            "scan_summary":response.scan_summary,
            "is_accepted":response.is_accepted}

        return finiding

    except Exception as e:
        logger.error("We have Error in Scanner Node: ",e)
        raise e
