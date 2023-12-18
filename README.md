# Machine Learning

This repository has some Demos and Information about Machine Learning algorithms in general

## Environment setup

_Requirement:_ You need to have **python 3.7** installed on your system.
You can download python versions from here: [Python](https://www.python.org/downloads/)

### **On windows**

`py -3.7 -m venv .venv` **Creates an environment '.venv' which will use python 3.7 as the default python version**

`.venv\Scripts\Activate.ps1`    **Activates the environment**

_If error about Set-ExecutionPolicy:_

- `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`    **Changes the ExecutionPolicy so you can activate the environment**

- `.venv\Scripts\Activate.ps1`  **Activates the environment**

`python -m pip install --upgrade pip`   **Upgrades pip to latest version, sometimes necessary to install required packages**

`pip install -r .\requirements.txt` **Installs the required packages for the repository**

### **On Linux like OS**

`sudo apt-get install python3.7-venv`   **Installs venv for python 3.7**

`python3.7 -m venv .venv`   **Creates a virtual environment named .venv**

`source .venv/bin/activate` **Activates the virtual environment**

`python -m pip install --upgrade pip`   **Upgrades pip in the virtual environment, sometimes necessary to install required packages**

`pip install -r requirements.txt`   **Installs packages from requirements.txt**





