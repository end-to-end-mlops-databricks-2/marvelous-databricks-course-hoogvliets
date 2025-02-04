<h1 align="center">
Marvelous MLOps End-to-end MLOps with Databricks course

# Setup

## Setup environment for development

### Create virtual environment

Create and activate a venv with your desire python version.
```
uv venv -p 3.11 venv
source venv/bin/activate
uv pip install -r pyproject.toml --all-extras
uv lock
```


### Install dev depedencies

The package has al dev depedencies configured. Install them by running `uv pip install -e ".[dev]"`, use the quotation marks if you are running zshell. For vanilla terminal you can leave them out.

## Access to the data

### Access to Kaggle API

Make sure you have access to the Kaggle API by:
* creating a token from your user profile page
* placing the token a local folder or secrets manager
For Mac/Linux locally the token should be in `~/.kaggle/kaggle.json`
* For Windows in `C:\Users\<Windows-username>\.kaggle\kaggle.json`

### Download the dataset

Run the script to download the dataset `bash scripts/get_data_kaggle.sh`