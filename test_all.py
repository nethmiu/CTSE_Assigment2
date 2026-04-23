from agents import summarizer_agent, question_generator_agent, evaluator_agent, study_planner_agent

def test_student_1_summarizer():
    print("\n--- Testing Student 1: Summarizer Agent ---")
    test_input = {"lecture_notes": "Software testing ensures quality. It includes unit, integration, and system testing."}
    result = summarizer_agent(test_input)
    
    # Assertions for Accuracy 
    assert "summary" in result, "The summarizer output must contain the 'summary' key."
    assert len(result["summary"]) > 10, "The generated summary is too short."
    assert "testing" in result["summary"].lower(), "The summary must mention the primary topic (testing)."
    print("Student 1 Test Passed!")

def test_student_2_question_gen():
    print("\n--- Testing Student 2: Question Generator Agent ---")
    test_input = {"summary": "Microservices are small, independent services communicating via APIs."}
    result = question_generator_agent(test_input)
    
    # Assertions for MCQ format and content
    assert "quiz_questions" in result, "The output must contain the 'quiz_questions' key."
    assert "?" in result["quiz_questions"], "The quiz must contain at least one question mark."
    print("Student 2 Test Passed!")

def test_student_3_evaluator():
    print("\n--- Testing Student 3: Performance Evaluator Agent ---")
    test_input = {"quiz_questions": "What is AI?", "student_answers": "AI is Artificial Intelligence."}
    result = evaluator_agent(test_input)
    
    # Assertions for Grading accuracy 
    assert "grading_results" in result, "The output must contain the 'grading_results' key."
    assert any(char.isdigit() for char in result["grading_results"]), "The evaluation result must contain a numeric score."
    print("Student 3 Test Passed!")

def test_student_4_planner():
    print("\n--- Testing Student 4: Study Planner Agent ---")
    test_input = {"grading_results": "The student scored 40/100. Weak in Microservices."}
    result = study_planner_agent(test_input)
    
    # Assertions for Plan structure
    assert "final_study_plan" in result, "The output must contain the 'final_study_plan' key."
    assert "Day" in result["final_study_plan"], "The study plan must follow a daily schedule format."
    print("Student 4 Test Passed!")

if __name__ == "__main__":
    print("Starting Individual Agent Validations...")
    try:
        test_student_1_summarizer()
        test_student_2_question_gen()
        test_student_3_evaluator()
        test_student_4_planner()
        print("\n" + "="*40)
        print("ALL INDIVIDUAL TESTS PASSED SUCCESSFULLY!")
        print("="*40)
    except AssertionError as e:
        print(f"\nTEST FAILED: {e}")