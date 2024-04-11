# this script automatically exports all existing conda environments to yml files, so that they can be easily recreated on another machine

import os
import subprocess

# Run the command 'conda env list' and get its output
output = subprocess.check_output("conda env list", shell=True).decode('utf-8')

# Split the output into lines
lines = output.split('\n')

# extract names of all existing conda environments
env_names = [line.split()[0] for line in lines[3:] if line] # The environment names are in the first column of the output, so we can extract them like this

# print(env_names)

for env_name in env_names:
    # Construct the command
    command = f'conda env export --from-history -n {env_name} > {env_name}.yml'
    
    # Execute the command
    os.system(command)