import subprocess

def check_errors(code):
    with open("temp_code.py", "w") as f:
        f.write(code)
    
    result = subprocess.run(["pylint", "temp_code.py", "--disable=all", "--enable=syntax-error"], capture_output=True, text=True)
    return result.stdout
