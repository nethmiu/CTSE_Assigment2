from typing import TypedDict, List

class AgentState(TypedDict):
    lecture_notes: str        # Student 1 සඳහා
    summary: str              # Student 1 නිපදවන සාරාංශය
    quiz_questions: str       # Student 2 නිපදවන ප්‍රශ්න
    student_answers: str      # පරීක්ෂණය සඳහා ශිෂ්‍ය පිළිතුරු (Dummy)
    grading_results: str      # Student 3 ලබාදෙන ලකුණු
    final_study_plan: str     # Student 4 ලබාදෙන සැලසුම