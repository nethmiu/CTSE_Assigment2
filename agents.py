from langchain_ollama import OllamaLLM
from state import AgentState
from logger_config import logger # Logging එකතු කරන ලදී

# Initialize the Local LLM (Llama 3)
llm = OllamaLLM(model="llama3")

# Student 1: The Content Summarizer
def summarizer_agent(state: AgentState):
    logger.info("AGENT 1: Summarizer task execution started.")
    print("\n--- [AGENT 1] SUMMARIZING CONTENT ---")
    prompt = f"""
    SYSTEM: You are a distinguished University Professor. 
    TASK: Summarize the following lecture notes into a professional academic abstract. 
    CONSTRAINT: Focus on core concepts and eliminate redundant information. Use only English.
    
    NOTES: {state['lecture_notes']}
    """
    state['summary'] = llm.invoke(prompt)
    logger.info("AGENT 1: Summarizer task execution finished.")
    return state

# Student 2: The Question Generator
def question_generator_agent(state: AgentState):
    logger.info("AGENT 2: Question Generator task execution started.")
    print("\n--- [AGENT 2] GENERATING MCQ QUIZ ---")
    prompt = f"""
    SYSTEM: You are a Senior Examiner. 
    TASK: Based on the summary provided, generate 3 challenging Multiple Choice Questions (MCQs).
    CONSTRAINT: Provide 4 options (A, B, C, D) for each question and indicate the correct answer. Use only English.
    
    SUMMARY: {state['summary']}
    """
    state['quiz_questions'] = llm.invoke(prompt)
    logger.info("AGENT 2: Question Generator task execution finished.")
    return state

# Student 3: The Performance Evaluator
def evaluator_agent(state: AgentState):
    logger.info("AGENT 3: Performance Evaluator task execution started.")
    print("\n--- [AGENT 3] EVALUATING PERFORMANCE ---")
    prompt = f"""
    SYSTEM: You are an Academic Evaluator. 
    TASK: Evaluate the student's understanding based on the generated quiz. 
    CONSTRAINT: Provide a grade out of 100 and identify specific areas where the student might struggle. Use only English.
    
    QUIZ: {state['quiz_questions']}
    """
    state['grading_results'] = llm.invoke(prompt)
    logger.info("AGENT 3: Performance Evaluator task execution finished.")
    return state

# Student 4: The Study Planner
def study_planner_agent(state: AgentState):
    logger.info("AGENT 4: Study Planner task execution started.")
    print("\n--- [AGENT 4] CREATING STUDY PLAN ---")
    prompt = f"""
    SYSTEM: You are an Expert Study Consultant. 
    TASK: Based on the grading results and identified weaknesses, design a 7-day intensive study schedule.
    CONSTRAINT: Format the plan clearly from Day 1 to Day 7. Include specific topics to review. Use only English.
    
    EVALUATION: {state['grading_results']}
    """
    state['final_study_plan'] = llm.invoke(prompt)
    logger.info("AGENT 4: Study Planner task execution finished.")
    return state