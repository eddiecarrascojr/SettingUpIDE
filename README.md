# SettingUpIDE
Just a simple repo for how I set up my IDE for Machine Learning and Data Science projects

## Have terminal for WSL for Windows
Install WSL (Windows Subsystem for Linux) by downloading it from the Microsoft store.

## 1) Download VS Code
Here is the [VSCode Link](https://code.visualstudio.com/) to download VS Code. It works very well with Python and Jupter Notebooks. It is the best IDE that is free to use and has tons of support and extensions for ML.

## 2) Download Python if you haven't
Here is the latest [python](https://www.python.org/) if you haven't downloaded it yet.
Nearly all ML is done in Python or C++.

## 3) Install Anacoda
Anacoda has become the standard for many people working in AI. You don't have to install it but for best practices I recommend starting to use it so everyone is using the same enviroment and version of python libraries. Link can be found [here](https://www.anaconda.com/).


## 4) Test installation and Enviroments
Now that you have installed all requirements. It is time to setup the enviroment.

Run the command:
`conda create -n firstenv`

This will create the same conda enviroment from this Github Repo with libraries I use.

Run the command:
`conda activate firstenv`

This will activate the environment for you to use.

Then install the needed libraries.

Run the command:
`conda install environment.yml`

## 5) Installing the extension.
On the extensions tab in VSCode there are a few extensions I recommended. 
- Python
- Pylance
- Jupyter
- Jupter Cell Tags
- WSL (for windows users)
- Python Indent
- Github Copilot (Optional)
- Github Copilot Chat (Optional)

##6) Run the main.py    
For Windows User run this commad in the terminal once you set up the virtual enviroment.
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
If things are succesfull you should get three matrices and an image called results.png