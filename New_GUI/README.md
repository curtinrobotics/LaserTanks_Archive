# Boozebot GUI Readme

This program uses [Flask](https://flask.palletsprojects.com) overlayed with [Reveal.js](https://revealjs.com/) to run. The purpose of this project is to provide the following:
- A user interface which displays the current status of a game (score, leaderboard etc.)
- A server which receives HTTP requests from a central arduino controller. The server interprets and updates the relevant fields in a database. 

## Software Requirements

You will need to have the following installed on your computer.

* [VS Code](https://code.visualstudio.com/download)
* [Python 3](https://www.python.org/downloads/)
* [Pip](https://pypi.org/project/pip/)

### Addittional Packages

The below packages are included in the virtual environment:

* [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) (necessary to use VS Code's debugging feature)
* [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)

If for some reason your computer says you need to install them, the links above redirect to the installation pages.

> :information-source: If you experience issues installing Flask on windows, see [Installing Flask on Windows](#Install-Flask-on-Windows).

## How to Run

There are two ways two run the app. It was successfully launched from the VS Code debugger from a Mac, however there is some difficulty getting it to work on Windows. The other method is running the app through a terminal, which is more reliable.

Try one of the below methods:

- [Run Flask Using the VS Code Debugger](#Run-Flask-Using-the-VS-Code-Debugger)

# Appendices

## Install Flask on Windows

Command prompt can work weirdly with python sometimes. To fix install issues, follow this guide:

1. First install python from their [website](https://www.python.org/downloads/). Make sure you use the executable installer.
2. Try installing Flask with `pip install flask`. If that doesn't work, install Pip with `py -3 -m pip install --upgrade pip`.

    >:information-source: If the terminal say you are missing an environment variable, copy the path listed in the output. The open the start menu and type path. A result saying edit sytem variables will appear. Click it, then click Environment Variables in the dialog box. In the box labelled "User Variables", click "Path" then "Edit...". Click new in the dialog box and paste the path you copied from the coomand-line.

    After installing pip and setting path varibles, try installing Flask again.
3. Flask should now work!

## Run Flask Using the VS Code Debugger

To run the app, open the **GUI_Main.py** file in **VS Code**.

On **VS Code**, go to the debugging menu here:

![VS Code: Debugging Icon](https://i.imgur.com/DNNyctq.png)

Make sure that *Python - Flask* is selected on the debugging menu. Click the play button.

![VS Code: Run Debugging](https://i.imgur.com/GYLKpdp.png)"

> :warning: *If VS Code says you need to have a launch.json configured, see [Launch.Json](#Launch.Json).*

Flask should now be running on a local port! Click the link to open in browser.

> :information_source: *If you click to the left of line numbers in VS Code, you can set break points which trigger when you run the code. THe debugger also displays local values. These tools are super helful for debugging!* :grin: :grin:

## Run Flask Using the Terminal

1.  Open a Terminal window and **navigate to the "New_GUI" folder** in the Laser  Tanks repository. 

    If using Windows, you can use the Terminal built into the app by pressing <kbd>Ctrl</kbd> + <kbd>`</kbd> (that's the weird key at the top-left of the keyboard, not an apostrophe).

2. Even though it is already there, we need to **recreate the virtual environment** the first time we run the app on your computer. To do this, enter one of the below commands:

    On Unix/Mac
    > `python3 -m venv venv`

    On Windows
    > `py -3 -m venv venv`

3. **Activate the virtual environment** by entering the one of the below commands:

    On Unix/Mac
    > `. venv/bin/activate`


    On  Windows
    > `venv\Scripts\activate`

4. 

## Launch.Json

Copy and paste the below text into the automatically generated file in VS Code.

```Json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "New_GUI/GUI_main.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
}
```