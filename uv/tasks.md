1. Create a new project using uv 'python-training', make sure you do it with the newest stable Python version.

2. In a newly created project, add 'typer' to dependencies (main group) and 'pytest' to dev dependencies group

Verify it works by running `uv run pytest -v`. You should get a message 'no tests ran in 0.00s'
Verify main dependency by running python interpreter and trying to import `typer`.
Remove .venv directory and try running `uv sync`
Remove .venv directory again and try running `uv run pytest -v`. Observe what's happening

3. Create a new script file `a_script.py` with the following contents:
```
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pythonpath: str = ""


settings = Settings()
```
If you try to run it with `uv run a_script.py` now, it will fail because pydantic-settings (a library required to run this module) is not installed.
Add it to script requirements (uv add --script ...) and try running the script again.
*Create a lockfile for the script.
