# VS Code

Visual studio code is a highly customizable tool. This page covers the most common settings.

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
