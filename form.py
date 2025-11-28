import time

def get_info():
    pro_name = input("Enter Project Name: ")
    link = input("Enter Project Link (no strings): ")
    time.sleep(0.5)
    time.sleep(0.5)
    desc = input("Enter Short Description (less than 50 words): ")
    time.sleep(0.5)
    tech_stack = input("Enter Tech Stack (eg: Python + React): ")
    time.sleep(0.5)
    main_features = input("Enter Main Features (Feature 1: Speedy, Feature 2: Easy to use): ")
    time.sleep(0.5)
    install_instr = input("Enter Installation Instructions (1. clone the repo 2.. 3..): ")
    time.sleep(0.5)
    run_cmd = input("Enter Run Commands (bash app.sh): ")
    time.sleep(0.5)
    env_vars = input("Enter Environment Variables (GROQ_API_KEY=YOUR?_GROQ_API_KEY): ")
    time.sleep(0.5)
    prjct_type = input("Enter Project Type (Webapp / CLI tool / Library / Hardware / Backend API): ")
    time.sleep(0.5)
    usage = input("Enter Usage Examples (eg: we use it to...): ")
    time.sleep(0.5)

    # fix this bug
    file_structure = input("Enter File Structure: ()")
    time.sleep(0.5)
    screenshots = input("Enter Screenshots / Demo Link (eg: https://webndev.io/wp-content/uploads/2024/02/groq-1024x1024.png): ")
    time.sleep(0.5)
    dependencies = input("Enter Dependencies (eg: nodejs LTS): ")
    time.sleep(0.5)
    license = input("Enter License (eg: MIT): ")
    time.sleep(0.5)
    install_req = input("Enter Installation Requirements (eg: pip install -r requirements.txt): ")
    time.sleep(0.5)
    known_issues = input("Enter Known Issues (eg: no issues yet): ")
    time.sleep(0.5)
    config_notes = input("Enter Configuration Notes (eg: no config): ")
    time.sleep(0.5)
    api_routes = input("Enter API Routes (if any) (eg: GET /api/users): ")
    time.sleep(0.5)
    overview = input("Enter High-Level Project Overview (less than 100 words): ")
    time.sleep(0.5)

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
