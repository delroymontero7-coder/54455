import json
import os

CONFIG_PATH = os.path.join("config", "unreal_config.json")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def build_python_command(script_path: str):
    cfg = load_config()
    return [cfg["unreal_editor"], cfg["project_path"], f"-ExecutePythonScript={script_path}"]
