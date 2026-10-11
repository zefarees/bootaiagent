import os
import subprocess


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python (.py) file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        wd_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(wd_path, file_path))
        valid_target = os.path.commonpath([wd_path, target_file])

        if valid_target != wd_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(
            command,
            cwd=wd_path,          # 1.1 working directory
            capture_output=True,  # 1.2 capture stdout and stderr
            text=True,            # 1.3 decode to str instead of bytes
            timeout=30,           # 1.4 stop after 30 seconds
            )
        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        else:
            if result.stdout:
                output.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output)


    except Exception as e:
        return f"Error: executing Python file: {e}"
