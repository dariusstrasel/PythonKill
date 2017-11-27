# PythonKill

This Python program will check for a designated list of applications per loop cycle and kill them forcefully if detected as alive.

- **PythonKill** is only supported under Windows.
- **PythonKill** uses Python 3.52

# How to use:

> 1. **Clone/download:** Download/clone the script to your computer
> 2.  **Edit** processListConfig.py using your favorite text-editor
>  - Goto line 3 and add any programs you'd like PythonKill to watch for. e.g. "explorer.exe" Or, add them to an enviornment variable "processList" in the Python list syntax: ["process.exe"]
>  - Goto line 4 and change "SECONDS_TO_LOOP_FOR" to be either 0 (no loop) or the number of seconds you want to loop for.
> 3. Execute the script from the CLI using "python pykill.py"
