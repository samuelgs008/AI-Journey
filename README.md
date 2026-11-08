# Python-Journey 🐍

A Python roadmap made with [Claude](https://claude.com/claude-code) to study Python from basics all the way to automation and artificial intelligence applied to real processes. 

Some exercises are inspired by beecrowd: each one has a problem statement, input/output descriptions and sample cases. From Phase 4 on, it is **more projects than exercises**.

Claude only writes the exercise statements and project briefs. It never writes my solutions, and only shows an answer if I ask for it after really trying. All the code, pipelines and algorithms are written by me. When I get stuck, Claude gives hints, explains concepts and errors, and reviews my code after I solve it.

To build pipelines, algorithms and solve mathematical problems, I will use [Excalidraw](https://excalidraw.com/)&nbsp;&nbsp;<img src="assets/excalidraw-logo.png" alt="Excalidraw Logo" width="28" align="center">

## Tech stack

The technologies this roadmap covers (hover over a logo to see its name):

| Area | Technologies |
|---|---|
| **Language & tools** | <img src="assets/python-logo.svg" alt="Python" title="Python" width="36">&nbsp;<img src="assets/vscode-logo.svg" alt="VS Code" title="VS Code" width="36">&nbsp;<img src="assets/git-logo.svg" alt="Git" title="Git" width="36">&nbsp;<img src="assets/github-logo.svg" alt="GitHub" title="GitHub" width="36">&nbsp;<img src="assets/githubactions-logo.svg" alt="GitHub Actions" title="GitHub Actions" width="36">&nbsp;<img src="assets/linux-logo.svg" alt="Linux" title="Linux" width="36">&nbsp;<img src="assets/pytest-logo.svg" alt="pytest" title="pytest" width="36">&nbsp;<img src="assets/ruff-logo.svg" alt="Ruff" title="Ruff" width="36">&nbsp;<img src="assets/uv-logo.svg" alt="uv" title="uv" width="36">&nbsp;<img src="assets/excalidraw-logo.png" alt="Excalidraw" title="Excalidraw" width="36"> |
| **AI & LLMs** | <img src="assets/claude-logo.svg" alt="Claude" title="Claude" width="36">&nbsp;<img src="assets/pydantic-logo.svg" alt="Pydantic" title="Pydantic" width="36">&nbsp;<img src="assets/huggingface-logo.svg" alt="Hugging Face" title="Hugging Face" width="36">&nbsp;<img src="assets/mcp-logo.svg" alt="MCP (Model Context Protocol)" title="MCP (Model Context Protocol)" width="36"> |
| **Data** | <img src="assets/postgresql-logo.svg" alt="PostgreSQL" title="PostgreSQL" width="36">&nbsp;<img src="assets/numpy-logo.svg" alt="NumPy" title="NumPy" width="36">&nbsp;<img src="assets/pandas-logo.svg" alt="pandas" title="pandas" width="36">&nbsp;<img src="assets/matplotlib-logo.svg" alt="Matplotlib" title="Matplotlib" width="36">&nbsp;<img src="assets/seaborn-logo.svg" alt="Seaborn" title="Seaborn" width="36">&nbsp;<img src="assets/streamlit-logo.svg" alt="Streamlit" title="Streamlit" width="36">&nbsp;<img src="assets/jupyter-logo.svg" alt="Jupyter" title="Jupyter" width="36"> |
| **Machine Learning** | <img src="assets/scikitlearn-logo.svg" alt="scikit-learn" title="scikit-learn" width="36">&nbsp;<img src="assets/pytorch-logo.svg" alt="PyTorch" title="PyTorch" width="36"> |
| **Production** | <img src="assets/fastapi-logo.svg" alt="FastAPI" title="FastAPI" width="36">&nbsp;<img src="assets/docker-logo.svg" alt="Docker" title="Docker" width="36">&nbsp;<img src="assets/aws-logo.svg" alt="AWS" title="AWS" width="36">&nbsp;<img src="assets/mlflow-logo.svg" alt="MLflow" title="MLflow" width="36"> |

## Roadmap

The goal: **improve real processes with Python and AI, and grow toward AI or Machine Learning Engineering**. The journey is split into phases, and each phase ends with a **project** for my portfolio.

| Phase | Focus | Project | Status |
|---|---|---|---|
| [1 — Python foundations](01-python-foundations/) | the language itself: syntax, data, functions, modules, recursion, algorithms, files, OOP | expense tracker (CLI) | 🟢 in progress |
| 2 — Tools & good practices | the tools professionals use: `venv` and `uv`, Git and teamwork, tests, logging, Ruff, type checking, CI | tested, packaged project | ⚪ Locked |
| 3 — My first AI | call an LLM from Python | terminal chatbot | ⚪ Locked |
| 4 — Automation | make Python do repetitive work | a manual report, automated | ⚪ Locked |
| 5 — Data analysis | turn data into insight: SQL, math for ML, pandas, data pipelines, stats, dashboards | data dashboard | ⚪ Locked |
| 6 — AI in processes | LLMs that read documents, act and run reliably in production | document-reading assistant | ⚪ Locked |
| 7 — Machine Learning | train and properly evaluate models (scikit-learn, XGBoost) | well-evaluated prediction model | ⚪ Locked |
| 8 — Deep Learning | PyTorch, computer vision, transformers, reinforcement learning | a fine-tuned model vs. an LLM | ⚪ Locked |
| 9 — ML Engineering | put a model in production (FastAPI, Docker, AWS, MLflow) | a deployed model with an API & monitoring | ⚪ Locked |
| Final | everything together | end-to-end AI automation | ⚪ Locked |

Each phase below opens with the details.

<details>
<summary><b>Phase 1 — Python foundations</b></summary>

<img src="assets/python-logo.svg" alt="Python" title="Python" width="32">&nbsp;<img src="assets/excalidraw-logo.png" alt="Excalidraw" title="Excalidraw" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 01 | [Fundamentals](01-python-foundations/#level-01-fundamentals) ✅ | `print`, `input`, variables, types, `if`, `for`, `while`, `//` and `%`, `range` with steps, nested loops, `break` and `continue`, input validation |
| 02 | [Strings](01-python-foundations/#level-02-strings) | quotes and escapes, raw and multi-line strings, `len`, indexing, slicing, immutability, methods (case, `is...`, `find`, `strip`, `replace`, `split`, `join`, `partition`...), comparing text, `ord`/`chr` and Unicode, formatting (alignment, separators, percentages), parsing text and log files |
| 03 | Data structures | lists (indexing and slicing like strings, `append`, `insert`, `remove`, `pop`, `sort` vs `sorted`, `min`/`max`/`sum`), mutability and copies (why changing one list can change another), lists of lists (grids and tables), tuples and unpacking, dictionaries (keys and values, `.get()`, looping with `.items()`, counting and grouping), sets (removing duplicates, fast `in`, union and intersection), nested data (a list of dictionaries: the shape of JSON), `enumerate` and `zip`, comprehensions (list, dict and set) |
| 04 | Functions | `def`, parameters (default values, keyword arguments), return values (returning several at once), scope (local vs global), docstrings, `lambda` and `sorted(key=...)`, `*args`/`**kwargs`, type hints |
| 05 | Modules and the standard library | `import` and the standard library (`math`, `random`, `string`, `datetime` for dates, `decimal` for money), splitting your code across files (your own modules), `if __name__ == "__main__"`, your first `pip install`. Mini-project: an ASCII-art banner generator for the terminal (`pyfiglet` + `rich`: fonts, colors, panels, validated prompts, save to `.txt`) |
| 06 | Recursion | the base case, how the call stack works, factorial, Fibonacci, Tower of Hanoi, recursion vs loops (and Python's recursion limit) |
| 07 | Algorithms | searching, sorting, the Sieve of Eratosthenes (all primes up to N at once), Big O (how fast code is), number bases (binary and hexadecimal, converting by hand), greedy algorithms and dynamic programming, interview-style coding practice (keep practicing through the later phases) |
| 08 | Files and errors | reading/writing files, `pathlib` (file paths that work on any computer), CSV, JSON, `try`/`except`, text encodings (UTF-8 vs Windows-1252, the reason `ç` sometimes shows up as `Ã§`), regular expressions (`re`) to find and clean patterns in text, removing accents (`unicodedata`) |
| 09 | Object-oriented programming | classes, objects, inheritance, `__str__` and `__repr__` (how your objects turn into text) |
| 10 | Iterators, generators and decorators | how `for` really works (`iter()` and `next()`), generators (`yield`: reading huge files without running out of memory), decorators (functions that wrap other functions, `@property`, `@staticmethod`, `@classmethod`) |

🎯 **Project:** a command-line expense tracker — add expenses, save them to a file, show totals and the biggest ones. The code is split into modules, and you run it with commands like `python tracker.py add 12.50 food` or `python tracker.py report` (`argparse`). (You'll analyze this same data in Phase 5.)

</details>

<details>
<summary><b>Phase 2 — Tools & good practices</b></summary>

<img src="assets/git-logo.svg" alt="Git" title="Git" width="32">&nbsp;<img src="assets/github-logo.svg" alt="GitHub" title="GitHub" width="32">&nbsp;<img src="assets/githubactions-logo.svg" alt="GitHub Actions" title="GitHub Actions" width="32">&nbsp;<img src="assets/linux-logo.svg" alt="Linux" title="Linux" width="32">&nbsp;<img src="assets/pytest-logo.svg" alt="pytest" title="pytest" width="32">&nbsp;<img src="assets/ruff-logo.svg" alt="Ruff" title="Ruff" width="32">&nbsp;<img src="assets/uv-logo.svg" alt="uv" title="uv" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 11 | Tools | `pip`, virtual environments (`venv`), then `uv` (packages, virtual environments and the project file `pyproject.toml` in one fast tool), logging, the debugger, the Linux terminal (WSL), SSH basics (practiced for free inside WSL), API keys and secrets (environment variables, `.env` files, `.gitignore`, what to do if a key leaks) |
| 12 | Code quality | tests with `pytest`, linting and formatting with Ruff, type checking with `mypy`, CI with GitHub Actions |
| 13 | Git and teamwork | branches, pull requests, code reviews, reading other people's code, contributing to an open-source project |

🎯 **Project:** turn the expense tracker into a real project — managed with `uv` (`pyproject.toml`), tests with `pytest`, and a clean Git history.

</details>

<details>
<summary><b>Phase 3 — My first AI</b></summary>

<img src="assets/claude-logo.svg" alt="Claude" title="Claude" width="32">&nbsp;<img src="assets/pydantic-logo.svg" alt="Pydantic" title="Pydantic" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 14 | APIs and my first AI | HTTP, `requests`, JSON, calling an LLM API, writing prompts, getting structured (JSON) answers, validating data with Pydantic, async Python (`async`/`await`), a first try with an open-source AI agent: give it small tasks in WSL and watch which tools it uses and what each task costs |

🎯 **Project:** a terminal chatbot that remembers the conversation.

</details>

<details>
<summary><b>Phase 4 — Automation</b></summary>

| Level | Topic | What you will learn |
|---|---|---|
| 15 | Office automation | process improvement basics (mapping a process, measuring it before changing it, finding the bottleneck), Excel (`openpyxl`), PDF (`pypdf` to merge, split and read simple text, `pdfplumber` to pull out tables), e-mail, scheduling scripts to run on their own |
| 16 | Web automation | consuming public APIs, HTML basics (tags and CSS selectors), basic web scraping |

🎯 **Project:** a report that is done by hand today, generated on its own.

</details>

<details>
<summary><b>Phase 5 — Data analysis</b></summary>

<img src="assets/postgresql-logo.svg" alt="PostgreSQL" title="PostgreSQL" width="32">&nbsp;<img src="assets/numpy-logo.svg" alt="NumPy" title="NumPy" width="32">&nbsp;<img src="assets/pandas-logo.svg" alt="pandas" title="pandas" width="32">&nbsp;<img src="assets/matplotlib-logo.svg" alt="Matplotlib" title="Matplotlib" width="32">&nbsp;<img src="assets/seaborn-logo.svg" alt="Seaborn" title="Seaborn" width="32">&nbsp;<img src="assets/streamlit-logo.svg" alt="Streamlit" title="Streamlit" width="32">&nbsp;<img src="assets/jupyter-logo.svg" alt="Jupyter" title="Jupyter" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 17 | SQL | PostgreSQL, `SELECT`, `JOIN`, aggregations |
| 18 | NumPy & linear algebra | arrays, vectors and matrices — the math behind ML |
| 19 | Calculus for ML | derivatives and the gradient idea |
| 20 | Probability | chance, distributions, conditional probability |
| 21 | Pandas and charts | Jupyter notebooks (in VS Code), data tables, filtering, grouping, Matplotlib and Seaborn |
| 22 | Data pipelines | cleaning messy data, data validation, scheduled pipelines |
| 23 | Statistics and dashboards | mean, variation, control charts, confidence intervals, hypothesis tests, A/B tests (to prove one model or prompt is really better), dashboards with Streamlit |

🎯 **Project:** a dashboard with a process's indicators (time, bottlenecks, errors).

</details>

<details>
<summary><b>Phase 6 — AI in processes</b></summary>

<img src="assets/claude-logo.svg" alt="Claude" title="Claude" width="32">&nbsp;<img src="assets/postgresql-logo.svg" alt="PostgreSQL" title="PostgreSQL" width="32">&nbsp;<img src="assets/mcp-logo.svg" alt="MCP (Model Context Protocol)" title="MCP (Model Context Protocol)" width="32">&nbsp;<img src="assets/fastapi-logo.svg" alt="FastAPI" title="FastAPI" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 24 | LLMs in practice | classify text, extract data from documents, structured output, measuring cost and response time |
| 25 | Agents and RAG | AI that runs tasks and reads internal documents to answer, tool use (build your own agent loop first: the LLM asks for a tool, your code runs it and sends back the result), agent frameworks, MCP (the standard way to connect an AI to tools), writing your own skills for an agent, embeddings and vector databases (Chroma to start, then pgvector inside PostgreSQL), AI safety and security (prompt injection, data leaks, unsafe agent actions) |
| 26 | LLMs in production | a basic API for your LLM app with FastAPI, streaming, caching, rate limits, fallbacks, tracing what the app did, evaluating LLM apps (a test set of real examples, scoring the answers automatically, catching what gets worse when you change a prompt or a model) |

🎯 **Project:** an assistant that reads e-mails or documents and fills a spreadsheet: an AI agent running skills you write yourself.

</details>

<details>
<summary><b>Phase 7 — Machine Learning</b></summary>

<img src="assets/scikitlearn-logo.svg" alt="scikit-learn" title="scikit-learn" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 27 | ML foundations | scikit-learn: train/test split, cross-validation, overfitting, feature engineering, choosing the right metric |
| 28 | Gradient boosting | XGBoost and LightGBM — the models that win most real tabular problems |

🎯 **Project:** a prediction model (e.g. process delays) that is trained and **properly evaluated**, not just `.fit()`.

</details>

<details>
<summary><b>Phase 8 — Deep Learning</b></summary>

<img src="assets/pytorch-logo.svg" alt="PyTorch" title="PyTorch" width="32">&nbsp;<img src="assets/huggingface-logo.svg" alt="Hugging Face" title="Hugging Face" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 29 | Neural networks | PyTorch: tensors, autograd, build and train your own network on a free GPU (Google Colab or Kaggle) |
| 30 | Computer vision | CNNs: teach a model to recognize images |
| 31 | Transformers & Hugging Face | attention, embeddings, using and fine-tuning pretrained models (LoRA) |
| 32 | Reinforcement learning | an agent that learns by trial and error (Gymnasium, Stable-Baselines3). Mini-project: the **red-ball agent**, an AI that learns to reach a random target as fast as it can |

🎯 **Project:** fine-tune a Hugging Face model to sort customer-support messages into categories, using a **public dataset** (no private or company data), and compare it with the Phase 6 LLM approach: accuracy, cost and speed.

</details>

<details>
<summary><b>Phase 9 — ML Engineering</b></summary>

<img src="assets/fastapi-logo.svg" alt="FastAPI" title="FastAPI" width="32">&nbsp;<img src="assets/postgresql-logo.svg" alt="PostgreSQL" title="PostgreSQL" width="32">&nbsp;<img src="assets/docker-logo.svg" alt="Docker" title="Docker" width="32">&nbsp;<img src="assets/aws-logo.svg" alt="AWS" title="AWS" width="32">&nbsp;<img src="assets/mlflow-logo.svg" alt="MLflow" title="MLflow" width="32">

| Level | Topic | What you will learn |
|---|---|---|
| 33 | Serve a model | wrap a model in a FastAPI API, connect it to PostgreSQL and package it with Docker |
| 34 | Cloud & MLOps | deploy to AWS (using the free plan credits), keep an AI agent running 24/7 on a free cloud server (AWS free plan) safely, track experiments with MLflow, monitor the model, system design interview practice |

🎯 **Project:** a model of mine **live on the internet**, with an API and basic monitoring.

</details>

<details>
<summary><b>Final project</b></summary>

A complete AI automation, end to end, with the **before and after measured**, used by **a real person** other than me.

</details>
