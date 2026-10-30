
import subprocess
import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent

subprocess.run([sys.executable, "-m", "streamlit", "run", str(project_folder / "dashboard.py"), "--server.headless=false"], cwd=project_folder)
