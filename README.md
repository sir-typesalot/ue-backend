# Urban Eden Project

## Prerequisites
You will need to have python 3.11.x and have Docker installed on your system.
If you are trying to test running the container on a Windows machine, you would
likely need a Bash terminal (Git Bash isn't a bad option).

## Setup
- Pull the repo locally
- Create a virtual env for this repo `python -m venv <virtual_env>`
- Activate the virtual environment
  - For UNIX systems - `source <path_to_virtual_env>/bin/activate`
  - For Windows systems - `<path_to_env>\Scripts\activate`
- Install all the required packages - `pip install -r requirements.txt`

## Run Locally
- To test the application without the container, just run - `python run.py`
- To run the app within a container run - `bash run_local.sh`

## Testing
Go through the setup steps. Run `pytest tests/ -vv` which will run the collection of tests and output the results.
To lint your code to make sure it keeps up with the PEP8 standards, run `pylint <path_to_file or directory>`
To better format your code, you can use `black <path_to_file>`.

## Contribution
- Create a new branch for your changes - `git checkout -B <name_of_branch>`
- Make your changes
- Add all the changes - `git add .`
- Commit all your changes - `git commit -m "Description of changes"`
- Push your changes to the remote repo - `git push`
  - If its your first time pushing to that remote branch, run `git push --set-upstream origin <branch_name>`
- Go to GitHub to view your changes and create a Pull Request.
