import subprocess
import os


def startenv(virtualenv_name):
    command = f"source ~{virtualenv_name}/bin/activate && pip install django"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print(f"Successfully installed Django in {virtualenv_name}")
    else:
        print(f"Failed to install Django in {virtualenv_name}:")
        print(stderr.decode())
        print("virtualenv_name")
startenv("develop")

home=os.chdir("/home/edcet003/.pyenv/versions/develop/bin")

# Print the current working directory
print(os.getcwd())
os.system(f"pyenv {home} develop")

print(subprocess)
