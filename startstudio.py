import os
import subprocess
import logging

activate_env="pyenv activate develop"
process_activate_env = subprocess.Popen(activate_env, shell=True, executable="/bin/bash")
process_activate_env.wait()
start_server="yarn run devserver:hot"
process_start_server = subprocess.Popen(start_server, shell=True, executable="/bin/bash")
traceback= "Traceback"
os.system("pyenv activate develop")
if (traceback==0):
    print("Failed to activate virtualenv.")


def environment():
    shell_reload='exec"$SHELL"'
    process_shell_reload = subprocess.Popen(shell_reload, shell=True, executable="/bin/bash")
    print("Shell reloaded")
    process_shell_reload.wait()


    activate_env="pyenv activate develop"
    process_activate_env = subprocess.Popen(activate_env, shell=True, executable="/bin/bash")
    process_activate_env.wait()


    start_server="yarn run devserver:hot"
    process_start_server = subprocess.Popen(start_server, shell=True, executable="/bin/bash")
    process_start_server.wait()
    os.system('exec"$SHELL"')
    command = "sudo make run-services"
    process = subprocess.Popen(command, shell=True, executable="/bin/bash")
# wait for the subprocess to finish
    process.wait()

environment()

def security_key():
    os.system("hello world")



cmd = ["ls","l"]
subprocess.check_call(cmd)
