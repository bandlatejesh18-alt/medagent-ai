from app.services.medical_tutor import generate_medical_explanation


def test_medical_tutor():

    # response = generate_medical_explanation(
    #     topic="Type 2 Diabetes",
    #     student_level="Intermediate"
    # )
    
    # response = generate_medical_explanation(
    # topic="Mechanism of action of insulin",
    # student_level="Beginner"
    # )
    
    response = generate_medical_explanation(
    topic="Pathophysiology of myocardial infarction",
    student_level="Advanced"
    )
    
    print("\n========== MEDICAL TUTOR ==========\n")

    print("OVERVIEW:")
    print(response.overview)

    print("\nBASIC EXPLANATION:")
    print(response.basic_explanation)

    print("\nSCIENTIFIC MECHANISM:")
    print(response.scientific_mechanism)

    print("\nTERMINOLOGY:")

    for term in response.terminology:
        print("-", term)

    print("\nCLINICAL RELEVANCE:")
    print(response.clinical_relevance)

    print("\nQUIZ:")

    for index, question in enumerate(response.quiz, start=1):

        print(f"\nQuestion {index}: {question.question}")

        for option in question.options:
            print("-", option)

        print("Correct answer:", question.correct_answer)
        print("Explanation:", question.explanation)

    print("\nDISCLAIMER:")
    print(response.disclaimer)


if __name__ == "__main__":
    test_medical_tutor()