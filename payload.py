import lang


# make  function that get the data from github.json

def read_github_file():
    github_file = "github.json"
    with open(github_file, "r") as f:
        github_data = f.read()
    return github_data

# make a function tht get the language from lang.py

# make  function that get the data from prompt.md
def read_prompt_file():
    prompt_file = "prompt.md"
    with open(prompt_file, "r") as f:
        prompt_data = f.read()
    return prompt_data

# make function that combine all of that and return a thing and put it on payload.md as content
def the_data():
    language = lang.choose_lang()
    github_data = read_github_file()
    prompt_data = read_prompt_file()
    data_content = f"use the following data: the language is{language}\n and the prompt data is{prompt_data}\nand the github data is{github_data}\n"
    Payload_file = "Payload.md"
    with open(Payload_file, "w", encoding="utf-8") as f:
        f.write(data_content)
    print("payload.md created successfully")    
    return data_content




