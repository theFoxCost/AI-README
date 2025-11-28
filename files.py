import os
import time

content = 'Hi'
data_content = 'Data'


def write_content():
    file = "README.md"
    with open(file, "w") as f:
        f.write(f"{content}\n")
    print(f"Created {file}")

    # data_file = "payload.md"
    # with open(data_file, "w") as f:
    #     f.write(f"{data_content}\n")
    # print(f"Created {data_file}")

def make_structure():   
    pro_repo = input("Enter the Project Name: ") 
    if os.path.exists(pro_repo):
        print("⚠️Directory already exists!")
        exit()
    path = f"./main/{pro_repo}"
    os.makedirs(path)
    print("Created ", path)
    time.sleep(1)
    # make a function that make a README file (later with content)
    os.chdir(path)
    open("github.json", "w").close()
    write_content() 
    
    return path


    
def write_github_file(github_data):
    github_file = "github.json"
    with open(github_file, "w") as f:
        f.write(f"{github_data}\n")
    print(f"Created {github_file}")