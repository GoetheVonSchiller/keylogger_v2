# README

## Introduction

This is a simple keylogger script written in Python, which records every key press and saves it into a log file.

The script creates a folder called `Key` in the `C:\ProgramData\` directory and saves the log file `log.txt` inside this folder.

Additionally, the script includes a function named `upload_to_github()` for uploading the log file to a designated GitHub repository.

## Requirements

The script requires the `keyboard` and `requests` module to be installed. You can install it using the following command:

``pip install keyboard``
``pip install requests``


## GitHub Upload

This script includes a function named `upload_to_github()` for uploading the log file to a designated GitHub repository. Note that you'll need appropriate access rights and a personal access token from GitHub. Follow these steps to configure GitHub upload:

1. Create a GitHub repository where you intend to upload the log file. It's advisable to make the repository private, especially if sensitive data might be captured and uploaded.
2. Generate a personal access token on GitHub with necessary permissions for file uploads. You can do this on https://github.com/settings/tokens/new. Make sure to check the repository scope option to grant the token permission for repository-related operations.
3. Copy the access token and insert it into the `access_token` variable within the script.
4. Adjust the `<github_name>` and `<repository_name>` variables in the script to match your GitHub username and repository name respectively.
5. Run the script to start capturing keyboard events. It will automatically upload the log file to GitHub at regular intervals.


## Disclaimer

This keylogger script is intended for educational purposes only. Please use it responsibly and do not use it for illegal activities. The author is not responsible for any damage caused by the misuse of this script.
It is recommended to only use this script on your own personal computer and to delete the log file regularly to avoid any potential security breaches.