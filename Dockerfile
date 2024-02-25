FROM mcr.microsoft.com/devcontainers/base:bullseye


# To rebuild your front-end Docker image without restarting your entire code space, you can use the Docker CLI (Command Line Interface) from your terminal. Here's a step-by-step guide:
# 1. **Open your terminal**: If you're using an integrated development environment (IDE) like VS Code, you can open the terminal within the IDE.
# 2. **Navigate to the directory**: Make sure you are in the directory where the Dockerfile for your front-end application is located. If it's in a specific folder, use `cd` to change to that directory.
# 3. **Build the image**: Run the Docker build command to rebuild your image. You'll need to specify the name of the image and optionally a tag. If you don't specify a tag, it will default to `latest`.
#    Here's the command format:
#    ```sh
#    docker build -t your-image-name:your-tag .
#    ```
#    For your case, it would be something like:
#    ```sh
#    docker build -t codefoliohomeworkdisplay-frontend .
#    ```
#    The period `.` at the end of the command indicates that Docker should look for the Dockerfile in the current directory.
# 4. **Stop the running container** (if it's running): Before you can run a new container from the rebuilt image, you need to stop the old container.
#    Find the container ID or name:
#    ```sh
#    docker ps
#    ```
#    Then stop the container:
#    ```sh
#    docker stop container_id_or_name
#    ```
# 5. **Run a new container**: After the build completes and you have stopped the old container, you can start a new container with the updated image.
#    Here's the command format:
#    ```sh
#    docker run -d --name your-container-name -p host_port:container_port your-image-name:your-tag
#    ```
#    Adjust the `host_port` and `container_port` to match the ports you want to use, and replace `your-container-name`, `your-image-name`, and `your-tag` with your specific details.
#    For example:
#    ```sh
#    docker run -d --name codefolio-frontend -p 3000:3000 codefoliohomeworkdisplay-frontend
#    ```
# This process will rebuild your front-end Docker image and run it as a new container without affecting the other parts of your code space or requiring a restart.