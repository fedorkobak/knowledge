# VS Code

Visual studio code is a highly customizable tool. This page covers the most common settings.

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
    "vim.langmap": "ФИСВУАПРШОЛДЬТЩЗЙКЫЕГМЦЧНЯ;ABCDEFGHIJKLMNOPQRSTUVWXYZ,фисвуапршолдьтщзйкыегмцчня;abcdefghijklmnopqrstuvwxyz"
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

## vim

The [Vim extension](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) allows you to use vim-like navigation and command system inside VS Code. This section provides useful tips for using vim.

### Search and replace

To **search** in vim just type `/<symbols combo to search>`. As you type, it will move you to the first occurrence below the cursor. It will also highlight all other instances of the search pattern. After pressing `Enter`, the cursor will move to the closest match below. You can move to the next match by pressing `n` and to the previous match by pressing `N`.

To **replace** values in vim, you have to use a command like:

```
:<scope>\<value to be replaced>\<value to replace>\<parameters>
```

The most usefull command are represented in the following table:

| Command                         | Description                                                   |
|--------------------------------|---------------------------------------------------------------|
| `:s/foo/bar/`                  | Replace first occurrence of `foo` with `bar` on the current line |
| `:s/foo/bar/g`                | Replace **all** occurrences of `foo` with `bar` on the current line |
| `:%s/foo/bar/`                | Replace first occurrence of `foo` with `bar` in **all lines**     |
| `:%s/foo/bar/g`              | Replace all occurrences of `foo` with `bar` in the whole file  |
| `:%s/foo/bar/gc`             | Same as above, but **ask for confirmation** before each change |
| `:n,m s/foo/bar/g`           | Replace `foo` with `bar` between lines `n` and `m`             |
| `:'<,'> s/foo/bar/g`         | Replace `foo` with `bar` in the selected in visual mode section. VSCode automatically adds `'<,'>` to the command line when you type `:` in visual mode. |
| `:%s/\<foo\>/bar/g`          | Replace whole word `foo` with `bar` globally                   |
| `:%s/foo/bar/gI`             | Replace `foo` with `bar` globally, **case-insensitive**         |
| `:%s/foo\c/bar/g`            | Also case-insensitive (with `\c` in pattern)                   |
| `:%s/\Vfoo/bar/g`            | Use **very magic** mode (fewer escapes needed in pattern)      |

Use backslash symbol to escape a symbol in a pattern. For example, to replace the pattern `/test` with `hello`, use the command:

```
:s/\/test/hello/
```

To escape a backslash itlself, use the `\\` combination before it. So, to replace the pattern `\$` with `$`:

```
:s/\\\$/$/
```
