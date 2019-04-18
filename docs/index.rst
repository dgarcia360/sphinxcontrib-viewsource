=================================================================================
 sphinxcontrib-viewsource - Add an "Edit on GitHub" button to your code examples.
=================================================================================

`sphinxcontrib-viewsource`_ is a `Sphinx`_ extension that enhances the ``literalinclude`` directive, adding a caption automatically with a link pointing to the source file.

The strategy to resolve the link can be coded in the configuration file, enabling you to point to internal files or external links as needed.

Use it to add an **Edit on GitHub** button to your code source files, or to **show the complete code** when the literalinclude directive renders a subset of the file.

**Example**

.. viewsource:: snippets/hello.py
    :language: python
    :lines: 2

.. toctree::
   :maxdepth: 2

   installation
   changelog

.. _sphinxcontrib-viewsource:
   http://pypi.python.org/pypi/_sphinxcontrib-viewsource
.. _Sphinx: http://www.sphinx-doc.org/en/master/
