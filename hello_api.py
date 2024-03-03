import os
from openai import OpenAI # version 1.0+
from dotenv import load_dotenv

load_dotenv()
# if you get openai errors, run pip install --upgrade openai

llm = OpenAI(
    # place your OpenAI key in an environment variable
    api_key=os.environ['OPENAI_API_KEY'], # this is the default
    #base_url="http://localhost:1234/v1"  # see chapter 1 video 3
)
print("OPENAI_API_KEY="+os.environ['OPENAI_API_KEY'])

system_prompt = """Make sure all responses are in French.
    DESCRIPTION:
"""
user_input = """what is the capital of Tunisia"""

response = llm.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=500,
    temperature=0.7,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)
