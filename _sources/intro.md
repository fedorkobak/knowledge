# Knowlege

Website provided by Fedor Kobak, with various studies in data science, computer science and related fields.

This site is mainly based on [jupyter notebooks](https://jupyter.org/) converted to the site using the [jupyter book](https://jupyterbook.org/en/stable/basics/build.html) tool.

Of course, this imposes some restrictions on the site's content, but any page generated from an IPYNB file can be downloaded and explored on your own.

For pages that use a lot of bash you should use the bash kernel. To install it use:

```bash
pip install bash_kernel
python -m bash_kernel.install
```

For deployment in docker use:

```bash
docker build -t knowledge_dev .
docker run -itd -v ./:/knowledge --name knowledge_dev knowledge_dev
```

Some pages require running specifically in a Docker environment, as they are associated with discovering system-level features.

Large part of this base related to python programming language is moved to special site - [python](https://fedorkobak.github.io/python/intro.html).
