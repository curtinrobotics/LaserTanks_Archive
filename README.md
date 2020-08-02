<!-- markdownlint-disable MD033 -->
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

<html><iframe src="https://drive.google.com/file/d/1htdf-faGNMdkhsFsCT0ZG_1CbQjnKd-L/preview" width="640" height="480"></iframe></html>

Click the play button. If VS Code says you need to have a launch.json configured, click [here](#Launch.Json).

Flask should now be running on a local port! Click the link to open in browser.

> :information_source: **If you click to the left of line numbers in VS Code, you can set break points which trigger when you run the code. THe debugger also displays local values. THese tools are super helful for debugging! :grin: :grin:

# Appendices

## Launch.Json
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