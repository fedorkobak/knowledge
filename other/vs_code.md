# VS Code

Visual studio code is a highly customizable tool. This page covers the most common settings.

## Settings

You can configure your VSCode with editing the `settings.json` file. There are separate `settings.json` for user and for workspace.

Look for `settings.json` in `./.vscode` folder for workspace.

Check information on the `settiongs.json` for the user [here](https://code.visualstudio.com/docs/configure/settings#_user-settingsjson-location). For linux, it's typically in `~/.config/Code/User/settings.json`.

My typical config is:

```json
{
    "workbench.colorTheme": "Default Light Modern",
    "window.zoomLevel": -2.5,
    "editor.lineNumbers": "relative",
    "python.analysis.typeCheckingMode": "strict",
}
```

Check [Default VSCode settings](https://code.visualstudio.com/docs/reference/default-settings). VSCode extensions usually have their own settings.


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
