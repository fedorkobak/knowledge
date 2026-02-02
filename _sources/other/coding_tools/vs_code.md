# VS Code

Visual studio code is a highly customizable tool. This page covers the most common settings.

## Environment variables

To access an environment variable in your vscode, simply open vscode from the terminal in which the required environment variable is installed. The list of commands is as following:

```bash
# just define variable inline
export VARIABLE="VALUE"
# load all required variables from .env file
source .env
# run vscode
code .
```

All the terminals that you run in vscode and jupyter notebooks will have defined variables during their execution.

## Settings

You can configure your VSCode with editing the `settings.json` file. There are separate `settings.json` for user and for workspace.

Look for `settings.json` in `./.vscode` folder for workspace.

Check information on the `settiongs.json` for the user [here](https://code.visualstudio.com/docs/configure/settings#_user-settingsjson-location). For linux, it's typically in `~/.config/Code/User/settings.json`.


You can list all available attributes that you can specify as settings using `defaultSettings.json` - a read only file that can be opened using the VSCode command `Preferences: OpenDefaultSettings (JSON)`. There are no other source, like official page where listed all settings with description: [Default VSCode settings](https://code.visualstudio.com/docs/reference/default-settings).

VSCode extensions usually have their own settings.

### My config


Here is my config:

```json
{
    "workbench.colorTheme": "Default Light Modern",
    "window.zoomLevel": -2.5,
    "editor.lineNumbers": "relative",
    "editor.fontFamily": "'Droid Sans Mono', 'monospace', monospace",
    "python.analysis.typeCheckingMode": "strict",
    "notebook.lineNumbers": "on", 
    "workbench.externalBrowser": "/usr/bin/firefox",

    "vim.langmap": "ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz",
    "vim.useSystemClipboard": true,
}
```

This is useful for being able to copy/paste it into various configurations.


**Note**: The `"editor.fontFamily"` attribute takes the same value as in the default settings. I've tried a few options, and the default VSCode font is the best for me. It is listed in the `configuration.json` file just as a reminder that it was purposely selected. 

**Note** for some environments, especially data science setups, the practically useful option is `"python.analysis.typeCheckingMode": "basic"`: This makes Pylance less strict.


## Debug

Check:

- [Visual studio code debug configuration](https://code.visualstudio.com/docs/debugtest/debugging-configuration).
- [Python debugging in VS Code](https://code.visualstudio.com/docs/python/debugging).

The configuration file, `.vscode/lanch.json` determines the behaviour of the vscode when debugging.

It's typical structure is:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "configuraiton1"
    },
    {
      "name": "configuration2"
    }
  ]
}
```

Under the "configuration" key, you can list a set of configurations, each of which represents a different debugging process.

The most basic debug configuration for python is:

```json
{
  "name": "Python Debugger: Current File",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal"
}
```

### Module

Use the "module" option to debug a program that starts as as a module.

---

For me, a typical case is checking the logic of code specified in a unit test. If the `unittest` framework is used, you should run the tests with the command `python3 -m unittest`. The following configuration is suppose to use the debuger for the current file run with the `unittest` framework.

```json
{
  "name": "Unittest: Current File",
  "type": "debugpy",
  "request": "launch",
  "module": "unittest",
  "args": "${file}",
  "console": "integratedTerminal"
}
```
