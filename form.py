import time

def get_info():
    pro_name = input("Enter Project Name: ")
    time.sleep(0.5)
    link = input("Enter Project Link: ")
    time.sleep(0.5)
    desc = input("Enter Short Description: ")
    time.sleep(0.5)
    tech_stack = input("Enter Tech Stack (eg: Python + React): ")
    time.sleep(0.5)
    main_features = input("Enter Main Features: ")
    time.sleep(0.5)
    install_instr = input("Enter Installation Instructions: ")
    time.sleep(0.5)
    run_cmd = input("Enter Run Commands: ")
    time.sleep(0.5)
    env_vars = input("Enter Environment Variables: ")
    time.sleep(0.5)
    prjct_type = input("Enter Project Type (Webapp / CLI tool / Library / Hardware / Backend API): ")
    time.sleep(0.5)
    usage = input("Enter Usage Examples: ")
    time.sleep(0.5)
    file_structure = input("Enter File Structure: ")
    time.sleep(0.5)
    screenshots = input("Enter Screenshots / Demo Link: ")
    time.sleep(0.5)
    dependencies = input("Enter Dependencies: ")
    time.sleep(0.5)
    license = input("Enter License: ")
    time.sleep(0.5)
    install_req = input("Enter Installation Requirements: ")
    time.sleep(0.5)
    known_issues = input("Enter Known Issues: ")
    time.sleep(0.5)
    config_notes = input("Enter Configuration Notes: ")
    time.sleep(0.5)
    api_routes = input("Enter API Routes (if any): ")
    time.sleep(0.5)
    overview = input("Enter High-Level Project Overview: ")
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
