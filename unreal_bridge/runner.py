import subprocess
from unreal_bridge.commands import build_python_command

def run_unreal_python(script_path: str):
    cmd = build_python_command(script_path)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "command": cmd
    }
