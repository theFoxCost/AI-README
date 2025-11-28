import files
import fetch
import form as f
import payload
import time
import Post as post

print("✨ If you wanted to let ai Auto-Generate Certain Info just place: [ai-auto-generate] in the form field")
time.sleep(2)
files.make_structure()
fetch.auth()
form_data = f.get_info()

def generate_prompt_file(form_data):
    prompt = f"""
You are a professional software engineer and technical writer. 
Your task is to generate a complete, high-quality README.md file for a project.

Here’s the project information (fill with actual details):
- Project Name: {form_data.get('name', '')}
- Link: {form_data.get('link', '')}
- Short Description: {form_data.get('desc', '')}
- Tech Stack: {form_data.get('tech_stack', '')}
- Main Features: {form_data.get('main_features', '')}
- Installation Instructions: {form_data.get('install_instr', '')}
- Run Commands: {form_data.get('run_cmd', '')}
- Environment Variables: {form_data.get('env_vars', '')}
- Project Type: {form_data.get('prjct_type', '')}
- Usage Examples: {form_data.get('usage', '')}
- File Structure: {form_data.get('file_structure', '')}
- Screenshots / Demo Link: {form_data.get('screenshots', '')}
- Dependencies: {form_data.get('dependencies', '')}
- License: {form_data.get('license', '')}
- Installation Requirements: {form_data.get('install_req', '')}
- Known Issues: {form_data.get('known_issues', '')}
- Configuration Notes: {form_data.get('config_notes', '')}
- API Routes: {form_data.get('api_routes', '')}
- High-Level Project Overview: {form_data.get('overview', '')}

**Requirements for the README:**
1. Start with the Project Name as a title (`# Project Name`) and link.
2. Include a clear description section explaining the purpose and value of the project.
3. List the Tech Stack and Main Features in bullet points.
4. Provide Installation Instructions and Run Commands in code blocks.
5. Include Environment Variables if necessary.
6. Clearly indicate the Project Type.
7. Provide Usage Examples and File Structure.
8. Include Screenshots or Demo Links as Markdown images/links.
9. List Dependencies and License clearly.
10. Include any Installation Requirements, Known Issues, and Configuration Notes.
11. Document API Routes (if any) in a table or code block.
12. Provide a High-Level Project Overview (architecture or flow diagram if applicable) in a clear section.
13. Make the README professional, clean, easy to read, well-formatted in Markdown, and suitable for GitHub.
14. Use proper headings (##, ###), bullet points, code blocks, and links.
15. Optional: Add badges for license, build status, or tech stack if relevant.

Return ONLY the fully formatted README Markdown content.
"""
    prompt_file = "prompt.md"
    with open(prompt_file, "w", encoding="utf-8", errors="replace") as f:
        f.write(prompt)
    print(f"✅ Generated the prompt file: {prompt_file}")
    return prompt_file


start_time = time.perf_counter()

generate_prompt_file(form_data)

payload_data = payload.the_data()

result = post.send_to_groq(payload_data)

end_time = time.perf_counter()
elapsed = round(end_time - start_time, 2)

print(f"⏱ Total processing time: {elapsed} seconds")
print("✅ Done!")
print("WARNING:⚠️ It Is recommended to edit your README.md file manually.")
