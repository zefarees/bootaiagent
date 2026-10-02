import argparse
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

from openai import OpenAI

if api_key is None:
    raise RuntimeError(
        "OPENROUTER_API_KEY not found"
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )
    if response.usage is None:
        raise RuntimeError("No usage data in the response.")

    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
