Installation
============

The latest Konoha supports Python 3.8 or newer.

We recommend to install via pip:

.. code-block:: bash

    $ pip install konoha[all]

You can also install Konoha with specific tokenizer, please run:

.. code-block:: bash

    $ pip install konoha[janome,kytea,mecab,sentencepiece,sudachi,nagisa]  # specify one or more of them

If you run `pip install konoha`, Konoha will be installed only with sentence splitter.

You can also install the development version of Konoha from the main branch of Git repository:

.. code-block:: bash

    $ pip install git+https://github.com/himkt/konoha.git
