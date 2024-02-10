import shutil
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Define the source and destination file paths
source_file = '/workspaces/.codespaces/shared/.env'
destination_dir = f'{parent_dir}/frontend'

# Construct the destination file path
destination_file = os.path.join(destination_dir, os.path.basename(source_file))

# Move the file
shutil.move(source_file, destination_file)

print(f"Moved {source_file} to {destination_file}")
