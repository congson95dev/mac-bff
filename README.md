# MAC-BFF

### Requirements
- **Python 3.8**

### Setting up environment
- Create .env file in the main folder.
- Copy the content from .env.example file to .env file.

### Install steps:
```
cd project_name

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Run on  local machine:
```
flask run
```
## Alternative, you could Dockerize this project:
```
make all
```
### Go to:
```
127.0.0.1:5000
```
### Run pre-commit
- Run this command and fix all the warning before committing code to the repo
```
pre-commit run --all-files
```
- Or run
```
pre-commit install
```