import subprocess

def run_ollama(model_name, query):
    command = f"ollama run {model_name} '{query}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Command: {command}")  # Debug print
    #print(f"Output: {result.stdout}")  # Debug print
    print(f"Error: {result.stderr}")  # Debug print
    return result.stdout.strip()

#this will run command on terminal 