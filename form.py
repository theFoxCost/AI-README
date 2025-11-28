import time

def get_info():
    pro_name = input("Enter Project Name: ")
    link = input("Enter Project Link (no strings): ")
    desc = input("Enter Short Description (less than 50 words): ")
    tech_stack = input("Enter Tech Stack (eg: Python + React): ")
    main_features = input("Enter Main Features (Feature 1: Speedy, Feature 2: Easy to use): ")
    install_instr = input("Enter Installation Instructions (1. clone the repo 2.. 3..): ")
    run_cmd = input("Enter Run Commands (bash app.sh): ")
    env_vars = input("Enter Environment Variables (GROQ_API_KEY=YOUR?_GROQ_API_KEY): ")
    prjct_type = input("Enter Project Type (Webapp / CLI tool / Library / Hardware / Backend API): ")
    usage = input("Enter Usage Examples (eg: we use it to...): ")

    print("Enter File Structure (press Enter on an empty line to finish) powershel(tree .) linux(ls -R):")
    file_structure_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        file_structure_lines.append(line)
    file_structure = "\n".join(file_structure_lines)

    screenshots = input("Enter Screenshots / Demo Link (eg: https://webndev.io/wp-content/uploads/2024/02/groq-1024x1024.png): ")
    dependencies = input("Enter Dependencies (eg: nodejs LTS): ")
    license = input("Enter License (eg: MIT): ")
    install_req = input("Enter Installation Requirements (eg: pip install -r requirements.txt): ")
    known_issues = input("Enter Known Issues (eg: no issues yet): ")
    config_notes = input("Enter Configuration Notes (eg: no config): ")
    api_routes = input("Enter API Routes (if any) (eg: GET /api/users): ")
    overview = input("Enter High-Level Project Overview (less than 100 words): ")

    return {
        "name": pro_name,
        "link": link,
        "desc": desc,
        "tech_stack": tech_stack,
        "main_features": main_features,
        "install_instr": install_instr,
        "run_cmd": run_cmd,
        "env_vars": env_vars,
        "prjct_type": prjct_type,
        "usage": usage,
        "file_structure": file_structure,
        "screenshots": screenshots,
        "dependencies": dependencies,
        "license": license,
        "install_req": install_req,
        "known_issues": known_issues,
        "config_notes": config_notes,
        "api_routes": api_routes,
        "overview": overview
    }
