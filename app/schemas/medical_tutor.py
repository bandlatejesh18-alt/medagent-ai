from pydantic import BaseModel, Field


class QuizQuestion(BaseModel):

    question: str = Field(
        description="A medical knowledge assessment question"
    )

    options: list[str] = Field(
        description="Four possible answer choices"
    )

    correct_answer: str = Field(
        description="The correct answer"
    )

    explanation: str = Field(
        description="Explanation of why the answer is correct"
    )


class MedicalTutorResponse(BaseModel):

    overview: str = Field(
        description="Brief definition of the medical concept"
    )

    basic_explanation: str = Field(
        description="Beginner-friendly explanation"
    )

    scientific_mechanism: str = Field(
        description="Detailed scientific and biological mechanism"
    )

    terminology: list[str] = Field(
        description="Important medical terminology with definitions"
    )

    clinical_relevance: str = Field(
        description="Educational clinical relevance of the concept"
    )

    quiz: list[QuizQuestion] = Field(
        description="Five MCQs to assess the student's understanding"
    )

    disclaimer: str = Field(
        description="Educational-use disclaimer"
    )