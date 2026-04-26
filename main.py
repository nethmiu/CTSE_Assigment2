from langgraph.graph import StateGraph, END
from state import AgentState
from agents import summarizer_agent, question_generator_agent, evaluator_agent, study_planner_agent
# summary_saver_tool එක import කරන ලදී
from tools import file_reader_tool, planner_formatter_tool, quiz_exporter_tool, summary_saver_tool
from logger_config import logger 

# Initialize the Workflow Graph
workflow = StateGraph(AgentState)

# 1. Add Nodes
workflow.add_node("summarizer", summarizer_agent)
workflow.add_node("quiz_gen", question_generator_agent)
workflow.add_node("evaluator", evaluator_agent)
workflow.add_node("planner", study_planner_agent)

# 2. Define Edges
workflow.set_entry_point("summarizer")
workflow.add_edge("summarizer", "quiz_gen")
workflow.add_edge("quiz_gen", "evaluator")
workflow.add_edge("evaluator", "planner")
workflow.add_edge("planner", END)

# 3. Compile the System
app = workflow.compile()

if __name__ == "__main__":
    logger.info("=== EDUCATIONAL MULTI-AGENT SYSTEM STARTED ===")
    
    content = file_reader_tool("notes.txt")
    
    if content and not content.startswith("Error"):
        # Execute the Multi-Agent System
        result = app.invoke({"lecture_notes": content})
        
        print("\n" + "="*70)
        print("          COMPLETE MULTI-AGENT SYSTEM EXECUTION LOG          ")
        print("="*70)
        
        # --- Student 1 Output ---
        print(f"\n[STUDENT 1: SUMMARIZER OUTPUT]\n{'-'*30}")
        summary_out = result.get('summary', 'No summary generated.')
        print(summary_out)
        # සාරාංශය summary.txt ලෙස සේව් කිරීම
        summary_saver_tool(summary_out)
        
        # --- Student 2 Output ---
        print(f"\n[STUDENT 2: QUESTION GENERATOR OUTPUT]\n{'-'*30}")
        print(result.get('quiz_questions', 'No quiz generated.'))
        quiz_exporter_tool(result['quiz_questions'])
        
        # --- Student 3 Output ---
        print(f"\n[STUDENT 3: PERFORMANCE EVALUATOR OUTPUT]\n{'-'*30}")
        print(result.get('grading_results', 'No evaluation results.'))
        
        # --- Student 4 Output ---
        print(f"\n[STUDENT 4: STUDY PLANNER OUTPUT]\n{'-'*30}")
        print(result.get('final_study_plan', 'No study plan generated.'))
        
        # Final Persistence for Student 4
        planner_formatter_tool(result['final_study_plan'])
        
        print("\n" + "="*70)
        print("SYSTEM EXECUTION COMPLETE: Summary, Quiz, and Plan saved locally.")
        print("="*70)
        
        logger.info("=== EDUCATIONAL MULTI-AGENT SYSTEM FINISHED SUCCESSFULLY ===")
    else:
        logger.error(f"CRITICAL ERROR: {content}")