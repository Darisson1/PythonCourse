## Copilot / AI agent instructions for this workspace

Purpose: short, actionable guidance so an AI coding agent can be productive quickly in this small Python learning workspace.

1) Big picture
- This repository contains small, standalone Python learning scripts (no package/virtualenv present). Two main folders of interest:
  - `PythonFullCourseForBeginners/` — very small demo script `app.py` (prints and simple variables).
  - `JustCrap/` — slightly more structured sample: `triangle_type_enum.py` defines `TriangleType` (an Enum) and `task.py` contains `triangle_type(a,b,c)` which imports that enum and prints a sample call.

2) How to run (Windows PowerShell)
- Run scripts directly with the system Python. Example:
  - `python .\PythonFullCourseForBeginners\app.py`
  - `python .\JustCrap\task.py`
- There is no requirements.txt or virtualenv in the repo. Assume a modern Python 3 interpreter (3.8+).

3) Project-specific patterns & conventions (discoverable from files)
- Files are simple, single-file scripts — avoid introducing complex packaging unless requested.
- `JustCrap/task.py` uses type hints and returns an Enum value from `triangle_type_enum.py` — prefer keeping the API signature stable: `triangle_type(a:int,b:int,c:int) -> TriangleType`.
- Top-level code prints test/demo output (e.g., `print(triangle_type(-3,-3,-3))`). If you add or change functions, keep the demo runnable as a top-level script unless converting the project to a package.

4) Safe edits the agent can make without asking
- Fix obvious bugs, add small helper functions, or improve readability in these scripts.
- Add unit tests under a new `tests/` folder (use `pytest`) if asked — but do not modify file names or delete demo prints unless requested.

5) When to ask the maintainer
- Before converting the workspace into a package or adding dependency management (venv/requirements/pyproject).
- Before removing or suppressing top-level demo/print statements that the owner likely added on purpose.

6) Integration points / external dependencies
- None discovered. No network calls, third-party libs, or CI config present.

7) Examples (use these lines in edits or tests to keep behavior predictable)
- `JustCrap/triangle_type_enum.py` — enum values: `TriangleType.EQUILATERAL`, `ISOSCELES`, `SCALENE`, `NONE`.
- `JustCrap/task.py` — triangle validity check: uses `abs()` and triangle inequality `a+b>c and a+c>b and b+c>a`.

8) Editing guidance for PRs
- Keep changes minimal and focused; include a short one-line description in commits.
- If adding tests, include a simple `pytest`-compatible test (e.g., `tests/test_triangle.py`) that imports `JustCrap.task.triangle_type`.

If anything here is unclear or you want different agent behavior (e.g., more aggressive refactoring or adding packaging), tell me which direction and I'll update this file.
