import json
import os
import subprocess

CONFIG_PATH = os.path.join("config", "unreal_config.json")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def open_unreal():
    cfg = load_config()
    editor = cfg["unreal_editor"]
    project = cfg["project_path"]
    if not os.path.exists(editor):
        raise FileNotFoundError(f"No existe UnrealEditor.exe: {editor}")
    if not os.path.exists(project):
        raise FileNotFoundError(f"No existe el proyecto: {project}")
    subprocess.Popen([editor, project])
    return {"status": "ok", "message": "Unreal abierto correctamente"}
