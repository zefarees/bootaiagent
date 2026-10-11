import argparse
import json
import os
import sys
from call_function import available_functions, call_function
from dotenv import load_dotenv
from prompts import system_prompt



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
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions,
        )

        if response.usage is None:
            raise RuntimeError("No usage data in the response. The API request likely failed.")
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose=args.verbose)
                messages.append(result_message)
                if not result_message.get("content"):
                    raise RuntimeError(
                        f"Empty result from function call: {tool_call.function.name}"
                    )

                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            print(message.content)
            break
    else:
        print("Exceeded maximum iterations without a final response.")
        sys.exit(1)

    #    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    #    print(f"Response tokens: {response.usage.completion_tokens}")
    #    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
