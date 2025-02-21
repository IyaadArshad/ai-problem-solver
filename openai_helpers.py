import os
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_solution(problem):
    response = client.chat.completions.create(
      model="o3-mini",
      messages=[
        {"role": "developer", "content": [
            {"type": "text", "text": "You are Sir Sigma, you are a problem solver. You solve complex problems. Use functions appropriately"}
        ]},
        {"role": "user", "content": [
            {"type": "text", "text": f"Solve the following problem: {problem}"}
        ]}
      ],
      response_format={"type": "text"},
      reasoning_effort="high",
      tools=[
        {
          "type": "function",
          "function": {
            "name": "create_image",
            "description": "Creates an image using DALLE based on a given description.",
            "parameters": {
              "type": "object",
              "required": ["description"],
              "properties": {
                "description": {
                  "type": "string",
                  "description": "A textual description of the image to be generated"
                }
              },
              "additionalProperties": False
            },
            "strict": True
          }
        },
        {
          "type": "function",
          "function": {
            "name": "search",
            "description": "Search the internet for results",
            "parameters": {
              "type": "object",
              "required": ["query"],
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The search term or criteria used to filter results"
                }
              },
              "additionalProperties": False
            },
            "strict": True
          }
        }
      ]
    )
    return response.choices[0].message.content.strip()

def create_image(problem):
    response = client.chat.completions.create(
      model="o3-mini",
      messages=[
        {"role": "developer", "content": [
            {"type": "text", "text": "You are Sir Sigma, you are a problem solver. You solve complex problems. Use functions appropriately"}
        ]},
        {"role": "user", "content": [
            {"type": "text", "text": f"Create an image with description: {problem}"}
        ]}
      ],
      response_format={"type": "text"},
      reasoning_effort="high",
      tools=[
        {
          "type": "function",
          "function": {
            "name": "create_image",
            "description": "Creates an image using DALLE based on a given description.",
            "parameters": {
              "type": "object",
              "required": ["description"],
              "properties": {
                "description": {
                  "type": "string",
                  "description": "A textual description of the image to be generated"
                }
              },
              "additionalProperties": False
            },
            "strict": True
          }
        }
      ]
    )
    return response.choices[0].message.content.strip()

def perform_search(problem):
    response = client.chat.completions.create(
      model="o3-mini",
      messages=[
        {"role": "developer", "content": [
            {"type": "text", "text": "You are Sir Sigma, you are a problem solver. You solve complex problems. Use functions appropriately"}
        ]},
        {"role": "user", "content": [
            {"type": "text", "text": f"Search for: {problem}"}
        ]}
      ],
      response_format={"type": "text"},
      reasoning_effort="high",
      tools=[
        {
          "type": "function",
          "function": {
            "name": "search",
            "description": "Search the internet for results",
            "parameters": {
              "type": "object",
              "required": ["query"],
              "properties": {
                "query": {
                  "type": "string",
                  "description": "The search term or criteria used to filter results"
                }
              },
              "additionalProperties": False
            },
            "strict": True
          }
        }
      ]
    )
    return response.choices[0].message.content.strip().splitlines()

def additional_feature(problem):
    response = client.chat.completions.create(
      model="o3-mini",
      messages=[
        {"role": "developer", "content": [
            {"type": "text", "text": "You are Sir Sigma, you are a problem solver. You solve complex problems. Use functions appropriately"}
        ]},
        {"role": "user", "content": [
            {"type": "text", "text": f"Provide an additional analysis on: {problem}"}
        ]}
      ],
      response_format={"type": "text"},
      reasoning_effort="high"
    )
    return response.choices[0].message.content.strip()