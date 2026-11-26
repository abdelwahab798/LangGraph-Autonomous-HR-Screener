from core.logger import get_logger
from core.state import WorkerState
from ulits.llms import get_structred_llm
from core.schema import EvaluatorSchema

logger=get_logger("Evaluator")
structerd_llm=get_structred_llm("gemini-2.5-pro",EvaluatorSchema)
logger.info("Structred llm iniliaze done")


def genrator_node(state:WorkerState)->dict:
    try:
        job_description=state["job_description"]
        cv=state["cv"]
        summary=state["scan_summary"]
        techincal_q=state["techincal_questions"]
        itreation=state["itreations_num"]

        prompt=f""" You are Tehcincal Lead eval this specif techical questions for this candiate cv: {cv} and this a summary of cv {summary} with this job description {job_description} to test his knowladge and make make a overall_score for questions -
          eval_summary - strengths - weaknesses  """

        response=structerd_llm.invoke(prompt)
        logger.info(f"Eval_overall_score: {response.overall_score}|Eval_summary: {response.eval_summary} |  Strengths: {response.strengths} | Weaknesses: {response.weaknesses} ")
        itreation=itreation+1
        return{
            "eval_overall_score":response.overall_score,
            "eval_summary":response.eval_summary,
            "strengths":response.strengths,
            "weaknesses":response.weaknesses,
            "itreations_num":itreation
        }
    except Exception as e:
        logger.error("we have error in genrator: ",e)
        raise e


