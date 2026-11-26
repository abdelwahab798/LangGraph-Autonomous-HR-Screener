from core.logger import get_logger
from core.state import WorkerState
from ulits.llms import get_structred_llm
from core.schema import GeneratorSchema

logger=get_logger("Genrator")
structerd_llm=get_structred_llm("gemini-2.5-flash",GeneratorSchema)
logger.info("Structred llm iniliaze done")


def genrator_node_f(state:WorkerState)->dict:
    try:
        job_description=state["job_description"]
        cv=state["cv"]
        summary=state["scan_summary"]
        itreation=state["itreations_num"]

        if itreation>0:
            strengths=state["strengths"]
            weaknesses=state["weaknesses"]
            eval_summary=state["eval_summary"]
            techincal_q=state["techincal_questions"]

            prompt=f"""You are Tehcincal Lead make a specif techical questions this 
            strngths: {strengths} | weaknesses: {weaknesses} | summary: {eval_summary} | and this old questions: {techincal_q}
            make a another techincal question depented in (strngths,weaknesses,summary"""
            response=structerd_llm.invoke(prompt)
            logger.info(f"Tehcincal Questions: {response.techincal_questions}")
            return{"techincal_questions":response.techincal_questions}

        if itreation==0:

            prompt=f""" You are Tehcincal Lead make a specif techical questions for this candiate cv: {cv} and this a summary of cv {summary} with this job description {job_description} and about his projects to test his knowladge"""

            response=structerd_llm.invoke(prompt)
            logger.info(f"Tehcincal Questions: {response.techincal_questions}")
            return{
            "techincal_questions":response.techincal_questions
        }
    except Exception as e:
        logger.error(f"we have error in genrator:{e}")
        raise e
