use the following data: the language isEnglish
 and the prompt data is
You are a professional software engineer and technical writer. 
Your task is to generate a complete, high-quality README.md file for a project.

Hereâ€™s the project information (fill with actual details):
- Project Name: HTTPRequests
- Link: https://github.com/nateprewitt/HTTPRequests
- Short Description: Basic HTTP request library written in Python for educational purposes 
- Tech Stack: Python
- Main Features: This is an attempt at building yet another http library for educational purposes. Any critiques or comments are welcome. I'm using RFC2616 and RFC7230 as the primary guides for this code, and testing it against popular web services (google, amazon, facebook, etc.)
- Installation Instructions: 
- Run Commands: fsdf
- Environment Variables: 45fgdfg45
- Project Type: Library
- Usage Examples: from HTTPRequests.request import HttpRequest
- File Structure: 
- Screenshots / Demo Link: req = HttpRequest('www.w3c.org')
- Dependencies: resp = req.get('/Protocols/rfc2616/ref2616.html')
- License: print resp #This will print response body
- Installation Requirements: mit
- Known Issues: dsq
- Configuration Notes: 
- API Routes: 
- High-Level Project Overview: idk i 

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

and the github data is{'id': 23167684, 'node_id': 'MDEwOlJlcG9zaXRvcnkyMzE2NzY4NA==', 'name': 'HTTPRequests', 'full_name': 'nateprewitt/HTTPRequests', 'private': False, 'owner': {'login': 'nateprewitt', 'id': 5271761, 'node_id': 'MDQ6VXNlcjUyNzE3NjE=', 'avatar_url': 'https://avatars.githubusercontent.com/u/5271761?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/nateprewitt', 'html_url': 'https://github.com/nateprewitt', 'followers_url': 'https://api.github.com/users/nateprewitt/followers', 'following_url': 'https://api.github.com/users/nateprewitt/following{/other_user}', 'gists_url': 'https://api.github.com/users/nateprewitt/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/nateprewitt/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/nateprewitt/subscriptions', 'organizations_url': 'https://api.github.com/users/nateprewitt/orgs', 'repos_url': 'https://api.github.com/users/nateprewitt/repos', 'events_url': 'https://api.github.com/users/nateprewitt/events{/privacy}', 'received_events_url': 'https://api.github.com/users/nateprewitt/received_events', 'type': 'User', 'user_view_type': 'public', 'site_admin': False}, 'html_url': 'https://github.com/nateprewitt/HTTPRequests', 'description': 'Basic HTTP request library written in Python for educational purposes', 'fork': False, 'url': 'https://api.github.com/repos/nateprewitt/HTTPRequests', 'forks_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/forks', 'keys_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/teams', 'hooks_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/hooks', 'issue_events_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/issues/events{/number}', 'events_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/events', 'assignees_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/assignees{/user}', 'branches_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/branches{/branch}', 'tags_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/tags', 'blobs_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/languages', 'stargazers_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/stargazers', 'contributors_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/contributors', 'subscribers_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/subscribers', 'subscription_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/subscription', 'commits_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/contents/{+path}', 'compare_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/merges', 'archive_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/downloads', 'issues_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/issues{/number}', 'pulls_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/labels{/name}', 'releases_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/releases{/id}', 'deployments_url': 'https://api.github.com/repos/nateprewitt/HTTPRequests/deployments', 'created_at': '2014-08-20T23:33:39Z', 'updated_at': '2022-07-16T05:06:17Z', 'pushed_at': '2016-03-23T17:09:09Z', 'git_url': 'git://github.com/nateprewitt/HTTPRequests.git', 'ssh_url': 'git@github.com:nateprewitt/HTTPRequests.git', 'clone_url': 'https://github.com/nateprewitt/HTTPRequests.git', 'svn_url': 'https://github.com/nateprewitt/HTTPRequests', 'homepage': '', 'size': 43, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'Python', 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'has_discussions': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': {'key': 'isc', 'name': 'ISC License', 'spdx_id': 'ISC', 'url': 'https://api.github.com/licenses/isc', 'node_id': 'MDc6TGljZW5zZTEw'}, 'allow_forking': True, 'is_template': False, 'web_commit_signoff_required': False, 'topics': [], 'visibility': 'public', 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master', 'temp_clone_token': None, 'network_count': 0, 'subscribers_count': 1}

