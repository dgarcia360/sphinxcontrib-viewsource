========================
sphinxcontrib-viewsource
========================

**Add an "Edit on GitHub" button to your code examples.**

`sphinxcontrib-viewsource`_ is a `Sphinx`_ extension that enhances the ``literalinclude`` directive, adding a caption automatically with a link pointing to the source file.

Use it to add an **Edit on GitHub** button to your code source files, or to **show the complete code** when the ``literalinclude`` directive renders a subset of the file.

**Example**

.. viewsource:: snippets/hello.py
    :language: python
    :lines: 2

Add the extension to your project following the :doc:`installation instructions <installation>`.


.. toctree::
    :caption: Table of Contents
    :maxdepth: 2

    installation
    resolve-link
    changelog

.. _sphinxcontrib-viewsource:
   http://pypi.python.org/pypi/_sphinxcontrib-viewsource
.. _Sphinx: http://www.sphinx-doc.org/en/master/

