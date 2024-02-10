import shutil
import os

# Define your source and destination file paths
source_file = '/workspaces/.codespaces/shared/.env'
destination_dir = '/workspaces/ClassworkApp/frontend'

# Construct the destination file path
destination_file = os.path.join(destination_dir, os.path.basename(source_file))

# Move the file
shutil.move(source_file, destination_file)

print(f"Moved {source_file} to {destination_file}")
