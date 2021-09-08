============
Installation
============

Getting Started
===============

1. Install ``sphinxcontrib-viewsource`` using pip.

.. code-block:: bash

    pip install sphinxcontrib-viewsource

2. Add the extension to your Sphinx project ``conf.py`` file.

.. code:: python

  extensions = ['sphinxcontrib.viewsource']

3. Define a caption text and link resolution function at the end of your ``conf.py`` file:

.. code:: python

  viewsource_title = 'Edit on GitHub'

  def viewsource_resolve_link(file_path, language=None):
    base_url = 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/snippets/'
    # get the name of the file
    path_split = file_path.split('/')
    file = path_split[len(path_split)-1]
    return base_url + file

Find here other :doc:`link resolution examples <resolve-link>`.

4. Use ``viewsource`` directive instead of ``literalinclude`` when rendering code:

.. code:: restructuredText

    .. viewsource:: snippets/hello.py
        :language: python
        :lines: 2

The ``viewsource`` extends from ``literalinclude``, so you can still use all the directive `options <http://www.sphinx-doc.org/es/stable/markup/code.html#includes>`_.

.. note:: The directive overwrites the ``caption`` option with the specified link. If you set the caption option, the extension will not render the link.

5. You can apply custom CSS to style the caption:

.. code:: css

    .code-block-caption .caption-text > a {
      float: right;
    }

6. Build the docs.
