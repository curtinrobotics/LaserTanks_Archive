# Boozebot GUI Readme

## How to Run

This program uses [Flask](https://flask.palletsprojects.com) to run. The flask extension should already be contained in the venv (Virtual Environment) folder.

### Software Requirements

You will need:

* VS Code
* Python 3 installed

### Terminal Commands

To run the app, open **VS Code**. Open the Terminal with <kbd>Control</kbd> + <kbd>`</kbd>.

Navigate the Terminal to the New_GUI directory from the root folder.

`JSON
cd New_GUI`

On **VS Code**, go to the debugging menu here:

![VS Code: Debugging Icon](https://i.imgur.com/DNNyctq.png)

Make sure that *Python - Flask* is selected on the debugging menu. Click the play button.

![VS Code: Run Debugging](https://i.imgur.com/GYLKpdp.png)"

> :warning: *If VS Code says you need to have a launch.json configured, click [here](#Launch.Json-File). If you still have problems, click [here](#Terminal-Launch).*

Flask should now be running on a local port! Click the link to open in browser.

> :information_source: *If you click to the left of line numbers in VS Code, you can set break points which trigger when you run the code. THe debugger also displays local values. These tools are super helful for debugging!* :grin: :grin:

## Who to Contact

---

### Adeepa Rajamanthri

Project Lead

[Adeep.rajamanthri@gmail.com](mailto:Adeep.rajamanthri@gmail.com.)

---

### Ryan Walton

GUI Lead

[ryanjwalton94@gmail.com](mailto:ryanjwalton94@gmail.com)

---

## Appendices

### Launch.Json File

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

## Terminal Launch

You will need to run flask manually through the terminal.

Since some of the configuration has already been done, use this guide, not the one below as it will overide current settings.

### Steps

1. Activate the virtual environment. Make sure this is done in the New_GUI directory.

    On Unix

    `$ . venv/bin/activate`

    On Windows

    `> venv\Scripts\activate`

2. Set the root app variable, then run the app. Type the below commands:

    ```shell
    $ export FLASK_APP=GUI_Main.py
    $ flask run
    * Running on http://127.0.0.1:5000/
    ```

Look at the [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for further details.