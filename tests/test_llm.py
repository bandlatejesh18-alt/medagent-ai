from app.services.llm import llm


def test_llm_connection():

    response = llm.invoke(
        "Explain insulin in simple terms."
    )

    print(response.content)


if __name__ == "__main__":
    test_llm_connection()