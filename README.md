# gen-ai-models-evaluation
Training course to learn Gen AI models evaluation for DQE

## Setup
1. Download Ollama at: https://ollama.com/download
2. Install using terminal : irm https://ollama.com/install.ps1 | iex
3. In terminal : pip install ollama
4. Check version: ollama --version  
5. Download the llm model : ollama pull llama3

## Task Prerequisites:
Python environment

##### This task runs on Python 3.12 — it has prebuilt wheels for the whole stack on Windows and macOS, so setup needs no compilers. Install the latest 3.12.x from https://www.python.org/downloads/ (on Windows, tick "Add python.exe to PATH").
Create and activate a virtual environment, then install this task's pinned dependencies.
Windows (PowerShell):
py -3.12 -m venv .venv 
.\.venv\Scripts\Activate.ps1 
pip install -r requirements.txt 
macOS / Linux:
python3.12 -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt 
To run the notebook, use VS Code (Python + Jupyter extensions) or install JupyterLab (pip install jupyterlab).


Ollama (local LLM runtime)


The task runs the model locally through Ollama — no cloud account or API key needed. It behaves the same on Windows and macOS.
Install: download the installer for your OS from https://ollama.com/download.
Pull the model (one-time, ~2 GB):ollama pull llama3.2 
Start the server: launch the Ollama app, or run ollama serve in a terminal. It listens on http://localhost:11434 (port 11434).
Check it is running:ollama list # lists installed models; errors if the server is down or open http://localhost:11434 in a browser — it should reply Ollama is running.
Stop it: press Ctrl+C in the terminal running ollama serve, or quit Ollama from the system tray (Windows) / menu bar (macOS).

The notebook's first code cell checks that Ollama is reachable and prints a clear message if it is not.

