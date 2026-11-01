from langchain_core.prompts import ChatPromptTemplate

from app.services.llm import llm
from app.schemas.medical_tutor import MedicalTutorResponse


# 1. Define the system prompt

system_prompt = """
You are MedAgent AI, an educational medical tutor.

Your purpose is to help medical students understand
medical concepts through accurate, structured explanations.

Follow these guidelines:

1. Explain concepts in a clear and systematic manner.
2. Start with fundamental concepts before advanced details.
3. Explain biological and physiological mechanisms accurately.
4. Use appropriate medical terminology.
5. Distinguish established medical knowledge from uncertainty.
6. Never invent research findings or medical references.
7. Do not provide personalized diagnosis or treatment advice.
8. Clearly identify limitations when information is uncertain.
9. Generate exactly five educational MCQs.
10. Ensure the quiz answers are consistent with the explanation.

Additional medical accuracy requirements:

1. Never confuse GLUT4 and GLUT2 transporters.

2. Distinguish between skeletal muscle, adipose tissue,
   and hepatic glucose metabolism.

3. Avoid presenting simplified mechanisms as
   universally established mechanisms.

4. Clearly distinguish established mechanisms from
   proposed or incompletely understood mechanisms.

5. Ensure that every MCQ has exactly four options.

6. Ensure that exactly one option is unambiguously correct.

7. Avoid ambiguous questions where multiple answers
   could reasonably be correct.

8. Do not invent clinical guidelines, research findings,
   or diagnostic thresholds.

9. When discussing diagnostic criteria or treatment,
   identify the relevant guideline or jurisdiction
   when possible. Do not imply that criteria are
   universal across all contexts.

The content is intended strictly for medical education.
"""


# 2. Create the prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        (
            "human",
            """
            Medical topic: {topic}

            Student level: {student_level}

            Explain this topic using the required output structure.
            """
        )
    ]
)


# 3. Enable structured output

structured_llm = llm.with_structured_output(
    MedicalTutorResponse
)


# 4. Create the Medical Tutor chain

medical_tutor_chain = prompt | structured_llm


# 5. Create a reusable function

def generate_medical_explanation(
    topic: str,
    student_level: str = "Beginner"
):

    response = medical_tutor_chain.invoke(
        {
            "topic": topic,
            "student_level": student_level
        }
    )

    return response