from openai import OpenAI

client = OpenAI()

VECTOR_STORE_ID = "vs_699cbe091514819182d503f1c6765803"  # your vector store

def answer_question(user_question: str) -> str:
    system_instructions = """
You are Revalia's client-facing assistant for the Human Data Trial Innovation collaboration.
Rules:
- Use ONLY the provided documents via file search for factual claims about offerings, timelines, eligibility, and processes.
- If the docs do not contain the answer, say so and offer to connect the person with the Revalia team.
- Do not provide medical advice. Do not guess.
- Keep answers concise and professional.
"""

    resp = client.responses.create(
        model="gpt-4.1-mini",  # example; pick your preferred model
        input=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_question},
        ],
        tools=[{"type": "file_search"}],
        tool_resources={
            "file_search": {
                "vector_store_ids": [VECTOR_STORE_ID]
            }
        }
    )

    return resp.output_text
