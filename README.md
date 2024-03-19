# knowledge
Here is a repository where I try to describe some of the challenges I face during my professional career.

For a better view of the information, please visit the githubpages for this repo - https://fedorkobak.github.io/knowledge/.


## Build site

For building website is used [jupyter book](https://jupyterbook.org/en/stable/).

To build the site, install `jupyter book` and use the command:

```
jb build .
```

After building, the `_build` directory is created.

**Note** `_build` directory added to `.gitignore`.

## Deploy site

One of the ways to deploy a site to github pages is to have a specific branch that contains all the necessary files. There is a special tool to do this [ghp-import](https://github.com/c-w/ghp-import). So you need to install this tool, which is distributed as a python package, and run it for the `_build/html` folder. This is what full commands will look like:

```bash
# installing package
pip3 install ghp-import
# running script
ghp-import _build/html
```

After all you will have new commit on `gh-pages` branch - after pulling it site will be updated.