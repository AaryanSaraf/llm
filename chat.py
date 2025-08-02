from openai import OpenAI
import os
import subprocess
import json

client = OpenAI(
    api_key="AIzaSyBFNVIPkou4BbwASnc8GAVvRHsLLjK3Aeg",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def command(cmd):
    result= subprocess.run(cmd,shell=True)

def create_file(sample_json):
    path = sample_json.get("path")
    content = sample_json.get("content")
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    with open(path, "w") as file:
        file.write(content)


system_prompt="""
    You are a helpful AI coding assistant who executes commands based on user inputs. Always suggest the plan to user and ask "Apply this? (y/n)" before making changes.
    You are a coding assistant that responds with structured JSON to help scaffold projects. Only create server-related files if explicitly asked. If the user only requests frontend functionality (like HTML/CSS/JS), do not include any backend code.

    Call the command() function if user asks to execute a terminal command. Call create_file() function when asked to create or write  code in a file.
    Always respond in JSON with:
    - type: "file" or "command"
    - path and content if type is file
    - command if type is command
    Organize files into logical directories. 
    - Backend/server files go in a 'server/' folder
    - Frontend files go in a 'client/' folder
    - Place HTML files in 'client/', not root
    - For Express projects, default to 'server/server.js'
    }
"""


messages=[
        {"role":"system","content":system_prompt},
    ]

while True:
    user_query = input('> ')
    if user_query.lower().strip() == "exit":
        print("👋 Exiting.")
        break
    messages.append({ "role": "user", "content": user_query })
    while True:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            response_format={"type": "json_object"},
            messages=messages
        )
        parsed_output = json.loads(response.choices[0].message.content)
        print(parsed_output)
        if parsed_output.get("type")=="file":
            res=input("Apply changes? (y/n)")
            if res=="y":
                create_file(parsed_output)
            break

        if parsed_output.get("type")=="command":
            res=input("Apply changes? (y/n)")
            if res=="y":
                com= parsed_output.get("command")
                command(com)
            break
