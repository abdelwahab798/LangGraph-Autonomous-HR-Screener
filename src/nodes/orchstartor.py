from core.state import overallstate
from core.logger import get_logger
from langgraph.types import Send


logger=get_logger("Orchstartor")

def orchstartor_node(state:overallstate)->list[Send]:
    try:
        logger.info("Orchstartor Starting...")
        job_description=state["job_description"]
        logger.info("Job Description: ",state["job_description"],)

        return [
            Send("Scanner",
            {
                "cv_text":cv_text,
                "worker_id": idx,
                "job_description": state["job_description"],
                "iteration_num": 0,
            },
            )
        for idx,cv_text in enumerate(state["cv"],start=1)
        ]
    except Exception as e:
        logger.error("Error in Orchstartor: ",e)
        raise e
