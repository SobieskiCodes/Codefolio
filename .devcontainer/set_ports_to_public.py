import subprocess
import sys

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python set_ports_to_public.py <CODESPACE_NAME>")
        sys.exit(1)

    # Retrieve arguments
    codespace_name = sys.argv[1]
    set_port_visibility_public(codespace_name)

def set_port_visibility_public(codespace_name):
    # Call gh commands using subprocess
    subprocess.run(["gh", "codespace", "ports", "visibility", "3000:public", "-c", codespace_name], check=True)
    subprocess.run(["gh", "codespace", "ports", "visibility", "8000:public", "-c", codespace_name], check=True)

if __name__ == "__main__":
    main()
