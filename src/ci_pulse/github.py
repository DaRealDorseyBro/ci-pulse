import requests

GITHUB_BASE_URL="https://api.github.com"

def get_workflow_runs(owner: str, repo: str, token: str) -> list[dict]:

    runs_url=f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/actions/runs"
    headers = { 'Authorization': f"Bearer {token}", 'Accept': 'application/vnd.github+json' }

    response = requests.get(runs_url, headers=headers, timeout=10)
    response.raise_for_status()

    runs = response.json().workflow_runs
    return [runs]



