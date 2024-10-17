# SettingUpIDE
Just a simple repo for how I set up my IDE for Machine Learning and Data Science projects

## Have terminal for WSL for Windows
Install WSL (Windows Subsystem for Linux) by downloading it from the Microsoft store.

## 1) Download VS Code
Here is the [VSCode Link](https://code.visualstudio.com/) to download VS Code. It works very well with Python and Jupter Notebooks. It is the best IDE that is free to use and has tons of support and extensions for ML.

## 2) Download Python if you haven't
Here is the latest [python](https://www.python.org/) if you haven't downloaded it yet.
Nearly all ML is done in Python or C++.

## 3) Installing the extension.
On the extensions tab in VSCode there are a few extensions I recommended. 
- Python
- Pylance
- Jupyter
- Jupter Cell Tags
- Python Indent
- Github Copilot (Optional)
- Github Copilot Chat (Optional)

## 4) Install Virtual Environment 
Now that you have installed all requirements. It is time to setup the enviroment.

Run the command:
`python -m venv firstenv`

This will create the same conda enviroment from this Github Repo with libraries I use.

Run the command:
`firstenv/Scripts/Activate.ps1`
This will activate the environment for you to use.
Then install the python libraries.:
* fastai

## 5) Run the main.py    
Note: For Windows User run this commad in the terminal once you set up the virtual enviroment.
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Otherwise run `python main.py` in the terminal.
If things are succesfull you should get three matrices and an image called results.png