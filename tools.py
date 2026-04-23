import json

# Student 1: File Reader
def file_reader_tool(file_path: str) -> str:
    """Used to read lecture notes from a local text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Student 2: Quiz Exporter
def quiz_exporter_tool(quiz_content: str):
    """Saves the generated quiz questions into a JSON file."""
    try:
        with open("quiz.json", "w", encoding='utf-8') as f:
            json.dump({"quiz": quiz_content}, f, ensure_ascii=False, indent=4)
        return "Quiz saved to quiz.json"
    except Exception as e:
        return f"Error saving quiz: {str(e)}"

# Student 3: Grader Tool
def grader_tool(score: int) -> str:
    """Determines the academic performance level based on the score provided."""
    if score >= 75: 
        return "Distinction"
    elif score >= 50: 
        return "Pass"
    else: 
        return "Needs Improvement"

# Student 4: Planner Formatter
def planner_formatter_tool(plan: str):
    """Saves the finalized study plan into a text file."""
    try:
        with open("study_plan.txt", "w", encoding='utf-8') as f:
            f.write(plan)
        return "Study plan saved to study_plan.txt"
    except Exception as e:
        return f"Error saving study plan: {str(e)}"