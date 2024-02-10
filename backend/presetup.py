import subprocess
import shutil
import sys
import os

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python presetup.py <CODESPACE_NAME> <GITHUB_TOKEN>")
        sys.exit(1)

    # Retrieve arguments
    codespace_name = sys.argv[1]
    github_token = sys.argv[2]
    env_content = f"VITE_CODESPACE_NAME={codespace_name}\nVITE_GITHUB_TOKEN={github_token}\n"

    # Define the source and destination file paths
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(current_dir)
    destination_dir = f'{parent_dir}/frontend'

    # Construct the destination file path
    env_file_path = os.path.join(destination_dir, '.env')

    # Prepare the content to write to the .env file
    env_content = f"VITE_CODESPACE_NAME={codespace_name}\nVITE_GITHUB_TOKEN={github_token}\n"

    # Writing to the .env file
    try:
        with open(env_file_path, 'w') as env_file:
            env_file.write(env_content)
            print(f".env file created at {env_file_path}")
    except Exception as e:
        print(f"Failed to write to {env_file_path}: {e}")

    # Set port visibility public
    #set_port_visibility_public(codespace_name)

def set_port_visibility_public(codespace_name):
    # Call gh commands using subprocess
    subprocess.run(["gh", "codespace", "ports", "visibility", "3000:public", "-c", codespace_name], check=True)
    subprocess.run(["gh", "codespace", "ports", "visibility", "8000:public", "-c", codespace_name], check=True)

if __name__ == "__main__":
    main()
