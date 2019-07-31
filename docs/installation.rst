============
Installation
============

Getting Started
===============

1. Install sphinxcontrib-viewsource using pip.

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

6. Build the docs and check the result.

Advanced Link Resolution Strategies
===================================

The ``viewsource_resolve_link`` function set in ``config.py`` is editable to fit your documentation needs.

.. py:function:: viewsource_resolve_link(file_path, language=None)

   Defines the link resolution strategy for each code of block.

   :param file_path: Contains the path of the file included.
   :type file_path: string
   :param language: Contains the name of the highlighting language if set.
   :type language: string
   :return: URL pointing to the file as string

Here there are some popular configurations that you can use to set up the link resolution strategy.

Point to an internal file
-------------------------
.. code:: python

  viewsource_title = 'Get the Code'
  def viewsource_resolve_link(file_path, language=None):
    snippets_folder = '/snippets/'
    # get the name of the file
    path_split = file_path.split('/')
    file = path_split[len(path_split)-1]
    return snippets_folder + file

Point to an external file
-------------------------

.. code:: python

      viewsource_title = 'Edit on Github'
      def viewsource_resolve_link(file_path, language=None):
        base_url = 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/snippets/'
        # get the name of the file
        path_split = file_path.split('/')
        file = path_split[len(path_split)-1]
        return base_url + file

Different link resolution strategy per language
-----------------------------------------------

.. code:: python

      viewsource_title = 'Edit on Github'
      def viewsource_resolve_link(file_path, language=None):
        # get the name of the file
        path_split = file_path.split('/')
        file = path_split[len(path_split)-1]

        url = 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/python/%s' % file
        if language == 'java':
            return 'https://github.com/dgarcia360/sphinxcontrib-viewsource/blob/master/docs/java/src/%s' % file
        return url
