import os
import openai

# Set your OpenAI API key (ensure your environment variable is configured)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_solution(problem):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Solve the following problem: {problem}"}
        ]
    )
    return response.choices[0].message.content.strip()

def create_image(problem):
    response = openai.Image.create(
        prompt=problem,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

def perform_search(problem):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Perform a search analysis for: {problem}"}
        ]
    )
    # Split the answer into a list if needed, or return as-is
    return response.choices[0].message.content.strip().splitlines()

def additional_feature(problem):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Provide an additional analysis on: {problem}"}
        ]
    )
    return response.choices[0].message.content.strip()
