# Knowledge

Fedor Kobak's Knowledge Base

## Development Deployment

This site is primarily built from [Jupyter Notebooks](https://jupyter.org/) converted into a website using the [Jupyter Book](https://jupyterbook.org/en/stable/basics/build.html) tool.
You can clone the repository and run many of the examples yourself.

For pages that rely heavily on Bash, you should use the Bash kernel. To install it, run:

```bash
pip install bash_kernel
python -m bash_kernel.install
```

To deploy the site in Docker, use:

```bash
docker build -t knowledge_dev .
docker run -itd -v ./:/knowledge --name knowledge_dev knowledge_dev
```

Some pages require running specifically in a Docker environment because they explore system-level features.

A large portion of this knowledge base related to the Python programming language has been moved to a dedicated site: [Python](https://fedorkobak.github.io/python/intro.html).

## Building the Site

The site is built using [Jupyter Book](https://jupyterbook.org/en/stable/).

To build the site, install `jupyter-book` and run:

```bash
jb build .
```

After building, the `_build` directory will be created.

## Deploying the Site

One common way to deploy a site to GitHub Pages is to use a dedicated branch that contains all the generated files.
The [ghp-import](https://github.com/c-w/ghp-import) tool automates this process. Install it as a Python package and run it for the `_build/html` folder:

```bash
# Install the package
pip install ghp-import

# Publish the site
ghp-import -n _build/html
```

This will create a new commit on the `gh-pages` branch.
After pushing it to GitHub, your site will be updated automatically.
