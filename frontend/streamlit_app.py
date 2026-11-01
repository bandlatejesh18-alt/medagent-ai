import sys
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Add project root to Python import path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from app.services.medical_tutor import generate_medical_explanation


# Page configuration
st.set_page_config(
    page_title="MedAgent AI",
    page_icon="🩺",
    layout="wide"
)


# Application heading
st.title("🩺 MedAgent AI")

st.subheader("Your AI-powered Medical Learning Assistant")

st.write(
    "Understand medical concepts through structured explanations, "
    "scientific mechanisms, terminology and interactive quizzes."
)

st.divider()


# User inputs
st.header("Medical Tutor")

topic = st.text_input(
    "Enter a medical topic",
    placeholder="Example: Type 2 Diabetes"
)

student_level = st.selectbox(
    "Select your learning level",
    ["Beginner", "Intermediate", "Advanced"]
)


# Generate explanation
if st.button("Generate Explanation", type="primary"):

    if not topic.strip():

        st.warning("Please enter a medical topic.")

    else:

        try:

            with st.spinner("Generating your medical explanation..."):

                response = generate_medical_explanation(
                    topic=topic,
                    student_level=student_level
                )

            st.success("Explanation generated successfully!")

            # Overview
            st.header("1. Overview")
            st.write(response.overview)

            # Basic explanation
            st.header("2. Basic Explanation")
            st.write(response.basic_explanation)

            # Scientific mechanism
            st.header("3. Scientific Mechanism")
            st.write(response.scientific_mechanism)

            # Terminology
            st.header("4. Medical Terminology")

            for term in response.terminology:
                st.write(f"• {term}")

            # Clinical relevance
            st.header("5. Clinical Relevance")
            st.write(response.clinical_relevance)

            # Quiz
            st.header("6. Test Your Understanding")

            for index, question in enumerate(response.quiz):

                with st.expander(f"Question {index + 1}"):

                    # Display question
                    st.write(question.question)

                    # Display options with A, B, C, D
                    option_letters = ["A", "B", "C", "D"]

                    formatted_options = [
                        f"{option_letters[i]}. {option}"
                        for i, option in enumerate(question.options)
                    ]

                    # Let the student select an answer
                    selected_option = st.radio(
                        "Select your answer:",
                        formatted_options,
                        key=f"quiz_option_{index}",
                        index=None
                    )

                    st.divider()

                    # Button to reveal answer
                    button_key = f"show_answer_{index}"

                    if button_key not in st.session_state:
                        st.session_state[button_key] = False

                    if st.button(
                        "Show Answer & Explanation",
                        key=f"reveal_button_{index}"
                    ):
                        st.session_state[button_key] = True

                    # Reveal answer only when requested
                    if st.session_state[button_key]:

                        st.success(
                            f"Correct Answer: {question.correct_answer}"
                        )

                        st.markdown("**Explanation:**")

                        st.write(question.explanation)

            # Disclaimer
            st.divider()

            st.caption(response.disclaimer)

        except Exception as e:

            st.error(
                "Something went wrong while generating the explanation."
            )

            st.exception(e)